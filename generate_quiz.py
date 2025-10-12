# -*- coding: utf-8 -*-
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
"""

from __future__ import annotations
import os
import re
import json
import random
import importlib
import pkgutil
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
POLITICS_CATEGORY_NAME = "Politik"

# Kategorie-Name für das reine Physik-Quiz
PHYSICS_CATEGORY_NAME = "Physik"

# Anzahl Fragen im Physik-Bundle
PHYSIK_QUESTIONS_COUNT = 10

# Schwierigkeit-Gewichte (Schlüssel = Difficulty 1..10, Wert = Gewicht) – ZENTRAL
DIFFICULTY_WEIGHTS: Dict[str, Dict[int, int]] = {
    "schwer": {10: 14, 9: 16, 8: 21, 7: 16, 6: 11, 5: 9, 4: 6, 3: 4, 2: 2, 1: 1},
    "normal": {10: 3, 9: 5, 8: 8, 7: 10, 6: 14, 5: 18, 4: 16, 3: 12, 2: 8, 1: 6},
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

    # Fallback: Verzeichnisse scannen
    if not dates:
        try:
            for name in os.listdir(OUT_ROOT):
                p = os.path.join(OUT_ROOT, name)
                try:
                    d = datetime.strptime(name, "%Y-%m-%d").date()
                    if d >= cutoff and os.path.isdir(p):
                        dates.add(name)
                except Exception:
                    continue
        except Exception:
            pass

    for d in sorted(dates, reverse=True):
        for fname in ("bundle.json", "bundle.normal.json", "bundle.schwer.json", "bundle.physik.json"):
            bundle_path = os.path.join(OUT_ROOT, d, fname)
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

    Rückgabe: Mapping { "Anzeigename": callable }
    - Anzeigename: mod.CATEGORY_NAME oder Dateiname -> Titelcase
    """
    plugins: Dict[str, Callable[..., Optional[dict]]] = {}
    try:
        import kategorien  # type: ignore
    except Exception:
        return plugins

    pkgpath = getattr(kategorien, "__path__", None)
    if not pkgpath:
        return plugins

    for _, modname, ispkg in pkgutil.iter_modules(pkgpath):
        if ispkg:
            continue
        fqmn = f"kategorien.{modname}"
        try:
            mod = importlib.import_module(fqmn)
        except Exception:
            continue
        fn = getattr(mod, "generate_one", None)
        if callable(fn):
            cname = getattr(mod, "CATEGORY_NAME", modname.replace("_", " ").title())
            plugins[cname] = fn
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
            item = plugins[cat](past_texts=past_texts, target_difficulty=target, mode=mode)  # Core -> Plugin
        except Exception:
            continue
        if not item:
            continue
        item.setdefault("difficulty", target)  # Fallback, falls Plugin noch nicht setzt
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
            q = plugins[category_name](past_texts=past_texts, target_difficulty=target, mode=mode)
        except Exception:
            continue
        if not q:
            continue
        q.setdefault("difficulty", target)
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
            q = plugins[POLITICS_CATEGORY_NAME](past_texts=past_texts, target_difficulty=target_diff, mode=mode)
        except Exception:
            continue
        if not q:
            continue
        q.setdefault("difficulty", target_diff)
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
    day_dir = os.path.join(OUT_ROOT, day)
    os.makedirs(day_dir, exist_ok=True)

    bundle = {
        "date": day,
        "generated_at": _now_iso(),
        "schema_version": 5,  # Multi-Modus (inkl. physik) + Plugins
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
    return f"{OUT_ROOT}/{day}/bundle{suffix}"


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

    for mode in ("normal", "schwer", "physik"):
        if mode in ("normal", "schwer"):
            # Zielverteilung je Modus:
            #  - 2x Politik
            #  - 4x andere Kategorien (ohne Politik)
            target_politics = POLITICS_TARGET  # = 2
            target_others = OTHER_QUESTIONS_PER_GENERAL_MODE  # = 4

            # 1) Erst Politik erzeugen
            politics = generate_politics_for_mode(
                plugins=plugins,
                target=target_politics,
                past_texts=past_texts,
                day_seen=day_dedupe_texts,
                mode=mode,  # NEU: Ziel-Schwierigkeit pro Frage
            )
            print(f"[{mode}] Politikfragen erzeugt (erste Runde): {len(politics)} / {POLITICS_TARGET}")

            # 2) Andere Kategorien erzeugen (ohne Politik)
            others = generate_random_categories(
                plugins=plugins,
                k=target_others,
                past_texts=past_texts,
                exclude={POLITICS_CATEGORY_NAME},
                mode=mode,  # NEU
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
                    mode=mode,  # NEU
                )
                politics.extend(politics_retry or [])

            # 4) Wenn immer noch < 2 Politik, fülle den Fehlbetrag mit Nicht-Politik auf,
            #    damit wir insgesamt trotzdem auf 6 Fragen kommen.
            if len(politics) < target_politics:
                deficit = target_politics - len(politics)
                others += generate_random_categories(
                    plugins=plugins,
                    k=deficit,
                    past_texts=past_texts,
                    exclude={POLITICS_CATEGORY_NAME},
                    mode=mode,  # NEU
                )

            # 5) Finalisieren: exakt die Zielanzahlen zuschneiden
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
                mode="physik",  # NEU
            )

        # 3.5 Tagesweites Dedupe-Set updaten
        for q in qlist:
            qt = _norm(q.get("question", ""))
            if qt:
                day_dedupe_texts.add(qt)

        # 3.6 Schwierigkeiten setzen (nur Fallback, falls Plugin keinen Wert gesetzt hat)
        assign_difficulties(qlist, mode)

        # 3.6b Antworten mischen (richtige Position wird angepasst)
        _shuffle_answers_in_bundle(qlist)

        # 3.7 Persistieren
        saved = write_daily_bundle(qlist, mode=mode)
        if saved:
            saved_paths[mode] = saved

    # 4) latest.json + catalog.json aktualisieren
    if saved_paths:
        update_latest_and_catalog(saved_paths)


if __name__ == "__main__":
    main()
