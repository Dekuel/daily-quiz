# -*- coding: utf-8 -*-
# kategorien/glaube_religion.py
import os, sys, re, json, time, random, importlib, importlib.util
from types import ModuleType
from typing import Optional, List, Tuple, Dict, Any
from openai import OpenAI

CATEGORY_NAME = "Glaube & Religion"

# ──────────────────────────────────────────────────────────────────────────────
# sys.path-Bootstrap: unterstütze beide Repo-Layouts
#   1) <root>/Unterkategorien/…
#   2) <root>/kategorien/Unterkategorien/…
# ──────────────────────────────────────────────────────────────────────────────
_THIS = os.path.abspath(__file__)
_DIR  = os.path.dirname(_THIS)

_CANDIDATE_ROOTS = [
    os.path.abspath(os.path.join(_DIR, "..")),        # <root>
    os.path.abspath(os.path.join(_DIR, "..", "..")),  # verschachtelte Repos
    os.path.abspath(os.getcwd()),                     # CI working dir
]

def _ensure_root_on_syspath() -> Optional[str]:
    # Fall 1: Unterkategorien direkt unter <root>
    for root in _CANDIDATE_ROOTS:
        if os.path.isdir(os.path.join(root, "Unterkategorien")):
            if root not in sys.path:
                sys.path.insert(0, root)
            return root
    # Fall 2: Unterkategorien unter <root>/kategorien
    for root in _CANDIDATE_ROOTS:
        kat_dir = os.path.join(root, "kategorien")
        if os.path.isdir(os.path.join(kat_dir, "Unterkategorien")):
            if kat_dir not in sys.path:
                sys.path.insert(0, kat_dir)
            return kat_dir
    return None

_PROJECT_ANCHOR = _ensure_root_on_syspath()

def _fs_debug() -> str:
    # Prüfe sowohl <anchor> als auch <anchor>/kategorien als Wurzel
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
        rp  = os.path.join(pkg, "Religion")
        lines.append(f"Base: {base}")
        lines.append(f"  - Exists {pkg}: {os.path.isdir(pkg)}")
        lines.append(f"  - Exists {rp}: {os.path.isdir(rp)}")
        if os.path.isdir(pkg):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(pkg,'__init__.py'))}")
        if os.path.isdir(rp):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(rp,'__init__.py'))}")
            for mod in (
                "monotheismus",
                "indien_fernost",
                "klassisch_nordisch",
                "mittelmeer_europa_rest",
                "afrika_indigen",
                "alter_orient",
                "ideen_theologie_mystik",
                "spiritualitaet_esoterik_nrb",
                "geschichte_soziologie_praxis",
            ):
                lines.append(f"    - {mod}.py: {os.path.isfile(os.path.join(rp, mod + '.py'))}")
    lines.append("sys.path (head):")
    for p in sys.path[:6]:
        lines.append("  * " + p)
    return "\n".join(lines)

# ──────────────────────────────────────────────────────────────────────────────
# Oberbereiche (Subperiods) & Gewichte
#   _SUBPERIODS: Default-Gewichte (Fallback)
#   _SUBPERIOD_WEIGHTS_BY_BUCKET: Gewichte je Schwierigkeits-Bucket 1–4 / 5–7 / 8–10
# ──────────────────────────────────────────────────────────────────────────────

_SUBPERIODS: Dict[str, int] = {
    "Monotheistische Religionen": 23,
    "Indische & fernöstliche Religionen": 11,
    "Klassische & nordische Mythologien": 34,
    "Weitere antike Mittelmeer- & europäische Mythologien": 13,
    "Afrikanische & indigene Religionen": 4,
    "Nahöstliche & altorientalische Kulte": 4,
    "Religiöse Ideen, Theologie & Mystik": 3,
    "Spiritualität, Esoterik & neue religiöse Bewegungen": 1,
    "Religionsgeschichte, Soziologie & Praxis": 5,
}

