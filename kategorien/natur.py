# kategorien/natur.py
# -*- coding: utf-8 -*-
import os, sys, re, json, time, random, importlib, importlib.util
from types import ModuleType
from typing import Optional, List, Tuple, Dict, Any
from openai import OpenAI

CATEGORY_NAME = "Natur"

# ──────────────────────────────────────────────────────────────────────────────
# sys.path-Bootstrap (wie in geographie.py)
# ──────────────────────────────────────────────────────────────────────────────
_THIS = os.path.abspath(__file__)
_DIR  = os.path.dirname(_THIS)

_CANDIDATE_ROOTS = [
    os.path.abspath(os.path.join(_DIR, "..")),        # <repo root>
    os.path.abspath(os.path.join(_DIR, "..", "..")),  # verschachtelte Repos
    os.path.abspath(os.getcwd()),                     # CI working dir
]

def _ensure_root_on_syspath() -> Optional[str]:
    for root in _CANDIDATE_ROOTS:
        if os.path.isdir(os.path.join(root, "Unterkategorien")):
            if root not in sys.path:
                sys.path.insert(0, root)
            return root
    for root in _CANDIDATE_ROOTS:
        kat_dir = os.path.join(root, "kategorien")
        if os.path.isdir(os.path.join(kat_dir, "Unterkategorien")):
            if kat_dir not in sys.path:
                sys.path.insert(0, kat_dir)
            return kat_dir
    return None

_PROJECT_ANCHOR = _ensure_root_on_syspath()

def _fs_debug() -> str:
    bases = []
    if _PROJECT_ANCHOR:
        bases.append(_PROJECT_ANCHOR)
        k = os.path.join(_PROJECT_ANCHOR, "kategorien")
        if os.path.isdir(k):
            bases.append(k)
    else:
        bases.append(_DIR)

    lines = []
    for base in bases:
        pkg = os.path.join(base, "Unterkategorien")
        rp  = os.path.join(pkg, "Natur")
        lines.append(f"Base: {base}")
        lines.append(f"  - Exists {pkg}: {os.path.isdir(pkg)}")
        lines.append(f"  - Exists {rp}: {os.path.isdir(rp)}")
        if os.path.isdir(pkg):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(pkg,'__init__.py'))}")
        if os.path.isdir(rp):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(rp,'__init__.py'))}")
            for mod in (
                "pflanzenwelt",
                "tierwelt",
                "oekosysteme",
                "wetter_klima",
            ):
                lines.append(f"    - {mod}.py: {os.path.isfile(os.path.join(rp, mod + '.py'))}")
    lines.append("sys.path (head):")
    for p in sys.path[:6]:
        lines.append("  * " + p)
    return "\n".join(lines)

# ──────────────────────────────────────────────────────────────────────────────
# Oberthemen & Gewichte + Bucket-Gewichte (1–4 / 5–7 / 8–10)
# ──────────────────────────────────────────────────────────────────────────────
_TOPICS: Dict[str, int] = {
    "Pflanzenwelt": 40,
    "Tierwelt": 40,
    "Lebensräume & Ökosysteme": 12,
    "Wetter & Klima": 8,
}

_TOPIC_WEIGHTS_BY_BUCKET: Dict[str, Dict[str, int]] = {
    "1-4": {
        "Pflanzenwelt": 48,
        "Tierwelt": 48,
        "Lebensräume & Ökosysteme": 2,
        "Wetter & Klima": 2,
    },
    "5-7": {
        "Pflanzenwelt": 40,
        "Tierwelt": 40,
        "Lebensräume & Ökosysteme": 12,
        "Wetter & Klima": 8,
    },
    "8-10": {
        "Pflanzenwelt": 38,
        "Tierwelt": 38,
        "Lebensräume & Ökosysteme": 15,
        "Wetter & Klima": 9,
    },
}

