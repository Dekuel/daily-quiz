# -*- coding: utf-8 -*-
from __future__ import annotations
"""
Daily Quiz Generator (dreimodig):
- Modi: "normal", "schwer" und "physik"
- Politik-Fragen werden pro Modus separat über das Politik-Plugin generiert (Ziel: 2) – außer im Modus "physik"
- Weitere Fragen über Kategorien-Plugins in ./kategorien/ (je Aufruf genau 1 Frage)
- Dedupe ggü. Vergangenheit (7 Tage), innerhalb eines Modus, und zwischen den Modi (tagesweit)
- Schwierigkeit pro Modus via Gewichten (zentral, Core->Plugin)
- Persistenz:
  quizzes/YYYY-MM-DD/bundle.normal.json
  quizzes/YYYY-MM-DD/bundle.schwer.json
  quizzes/YYYY-MM-DD/bundle.physik.json
  latest.json -> { "latest_date": "...", "paths": {"normal": "...", "schwer": "...", "physik": "..."} }
  catalog.json -> [{ "date": "...", "paths": {"normal": "...", "schwer": "...", "physik": "..."} }, ...]

Zusatz (NEU):
- Kategorieweises Archiv pro Modus:
  - "normal"  -> Ordner "Fragen leicht", Datei pro Kategorie (z. B. "Natur.json")
  - "schwer"  -> Ordner "Fragen schwer", Datei pro Kategorie
  - "physik"  -> KEINE Archivierung
- Dateien werden geladen, erweitert und zurückgeschrieben (Bestand bleibt erhalten)
- Einfache Dedupe innerhalb der Kategorie-Datei (identischer question-Text + Kategorie)

NEU (diese Version):
- Harmonisierung von Unterkategorien/Subdisziplinen auf das Feld `subcategory`.
  Falls Plugins unterschiedliche Schlüssel wie `subtopic`, `subdiscipline`, `Unterkategorie` etc. liefern,
  werden diese automatisch in `subcategory` gespiegelt (ohne die Originalfelder zu löschen).
  Wenn ein Plugin keine Unterkategorie liefert, bleibt `subcategory` einfach ungesetzt.
"""

# --- ensure repo root and kategorien dir on sys.path ---
import os, sys
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
KATEGORIEN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "kategorien"))
if REPO_ROOT not in sys.path:
    # append (not insert at front) to avoid shadowing Python stdlib modules
    sys.path.append(REPO_ROOT)
if KATEGORIEN_DIR not in sys.path:
    # Add kategorien dir so Unterkategorien package can be imported
    sys.path.append(KATEGORIEN_DIR)

import re
import json
import random
import importlib
import pkgutil
import traceback
import inspect
from datetime import datetime, timezone, timedelta
from difflib import SequenceMatcher
from typing import Callable, Dict, List, Optional

# ===================== Konfiguration =====================

OUT_ROOT = "quizzes"
PAST_DAYS_TO_CHECK = 7

# Wie viele Politikfragen pro Modus?
POLITICS_TARGET = 2

# Wie viele Nicht-Politik-Fragen pro Modus (normal/schwer)?
OTHER_QUESTIONS_PER_GENERAL_MODE = 7  # vorher: 3

# Kategorie-Name des Politik-Plugins
POLITICS_CATEGORY_NAME = "politik"

# Kategorie-Name für das reine Physik-Quiz
PHYSICS_CATEGORY_NAME = "physik"

# Anzahl Fragen im Physik-Bundle
PHYSIK_QUESTIONS_COUNT = 10

# Schwierigkeit-Gewichte (Schlüssel = Difficulty 1..10, Wert = Gewicht) – ZENTRAL
DIFFICULTY_WEIGHTS: Dict[str, Dict[int, int]] = {
    "schwer": {10: 16, 9: 17, 8: 21, 7: 16, 6: 11, 5: 9, 4: 6, 3: 4, 2: 0, 1: 0},
    "normal": {10: 0, 9: 0, 8: 10, 7: 10, 6: 14, 5: 18, 4: 16, 3: 12, 2: 10, 1: 10},
    "physik": {10: 3, 9: 5, 8: 8, 7: 10, 6: 14, 5: 18, 4: 16, 3: 12, 2: 8, 1: 6},
}

# Text-Ähnlichkeitsschwelle für Dedupe
SIM_THRESHOLD = 0.82


# ===================== Utilities =====================

def _iso_date_today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "")).strip().lower()


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, _norm(a), _norm(b)).ratio()


def is_duplicate(candidate_q: str, corpus_questions: List[str], threshold: float = SIM_THRESHOLD) -> bool:
    cand = _norm(candidate_q)
    for q in corpus_questions:
        if similarity(cand, q) >= threshold:
            return True
    return False


def weighted_choice(weights: Dict[int, int]) -> int:
    # weights: {difficulty: weight}
    if not weights:
        return 5
    items = sorted(weights.items(), key=lambda x: x[0])
    keys = [k for k, _ in items]
    vals = [w for _, w in items]
    return random.choices(keys, weights=vals, k=1)[0]


def pick_target_difficulty_for_mode(mode: str) -> int:
    weights = DIFFICULTY_WEIGHTS.get(mode) or DIFFICULTY_WEIGHTS["normal"]
    return int(weighted_choice(weights))


# ===================== Feld-Harmonisierung (Unterkategorie) =====================

# Mögliche Plugin-Feldnamen für Unterkategorien/Subdisziplinen
_SUBCATEGORY_ALIASES = [
    "subcategory", "subtopic", "sub_topic",
    "subdiscipline", "sub_discipline",
    "unterkategorie", "unter_kategorie",
]

