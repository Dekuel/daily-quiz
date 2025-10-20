# kategorien/physik.py
# -*- coding: utf-8 -*-
import os, sys, re, json, time, random, importlib, importlib.util
from types import ModuleType
from typing import Optional, List, Tuple, Dict
from openai import OpenAI

# ──────────────────────────────────────────────────────────────────────────────
# Pfad-Setup: <repo_root> auf sys.path, damit 'Unterkategorien' sicher importierbar ist
# Dieses File liegt bei: <repo_root>/kategorien/physik.py → ein Verzeichnis hoch = <repo_root>
# ──────────────────────────────────────────────────────────────────────────────
_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

CATEGORY_NAME = "Physik"

# Disziplin → Modulpfad (Top-Level groß geschrieben; wir probieren bei Bedarf auch klein)
_SUBMODULE_PATHS: Dict[str, str] = {
    "Klassische Mechanik":        "Unterkategorien.Physik.klassische_mechanik",
    "Analytische Mechanik":       "Unterkategorien.Physik.analytische_mechanik",
    "Thermodynamik":              "Unterkategorien.Physik.thermodynamik",
    "Elektrodynamik":             "Unterkategorien.Physik.elektrodynamik",
    "Relativitätstheorie":        "Unterkategorien.Physik.srt",
    "Quantenmechanik":            "Unterkategorien.Physik.quantenmechanik",
    "Optik":                      "Unterkategorien.Physik.optik",
    "Kern- und Teilchenphysik":   "Unterkategorien.Physik.kernteilchen",
    "Festkörperphysik":           "Unterkategorien.Physik.festkoerper",  # ASCII!
    "Statistische Mechanik":      "Unterkategorien.Physik.statmech",
}

def _find_spec_with_casing_fallback(path: str):
    """find_spec mit Fallback auf kleingeschriebenes Top-Level ('unterkategorien.*')."""
    spec = importlib.util.find_spec(path)
    if spec is not None:
        return spec, path
    if path.startswith("Unterkategorien."):
        alt = "unterkategorien." + path[len("Unterkategorien."):]
        spec = importlib.util.find_spec(alt)
        if spec is not None:
            return spec, alt
    return None, path

def _fs_debug_for_top_package() -> str:
    """Hilfreiche Dateisystem-Diagnose, falls 'Unterkategorien' nicht gefunden wird."""
    lines = []
    for name in ("Unterkategorien", "unterkategorien"):
        pkg_dir = os.path.join(_PROJECT_ROOT, name)
        init_py = os.path.join(pkg_dir, "__init__.py")
        phys_dir = os.path.join(pkg_dir, "Physik")
        phys_init = os.path.join(phys_dir, "__init__.py")
        lines.append(f"  - Exists {pkg_dir}: {os.path.isdir(pkg_dir)}")
        lines.append(f"    - __init__.py present: {os.path.isfile(init_py)}")
        lines.append(f"    - Physik dir: {phys_dir} -> {os.path.isdir(phys_dir)}")
        lines.append(f"      - __init__.py present: {os.path.isfile(phys_init)}")
    lines.append("  - sys.path head:")
    for p in sys.path[:5]:
        lines.append(f"    * {p}")
    return "\n".join(lines)

def _load_subs_strict() -> Dict[str, List[Tuple[str, int]]]:
    errors: List[str] = []
    result: Dict[str, List[Tuple[str, int]]] = {}

    for disc, path in _SUBMODULE_PATHS.items():
        spec, used_path = _find_spec_with_casing_fallback(path)
        if spec is None:
            errors.append(f"[{disc}] Modul nicht gefunden: {path} (versucht auch casing-Fallback).")
            continue
        try:
            mod: ModuleType = importlib.import_module(used_path)
        except Exception as e:
            errors.append(f"[{disc}] Importfehler in {used_path}: {e.__class__.__name__}: {e}")
            continue

        if not hasattr(mod, "SUBDISCIPLINES"):
            errors.append(f"[{disc}] {used_path} enthält kein 'SUBDISCIPLINES'")
            continue

        subs = getattr(mod, "SUBDISCIPLINES")
        ok = (
            isinstance(subs, list) and
            all(isinstance(x, tuple) and len(x) == 2 for x in subs) and
            all(isinstance(x[0], str) and isinstance(x[1], int) for x in subs)
        )
        if not ok:
            errors.append(f"[{disc}] {used_path}.SUBDISCIPLINES hat falsches Format (List[Tuple[str,int]])")
            continue

        result[disc] = subs

    if errors:
        fsdiag = _fs_debug_for_top_package()
        raise ImportError(
            "Physik-Plugin konnte Subthemen nicht laden:\n"
            + "\n".join(f" - {e}" for e in errors)
            + "\n\nDateisystem-Check:\n" + fsdiag
        )

    return result

_SUBDISCIPLINES: Dict[str, List[Tuple[str, int]]] = _load_subs_strict()

# ──────────────────────────────────────────────────────────────────────────────
# Disziplin-Gewichte & Prompt-Schema
# ──────────────────────────────────────────────────────────────────────────────

_PHYSIK: Dict[str, int] = {
    "Klassische Mechanik": 10,
    "Thermodynamik": 10,
    "Quantenmechanik": 15,
    "Analytische Mechanik": 10,
    "Relativitätstheorie": 5,
    "Elektrodynamik": 10,
    "Optik": 10,
    "Kern- und Teilchenphysik": 10,
    "Statistische Mechanik": 10,
    "Festkörperphysik": 10,
}

