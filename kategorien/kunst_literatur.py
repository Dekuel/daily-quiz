# -*- coding: utf-8 -*-
# kategorien/kunst_literatur.py
import os, sys, re, json, time, random, importlib, importlib.util
from types import ModuleType
from typing import Optional, List, Tuple, Dict, Any
from openai import OpenAI

CATEGORY_NAME = "Kunst und Literatur"

# ──────────────────────────────────────────────────────────────────────────────
# sys.path-Bootstrap (wie im Religions-Modul)
# ──────────────────────────────────────────────────────────────────────────────
_THIS = os.path.abspath(__file__)
_DIR  = os.path.dirname(_THIS)

_CANDIDATE_ROOTS = [
    os.path.abspath(os.path.join(_DIR, "..")),
    os.path.abspath(os.path.join(_DIR, "..", "..")),
    os.path.abspath(os.getcwd()),
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

    files = (
        # Kunst
        "bildende_kunst_malerei", "kunstgeschichte_epochen",
        "moderne_zeitgenoessische_kunst", "kunstwissen_allgemeines",
        # Literatur
        "klassische_werke_autoren", "epochen_stroemungen",
        "weltliteratur_genres", "zitate_figuren_allgemeinwissen",
        # Musik
        "musikgeschichte_epochen", "kuenstler_bands_hits",
        "genres_stilrichtungen", "musikwissen_theorie_allgemein",
    )

    lines = []
    for base in bases:
        pkg = os.path.join(base, "Unterkategorien")
        kp  = os.path.join(pkg, "KunstLiteratur")
        lines.append(f"Base: {base}")
        lines.append(f"  - Exists {pkg}: {os.path.isdir(pkg)}")
        lines.append(f"  - Exists {kp}: {os.path.isdir(kp)}")
        if os.path.isdir(pkg):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(pkg,'__init__.py'))}")
        if os.path.isdir(kp):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(kp,'__init__.py'))}")
            for mod in files:
                lines.append(f"    - {mod}.py: {os.path.isfile(os.path.join(kp, mod + '.py'))}")
    lines.append("sys.path (head):")
    for p in sys.path[:6]:
        lines.append("  * " + p)
    return "\n".join(lines)

# ──────────────────────────────────────────────────────────────────────────────
# Oberthemen (Topics) & Gewichte
#   Kunst (4×10), Literatur (4×10), Musik (4×5)  → sum = 100
# ──────────────────────────────────────────────────────────────────────────────
TOPICS_ART = [
    "Bildende Kunst & Malerei",
    "Kunstgeschichte & Epochen",
    "Moderne & Zeitgenössische Kunst",
    "Kunstwissen & Allgemeines",
]
TOPICS_LIT = [
    "Klassische Werke & Autoren",
    "Epochen & Strömungen",
    "Weltliteratur & Genres",
    "Zitate, Figuren & Allgemeinwissen",
]
TOPICS_MUS = [
    "Musikgeschichte & Epochen",
    "Künstler, Bands & Hits",
    "Musikgenres & Stilrichtungen",
    "Allgemeines Musikwissen & Theorie",
]

_TOPICS: Dict[str, int] = {
    **{t: 10 for t in TOPICS_ART},
    **{t: 10 for t in TOPICS_LIT},
    **{t: 5  for t in TOPICS_MUS},
}