_SUBPERIOD_WEIGHTS_BY_BUCKET: Dict[str, Dict[str, int]] = {
    "1-4": {
        "Monotheistische Religionen": 40,
        "Indische & fernöstliche Religionen": 0,
        "Klassische & nordische Mythologien": 50,
        "Weitere antike Mittelmeer- & europäische Mythologien": 0,
        "Afrikanische & indigene Religionen": 0,
        "Nahöstliche & altorientalische Kulte": 0,
        "Religiöse Ideen, Theologie & Mystik": 3,
        "Spiritualität, Esoterik & neue religiöse Bewegungen": 2,
        "Religionsgeschichte, Soziologie & Praxis": 5,
    },
    "5-7": {
        "Monotheistische Religionen": 30,
        "Indische & fernöstliche Religionen": 9,
        "Klassische & nordische Mythologien": 39,
        "Weitere antike Mittelmeer- & europäische Mythologien": 4,
        "Afrikanische & indigene Religionen": 2,
        "Nahöstliche & altorientalische Kulte": 5,
        "Religiöse Ideen, Theologie & Mystik": 5,
        "Spiritualität, Esoterik & neue religiöse Bewegungen": 2,
        "Religionsgeschichte, Soziologie & Praxis": 4,
    },
    "8-10": {
        "Monotheistische Religionen": 25,
        "Indische & fernöstliche Religionen": 9,
        "Klassische & nordische Mythologien": 30,
        "Weitere antike Mittelmeer- & europäische Mythologien": 11,
        "Afrikanische & indigene Religionen": 6,
        "Nahöstliche & altorientalische Kulte": 6,
        "Religiöse Ideen, Theologie & Mystik": 6,
        "Spiritualität, Esoterik & neue religiöse Bewegungen": 2,
        "Religionsgeschichte, Soziologie & Praxis": 5,
    },
}

def _bucket_for(d: int) -> str:
    if d <= 4: return "1-4"
    if d <= 7: return "5-7"
    return "8-10"

def _pick_subperiod_for_difficulty(d: int) -> str:
    bucket = _bucket_for(d)
    weights_map = _SUBPERIOD_WEIGHTS_BY_BUCKET.get(bucket, _SUBPERIODS)
    names = list(weights_map.keys())
    weights = [weights_map[n] for n in names]
    return random.choices(names, weights=weights, k=1)[0]

# Epoche -> Modulpfad (einheitlich Religion, keine doppelte Definition)
_SUBMODULE_PATHS: Dict[str, str] = {
    "Monotheistische Religionen": "Unterkategorien.Religion.monotheismus",
    "Indische & fernöstliche Religionen": "Unterkategorien.Religion.indien_fernost",
    "Klassische & nordische Mythologien": "Unterkategorien.Religion.klassisch_nordisch",
    "Weitere antike Mittelmeer- & europäische Mythologien": "Unterkategorien.Religion.mittelmeer_europa_rest",
    "Afrikanische & indigene Religionen": "Unterkategorien.Religion.afrika_indigen",
    "Nahöstliche & altorientalische Kulte": "Unterkategorien.Religion.alter_orient",
    "Religiöse Ideen, Theologie & Mystik": "Unterkategorien.Religion.ideen_theologie_mystik",
    "Spiritualität, Esoterik & neue religiöse Bewegungen": "Unterkategorien.Religion.spiritualitaet_esoterik_nrb",
    "Religionsgeschichte, Soziologie & Praxis": "Unterkategorien.Religion.geschichte_soziologie_praxis",
}

# Geladene Unterthemen-Listen:
#   subperiod -> List[Dict(name,weight,min_difficulty,max_difficulty)]
_SUBTOPICS: Dict[str, List[Dict[str, Any]]] = {}

# ──────────────────────────────────────────────────────────────────────────────
# Loader akzeptiert 2-Tuple (name, weight) ODER 3-Tuple (name, weight, (min,max))
# ──────────────────────────────────────────────────────────────────────────────
def _load_subtopics_from_module(mod: ModuleType) -> List[Dict[str, Any]]:
    """
    Akzeptiert:
      - List[Tuple[str, int]]
      - List[Tuple[str, int, Tuple[int,int]]]
    Normalisiert auf Dict:
      { "name": str, "weight": int, "min_difficulty": int, "max_difficulty": int }
    Default-Range: (1,10)
    """
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
    for period, module_path in _SUBMODULE_PATHS.items():
        try:
            spec = importlib.util.find_spec(module_path)
        except ModuleNotFoundError:
            spec = None
        if spec is None:
            errors.append(f"[{period}] Modul nicht gefunden: {module_path}")
            continue
        try:
            mod = importlib.import_module(module_path)
            result[period] = _load_subtopics_from_module(mod)
        except Exception as e:
            errors.append(f"[{period}] Import-/Ladefehler in {module_path}: {e.__class__.__name__}: {e}")
            continue

    if errors:
        raise ImportError(
            "Glaube & Religion-Plugin konnte Unterthemen nicht laden:\n"
            + "\n".join(f" - {e}" for e in errors)
            + "\n\nDateisystem-Check:\n" + _fs_debug()
        )
    return result

# Beim Import streng laden (Fehler früh sichtbar)
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

def _choose_subdiscipline(subperiod: str, target_difficulty: int) -> Optional[str]:
    entries = _SUBTOPICS.get(subperiod, [])
    eligible = [d for d in entries if d["min_difficulty"] <= target_difficulty <= d["max_difficulty"]]
    if eligible:
        return _pick_weighted_name(eligible)
    # Sanfter Fallback, um nicht leerzulaufen
    for delta in (1, 2, 3):
        eligible = [d for d in entries if (d["min_difficulty"] - delta) <= target_difficulty <= (d["max_difficulty"] + delta)]
        if eligible:
            return _pick_weighted_name(eligible)
    return _pick_weighted_name(entries)