def _harmonize_question_metadata(q: dict) -> None:
    """
    Vereinheitlicht optionale Metadaten der Fragen:
    - Spiegelt diverse Alias-Felder auf 'subcategory' (falls vorhanden).
    - Löscht Originalfelder nicht (Backward-Kompatibilität).
    - Greift nur, wenn 'subcategory' noch nicht gesetzt ist.
    """
    if not isinstance(q, dict):
        return
    if "subcategory" not in q:
        for k in _SUBCATEGORY_ALIASES:
            if k in q and isinstance(q[k], str) and q[k].strip():
                q["subcategory"] = q[k].strip()
                break


# ===================== Vergangenheit laden =====================

def load_past_questions(days: int = PAST_DAYS_TO_CHECK) -> List[dict]:
    """
    Lädt Fragen aus bundle.json, bundle.normal.json, bundle.schwer.json, bundle.physik.json der letzten N Tage.
    """
    past: List[dict] = []
    if not os.path.exists(OUT_ROOT):
        return past

    cutoff = datetime.now().date() - timedelta(days=days)
    dates = set()

    # bevorzugt catalog.json
    catalog_path = os.path.join(OUT_ROOT, "catalog.json")
    if os.path.exists(catalog_path):
        try:
            catalog = json.load(open(catalog_path, "r", encoding="utf-8"))
            for entry in catalog:
                try:
                    d = datetime.strptime(entry.get("date", ""), "%Y-%m-%d").date()
                    if d >= cutoff:
                        dates.add(entry["date"])
                except Exception:
                    continue
        except Exception:
            pass

    # Fallback: Verzeichnisse scannen (neue Struktur: YYYY/MM/DD)
    if not dates:
        try:
            for year_name in os.listdir(OUT_ROOT):
                year_path = os.path.join(OUT_ROOT, year_name)
                if not os.path.isdir(year_path) or not year_name.isdigit():
                    continue
                for month_name in os.listdir(year_path):
                    month_path = os.path.join(year_path, month_name)
                    if not os.path.isdir(month_path) or not month_name.isdigit():
                        continue
                    for day_name in os.listdir(month_path):
                        day_path = os.path.join(month_path, day_name)
                        if not os.path.isdir(day_path) or not day_name.isdigit():
                            continue
                        try:
                            date_str = f"{year_name}-{month_name.zfill(2)}-{day_name.zfill(2)}"
                            d = datetime.strptime(date_str, "%Y-%m-%d").date()
                            if d >= cutoff:
                                dates.add(date_str)
                        except Exception:
                            continue
        except Exception:
            pass

    for d in sorted(dates, reverse=True):
        year, month, day = d.split('-')
        for fname in ("bundle.json", "bundle.normal.json", "bundle.schwer.json", "bundle.physik.json"):
            bundle_path = os.path.join(OUT_ROOT, year, month, day, fname)
            if os.path.exists(bundle_path):
                try:
                    bundle = json.load(open(bundle_path, "r", encoding="utf-8"))
                    past.extend(bundle.get("questions", []))
                except Exception:
                    continue

    return past


# ===================== Plugin Discovery =====================

def discover_category_plugins() -> Dict[str, Callable[..., Optional[dict]]]:
    """
    Findet alle Module in ./kategorien/ mit einer Funktion:
        generate_one(past_texts: list[str], target_difficulty: Optional[int] = None, mode: Optional[str] = None) -> dict | None

    Rückgabe: Mapping { key: callable }
    - key = modulname in lowercase (z.B. 'physik', 'politik', 'geschichte')
    - Anzeigename bleibt im Modul (CATEGORY_NAME), wird aber NICHT als Key verwendet.
    """
    plugins: Dict[str, Callable[..., Optional[dict]]] = {}
    try:
        import kategorien  # type: ignore
    except Exception as e:
        print("[DISCOVERY] Konnte Package 'kategorien' nicht importieren:", e)
        raise

    pkgpath = getattr(kategorien, "__path__", None)
    if not pkgpath:
        print("[DISCOVERY] 'kategorien' hat kein __path__ – ist es ein Package?")
        return plugins

    for _, modname, ispkg in pkgutil.iter_modules(pkgpath):
        if ispkg:
            continue
        fqmn = f"kategorien.{modname}"
        try:
            mod = importlib.import_module(fqmn)
        except Exception as e:
            print(f"[PLUGIN-IMPORT-ERROR] {fqmn}: {e}")
            traceback.print_exc()
            # Physik ist essenziell: hier bewusst hart scheitern
            if modname.lower() == "physik":
                raise
            continue

        fn = getattr(mod, "generate_one", None)
        if callable(fn):
            key = modname.lower()
            plugins[key] = fn
            print(f"[DISCOVERY] Plugin registriert: {key} -> {fn}")
    return plugins


# ===================== Antwort-Shuffle =====================

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def _strip_letter_prefix(s: str) -> str:
    # Entfernt "A: " / "B) " / "C - " etc. am Anfang
    return re.sub(r"^[A-D]\s*[:\)\]\.-]\s*", "", s.strip(), flags=re.IGNORECASE)

def _apply_letter_prefixes(choices: List[str]) -> List[str]:
    return [f"{LETTERS[i]}: {choices[i]}" for i in range(len(choices))]