_SCHEMA = """{
  "category": "Physik",
  "discipline": "Klassische Mechanik|Thermodynamik|Quantenmechanik|Analytische Mechanik|Relativitätstheorie|Elektrodynamik|Optik|Kern- und Teilchenphysik|Astrophysik|Festkörperphysik|berühmte Physiker",
  "subcategory": "...",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

_DIFF_BANDS = [
    ((1, 2), "SEHR LEICHT (1–2): Alltagsphysik, anschauliche Begriffe, kaum Fachsprache.", 0.75),
    ((3, 4), "LEICHT (3–4): Grundbegriffe/Definitionen, einfache qualitative Zusammenhänge.", 0.75),
    ((5, 6), "MITTEL (5–6): Kombination mehrerer Konzepte, einfache quantitative Aussagen ohne Rechnen.", 0.75),
    ((7, 8), "ANSPRUCHSVOLL (7–8): präzisere Konzepte/Fallunterscheidungen, engere Distraktoren.", 0.75),
    ((9,10), "SCHWER (9–10): tiefe Konzepte/Edge Cases, genaue Begriffsabgrenzungen", 0.78),
]

def _band_for_difficulty(target: int) -> Tuple[str, float]:
    for (lo, hi), note, temp in _DIFF_BANDS:
        if lo <= target <= hi:
            return note, temp
    return "MITTEL (5–6): Kombination mehrerer Konzepte.", 0.55

def _pick_weighted(pairs: List[Tuple[str, int]]) -> str:
    names, weights = zip(*pairs)
    return random.choices(list(names), weights=list(weights), k=1)[0]

def _prompt(disc: str, target_difficulty: int, mode: Optional[str], subtopic: Optional[str] = None) -> Tuple[str, float]:
    band_note, temperature = _band_for_difficulty(target_difficulty)
    sub_line = f'- Subthema: "{subtopic}"\n' if subtopic else '- Subthema: ""\n'
    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie "Physik" (Deutsch).
- Disziplin: "{disc}"
{sub_line}Ziel-Schwierigkeit: {target_difficulty}/10 – {band_note}

Vorgaben:
- Nutze das Subthema (falls nicht leer) als inhaltlichen Fokus der Frage.
- Setze "discipline" exakt auf "{disc}" und "subcategory" exakt auf das oben angegebene Subthema (oder "" wenn keins).
- Vier plausible Antwortoptionen (A–D), eine korrekt.
- Erklärung in 2–3 Sätzen: kurz, präzise, hilfreich.
- Antworte ausschließlich mit validem JSON gemäß Schema.

JSON-SCHEMA:
{_SCHEMA}
""".strip()
    return prompt, temperature

def _normalize_choice_letter(s: str) -> str:
    s = (s or "").strip()
    if not s:
        return ""
    c = s[0].upper()
    return c if c in "ABCD" else ""

def _postprocess(data: dict) -> Optional[dict]:
    if not isinstance(data, dict):
        return None
    if "choices" not in data or "correct_answer" not in data or "question" not in data:
        return None

    raw_choices = data["choices"]
    if not isinstance(raw_choices, list) or len(raw_choices) != 4:
        return None
    norm_choices: List[str] = []
    for c in raw_choices:
        c = str(c)
        if len(c) >= 2 and c[0].upper() in "ABCD" and c[1] in [":", ")", "."]:
            c = c[2:].strip()
        norm_choices.append(c)
    data["choices"] = norm_choices

    ca = _normalize_choice_letter(str(data["correct_answer"]))
    if ca not in "ABCD":
        return None
    data["correct_answer"] = ca

    if not isinstance(data["question"], str) or not data["question"].strip():
        return None
    if not isinstance(data.get("explanation", ""), str):
        data["explanation"] = ""

    return data

def _ask_json(p: str, temperature: float) -> Optional[dict]:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Antworte ausschließlich mit valide parsem barem JSON."},
            {"role": "user", "content": p},
        ],
        temperature=temperature,
    )
    raw = r.choices[0].message.content.strip()
    m = re.search(r"\{.*\}", raw, re.DOTALL)
    return json.loads(m.group(0)) if m else None

def _pick_disc() -> str:
    return random.choices(list(_PHYSIK.keys()), weights=list(_PHYSIK.values()), k=1)[0]

def generate_one(past_texts: List[str], target_difficulty: Optional[int] = None, mode: Optional[str] = None) -> Optional[dict]:
    disc = _pick_disc()
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([6, 8])

    sub: Optional[str] = None
    subs_for_disc = _SUBDISCIPLINES.get(disc, [])
    if subs_for_disc:
        sub = _pick_weighted(subs_for_disc)

    prompt, temp = _prompt(disc, tier, mode, subtopic=sub)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.8)

    if not data:
        return None

    data["category"] = CATEGORY_NAME
    data["discipline"] = data.get("discipline", disc)
    data["subcategory"] = data.get("subcategory", sub or "")
    data["difficulty"] = int(data.get("difficulty", tier))

    data = _postprocess(data)
    return data

def make_question(*args, **kwargs):
    return generate_one(*args, **kwargs)

PLUGIN = {
    "key": "physik",
    "name": CATEGORY_NAME,
    "generator": generate_one,
}