def _bucket_for(d: int) -> str:
    if d <= 4: return "1-4"
    if d <= 7: return "5-7"
    return "8-10"

def _pick_topic_for_difficulty(d: int) -> str:
    bucket = _bucket_for(d)
    weights_map = _TOPIC_WEIGHTS_BY_BUCKET.get(bucket, _TOPICS)
    names = list(weights_map.keys())
    weights = [weights_map[n] for n in names]
    return random.choices(names, weights=weights, k=1)[0]

# Topic -> Modulpfad in Unterkategorien/Natur/*.py
_SUBMODULE_PATHS: Dict[str, str] = {
    "Pflanzenwelt":               "Unterkategorien.Natur.pflanzenwelt",
    "Tierwelt":                   "Unterkategorien.Natur.tierwelt",
    "Lebensräume & Ökosysteme":   "Unterkategorien.Natur.oekosysteme",
    "Wetter & Klima":             "Unterkategorien.Natur.wetter_klima",
}

# ──────────────────────────────────────────────────────────────────────────────
# Loader: SUBTOPICS/SUBDISCIPLINES als Liste von Tupeln
#   ("Name", weight) oder ("Name", weight, (min_d, max_d))
# ──────────────────────────────────────────────────────────────────────────────
_SUBTOPICS: Dict[str, List[Dict[str, Any]]] = {}

def _load_subtopics_from_module(mod: ModuleType) -> List[Dict[str, Any]]:
    if hasattr(mod, "SUBTOPICS"):
        data = getattr(mod, "SUBTOPICS")
    elif hasattr(mod, "SUBDISCIPLINES"):
        data = getattr(mod, "SUBDISCIPLINES")
    else:
        raise AttributeError("weder SUBTOPICS noch SUBDISCIPLINES gefunden")

    if not isinstance(data, list):
        raise TypeError("SUBTOPICS/SUBDISCIPLINES muss eine Liste sein")

    normed: List[Dict[str, Any]] = []
    for item in data:
        if not isinstance(item, tuple):
            raise TypeError("Eintrag muss Tuple sein")
        if len(item) == 2:
            name, w = item
            rng = (1, 10)
        elif len(item) == 3:
            name, w, rng = item
            if not (isinstance(rng, tuple) and len(rng) == 2 and all(isinstance(x, int) for x in rng)):
                raise TypeError("Range muss Tuple[int,int] sein")
        else:
            raise TypeError("Tuple-Länge 2 oder 3 erwartet")

        if not (isinstance(name, str) and isinstance(w, int)):
            raise TypeError("Format (str,int[, (int,int)]) erwartet")

        mn, mx = rng
        mn = max(1, min(10, mn))
        mx = max(1, min(10, mx))
        if mn > mx:
            mn, mx = mx, mn

        normed.append({
            "name": name,
            "weight": w,
            "min_difficulty": mn,
            "max_difficulty": mx,
        })

    return normed

def _load_all_subtopics_strict() -> Dict[str, List[Dict[str, Any]]]:
    errors: List[str] = []
    result: Dict[str, List[Dict[str, Any]]] = {}
    for topic, module_path in _SUBMODULE_PATHS.items():
        try:
            spec = importlib.util.find_spec(module_path)
        except ModuleNotFoundError:
            spec = None
        if spec is None:
            errors.append(f"[{topic}] Modul nicht gefunden: {module_path}")
            continue
        try:
            mod = importlib.import_module(module_path)
            result[topic] = _load_subtopics_from_module(mod)
        except Exception as e:
            errors.append(f"[{topic}] Import-/Ladefehler in {module_path}: {e.__class__.__name__}: {e}")
            continue

    if errors:
        raise ImportError(
            "Natur-Plugin konnte Unterthemen nicht laden:\n"
            + "\n".join(f" - {e}" for e in errors)
            + "\n\nDateisystem-Check:\n" + _fs_debug()
        )
    return result

_SUBTOPICS = _load_all_subtopics_strict()