def _shuffle_answers_in_question(q: dict) -> None:
    """
    Unterstützt gängige Schemata:
      - q["choices"] = ["A: ...","B: ...",...], q["correct_answer"] = "A|B|C|D"
      - q["choices"] = ["...","..."], q["answer_index"] / q["correct_index"]
      - q["answers"] mit Dict-Objekten und "correct"-Flag
    """
    # Feld identifizieren
    field = None
    if isinstance(q.get("choices"), list):
        field = "choices"
    elif isinstance(q.get("options"), list):
        field = "options"
    elif isinstance(q.get("answers"), list):
        field = "answers"
    if not field:
        return

    opts = list(q[field])
    if not opts:
        return

    # Korrekt-Index bestimmen
    correct_idx = None

    # Fall: Index-Felder
    for k in ("answer_index", "correct_index"):
        if isinstance(q.get(k), int):
            correct_idx = q[k]
            break

    # Fall: Buchstabe
    if correct_idx is None and isinstance(q.get("correct_answer"), str):
        try:
            correct_idx = LETTERS.index(q["correct_answer"].strip().upper())
        except ValueError:
            pass

    # Fall: Objektliste mit correct-Flag
    if correct_idx is None and isinstance(opts[0], dict) and "correct" in opts[0]:
        correct_idx = next((i for i, c in enumerate(opts) if c.get("correct")), None)

    if correct_idx is None or not (0 <= correct_idx < len(opts)):
        return

    # Inhalte ohne A:/B: Präfixe normalisieren (nur für String-Choices)
    def normalize_choice(x):
        if isinstance(x, str):
            return _strip_letter_prefix(x)
        if isinstance(x, dict) and "text" in x:
            return _strip_letter_prefix(str(x["text"]))
        return x

    normalized_opts = [normalize_choice(x) for x in opts]

    # Permutation ziehen
    idxs = list(range(len(opts)))
    random.shuffle(idxs)

    # Neuen Korrekt-Index finden
    new_correct = idxs.index(correct_idx)

    # Feld aktualisieren
    if isinstance(opts[0], dict) and "correct" in opts[0]:
        new_opts = []
        for i, old_i in enumerate(idxs):
            item = dict(opts[old_i])
            # Text ggf. überschreiben
            if "text" in item:
                item["text"] = normalized_opts[old_i]
            # correct-Flag setzen
            item["correct"] = (i == new_correct)
            new_opts.append(item)
        q[field] = new_opts
    else:
        # String-Liste – nach Shuffle neu mit A:/B: labeln, falls vorher gelabelt
        relabeled = _apply_letter_prefixes([normalized_opts[old_i] for old_i in idxs])
        q[field] = relabeled

    # Korrektheits-Felder synchronisieren
    if "answer_index" in q:
        q["answer_index"] = new_correct
    if "correct_index" in q:
        q["correct_index"] = new_correct
    if "correct_answer" in q:
        q["correct_answer"] = LETTERS[new_correct]


def _shuffle_answers_in_bundle(qlist: List[dict]) -> None:
    for q in qlist:
        try:
            _shuffle_answers_in_question(q)
        except Exception:
            # Nicht tödlich – einfach überspringen
            continue


# ===================== Archiv (kategorieweise) =====================

ARCHIVE_DIRS = {
    "normal": "Fragen leicht",
    "schwer": "Fragen schwer",
}

# English archives (copies / translations go here)
ARCHIVE_DIRS_EN = {
    "normal": "Fragen leicht_en",
    "schwer": "Fragen schwer_en",
}


# ===================== Optional Translation Support (OpenAI) =====================

def _has_openai_api() -> bool:
    return bool(os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_KEY") or os.getenv("OPENAI"))


def _openai_key_source() -> Optional[str]:
    for name in ("OPENAI_API_KEY", "OPENAI_KEY", "OPENAI"):
        if os.getenv(name):
            return name
    return None


def _openai_translate_text(text: str, src: str = "de", tgt: str = "en") -> Optional[str]:
    """Translate a short piece of text using OpenAI if API key is available.
    Returns translated text or None on any failure / missing key.
    """
    key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_KEY")
    if not key:
        return None
    try:
        # Prefer new OpenAI client (openai>=1.0.0)
        try:
            from openai import OpenAI
            client = OpenAI(api_key=key)
            resp = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a helpful, concise translator. Translate the provided quiz text from {src} to {tgt}. Keep lists, punctuation and letters (A:, B:, ...) intact where possible."},
                    {"role": "user", "content": text},
                ],
                temperature=0,
                max_tokens=800,
            )
            out = resp.choices[0].message.content.strip()
            return out
        except Exception:
            # Fallback to older openai package API if present
            import openai
            openai.api_key = key
            resp = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": f"You are a helpful, concise translator. Translate the provided quiz text from {src} to {tgt}. Keep lists, punctuation and letters (A:, B:, ...) intact where possible."}, {"role": "user", "content": text}],
                temperature=0,
                max_tokens=800,
            )
            out = resp.choices[0].message.content.strip()
            return out
    except Exception as e:
        print("[TRANSLATE-ERROR]", e)
        return None


def _translate_question_dict(q: dict) -> dict:
    """Translate the question dict fields (question, choices/options/answers, explanation) to English if possible.
    If translation service not available, returns the original dict.
    """
    if not isinstance(q, dict):
        return q
    if not _has_openai_api():
        # no translation available
        return q

    out = dict(q)

    # Translate main question text
    qtext = str(q.get("question") or "")
    if qtext:
        tr = _openai_translate_text(qtext, src="de", tgt="en")
        if tr:
            out["question"] = tr

    # Translate explanation if present
    if "explanation" in q and q.get("explanation"):
        tr = _openai_translate_text(str(q.get("explanation")), src="de", tgt="en")
        if tr:
            out["explanation"] = tr

    # Translate category name (best-effort)
    cat = str(q.get("category") or "")
    if cat:
        # simple mapping common categories
        cat_map = {"politik": "politics", "physik": "physics", "geschichte": "history", "natur": "nature", "sport": "sport", "kunst_und_literatur": "arts_and_literature"}
        low = cat.lower()
        out["category"] = cat_map.get(low, cat)

    # Translate choices / options / answers
    for field in ("choices", "options", "answers"):
        if field in q and isinstance(q[field], list):
            new_list = []
            for item in q[field]:
                if isinstance(item, str):
                    tr = _openai_translate_text(item, src="de", tgt="en")
                    new_list.append(tr or item)
                elif isinstance(item, dict):
                    it = dict(item)
                    if "text" in it:
                        tr = _openai_translate_text(str(it["text"]), src="de", tgt="en")
                        if tr:
                            it["text"] = tr
                    new_list.append(it)
                else:
                    new_list.append(item)
            out[field] = new_list

    # Sync letter prefixes if needed: we don't try to reinterpret correct_answer indices
    return out


