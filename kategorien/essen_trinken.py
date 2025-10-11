# kategorien/essen_trinken.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from openai import OpenAI

CATEGORY_NAME = "Essen und Trinken"

_TOPICS = {"Küche international":40,"Ernährung":30,"Getränke":15,"Kulinarische Geschichte":15}

_SCHEMA = """{
  "category": "Essen und Trinken",
  "topic": "Küche international|Ernährung|Getränke|Kulinarische Geschichte",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A",
  "explanation": "2–3 Sätze, kurz und hilfreich."
}"""

def _prompt(topic: str) -> str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, eine richtig) zur Kategorie „Essen und Trinken“, Thema „{topic}“.
- Keine Rezeptdetails, sondern Hintergrundwissen oder Ursprung.
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
    t = random.choices(list(_TOPICS.keys()), weights=_TOPICS.values(), k=1)[0]
    d = _ask_json(_prompt(t))
    time.sleep(0.8)
    if not d: return None
    d["category"] = CATEGORY_NAME
    d["topic"] = d.get("topic", t)
    return d