# ──────────────────────────────────────────────────────────────────────────────
# Auswahl-Hilfen
# ──────────────────────────────────────────────────────────────────────────────
def _pick_weighted_name(dicts: List[Dict[str, Any]]) -> Optional[str]:
    if not dicts:
        return None
    names = [d["name"] for d in dicts]
    weights = [d["weight"] for d in dicts]
    return random.choices(names, weights=weights, k=1)[0]

def _choose_subdiscipline(topic: str, target_difficulty: int) -> Optional[str]:
    entries = _SUBTOPICS.get(topic, [])
    eligible = [d for d in entries if d["min_difficulty"] <= target_difficulty <= d["max_difficulty"]]
    if eligible:
        return _pick_weighted_name(eligible)
    for delta in (1, 2, 3):
        eligible = [d for d in entries if (d["min_difficulty"] - delta) <= target_difficulty <= (d["max_difficulty"] + delta)]
        if eligible:
            return _pick_weighted_name(eligible)
    return _pick_weighted_name(entries)

# ──────────────────────────────────────────────────────────────────────────────
# Prompting & Schema
# ──────────────────────────────────────────────────────────────────────────────
_SCHEMA = """{
  "category": "Natur",
  "topic": "Pflanzenwelt|Tierwelt|Lebensräume & Ökosysteme|Wetter & Klima",
  "question": "...",
  "choices": ["A: ...", "B: ...", "C: ...", "D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

_DIFF_GUIDE = """
1 = absolutes Grundwissen (≈ 95 % der Bevölkerung in DE)
2 = sehr einfaches Grundwissen
3 = einfache Fragen (ohne schwere Thematik)
4 = leichte Fragen (Recall, einfache Anwendung)
5 = einfach–mittel (70–80 % schaffbar)
6 = mittlere Komplexität (≈ 60 % schaffbar)
7 = mittel–schwer (für Nicht-Expert:innen anspruchsvoll)
8 = schwer (deutliches Vorwissen/vertieftes Verständnis nötig)
9 = Expertenwissen (Fachkenntnisse erforderlich)
10 = schwerstmöglich (oberes Expertenniveau)
""".strip()

_DIFF_LEVELS: Dict[int, str] = {
    1: "absolutes Grundwissen (≈ 95 % der Bevölkerung in DE)",
    2: "sehr einfaches Grundwissen",
    3: "einfache Fragen (ohne schwere Thematik)",
    4: "leichte Fragen (Recall, einfache Anwendung)",
    5: "einfach–mittel (70–80 % schaffbar)",
    6: "mittlere Komplexität (≈ 60 % schaffbar)",
    7: "mittel–schwer (für Nicht-Expert:innen anspruchsvoll)",
    8: "schwer (deutliches Vorwissen/vertieftes Verständnis nötig)",
    9: "Expertenwissen (Fachkenntnisse erforderlich)",
    10:"schwerstmöglich (oberes Expertenniveau)",
}

def _temperature_for(d: int) -> float:
    return 0.8 + (0.02 if d >= 9 else 0.0)

def _prompt(topic: str, target_difficulty: int, mode: Optional[str], subtopic: Optional[str] = None) -> tuple[str, float]:
    temperature = _temperature_for(int(target_difficulty))
    level_desc = _DIFF_LEVELS.get(int(target_difficulty), "siehe Stufenleitfaden")
    sub_hint = f"- Unterthema (nur als inhaltlicher Hinweis, NICHT ins JSON übernehmen): „{subtopic}“.\n" if subtopic else ""

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „{CATEGORY_NAME}“, Oberthema „{topic}“ (Deutsch).
{sub_hint}Ziel-Schwierigkeit: {target_difficulty}/10 – {level_desc}

Kontext zu Schwierigkeitsstufen (1–10):
{_DIFF_GUIDE}

Vorgaben:
- Neutrale, gut verständliche Formulierung; keine Tagesbezüge.
- Vier plausible Antworten, genau eine korrekt; keine „alle oben/keine der oben“-Optionen.
- Bevorzuge sinnvollen Kontext (Lage-/Ökosystembezug, Anpassungen, Kreisläufe) statt reiner Listenabfragen.
- Keine Rechnungen; qualitative/konzeptionelle Prüfung reicht.
- Erklärung: 2–3 Sätze, knapp und hilfreich (Einordnung, Hinweise).
- Das Feld "topic" im JSON enthält ausschließlich das Oberthema („{topic}“). Unterthema nicht ins JSON.
- Antworte ausschließlich mit **validem JSON** gemäß Schema.

JSON-SCHEMA:
{_SCHEMA}
""".strip()
    return prompt, temperature

