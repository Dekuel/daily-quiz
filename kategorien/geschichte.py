# kategorien/geschichte.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from openai import OpenAI

CATEGORY_NAME = "Geschichte"

_SUBPERIODS = {
    "Antike": 25,
    "Mittelalter": 25,
    "Neuzeit": 30,
    "Zeitgeschichte (ab 1945)": 20,
}

_SCHEMA = """{
  "category": "Geschichte",
  "subperiod": "Antike|Mittelalter|Neuzeit|Zeitgeschichte (ab 1945)",
  "question": "...",
  "choices": ["A: ...", "B: ...", "C: ...", "D: ..."],
  "correct_answer": "A",
  "explanation": "2–3 Sätze, kurz und hilfreich."
}"""

def _prompt(sub: str) -> str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, eine richtig) zur Kategorie „Geschichte“, Unterbereich „{sub}“, auf Deutsch.
- Verständlich für Laien, keine tagesaktuelle Nachricht.
- Falls Fachbegriffe vorkommen, kurz erklären.
- Gib ausschließlich valides JSON gemäß Schema zurück.

JSON-SCHEMA:
{_SCHEMA}
"""

def _ask_json(prompt: str) -> dict | None:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"system","content":"Du gibst ausschließlich valides JSON zurück."},
                      {"role":"user","content":prompt}],
            temperature=0.7,
        )
        raw = r.choices[0].message.content.strip()
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception:
        return None

def _pick() -> str:
    names, weights = list(_SUBPERIODS.keys()), list(_SUBPERIODS.values())
    return random.choices(names, weights=weights, k=1)[0]

def generate_one(past_texts: list[str]) -> dict | None:
    sub = _pick()
    data = _ask_json(_prompt(sub))
    time.sleep(0.8)
    if not data: return None
    data["category"] = CATEGORY_NAME
    data["subperiod"] = data.get("subperiod", sub)
    return data
