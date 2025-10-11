# kategorien/wissenschaft.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from openai import OpenAI

CATEGORY_NAME = "Wissenschaft"

# Top-Level-Themen mit Gewichten (wie gehabt)
_TOPICS = {
    "Physik": 25,
    "Biologie": 25,
    "Chemie": 20,
    "Astronomie": 15,
    "Medizin": 15,
}

# NEU: Subtopics pro Top-Level-Topic, jeweils (name, gewicht)
_SUBTOPICS = {
    "Physik": [
        ("Klassische Mechanik", 2),
        ("Thermodynamik", 2),
        ("Quantenmechanik", 2),
        ("Analytische Mechanik", 2),
        ("Relativitätstheorie", 2),
        ("Elektrodynamik", 2),
        ("Optik", 2),
        ("Kern- und Teilchenphysik", 2),
        ("Astrophysik", 2),
        ("Festkörperphysik", 2),
        ("berühmte Physiker", 5),
    ],
    "Biologie": [
        ("Genetik", 3),
        ("Evolution", 2),
        ("Ökologie", 2),
        ("Zellbiologie", 2),
        ("Neurobiologie", 1),
        ("Physiologie", 1),
        ("Mikrobiologie", 1),
        ("berühmte Biologen", 4),
    ],
    "Chemie": [
        ("Physikalische Chemie", 2),
        ("Organische Chemie", 3),
        ("Anorganische Chemie", 2),
        ("Analytische Chemie", 2),
        ("Biochemie", 1),
        ("berühmte Chemiker", 3),
    ],
    "Astronomie": [
        ("Planetenkunde", 2),
        ("Sternentwicklung", 2),
        ("Kosmologie", 2),
        ("Exoplaneten", 2),
        ("Galaxien", 1),
    ],
    "Medizin": [
        ("Kardiologie", 2),
        ("Neurologie", 2),
        ("Infektiologie", 2),
        ("Onkologie", 2),
        ("Endokrinologie", 1),
        ("Pulmologie", 1),
    ],
}

_SCHEMA = """{
  "category": "Wissenschaft",
  "topic": "Physik|Biologie|Chemie|Astronomie|Medizin",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A",
  "explanation": "2–3 Sätze, kurz und hilfreich."
}"""

def _prompt(topic: str, subtopic: str | None = None) -> str:
    sub_hint = f"Subthema (nur zur inhaltlichen Orientierung): „{subtopic}“.\n" if subtopic else ""
    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, eine richtig) zur Kategorie „Wissenschaft“, Thema „{topic}“.
{sub_hint}- Verständlich für Laien.
- Wenn Fachbegriff, kurz erklären.
- Keine reinen Definitionsfragen ohne Kontext.
- Schreibe das Subthema NICHT separat ins JSON (im Feld "topic" steht weiterhin nur „{topic}“).
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

def _pick_weighted(pairs: list[tuple[str,int]]) -> str:
    names, weights = zip(*pairs)
    return random.choices(names, weights=weights, k=1)[0]

def generate_one(past_texts: list[str]) -> dict | None:
    # 1) Top-Level-Topic ziehen
    t = random.choices(list(_TOPICS.keys()), weights=_TOPICS.values(), k=1)[0]
    # 2) (Optional) Subtopic für die inhaltliche Steuerung ziehen
    sub = _pick_weighted(_SUBTOPICS[t]) if t in _SUBTOPICS and _SUBTOPICS[t] else None
    # 3) Frage generieren (Subtopic nur im Prompt als Hinweis)
    d = _ask_json(_prompt(t, sub))
    time.sleep(0.8)
    if not d:
        return None
    # 4) Ausgabe hart fixieren: topic bleibt das Oberthema
    d["category"] = CATEGORY_NAME
    d["topic"] = t
    return d