# Buckets beibehaltenes Verhältnis (Art≈45, Lit≈40, Mus≈15 etc.), gleichmäßig verteilt
_TOPIC_WEIGHTS_BY_BUCKET: Dict[str, Dict[str, int]] = {
    "1-4": {
        # Kunst 45 → 12,11,11,11
        TOPICS_ART[0]: 5, TOPICS_ART[1]: 16, TOPICS_ART[2]: 6, TOPICS_ART[3]: 16,
        # Literatur 40 → 10,10,10,10
        TOPICS_LIT[0]: 5, TOPICS_LIT[1]: 6, TOPICS_LIT[2]: 6, TOPICS_LIT[3]: 20,
        # Musik 15 → 4,4,4,3
        TOPICS_MUS[0]: 6,  TOPICS_MUS[1]: 6,  TOPICS_MUS[2]: 6,  TOPICS_MUS[3]: 2,
    },
    "5-7": {
        # Kunst 38 → 10,10,9,9
        TOPICS_ART[0]: 8, TOPICS_ART[1]: 12, TOPICS_ART[2]: 8,  TOPICS_ART[3]: 12,
        # Literatur 40 → 10,10,10,10
        TOPICS_LIT[0]: 7, TOPICS_LIT[1]: 7, TOPICS_LIT[2]: 7, TOPICS_LIT[3]: 19,
        # Musik 22 → 6,6,5,5
        TOPICS_MUS[0]: 5,  TOPICS_MUS[1]: 5,  TOPICS_MUS[2]: 5,  TOPICS_MUS[3]: 5,
    },
    "8-10": {
        # Kunst 32 → 8,8,8,8
        TOPICS_ART[0]: 10,  TOPICS_ART[1]: 10,  TOPICS_ART[2]: 10,  TOPICS_ART[3]: 10,
        # Literatur 40 → 10,10,10,10
        TOPICS_LIT[0]: 10, TOPICS_LIT[1]: 10, TOPICS_LIT[2]: 10, TOPICS_LIT[3]: 10,
        # Musik 28 → 7,7,7,7
        TOPICS_MUS[0]: 6,  TOPICS_MUS[1]: 2,  TOPICS_MUS[2]: 6,  TOPICS_MUS[3]: 6,
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

# Topic -> Modulpfad
_SUBMODULE_PATHS: Dict[str, str] = {
    # Kunst
    "Bildende Kunst & Malerei":      "Unterkategorien.KunstLiteratur.bildende_kunst_malerei",
    "Kunstgeschichte & Epochen":     "Unterkategorien.KunstLiteratur.kunstgeschichte_epochen",
    "Moderne & Zeitgenössische Kunst":"Unterkategorien.KunstLiteratur.moderne_zeitgenoessische_kunst",
    "Kunstwissen & Allgemeines":     "Unterkategorien.KunstLiteratur.kunstwissen_allgemeines",
    # Literatur
    "Klassische Werke & Autoren":    "Unterkategorien.KunstLiteratur.klassische_werke_autoren",
    "Epochen & Strömungen":          "Unterkategorien.KunstLiteratur.epochen_stroemungen",
    "Weltliteratur & Genres":        "Unterkategorien.KunstLiteratur.weltliteratur_genres",
    "Zitate, Figuren & Allgemeinwissen":"Unterkategorien.KunstLiteratur.zitate_figuren_allgemeinwissen",
    # Musik
    "Musikgeschichte & Epochen":     "Unterkategorien.KunstLiteratur.musikgeschichte_epochen",
    "Künstler, Bands & Hits":        "Unterkategorien.KunstLiteratur.kuenstler_bands_hits",
    "Musikgenres & Stilrichtungen":       "Unterkategorien.KunstLiteratur.genres_stilrichtungen",
    "Allgemeines Musikwissen & Theorie":"Unterkategorien.KunstLiteratur.musikwissen_theorie_allgemein",
}

# topic -> List[Dict(name,weight,min_difficulty,max_difficulty)]
_SUBTOPICS: Dict[str, List[Dict[str, Any]]] = {}

# ──────────────────────────────────────────────────────────────────────────────
# Loader (akzeptiert 2er/3er-Tuples)
# ──────────────────────────────────────────────────────────────────────────────
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
            "Kunst & Literatur-Plugin konnte Unterthemen nicht laden:\n"
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
  "category": "Kunst und Literatur",
  "topic": "Bildende Kunst & Malerei|Kunstgeschichte & Epochen|Moderne & Zeitgenössische Kunst|Kunstwissen & Allgemeines|Klassische Werke & Autoren|Epochen & Strömungen|Weltliteratur & Genres|Zitate, Figuren & Allgemeinwissen|Musikgeschichte & Epochen|Künstler, Bands & Hits|Genres & Stilrichtungen|Allgemeines Musikwissen & Theorie",
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

def _prompt(topic: str, target_difficulty: int, mode: Optional[str], subtopic: Optional[str] = None) -> tuple[str, float]:
    if target_difficulty <= 2:
        temperature = 0.8
    elif target_difficulty <= 4:
        temperature = 0.8
    elif target_difficulty <= 6:
        temperature = 0.8
    elif target_difficulty <= 8:
        temperature = 0.8
    else:
        temperature = 0.82

    level_desc = _DIFF_LEVELS.get(int(target_difficulty), "siehe Stufenleitfaden")
    sub_hint = f"- Unterthema (nur als inhaltlicher Hinweis, NICHT ins JSON übernehmen): „{subtopic}“.\n" if subtopic else ""

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „{CATEGORY_NAME}“, Oberthema „{topic}“ (Deutsch).
{sub_hint}Ziel-Schwierigkeit: {target_difficulty}/10 – {level_desc}

Kontext zu Schwierigkeitsstufen (1–10):
{_DIFF_GUIDE}

Vorgaben:
- Neutrale, gut verständliche Formulierung; keine Gegenwarts-/Tagesbezüge.
- Kultur-/Werkverständnis statt reine Datumsraterei; Daten nur, wenn sinnvoll.
- Keine „alle oben/keine der oben“-Optionen; vier plausible Antworten, genau eine korrekt.
- Erklärung: 2–3 Sätze, knapp und hilfreich (ggf. Stilrichtung/Einordnung/Datierung).
- Das Feld "topic" im JSON enthält ausschließlich das Oberthema („{topic}“). Unterthema nicht ins JSON.
- Antworte ausschließlich mit **validem JSON** gemäß Schema.
-Vermeide Fragen, in denen die richtige Lösung oder Varianten davon bereits im Fragetext vorkommen. Auch konjugierte, abgewandelte oder zusammengesetzte Formen der Lösung dürfen nicht im Fragetext vorkommen.


JSON-SCHEMA:
{_SCHEMA}
""".strip()
    return prompt, temperature

def _ask_json(prompt: str, temperature: float) -> dict | None:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Antwort ausschließlich als valides JSON, keine Zusätze."},
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
        )
        raw = r.choices[0].message.content.strip()
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception:
        return None

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

    data["category"]   = CATEGORY_NAME
    data["topic"]      = topic
    data["difficulty"] = int(data.get("difficulty", tier))

    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str):
        return None

    return data

def make_question(*args, **kwargs):
    return generate_one(*args, **kwargs)

PLUGIN = {
    "key": "Kunst und Literatur",
    "name": CATEGORY_NAME,
    "generator": generate_one,
}
