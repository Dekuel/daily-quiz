# kategorien/sport.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional
from openai import OpenAI

CATEGORY_NAME = "Sport"

_SPORTS = {
    "Fußball": 30,
    "Olympische Spiele": 20,
    "Tennis": 15,
    "Formel 1": 15,
    "Basketball": 10,
    "Sonstige": 10,
}

_SCHEMA = """{
  "category": "Sport",
  "discipline": "Fußball|Olympische Spiele|Tennis|Formel 1|Basketball|Sonstige",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

# Schwierigkeitsbänder (feiner als nur leicht/mittel/schwer)
_DIFF_BANDS = [
    ((1, 2), "SEHR LEICHT (1–2): weithin bekannte Regeln, ikonische Personen/Ereignisse; klare Distraktoren.", 0.75),
    ((3, 4), "LEICHT (3–4): Grundwissen zu Turnieren, Positionen, einfachen Statistiken oder Rekorden.", 0.75),
    ((5, 6), "MITTEL (5–6): taktische Grundkonzepte, historische Kontexte, differenzierte Regeln.", 0.75),
    ((7, 8), "ANSPRUCHSVOLL (7–8): seltenere Fakten, präzise Regelausnahmen, vergleichende Rekorde.", 0.75),
    ((9,10), "SCHWER (9–10): Detailwissen (z. B. spezifische Regelpassagen, historische Sonderfälle, exakte Zuordnungen).", 0.82),
]

def _band_for_difficulty(target: int) -> tuple[str, float]:
    t = int(target)
    for (lo, hi), note, temp in _DIFF_BANDS:
        if lo <= t <= hi:
            return note, temp
    return "MITTEL (5–6): taktische Grundkonzepte, historische Kontexte.", 0.55

def _prompt(disc: str, target_difficulty: int, mode: Optional[str]) -> tuple[str, float]:
    band_note, temperature = _band_for_difficulty(target_difficulty)

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „Sport“, Disziplin „{disc}“ (Deutsch).
Ziel-Schwierigkeit: {target_difficulty}/10 – {band_note}

Vorgaben:
- Allgemeines Sportwissen; vermeide tagesaktuelle Ergebnisse/Transfers (keine Datumsabhängigkeit).
- Klar verständlich für Laien, dennoch präzise.
- Vier plausible Antwortoptionen (A–D), eine korrekt; keine Optionen wie „alle oben/keine der oben“.
- Erklärung in 2–3 Sätzen, die die richtige Lösung knapp begründet.
- Gib ausschließlich valides JSON gemäß Schema zurück.

JSON-SCHEMA:
{_SCHEMA}
""".strip()

    return prompt, temperature


def _ask_json(p: str, temperature: float) -> dict | None:
    c = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        r = c.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Antworte ausschließlich mit valide parsem barem JSON (kein Text außerhalb des JSON)."},
                {"role": "user", "content": p},
            ],
            temperature=temperature,
        )
        raw = r.choices[0].message.content.strip()
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception:
        return None


def _pick_disc() -> str:
    names, weights = list(_SPORTS.keys()), list(_SPORTS.values())
    return random.choices(names, weights=weights, k=1)[0]


def generate_one(
    past_texts: list[str],
    target_difficulty: Optional[int] = None,
    mode: Optional[str] = None,
) -> dict | None:
    """
    Wird vom Core mit target_difficulty (1..10) und mode ("normal"|"schwer"|"physik") aufgerufen.
    Fallback bei fehlender target_difficulty: moderater Zielwert.
    """
    disc = _pick_disc()
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3, 5, 7])
    prompt, temp = _prompt(disc, tier, mode)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.8)
    if not data:
        return None

    # Pflichtfelder pflegen/normalisieren
    data["category"] = CATEGORY_NAME
    data["discipline"] = data.get("discipline", disc)
    data["difficulty"] = int(data.get("difficulty", tier))

    # minimale Validierung
    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str):
        return None

    # Shuffle passiert zentral im Core
    return data
