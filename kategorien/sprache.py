# kategorien/sprache.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from openai import OpenAI

CATEGORY_NAME = "Sprache"

_THEMES = {"Grammatik":30,"Wortherkunft":30,"Redewendungen":25,"Fremdsprachen":15}

_SCHEMA = """{
  "category": "Sprache",
  "topic": "Grammatik|Wortherkunft|Redewendungen|Fremdsprachen",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich."
}"""

def _prompt(topic: str) -> str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D) zur Kategorie „Sprache“, Thema „{topic}“.
- Auf Deutsch formulieren.
- Verständlich für Laien.
- Wenn Fachbegriff: kurz erklären.
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
    t = random.choices(list(_THEMES.keys()), weights=_THEMES.values(), k=1)[0]
    d = _ask_json(_prompt(t))
    time.sleep(0.8)
    if not d: return None
    d["category"] = CATEGORY_NAME
    d["topic"] = d.get("topic", t)
    return d
