# kategorien/natur.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional, List, Tuple
from openai import OpenAI

CATEGORY_NAME = "Natur"

# Top-Level-Themen mit Gewichten
_TOPICS = {
    "Pflanzenwelt": 25,
    "Tierwelt": 25,
    "Lebensräume & Ökosysteme": 20,
    "Wetter & Klima": 15,
    "Geologie & Erde": 15,
}

# Subtopics pro Top-Level-Topic (name, gewicht)
_SUBTOPICS: dict[str, List[Tuple[str, int]]] = {
    "Pflanzenwelt": [
        ("Bäume & Sträucher", 2),
        ("Blumen & Blüten", 2),
        ("Heilpflanzen & Kräuter", 2),
        ("Nutzpflanzen", 2),
        ("Pilze & Flechten", 2),
        ("Pflanzenanatomie", 1),
        ("Bestäubung & Samen", 1),
    ],
    "Tierwelt": [
        ("Säugetiere", 2),
        ("Vögel", 2),
        ("Insekten", 2),
        ("Reptilien & Amphibien", 2),
        ("Fische & Meeresbewohner", 2),
        ("Tierverhalten", 1),
        ("Tierrekorde", 1),
    ],
    "Lebensräume & Ökosysteme": [
        ("Wald", 2),
        ("Wüste", 2),
        ("Gebirge", 2),
        ("Polarregionen", 2),
        ("Süßwasser-Ökosysteme", 2),
        ("Meere & Küsten", 2),
        ("Stadtökologie", 1),
        ("Artenvielfalt & Schutzgebiete", 1),
    ],
    "Wetter & Klima": [
        ("Wetterphänomene", 2),
        ("Klimazonen", 2),
        ("Klimawandel", 2),
        ("Jahreszeiten", 2),
        ("Extremwetter", 2),
        ("Wolken & Niederschlag", 1),
    ],
    "Geologie & Erde": [
        ("Gesteine & Mineralien", 2),
        ("Vulkane & Erdbeben", 2),
        ("Bodenkunde", 2),
        ("Erdgeschichte & Fossilien", 2),
        ("Plattentektonik", 2),
        ("Geomorphologie", 1),
        ("Rohstoffe & Kreisläufe", 1),
    ],
}

_SCHEMA = """{
  "category": "Natur",
  "topic": "Pflanzenwelt|Tierwelt|Lebensräume & Ökosysteme|Wetter & Klima|Geologie & Erde",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

# Schwierigkeitsbänder (feiner als nur leicht/mittel/schwer)
_DIFF_BANDS = [
    ((1, 2), "SEHR LEICHT (1–2): sehr bekanntes Grundlagenwissen, klare Distraktoren; keine Fachsprache nötig.", 0.75),
    ((3, 4), "LEICHT (3–4): grundlegende Begriffe/Konzepte mit kurzem Kontext; relativ einfache Beispiele.", 0.75),
    ((5, 6), "MITTEL (5–6): ", 0.75),
    ((7, 8), "ANSPRUCHSVOLL (7–8): seltenere Konzepte/Subdisziplinen; eng verwandte, plausible Distraktoren.", 0.75),
    ((9,10), "SCHWER (9–10): präzise Details/Edge Cases, exakte Terminologie;", 0.82),
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
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „Natur“, Thema „{topic}“ (Deutsch).
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