# ──────────────────────────────────────────────────────────────────────────────
# Prompting & Schema (korrigiert auf „Glaube & Religion“)
# ──────────────────────────────────────────────────────────────────────────────
_SCHEMA = """{
  "category": "Glaube & Religion",
  "subperiod": "Monotheistische Religionen|Indische & fernöstliche Religionen|Klassische & nordische Mythologien|Weitere antike Mittelmeer- & europäische Mythologien|Afrikanische & indigene Religionen|Nahöstliche & altorientalische Kulte|Religiöse Ideen, Theologie & Mystik|Spiritualität, Esoterik & neue religiöse Bewegungen|Religionsgeschichte, Soziologie & Praxis",
  "question": "...",
  "choices": ["A: ...", "B: ...", "C: ...", "D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

_DIFF_GUIDE = """
- 1–3 (leicht): ikonische Ereignisse oder Personen, Grundwissen.
- 4–7 (mittel): weniger bekannte Zusammenhänge, Ursachen/Folgen, einfache Datierungen.
- 8–10 (schwer): exakte Terminologie/Datierungen, komplexe Prozesse, seltene Begriffe.
"""

def _prompt(subperiod: str, target_difficulty: int, mode: Optional[str], subtopic: Optional[str] = None) -> tuple[str, float]:
    if target_difficulty <= 2:
        tier_note = "LEICHT (1–2): bekannte Fakten, teils logisch erschließbar."
        temperature = 0.8
    elif target_difficulty <= 4:
        tier_note = "MITTEL (3–4): etwas weniger bekannte Fakten, moderate Komplexität."
        temperature = 0.8
    elif target_difficulty <= 6:
        tier_note = "Etwas schwerer (5–6): spezifischere Details, engere Distraktoren."
        temperature = 0.8
    elif target_difficulty <= 8:
        tier_note = "Schwer (7–8): präzise Details oder tiefere Konzepte, enge Distraktoren."
        temperature = 0.8
    else:
        tier_note = "Sehr schwer (9–10): exakte Terminologie/Datierungen, Expertenwissen."
        temperature = 0.82

    sub_hint = f"- Unterthema (nur als inhaltlicher Hinweis, NICHT ins JSON übernehmen): „{subtopic}“.\n" if subtopic else ""

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „{CATEGORY_NAME}“, Oberbereich „{subperiod}“ (Deutsch).
{sub_hint}Ziel-Schwierigkeit: {target_difficulty}/10 – {tier_note}

Kontext zu Schwierigkeitsstufen:
{_DIFF_GUIDE}

Vorgaben:
- Neutrale, gut verständliche Formulierung; keine Gegenwarts-/Tagesbezüge.
- Keine „alle oben/keine der oben“-Optionen; vier plausible Antworten, genau eine korrekt.
- Erklärung: 2–3 Sätze, knapp und hilfreich (ggf. kurze Einordnung/Datierung).
- Das Feld "subperiod" im JSON enthält ausschließlich den Oberbereich („{subperiod}“). Unterthema nicht ins JSON.
- Antworte ausschließlich mit **validem JSON** gemäß Schema.

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
    """
    Core-Aufruf mit target_difficulty (1..10) und mode ("normal"|"schwer"|...).
    Unterthema wird aus Untermodulen geladen und dient nur als Prompt-Hinweis.
    """
    # 1) Zielschwierigkeit losen/bestimmen
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3, 5, 7])

    # 2) Subperiod abhängig von tier (Buckets)
    subperiod = _pick_subperiod_for_difficulty(tier)

    # 3) Passende Subdisziplin innerhalb der Subperiod gemäß Range-Filter
    subtopic = _choose_subdiscipline(subperiod, tier)

    # 4) Prompt bauen & Anfrage
    prompt, temp = _prompt(subperiod, tier, mode, subtopic=subtopic)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.6)
    if not data:
        return None

    # 5) Pflichtfelder normieren
    data["category"]   = CATEGORY_NAME
    data["subperiod"]  = subperiod  # Unterthema nie ins JSON übernehmen
    data["difficulty"] = int(data.get("difficulty", tier))

    # 6) Minimale Validierung
    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str):
        return None

    return data

# Optionaler Alias
def make_question(*args, **kwargs):
    return generate_one(*args, **kwargs)

# Optionales Registry-Objekt
PLUGIN = {
    "key": "Glaube & Religion",
    "name": CATEGORY_NAME,
    "generator": generate_one,
}