def _openai_translate_texts(texts: List[str], src: str = "de", tgt: str = "en") -> Optional[List[str]]:
    """Translate a list of strings in a single batch OpenAI call. Returns list of translations
    or None on failure.
    """
    if not texts:
        return []
    key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_KEY")
    if not key:
        return None
    try:
        import json as _json
        system = {"role": "system", "content": f"You are a concise translator from {src} to {tgt}. Return only a JSON array of translated strings with no commentary."}
        user = {"role": "user", "content": _json.dumps(texts, ensure_ascii=False)}
        # Prefer new client
        try:
            from openai import OpenAI
            client = OpenAI(api_key=key)
            resp = client.chat.completions.create(model="gpt-3.5-turbo", messages=[system, user], temperature=0, max_tokens=4000)
            out_text = resp.choices[0].message.content.strip()
        except Exception:
            import openai
            openai.api_key = key
            resp = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[system, user], temperature=0, max_tokens=4000)
            out_text = resp.choices[0].message.content.strip()

        # extract JSON array
        start = out_text.find("[")
        end = out_text.rfind("]")
        if start != -1 and end != -1:
            arr_text = out_text[start:end+1]
        else:
            arr_text = out_text
        try:
            arr = _json.loads(arr_text)
            if isinstance(arr, list):
                return [str(x) if x is not None else "" for x in arr]
        except Exception:
            return None
    except Exception as e:
        print("[TRANSLATE-BATCH-ERROR]", e)
        return None


def _translate_questions_batch(questions: List[dict]) -> List[dict]:
    """Translate fields of multiple questions in a single batched call.
    This function gathers all strings that need translation, calls OpenAI once,
    and maps translations back into the question dicts.
    """
    # Build list of source strings in stable order and keep mapping
    to_translate: List[str] = []
    mapping: List[tuple[int, str, Optional[int]]] = []  # (qidx, field, opt_idx)

    for qi, q in enumerate(questions):
        # main question text
        qtext = str(q.get("question") or "")
        to_translate.append(qtext)
        mapping.append((qi, "question", None))

        # explanation
        expl = str(q.get("explanation") or "")
        to_translate.append(expl)
        mapping.append((qi, "explanation", None))

        # choices/options/answers
        for field in ("choices", "options", "answers"):
            if field in q and isinstance(q[field], list):
                for oi, item in enumerate(q[field]):
                    if isinstance(item, str):
                        to_translate.append(item)
                        mapping.append((qi, field, oi))
                    elif isinstance(item, dict) and "text" in item:
                        to_translate.append(str(item.get("text") or ""))
                        mapping.append((qi, field, oi))

    if not to_translate:
        return questions

    translated = _openai_translate_texts(to_translate, src="de", tgt="en")
    if not translated:
        # translation failed; return original
        return questions

    # Apply translations
    out_questions = [dict(q) for q in questions]
    for (qi, field, oi), tr in zip(mapping, translated):
        try:
            if field in ("question", "explanation"):
                if tr:
                    out_questions[qi][field] = tr
            else:
                # list element
                if field in out_questions[qi] and isinstance(out_questions[qi][field], list):
                    if isinstance(out_questions[qi][field][oi], str):
                        out_questions[qi][field][oi] = tr or out_questions[qi][field][oi]
                    elif isinstance(out_questions[qi][field][oi], dict) and "text" in out_questions[qi][field][oi]:
                        out_questions[qi][field][oi]["text"] = tr or out_questions[qi][field][oi]["text"]
        except Exception:
            continue

    return out_questions

def _sanitize_filename(name: str) -> str:
    #rudimentär: Leerzeichen -> Unterstrich; nur Buchstaben/Ziffern/_/-/Umlaute/ß
    base = re.sub(r"\s+", "_", name.strip())
    base = re.sub(r"[^A-Za-z0-9_\-ÄÖÜäöüß]", "", base)
    return base or "Unbekannt"

def _load_json_list(path: str) -> List[dict]:
    if not os.path.exists(path):
        return []
    try:
        data = json.load(open(path, "r", encoding="utf-8"))
        if isinstance(data, dict) and isinstance(data.get("questions"), list):
            return list(data["questions"])
        if isinstance(data, list):
            return list(data)
    except Exception:
        pass
    return []

