# kategorien/geschichte.py
# -*- coding: utf-8 -*-
import os, sys, re, json, time, random, importlib, importlib.util
from types import ModuleType
from typing import Optional, List, Tuple, Dict
from openai import OpenAI

CATEGORY_NAME = "Glaube & Religion"

# ──────────────────────────────────────────────────────────────────────────────
# sys.path-Bootstrap: unterstütze beide Repo-Layouts
#   1) <root>/Unterkategorien/…
#   2) <root>/kategorien/Unterkategorien/…   (dein CI-Layout)
# Keine Groß-/Kleinschreibungstricks; wir erwarten exakt "Unterkategorien".
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
        gp  = os.path.join(pkg, "Geschichte")
        lines.append(f"Base: {base}")
        lines.append(f"  - Exists {pkg}: {os.path.isdir(pkg)}")
        lines.append(f"  - Exists {gp}: {os.path.isdir(gp)}")
        if os.path.isdir(pkg):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(pkg,'__init__.py'))}")
        if os.path.isdir(gp):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(gp,'__init__.py'))}")
            for mod in ("antike","mittelalter","neuzeit","zeitgeschichte"):
                lines.append(f"    - {mod}.py: {os.path.isfile(os.path.join(gp, mod + '.py'))}")
    lines.append("sys.path (head):")
    for p in sys.path[:6]:
        lines.append("  * " + p)
    return "\n".join(lines)

# ──────────────────────────────────────────────────────────────────────────────
# Epochen & Modulpfade (ohne Case-Fallback; exakt 'Unterkategorien')
# ──────────────────────────────────────────────────────────────────────────────
# ──────────────────────────────────────────────────────────────────────────────
# Epochen & Modulpfade (9 Themenblöcke für „Glaube & Religion“)
# ──────────────────────────────────────────────────────────────────────────────
_SUBPERIODS: Dict[str, int] = {
    "Monotheistische Religionen": 20,
    "Indische & fernöstliche Religionen": 9,
    "Klassische & nordische Mythologien": 32,
    "Weitere antike Mittelmeer- & europäische Mythologien": 13,
    "Afrikanische & indigene Religionen": 8,
    "Nahöstliche & altorientalische Kulte": 7,
    "Religiöse Ideen, Theologie & Mystik": 3,
    "Spiritualität, Esoterik & neue religiöse Bewegungen": 1,
    "Religionsgeschichte, Soziologie & Praxis": 5,
}

# Epoche -> Modulpfad (lege passende Module unter Unterkategorien/Religion/… an)
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

# Epoche -> Modulpfad
_SUBMODULE_PATHS: Dict[str, str] = {
    "Antike": "Unterkategorien.Geschichte.antike",
    "Mittelalter": "Unterkategorien.Geschichte.mittelalter",
    "Neuzeit": "Unterkategorien.Geschichte.neuzeit",
    "Zeitgeschichte (ab 1945)": "Unterkategorien.Geschichte.zeitgeschichte",
}

# Geladene Unterthemen-Listen (Epoche -> List[(subtopic, weight)])
_SUBTOPICS: Dict[str, List[Tuple[str, int]]] = {}

def _load_subtopics_from_module(mod: ModuleType) -> List[Tuple[str, int]]:
    """
    Erlaubt entweder SUBTOPICS oder SUBDISCIPLINES im Untermodul.
    Erwartet: List[Tuple[str,int]].
    """
    if hasattr(mod, "SUBTOPICS"):
        data = getattr(mod, "SUBTOPICS")
    elif hasattr(mod, "SUBDISCIPLINES"):
        data = getattr(mod, "SUBDISCIPLINES")
    else:
        raise AttributeError("weder SUBTOPICS noch SUBDISCIPLINES gefunden")

    ok = (
        isinstance(data, list)
        and all(isinstance(x, tuple) and len(x) == 2 for x in data)
        and all(isinstance(x[0], str) and isinstance(x[1], int) for x in data)
    )
    if not ok:
        raise TypeError("SUBTOPICS/SUBDISCIPLINES hat falsches Format (List[Tuple[str,int]] erwartet)")
    return data

def _load_all_subtopics_strict() -> Dict[str, List[Tuple[str, int]]]:
    errors: List[str] = []
    result: Dict[str, List[Tuple[str, int]]] = {}
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

# Lade bei Import streng (damit Fehler früh sichtbar sind)
_SUBTOPICS = _load_all_subtopics_strict()

# ──────────────────────────────────────────────────────────────────────────────
# Prompting & Schema
# ──────────────────────────────────────────────────────────────────────────────
_SCHEMA = """{
  "category": "Glaube & Religion",
  "subperiod": "Antike|Mittelalter|Neuzeit|Zeitgeschichte ",
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

def _pick_weighted(pairs: List[Tuple[str, int]]) -> str:
    names, weights = zip(*pairs)
    return random.choices(list(names), weights=list(weights), k=1)[0]

def _pick_subperiod() -> str:
    names, weights = list(_SUBPERIODS.keys()), list(_SUBPERIODS.values())
    return random.choices(names, weights=weights, k=1)[0]

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
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „Geschichte“, Oberbereich „{subperiod}“ (Deutsch).
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
    past_texts: list[str],
    target_difficulty: Optional[int] = None,
    mode: Optional[str] = None,
) -> dict | None:
    """
    Core-Aufruf mit target_difficulty (1..10) und mode ("normal"|"schwer"|"physik").
    Unterthema wird aus Untermodulen geladen und dient nur als Prompt-Hinweis.
    """
    # 1) Epoche wählen
    subperiod = _pick_subperiod()

    # 2) Unterthema per Gewicht ziehen (aus Untermodulen)
    subtopic = None
    pairs = _SUBTOPICS.get(subperiod, [])
    if pairs:
        subtopic = _pick_weighted(pairs)

    # 3) Zielschwierigkeit bestimmen
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3, 5, 7])

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
