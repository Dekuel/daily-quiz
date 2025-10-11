# kategorien/wissenschaft.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional, List, Tuple
from openai import OpenAI

CATEGORY_NAME = "Wissenschaft"

# Top-Level-Themen mit Gewichten
_TOPICS = {
    "Physik": 25,
    "Biologie": 25,
    "Chemie": 20,
    "Astronomie": 15,
    "Medizin": 15,
}

# Subtopics pro Top-Level-Topic (name, gewicht)
_SUBTOPICS: dict[str, List[Tuple[str, int]]] = {
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
    ],
    "Biologie": [
        ("Genetik", 3),
        ("Evolution", 2),
        ("Ökologie", 2),
        ("Zellbiologie", 2),
        ("Neurobiologie", 1),
        ("Physiologie", 1),
        ("Mikrobiologie", 1),
    ],
    "Chemie": [
        ("Physikalische Chemie", 2),
        ("Organische Chemie", 3),
        ("Anorganische Chemie", 2),
        ("Analytische Chemie", 2),
        ("Biochemie", 1),
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
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

# Schwierigkeitsbänder (feiner als nur leicht/mittel/schwer)
_DIFF_BANDS = [
    ((1, 2), "SEHR LEICHT (1–2): sehr bekanntes Grundlagenwissen, klare Distraktoren; keine Fachsprache nötig.", 0.75),
    ((3, 4), "LEICHT (3–4): grundlegende Begriffe/Konzepte mit kurzem Kontext; einfache Beispiele.", 0.75),
    ((5, 6), "MITTEL (5–6): Verknüpfung mehrerer Konzepte; knappe, präzise Begriffsabgrenzungen.", 0.75),
    ((7, 8), "ANSPRUCHSVOLL (7–8): seltenere Konzepte/Subdisziplinen; eng verwandte, plausible Distraktoren.", 0.75),
    ((9,10), "SCHWER (9–10): präzise Details/Edge Cases, exakte Terminologie; keine Rechnungen/Herleitungen nötig.", 0.82),
]

def _band_for_difficulty(target: int) -> tuple[str, float]:
    t = int(target)
    for (lo, hi), note, temp in _DIFF_BANDS:
        if lo <= t <= hi:
            return note, temp
    return "MITTEL (5–6): Verknüpfung mehrerer Konzepte; präzise Abgrenzungen.", 0.55

def _prompt(topic: str, target_difficulty: int, mode: Optional[str], subtopic: Optional[str] = None) -> tuple[str, float]:
    band_note, temperature = _band_for_difficulty(target_difficulty)
    sub_hint = f"- Subthema (nur als inhaltlicher Hinweis, NICHT ins JSON übernehmen): „{subtopic}“.\n" if subtopic else ""

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „Wissenschaft“, Thema „{topic}“ (Deutsch).
{sub_hint}Ziel-Schwierigkeit: {target_difficulty}/10 – {band_note}

Vorgaben:
- Verständlich für Laien; Fachbegriffe nur wenn nötig und kurz erläutern (in der Erklärung).
- Keine reinen Definitionsfragen ohne Kontext.
- Keine Rechnungen oder Herleitungen; qualitative/konzeptionelle Prüfung reicht.
- Vier plausible Antwortoptionen (A–D), genau eine korrekt; keine Optionen wie „alle oben/keine der oben“.
- Erklärung 2–3 Sätze: kurz, präzise, hilfreich.
- Das Feld "topic" im JSON enthält ausschließlich das Oberthema („{topic}“). Subthema nicht gesondert ausgeben.
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

def _pick_weighted(pairs: List[Tuple[str, int]]) -> str:
    names, weights = zip(*pairs)
    return random.choices(list(names), weights=list(weights), k=1)[0]

def generate_one(
    past_texts: list[str],
    target_difficulty: Optional[int] = None,
    mode: Optional[str] = None,
) -> dict | None:
    """
    Wird vom Core mit target_difficulty (1..10) und mode ("normal"|"schwer"|"physik") aufgerufen.
    Fallback bei fehlender target_difficulty: moderater Zielwert.
    """
    # 1) Top-Level-Topic ziehen
    t = random.choices(list(_TOPICS.keys()), weights=list(_TOPICS.values()), k=1)[0]
    # 2) Optionales Subtopic (nur für den Prompt)
    sub = _pick_weighted(_SUBTOPICS[t]) if t in _SUBTOPICS and _SUBTOPICS[t] else None

    # 3) Zielschwierigkeit
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3, 5, 7])

    # 4) Frage generieren
    prompt, temp = _prompt(t, tier, mode, subtopic=sub)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.8)
    if not data:
        return None

    # 5) Ausgabe hart fixieren: topic bleibt das Oberthema
    data["category"] = CATEGORY_NAME
    data["topic"] = t
    data["difficulty"] = int(data.get("difficulty", tier))

    # 6) minimale Validierung
    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str):
        return None

    # Shuffle der Antworten übernimmt der Core zentral
    return data