def _save_json_list(path: str, category_name: str, questions: List[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    payload = {
        "category": category_name,
        "questions": questions,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

def _append_questions_to_category_files(questions: List[dict], mode: str) -> None:
    """
    Hängt Fragen kategorieweise in ARCHIVE_DIRS[mode] an.
    - Nur für Modi 'normal' und 'schwer'
    - Physik wird nicht archiviert
    - Bewahrt bisherigen Inhalt; einfache Dedupe pro Datei (identische question+category)
    """
    archive_root = ARCHIVE_DIRS.get(mode)
    if not archive_root:
        return

    # kategorie -> neue fragen
    buckets: Dict[str, List[dict]] = {}
    for q in questions:
        cat = str(q.get("category") or "Unbekannt").strip()
        if not cat:
            cat = "Unbekannt"
        buckets.setdefault(cat, []).append(q)

    for cat, qlist in buckets.items():
        fname = f"{_sanitize_filename(cat)}.json"
        fpath = os.path.join(archive_root, fname)

        existing = _load_json_list(fpath)

        # Dedupe: keine identischen Frage-Texte in gleicher Kategorie
        seen = {(_norm(x.get("question", "")), _norm(x.get("category", ""))) for x in existing}
        merged = list(existing)
        for q in qlist:
            key = (_norm(q.get("question", "")), _norm(q.get("category", "")))
            if key in seen:
                continue
            merged.append(q)
            seen.add(key)

        _save_json_list(fpath, cat, merged)


# ===================== Fragen-Generatoren =====================

def generate_random_categories(
    plugins: Dict[str, Callable[..., Optional[dict]]],
    k: int,
    past_texts: List[str],
    exclude: Optional[set[str]] = None,
    mode: str = "normal",
) -> List[dict]:
    """
    Wählt k Kategorien (ohne exclude) und erzeugt jeweils eine Frage.
    Dedupe gegen Vergangenheit und innerhalb des Sets.
    Übergibt eine Ziel-Schwierigkeit pro Frage ans Plugin.
    """
    names = [n for n in plugins.keys() if not exclude or n not in exclude]
    if not names or k <= 0:
        return []

    chosen = random.sample(names, k=min(k, len(names)))
    while len(chosen) < k:
        chosen.append(random.choice(names))

    out: List[dict] = []
    tries = 0
    while len(out) < k and tries < k * 6:
        cat = chosen[len(out)]
        tries += 1
        try:
            target = pick_target_difficulty_for_mode(mode)
            # Inspect plugin signature and call with appropriate arguments
            plugin_fn = plugins[cat]
            sig = inspect.signature(plugin_fn)
            kwargs = {}
            if 'past_texts' in sig.parameters:
                kwargs['past_texts'] = past_texts
            if 'target_difficulty' in sig.parameters:
                kwargs['target_difficulty'] = target
            elif 'tier' in sig.parameters:
                kwargs['tier'] = target
            if 'mode' in sig.parameters:
                kwargs['mode'] = mode
            item = plugin_fn(**kwargs)
        except Exception as e:
            print(f"⚠️ Fehler beim Generieren aus Kategorie '{cat}': {e.__class__.__name__}: {e}")
            traceback.print_exc()
            continue
        if not item:
            continue
        item.setdefault("difficulty", target)   # Fallback, falls Plugin noch nicht setzt
        item.setdefault("category", cat)        # NEU: Kategorie mitschreiben

        # Unterkategorie/Subdisziplin harmonisieren
        _harmonize_question_metadata(item)

        qt = _norm(item.get("question", ""))
        if not qt:
            continue
        if any(similarity(qt, x.get("question", "")) >= SIM_THRESHOLD for x in out):
            continue
        if is_duplicate(qt, past_texts, SIM_THRESHOLD):
            continue
        out.append(item)
    return out


def generate_specific_category_questions(
    plugins: Dict[str, Callable[..., Optional[dict]]],
    category_name: str,
    target_count: int,
    past_texts: List[str],
    day_seen: set[str],
    mode: str = "normal",
) -> List[dict]:
    """
    Erzeugt ausschließlich Fragen aus einer bestimmten Kategorie (z. B. nur 'Physik').
    Dedupe: Vergangenheit, innerhalb dieses Sets und tagesweit (day_seen).
    Übergibt Ziel-Schwierigkeit pro Frage ans Plugin.
    """
    if category_name not in plugins:
        print(f"⚠️ Kategorie-Plugin '{category_name}' nicht gefunden.")
        return []

    out: List[dict] = []
    tries = 0
    max_tries = target_count * 8

    while len(out) < target_count and tries < max_tries:
        tries += 1
        try:
            target = pick_target_difficulty_for_mode(mode)
            # Inspect plugin signature and call with appropriate arguments
            plugin_fn = plugins[category_name]
            sig = inspect.signature(plugin_fn)
            kwargs = {}
            if 'past_texts' in sig.parameters:
                kwargs['past_texts'] = past_texts
            if 'target_difficulty' in sig.parameters:
                kwargs['target_difficulty'] = target
            elif 'tier' in sig.parameters:
                kwargs['tier'] = target
            if 'mode' in sig.parameters:
                kwargs['mode'] = mode
            q = plugin_fn(**kwargs)
        except Exception:
            continue
        if not q:
            continue
        q.setdefault("difficulty", target)
        q.setdefault("category", category_name)  # NEU: Kategorie mitschreiben

        # Unterkategorie/Subdisziplin harmonisieren
        _harmonize_question_metadata(q)

        qt = _norm(q.get("question", ""))
        if not qt:
            continue
        if is_duplicate(qt, past_texts, SIM_THRESHOLD):
            continue
        if any(similarity(qt, x.get("question", "")) >= SIM_THRESHOLD for x in out):
            continue
        if any(similarity(qt, t) >= SIM_THRESHOLD for t in day_seen):
            continue
        out.append(q)

    return out


def generate_politics_for_mode(
    plugins: Dict[str, Callable[..., Optional[dict]]],
    target: int,
    past_texts: List[str],
    day_seen: set[str],
    mode: str,
) -> List[dict]:
    """
    Erzeugt bis zu 'target' Politikfragen für einen Modus.
    Dedupe: Vergangenheit, innerhalb dieses Sets, und 'day_seen'.
    Übergibt Ziel-Schwierigkeit pro Frage ans Politik-Plugin.
    """
    if POLITICS_CATEGORY_NAME not in plugins:
        return []

    out: List[dict] = []
    tries = 0
    while len(out) < target and tries < target * 6:
        tries += 1
        try:
            target_diff = pick_target_difficulty_for_mode(mode)
            # Inspect plugin signature and call with appropriate arguments
            plugin_fn = plugins[POLITICS_CATEGORY_NAME]
            sig = inspect.signature(plugin_fn)
            kwargs = {}
            if 'past_texts' in sig.parameters:
                kwargs['past_texts'] = past_texts
            if 'target_difficulty' in sig.parameters:
                kwargs['target_difficulty'] = target_diff
            elif 'tier' in sig.parameters:
                kwargs['tier'] = target_diff
            if 'mode' in sig.parameters:
                kwargs['mode'] = mode
            q = plugin_fn(**kwargs)
        except Exception:
            continue
        if not q:
            continue
        q.setdefault("difficulty", target_diff)
        q.setdefault("category", POLITICS_CATEGORY_NAME)  # NEU: Kategorie mitschreiben

        # Unterkategorie/Subdisziplin harmonisieren (falls Politik-Plugin sowas hat)
        _harmonize_question_metadata(q)

        qt = _norm(q.get("question", ""))
        if not qt:
            continue
        if is_duplicate(qt, past_texts, SIM_THRESHOLD):
            continue
        if any(similarity(qt, x.get("question", "")) >= SIM_THRESHOLD for x in out):
            continue
        if any(similarity(qt, t) >= SIM_THRESHOLD for t in day_seen):
            continue
        out.append(q)

    return out


# ===================== Persistenz =====================

def write_daily_bundle(quiz_list: List[dict], mode: str, date_str: Optional[str] = None) -> Optional[str]:
    """
    Schreibt bundle.<mode>.json ins Tagesverzeichnis.
    Gibt den relative Pfad zurück oder None, wenn leer.
    """
    if not quiz_list:
        print(f"❌ Keine gültigen Quizfragen für Modus '{mode}'.")
        return None

    day = date_str or _iso_date_today()
    # Neue Struktur: YYYY/MM/DD statt YYYY-MM-DD
    year, month, day_only = day.split('-')
    day_dir = os.path.join(OUT_ROOT, year, month, day_only)
    os.makedirs(day_dir, exist_ok=True)

    bundle = {
        "date": day,
        "generated_at": _now_iso(),
        "schema_version": 6,  # <-- erhöht: Harmonisierung 'subcategory'
        "mode": mode,
        "questions": quiz_list,
    }

    if mode == "schwer":
        suffix = ".schwer.json"
    elif mode == "physik":
        suffix = ".physik.json"
    else:
        suffix = ".normal.json"

    bundle_path = os.path.join(day_dir, f"bundle{suffix}")
    with open(bundle_path, "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=2)

    print(f"✅ Bundle gespeichert ({mode}): {bundle_path}")
    return f"{OUT_ROOT}/{year}/{month}/{day_only}/bundle{suffix}"


def _write_daily_bundle_en(quiz_list: List[dict], mode: str, date_str: Optional[str], plugins: Dict[str, Callable[..., Optional[dict]]]) -> Optional[str]:
    """
    Writes an English variant of the bundle. Strategy:
    - Start from the provided quiz_list (usually the German one)
    - Replace questions whose category == 'politiker' using the 'politics' plugin when available
    - Save as bundle.<mode>_en.json and append to EN archive dirs
    """
    if not quiz_list:
        return None

    day = date_str or _iso_date_today()
    # Neue Struktur: YYYY/MM/DD statt YYYY-MM-DD
    year, month, day_only = day.split('-')
    day_dir = os.path.join(OUT_ROOT, year, month, day_only)
    os.makedirs(day_dir, exist_ok=True)

    # deep copy entries (shallow copy of dicts is enough since we'll swap some)
    en_questions: List[dict] = [dict(q) for q in quiz_list]

    # Attempt to generate English replacements using available EN-capable plugins.
    # Mapping: German category key -> plugin key that can create English questions.
    # We explicitly prefer 'politics' for 'politiker' and 'language' for 'sprache' if present.
    german_to_en_plugin = {}
    if "politics" in plugins:
        german_to_en_plugin["politiker"] = "politics"
        german_to_en_plugin["politik"] = "politics"
    if "language" in plugins:
        german_to_en_plugin["sprache"] = "language"

    new_en_questions: List[dict] = []
    for q in en_questions:
        try:
            cat = str(q.get("category") or "").lower()
            mapped = german_to_en_plugin.get(cat)
            if mapped and mapped in plugins and callable(plugins[mapped]):
                try:
                    target = q.get("difficulty") if isinstance(q.get("difficulty"), int) else None
                    # Inspect plugin signature and call with appropriate arguments
                    plugin_fn = plugins[mapped]
                    sig = inspect.signature(plugin_fn)
                    kwargs = {}
                    if 'past_texts' in sig.parameters:
                        kwargs['past_texts'] = []
                    if 'target_difficulty' in sig.parameters:
                        kwargs['target_difficulty'] = target
                    elif 'tier' in sig.parameters:
                        kwargs['tier'] = target
                    if 'mode' in sig.parameters:
                        kwargs['mode'] = mode
                    repl = plugin_fn(**kwargs)
                    if repl:
                        # ensure category name is English and harmonize
                        repl.setdefault("category", mapped)
                        _harmonize_question_metadata(repl)
                        new_en_questions.append(repl)
                        continue
                except Exception:
                    # fallback: keep original for translation below
                    pass

            # No EN plugin replacement performed — keep original for subsequent translation
            new_en_questions.append(q)
        except Exception:
            # If anything goes wrong for a single question, preserve it so bundle isn't lost
            new_en_questions.append(q)

    en_questions = new_en_questions

    # if after substitution we have no questions, skip writing
    if not en_questions:
        print(f"⚠️ English bundle for mode '{mode}' would be empty after substitutions - skipping.")
        return None

    # Translate remaining questions if OpenAI is configured (best-effort)
    if _has_openai_api():
        try:
            en_questions = _translate_questions_batch(en_questions)
        except Exception:
            # on any failure, keep original en_questions
            pass
    else:
        # No OpenAI translator available. Try to improve English output by
        # applying simple category-name mappings and flagging items that
        # likely remain untranslated so they can be inspected.
        cat_map = {"politik": "politics", "physik": "physics", "politiker": "politics", "sprache": "language"}
        for q in en_questions:
            c = str(q.get("category") or "").lower()
            if c in cat_map:
                q["category"] = cat_map[c]
            # mark untranslated items so humans can filter/translate later
            q.setdefault("_untranslated", True)

    bundle = {
        "date": day,
        "generated_at": _now_iso(),
        "schema_version": 6,
        "mode": mode,
        "questions": en_questions,
    }

    if mode == "schwer":
        suffix = ".schwer.json"
    elif mode == "physik":
        suffix = ".physik.json"
    else:
        suffix = ".normal.json"

    # create _en filename
    bundle_path = os.path.join(day_dir, f"bundle{suffix}")
    bundle_path_en = bundle_path.replace('.json', '_en.json')
    with open(bundle_path_en, "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=2)

    print(f"✅ English bundle gespeichert ({mode}): {bundle_path_en}")

    # also append to EN archive dirs (normal/schwer)
    if mode in ("normal", "schwer"):
        _append_questions_to_category_files_en(en_questions, mode)

    return f"{OUT_ROOT}/{year}/{month}/{day_only}/bundle{suffix.replace('.json', '_en.json')}"


def _append_questions_to_category_files_en(questions: List[dict], mode: str) -> None:
    """
    Append questions into EN archive dirs (Fragen leicht_en / Fragen schwer_en).
    Behavior mirrors _append_questions_to_category_files.
    """
    archive_root = ARCHIVE_DIRS_EN.get(mode)
    if not archive_root:
        return

    buckets: Dict[str, List[dict]] = {}
    for q in questions:
        cat = str(q.get("category") or "Unknown").strip()
        if not cat:
            cat = "Unknown"
        buckets.setdefault(cat, []).append(q)

    for cat, qlist in buckets.items():
        fname = f"{_sanitize_filename(cat)}.json"
        fpath = os.path.join(archive_root, fname)

        existing = _load_json_list(fpath)

        seen = {(_norm(x.get("question", "")), _norm(x.get("category", ""))) for x in existing}
        merged = list(existing)
        for q in qlist:
            key = (_norm(q.get("question", "")), _norm(q.get("category", "")))
            if key in seen:
                continue
            merged.append(q)
            seen.add(key)

        _save_json_list(fpath, cat, merged)


def update_latest_and_catalog(paths_by_mode: Dict[str, str], date_str: Optional[str] = None) -> None:
    """
    Aktualisiert latest.json (mit allen Pfaden) und catalog.json (Eintrag pro Datum mit allen Pfaden).
    """
    day = date_str or _iso_date_today()

    # latest.json
    latest_path = os.path.join(OUT_ROOT, "latest.json")
    latest = {"latest_date": day, "paths": {}}
    if os.path.exists(latest_path):
        try:
            latest = json.load(open(latest_path, "r", encoding="utf-8"))
        except Exception:
            pass
    latest["latest_date"] = day
    latest.setdefault("paths", {}).update(paths_by_mode)
    with open(latest_path, "w", encoding="utf-8") as f:
        json.dump(latest, f, ensure_ascii=False, indent=2)
    print(f"➡️  latest.json aktualisiert: {latest_path}")

    # catalog.json
    catalog_path = os.path.join(OUT_ROOT, "catalog.json")
    catalog = []
    if os.path.exists(catalog_path):
        try:
            catalog = json.load(open(catalog_path, "r", encoding="utf-8"))
        except Exception:
            catalog = []
    # Eintrag ersetzen/ergänzen
    existing = next((e for e in catalog if e.get("date") == day), None)
    entry = existing or {"date": day, "paths": {}}
    entry["paths"].update(paths_by_mode)
    catalog = [e for e in catalog if e.get("date") != day] + [entry]
    catalog.sort(key=lambda e: e.get("date", ""), reverse=True)
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    print(f"🗂️  catalog.json aktualisiert: {catalog_path}")


# ===================== Orchestrierung =====================

def assign_difficulties(questions: List[dict], mode: str) -> None:
    """
    Fallback: setzt difficulty NUR, wenn das Plugin keinen Wert gesetzt hat.
    (Core überschreibt Plugin-Werte nicht.)
    """
    weights = DIFFICULTY_WEIGHTS.get(mode) or DIFFICULTY_WEIGHTS["normal"]
    for q in questions:
        if "difficulty" not in q or not isinstance(q["difficulty"], int):
            q["difficulty"] = int(weighted_choice(weights))


def main():
    # 0) Plugins laden
    plugins = discover_category_plugins()
    print("[DEBUG] Plugins gefunden:", sorted(plugins.keys()))

    # Report whether an OpenAI key is available in the environment — useful
    # to know if translation will run in this execution context.
    key_src = _openai_key_source()
    if key_src:
        print(f"[DEBUG] OpenAI key detected via env var: {key_src}")
    else:
        print("[DEBUG] No OpenAI key detected in environment; EN translations will be skipped or best-effort only.")

    # Expliziter Direktimport-Test für 'kategorien.physik' (zeigt Pfad/Fehler klar an)
    try:
        import inspect
        physik_mod = importlib.import_module("kategorien.physik")
        print("[DEBUG] kategorien.physik geladen aus:", inspect.getfile(physik_mod))
        print("[DEBUG] hat generate_one:", hasattr(physik_mod, "generate_one"))
    except Exception as e:
        print("[DEBUG] Direktimport 'kategorien.physik' fehlgeschlagen:", e)
        traceback.print_exc()
        # Wenn physik für dich zwingend ist, hier hard fail:
        # raise

    if not plugins:
        print("⚠️ Keine Plugins unter ./kategorien/ gefunden – keine Fragen generierbar.")
        return

    if POLITICS_CATEGORY_NAME not in plugins:
        print("⚠️ Politik-Plugin nicht gefunden – es werden keine Politikfragen generiert.")

    # 1) Vergangenheit (für Dedupe)
    past = load_past_questions(PAST_DAYS_TO_CHECK)
    past_texts = [q.get("question", "") for q in past if isinstance(q, dict)]

    # 2) Tagesweite Dedupe-Sammlung, um Duplikate zwischen den Modi zu vermeiden
    day_dedupe_texts: set[str] = set()

    # 3) pro Modus generieren und speichern
    saved_paths: Dict[str, str] = {}
    # keep generated question lists in memory so we can create EN variants
    qlists_by_mode: Dict[str, List[dict]] = {}

    for mode in ("normal", "schwer", "physik"):
        if mode in ("normal", "schwer"):
            # Zielverteilung je Modus:
            #  - 2x Politik
            #  - 7x andere Kategorien (ohne Politik)
            target_politics = POLITICS_TARGET  # = 2
            target_others = OTHER_QUESTIONS_PER_GENERAL_MODE  # = 7

            # 1) Erst Politik erzeugen
            politics = generate_politics_for_mode(
                plugins=plugins,
                target=target_politics,
                past_texts=past_texts,
                day_seen=day_dedupe_texts,
                mode=mode,
            )
            print(f"[{mode}] Politikfragen erzeugt (erste Runde): {len(politics)} / {POLITICS_TARGET}")

            # 2) Andere Kategorien erzeugen (ohne Politik)
            # Exclude also English-only plugin names (e.g. 'politics', 'language')
            def _german_exclude_set(plugins_map: Dict[str, Callable[..., Optional[dict]]]) -> set:
                ex = {POLITICS_CATEGORY_NAME, PHYSICS_CATEGORY_NAME}
                # if English-language plugin modules exist, don't include them in German generation
                if "politics" in plugins_map:
                    ex.add("politics")
                if "language" in plugins_map:
                    ex.add("language")
                return ex

            others = generate_random_categories(
                plugins=plugins,
                k=target_others,
                past_texts=past_texts,
                exclude=_german_exclude_set(plugins),
                mode=mode,
            )

            # 3) Fallback: wenn Politik < 2, versuche nochmals Politik nachzulegen
            if len(politics) < target_politics and POLITICS_CATEGORY_NAME in plugins:
                missing = target_politics - len(politics)
                tmp_day_seen = set(day_dedupe_texts)
                for q in politics + others:
                    qt = _norm(q.get("question", ""))
                    if qt:
                        tmp_day_seen.add(qt)
                politics_retry = generate_politics_for_mode(
                    plugins=plugins,
                    target=missing,
                    past_texts=past_texts,
                    day_seen=tmp_day_seen,
                    mode=mode,
                )
                politics.extend(politics_retry or [])

            # 4) Wenn immer noch < 2 Politik, fülle den Fehlbetrag mit Nicht-Politik auf
            if len(politics) < target_politics:
                deficit = target_politics - len(politics)
                others += generate_random_categories(
                    plugins=plugins,
                    k=deficit,
                    past_texts=past_texts,
                    exclude=_german_exclude_set(plugins),
                    mode=mode,
                )

            # 5) Finalisieren
            politics = politics[:target_politics]
            others = others[:target_others]
            qlist: List[dict] = politics + others

        else:  # mode == "physik"
            # nur Physik, 10 Fragen
            qlist = generate_specific_category_questions(
                plugins=plugins,
                category_name=PHYSICS_CATEGORY_NAME,
                target_count=PHYSIK_QUESTIONS_COUNT,
                past_texts=past_texts,
                day_seen=day_dedupe_texts,
                mode="physik",
            )

        # 3.5 Tagesweites Dedupe-Set updaten
        for q in qlist:
            qt = _norm(q.get("question", ""))
            if qt:
                day_dedupe_texts.add(qt)

        # 3.6 Schwierigkeiten setzen (nur Fallback, falls Plugin keinen Wert gesetzt hat)
        assign_difficulties(qlist, mode)

        # 3.6b Antworten mischen
        _shuffle_answers_in_bundle(qlist)

        # 3.7 Persistieren (Tages-Bundle)
        saved = write_daily_bundle(qlist, mode=mode)
        if saved:
            saved_paths[mode] = saved
        # keep the in-memory list for EN variant generation
        qlists_by_mode[mode] = qlist

        # 3.8 Zusatz: kategorieweise Archivierung (nur normal/schwer)
        if mode in ("normal", "schwer"):
            _append_questions_to_category_files(qlist, mode)

    # 3.9 Generate English variants for each mode (if possible)
    for mode, qlist in qlists_by_mode.items():
        try:
            en_path = _write_daily_bundle_en(qlist, mode=mode, date_str=None, plugins=plugins)
            if en_path:
                saved_paths[f"{mode}_en"] = en_path
        except Exception as e:
            print(f"[EN-GENERATION-ERROR] mode={mode}: {e}")

    # 4) latest.json + catalog.json aktualisieren (includes EN variants)
    if saved_paths:
        update_latest_and_catalog(saved_paths)


if __name__ == "__main__":
    main()
