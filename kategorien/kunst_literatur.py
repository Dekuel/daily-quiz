# kategorien/kunst_literatur.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from openai import OpenAI

CATEGORY_NAME = "Kunst und Literatur"

_SUB = {"Kunstgeschichte":40,"Literatur":40,"Musik":20}

_SCHEMA = """{
  "category": "Kunst und Literatur",
  "subtopic": "Kunstgeschichte|Literatur|Musik",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich."
}"""

def _prompt(sub: str) -> str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D) zur Kategorie „Kunst und Literatur“, Unterthema „{sub}“.
- Kulturwissen, kein Datumsquiz.
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
    sub = random.choices(list(_SUB.keys()), weights=_SUB.values(), k=1)[0]
    data = _ask_json(_prompt(sub))
    time.sleep(0.8)
    if not data: return None
    data["category"] = CATEGORY_NAME
    data["subtopic"] = data.get("subtopic", sub)
    return data