_JSON_OBJ_RE = re.compile(r"\{.*\}", re.DOTALL)
_CHOICE_PREFIX_RE = re.compile(r"^[A-D]:\s*", re.IGNORECASE)

def _ask_json(prompt: str, temperature: float) -> dict | None:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    last_err = None
    for attempt in range(3):
        try:
            r = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Antwort ausschließlich als valides JSON, keine Zusätze."},
                    {"role": "user", "content": prompt},
                ],
                temperature=temperature,
            )
            raw = (r.choices[0].message.content or "").strip()
            m = _JSON_OBJ_RE.search(raw)
            if not m:
                raise ValueError("Kein JSON im Modell-Output gefunden")
            return json.loads(m.group(0))
        except Exception as e:
            last_err = e
            time.sleep(0.3 * (attempt + 1))
    return None

def _normalize_choice(s: str) -> str:
    return _CHOICE_PREFIX_RE.sub("", s.strip())

def _letter_to_index(letter: str) -> Optional[int]:
    if not isinstance(letter, str) or not letter:
        return None
    L = letter.strip().upper()[:1]
    return {"A":0, "B":1, "C":2, "D":3}.get(L)

# ──────────────────────────────────────────────────────────────────────────────
# Öffentliche Generator-API
# ──────────────────────────────────────────────────────────────────────────────
def generate_one(
    past_texts: List[str],
    target_difficulty: Optional[int] = None,
    mode: Optional[str] = None,
) -> dict | None:
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3, 5, 7])
    topic = _pick_topic_for_difficulty(tier)
    subtopic = _choose_subdiscipline(topic, tier)

    prompt, temp = _prompt(topic, tier, mode, subtopic=subtopic)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.6)
    if not data:
        return None

    # enforce/normalize
    data["category"]   = CATEGORY_NAME
    data["topic"]      = topic                 # überschreibt Modell-Rückgabe
    data["difficulty"] = int(data.get("difficulty", tier))

    q = data.get("question")
    choices = data.get("choices")
    ca = data.get("correct_answer")

    if not isinstance(q, str) or not q.strip():
        return None
    if not isinstance(choices, list) or len(choices) != 4 or not all(isinstance(c, str) for c in choices):
        return None

    norm_choices = [_normalize_choice(c) for c in choices]
    idx = _letter_to_index(ca)
    if idx is None or not (0 <= idx < 4):
        return None

    # Optionales Meta für Downstream (z.B. Anzeige)
    data["meta"] = f"topic={topic};subtopic={subtopic}" if subtopic else f"topic={topic}"

    # Für App-Kompatibilität (falls gewünscht):
    data["options"] = norm_choices
    data["correctIndex"] = idx

    # Original-Felder beibehalten (wenn andere Pfade sie lesen)
    data["choices"] = norm_choices
    data["correct_answer"] = "ABCD"[idx]

    if not isinstance(data.get("explanation"), str) or not data["explanation"].strip():
        return None

    return data

def make_question(*args, **kwargs):
    return generate_one(*args, **kwargs)

PLUGIN = {
    "key": "Natur",
    "name": CATEGORY_NAME,
    "generator": generate_one,
}
