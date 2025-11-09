# kategorien/geographie.py
# -*- coding: utf-8 -*-
import os, sys, re, json, time, random, importlib, importlib.util
from types import ModuleType
from typing import Optional, List, Tuple, Dict, Any
from openai import OpenAI

CATEGORY_NAME = "Geographie"

# ──────────────────────────────────────────────────────────────────────────────
# sys.path-Bootstrap (wie im Religion-Plugin)
# ──────────────────────────────────────────────────────────────────────────────
_THIS = os.path.abspath(__file__)
_DIR  = os.path.dirname(_THIS)

_CANDIDATE_ROOTS = [
    os.path.abspath(os.path.join(_DIR, "..")),        # <root>
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
        rp  = os.path.join(pkg, "Geographie")
        lines.append(f"Base: {base}")
        lines.append(f"  - Exists {pkg}: {os.path.isdir(pkg)}")
        lines.append(f"  - Exists {rp}: {os.path.isdir(rp)}")
        if os.path.isdir(pkg):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(pkg,'__init__.py'))}")
        if os.path.isdir(rp):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(rp,'__init__.py'))}")
            for mod in (
                "hauptstaedte",
                "staedte_laender_flaggen",
                "gewaesser",
                "relief_inseln_gebirge",
                "humangeographie_staede_wirtschaft",
                "klima_biome_naturregionen",
                "kartographie_gis",
                "naturkatastrophen_georisiken",
            ):
                lines.append(f"    - {mod}.py: {os.path.isfile(os.path.join(rp, mod + '.py'))}")
    lines.append("sys.path (head):")
    for p in sys.path[:6]:
        lines.append("  * " + p)
    return "\n".join(lines)

# ──────────────────────────────────────────────────────────────────────────────
# Oberthemen & Gewichte (inkl. „Naturkatastrophen & Georisiken“)
# plus Bucket-spezifische Gewichte für 1–4 / 5–7 / 8–10
# ──────────────────────────────────────────────────────────────────────────────
_TOPICS: Dict[str, int] = {
    "Hauptstädte": 18,
    "Städte, Länder & Flaggen": 18,
    "Flüsse, Seen & Meere": 14,
    "Gebirge, Inseln & Relief": 14,
    "Humangeographie & Städte": 12,
    "Klima, Biome & Naturregionen": 10,
    "Kartographie & GIS": 7,
    "Naturkatastrophen & Georisiken": 7,
}

_TOPIC_WEIGHTS_BY_BUCKET: Dict[str, Dict[str, int]] = {
    "1-4": {
        "Hauptstädte": 38,
        "Städte, Länder & Flaggen": 20,
        "Flüsse, Seen & Meere": 14,
        "Gebirge, Inseln & Relief": 14,
        "Humangeographie & Städte": 6,
        "Klima, Biome & Naturregionen": 4,
        "Kartographie & GIS": 2,
        "Naturkatastrophen & Georisiken": 2,
    },
    "5-7": {
        "Hauptstädte": 25,
        "Städte, Länder & Flaggen": 17,
        "Flüsse, Seen & Meere": 19,
        "Gebirge, Inseln & Relief": 17,
        "Humangeographie & Städte": 10,
        "Klima, Biome & Naturregionen": 6,
        "Kartographie & GIS": 3,
        "Naturkatastrophen & Georisiken": 3,
    },
    "8-10": {
        "Hauptstädte": 18,
        "Städte, Länder & Flaggen": 18,
        "Flüsse, Seen & Meere": 18,
        "Gebirge, Inseln & Relief": 18,
        "Humangeographie & Städte": 10,
        "Klima, Biome & Naturregionen": 7,
        "Kartographie & GIS": 6,
        "Naturkatastrophen & Georisiken": 7,
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
    "Hauptstädte":                      "Unterkategorien.Geographie.hauptstaedte",
    "Städte, Länder & Flaggen":        "Unterkategorien.Geographie.staedte_laender_flaggen",
    "Flüsse, Seen & Meere":            "Unterkategorien.Geographie.gewaesser",
    "Gebirge, Inseln & Relief":        "Unterkategorien.Geographie.relief_inseln_gebirge",
    "Humangeographie & Städte":        "Unterkategorien.Geographie.humangeographie_staede_wirtschaft",
    "Klima, Biome & Naturregionen":    "Unterkategorien.Geographie.klima_biome_naturregionen",
    "Kartographie & GIS":              "Unterkategorien.Geographie.kartographie_gis",
    "Naturkatastrophen & Georisiken":  "Unterkategorien.Geographie.naturkatastrophen_georisiken",
}

# Geladene Unterthemen
_SUBTOPICS: Dict[str, List[Dict[str, Any]]] = {}

# ──────────────────────────────────────────────────────────────────────────────
# Loader
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
            "Geographie-Plugin konnte Unterthemen nicht laden:\n"
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
  "category": "Geographie",
  "topic": "Hauptstädte|Städte, Länder & Flaggen|Flüsse, Seen & Meere|Gebirge, Inseln & Relief|Humangeographie & Städte|Klima, Biome & Naturregionen|Kartographie & GIS|Naturkatastrophen & Georisiken",
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
- Vier plausible Antworten, genau eine korrekt; keine „alle oben/keine der oben“-Optionen.
- Bevorzuge sinnvollen Kontext statt bloßer Listenabfragen (z. B. Lagebezug, Nachbarländer, Flussverläufe, Reliefbezug).
- Keine Rechnungen; qualitative/konzeptionelle Prüfung reicht.
- Erklärung: 2–3 Sätze, knapp und hilfreich (ggf. Lagehinweise, Einordnung).
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
    "key": "Geographie",
    "name": CATEGORY_NAME,
    "generator": generate_one,
}
