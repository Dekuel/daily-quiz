# kategorien/physik.py
# -*- coding: utf-8 -*-
import os
import re
import json
import time
import random
import importlib
import importlib.util
import sys
from types import ModuleType
from typing import Optional, List, Tuple, Dict

from openai import OpenAI

# =============================================================================
# Public plugin metadata
# =============================================================================

CATEGORY_NAME = "Physik"

# =============================================================================
# Strict subtopic discovery (NO fallbacks)
# - Ensure all submodules exist, import cleanly, and expose SUBDISCIPLINES
# - Enforce ASCII for module names (e.g., festkoerper instead of festkörper)
# =============================================================================

# Mapping: canonical discipline name -> python module path
_SUBMODULE_PATHS: Dict[str, str] = {
    "Klassische Mechanik":        "Unterkategorien.Physik.klassische_mechanik",
    "Analytische Mechanik":       "Unterkategorien.Physik.analytische_mechanik",
    "Thermodynamik":              "Unterkategorien.Physik.thermodynamik",
    "Elektrodynamik":             "Unterkategorien.Physik.elektrodynamik",
    "Relativitätstheorie":        "Unterkategorien.Physik.srt",
    "Quantenmechanik":            "Unterkategorien.Physik.quantenmechanik",
    "Optik":                      "Unterkategorien.Physik.optik",
    "Kern- und Teilchenphysik":   "Unterkategorien.Physik.kernteilchen",
    "Festkörperphysik":           "Unterkategorien.Physik.festkoerper",  # ASCII only!
    "Statistische Mechanik":      "Unterkategorien.Physik.statmech",
}

def _load_subs_strict() -> Dict[str, List[Tuple[str, int]]]:
    errors: List[str] = []
    result: Dict[str, List[Tuple[str, int]]] = {}

    for disc, path in _SUBMODULE_PATHS.items():
        spec = importlib.util.find_spec(path)
        if spec is None:
            errors.append(f"[{disc}] Modul nicht gefunden: {path}")
            continue
        try:
            mod: ModuleType = importlib.import_module(path)
        except Exception as e:
            errors.append(f"[{disc}] Importfehler in {path}: {e.__class__.__name__}: {e}")
            continue

        if not hasattr(mod, "SUBDISCIPLINES"):
            errors.append(f"[{disc}] {path} enthält kein 'SUBDISCIPLINES'")
            continue

        subs = getattr(mod, "SUBDISCIPLINES")
        ok = (
            isinstance(subs, list) and
            all(isinstance(x, tuple) and len(x) == 2 for x in subs) and
            all(isinstance(x[0], str) and isinstance(x[1], int) for x in subs)
        )
        if not ok:
            errors.append(f"[{disc}] {path}.SUBDISCIPLINES hat falsches Format (erwartet List[Tuple[str,int]])")
            continue

        result[disc] = subs

    if errors:
        details = "\n".join(f" - {e}" for e in errors)
        cwd = os.getcwd()
        syspath = "\n".join(f"   - {p}" for p in sys.path)
        raise ImportError(
            "Physik-Plugin konnte Subthemen nicht laden:\n"
            f"{details}\n\n"
            f"Arbeitsverzeichnis: {cwd}\n"
            "sys.path:\n" + syspath + "\n"
            "Hinweis: Prüfe ASCII-Modulnamen (z.B. 'festkoerper' statt 'festkörper'), "
            "exakte Groß-/Kleinschreibung und __init__.py-Dateien."
        )

    return result

_SUBDISCIPLINES: Dict[str, List[Tuple[str, int]]] = _load_subs_strict()

# =============================================================================
# Discipline weights and generation schema
# =============================================================================

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

# =============================================================================
# Helpers
# =============================================================================

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
    """
    Normalize:
    - choices may come as 'A: text' ... strip the 'A:' prefix
    - correct_answer may be 'A' or 'A:' or 'a' etc.
    Return None if invalid after normalization.
    """
    if not isinstance(data, dict):
        return None
    if "choices" not in data or "correct_answer" not in data or "question" not in data:
        return None

    # Normalize choices
    raw_choices = data["choices"]
    if not isinstance(raw_choices, list) or len(raw_choices) != 4:
        return None
    norm_choices: List[str] = []
    for c in raw_choices:
        c = str(c)
        # remove "X:" / "X)" / "X." prefixes, where X in A-D
        if len(c) >= 2 and c[0].upper() in "ABCD" and c[1] in [":", ")", "."]:
            c = c[2:].strip()
        norm_choices.append(c)
    data["choices"] = norm_choices

    # Normalize correct answer
    ca = _normalize_choice_letter(str(data["correct_answer"]))
    if ca not in "ABCD":
        return None
    data["correct_answer"] = ca

    # Basic sanity
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

# =============================================================================
# Public generator API
# =============================================================================

def generate_one(past_texts: List[str], target_difficulty: Optional[int] = None, mode: Optional[str] = None) -> Optional[dict]:
    """
    Returns a single MC question dict or None (if the LLM response was unusable).
    Import-time will already have raised if any subtopic module is broken.
    """
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

# Optional alias for loaders expecting a different symbol name
def make_question(*args, **kwargs):
    return generate_one(*args, **kwargs)

# Optional plugin registry object for dynamic discovery
PLUGIN = {
    "key": "physik",
    "name": CATEGORY_NAME,
    "generator": generate_one,
}
