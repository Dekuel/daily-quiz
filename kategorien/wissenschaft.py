# kategorien/physik.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from openai import OpenAI

CATEGORY_NAME = "Physik"

# Neue Themen mit Gewichten (Zahl × 4 = Prozentchance)
_PHYSIK = {
    "Klassische Mechanik": 8,
    "Thermodynamik": 8,
    "Quantenmechanik": 8,
    "Analytische Mechanik": 8,
    "Relativitätstheorie": 8,
    "Elektrodynamik": 8,
    "Optik": 8,
    "Kern- und Teilchenphysik": 8,
    "Astrophysik": 8,
    "Festkörperphysik": 8,
    "berühmte Physiker": 20,
}

_SCHEMA = """{
  "category": "Physik",
  "discipline": "Klassische Mechanik|Thermodynamik|Quantenmechanik|Analytische Mechanik|Relativitätstheorie|Elektrodynamik|Optik|Kern- und Teilchenphysik|Astrophysik|Festkörperphysik|berühmte Physiker",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A",
  "explanation": "2–3 Sätze, kurz und hilfreich."
}"""

def _prompt(disc: str) -> str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, eine richtig) zur Kategorie „Physik“, Disziplin „{disc}“.
- Frage soll allgemeines Wissen oder grundlegendes physikalisches Verständnis testen (nicht zu mathematisch).
- Für Laien und Studierende verständlich.
- Gib ausschließlich valides JSON gemäß Schema zurück.

JSON-SCHEMA:
{_SCHEMA}
"""

def _ask_json(p: str) -> dict | None:
    c = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        r = c.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Nur valides JSON."},
                      {"role": "user", "content": p}],
            temperature=0.7,
        )
        raw = r.choices[0].message.content.strip()
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception:
        return None

def generate_one(past_texts: list[str]) -> dict | None:
    d = random.choices(list(_PHYSIK.keys()), weights=_PHYSIK.values(), k=1)[0]
    data = _ask_json(_prompt(d))
    time.sleep(0.8)
    if not data:
        return None
    data["category"] = CATEGORY_NAME
    data["discipline"] = data.get("discipline", d)
    return data
