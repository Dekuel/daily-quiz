# kategorien/sport.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from openai import OpenAI

CATEGORY_NAME = "Sport"

_SPORTS = {"Fußball":30,"Olympische Spiele":20,"Tennis":15,"Formel 1":15,"Basketball":10,"Sonstige":10}

_SCHEMA = """{
  "category": "Sport",
  "discipline": "Fußball|Olympische Spiele|Tennis|Formel 1|Basketball|Sonstige",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich."
}"""

def _prompt(disc: str) -> str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, eine richtig) zur Kategorie „Sport“, Disziplin „{disc}“.
- Frage soll allgemeines Wissen testen (nicht nur letzte Ereignisse).
- Für Laien verständlich.
- Gib ausschließlich valides JSON gemäß Schema zurück.

JSON-SCHEMA:
{_SCHEMA}
"""

def _ask_json(p: str) -> dict | None:
    c = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        r = c.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"system","content":"Nur valides JSON."},{"role":"user","content":p}],
            temperature=0.7,
        )
        raw = r.choices[0].message.content.strip()
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception:
        return None

def generate_one(past_texts: list[str]) -> dict | None:
    d = random.choices(list(_SPORTS.keys()), weights=_SPORTS.values(), k=1)[0]
    data = _ask_json(_prompt(d))
    time.sleep(0.8)
    if not data: return None
    data["category"] = CATEGORY_NAME
    data["discipline"] = data.get("discipline", d)
    return data
