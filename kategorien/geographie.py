# kategorien/geographie.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional, List, Tuple
from openai import OpenAI

CATEGORY_NAME = "Geographie"

# Top-Level-Themen mit Gewichten (leicht erhöhter Fokus auf Hauptstädte/Flüsse)
_TOPICS = {
    "Länder, Hauptstädte & Flaggen": 35,
    "Flüsse, Seen & Meere": 15,
    "Gebirge, Inseln & Relief": 15,
    "Humangeographie & Städte": 15,
    "Klima, Biome & Naturregionen": 10,
    "Kartographie & GIS": 10,
}

# Subtopics pro Top-Level-Topic (name, gewicht)
_SUBTOPICS: dict[str, List[Tuple[str, int]]] = {
    "Länder, Hauptstädte & Flaggen": [
        ("Europa: Hauptstädte & Nachbarländer", 3),
        ("Afrika: Hauptstädte & Küstenlage", 2),
        ("Asien: Hauptstädte & Flusslagen", 2),
        ("Amerika: Hauptstädte & Gebirge", 2),
        ("Ozeanien: Hauptstädte & Inselstaaten", 1),
        ("Grenzverläufe & historische Umbenennungen", 1),
    ],
    "Flüsse, Seen & Meere": [
        ("Längste Flüsse & Einzugsgebiete", 3),
        ("Mündungen, Deltas & Ästuare", 2),
        ("Stauseen & Binnenmeere", 2),
        ("Flussverläufe durch Hauptstädte", 2),
        ("Wasserscheiden & Kanäle", 1),
    ],
    "Gebirge, Inseln & Relief": [
        ("Höchste Gipfel & Gebirgsketten", 3),
        ("Vulkanische Inselbögen", 2),
        ("Küstenformen (Fjorde, Dünen, Kliffs)", 2),
        ("Wüsten & Hochplateaus", 2),
        ("Karst & Höhlenlandschaften", 1),
    ],
    "Humangeographie & Städte": [
        ("Megastädte & Urbanisierung", 2),
        ("Wirtschaftsräume & Verkehrskorridore", 2),
        ("Häfen, Handelsrouten & Logistik", 2),
        ("Demografie & Wanderungen", 2),
        ("Stadtklima & Landnutzung", 1),
    ],
    "Klima, Biome & Naturregionen": [
        ("Köppen-Geiger & Klimadiagramme", 2),
        ("Monsune & Telekonnektionen (ENSO/NAO)", 2),
        ("Permafrost & Tundra", 1),
        ("Savannen, Taiga, Regenwald", 2),
        ("Extreme Wetterereignisse", 1),
    ],
    "Kartographie & GIS": [
        ("Maßstab & Generalisierung", 2),
        ("Kartennetzentwürfe & Verzerrungen", 2),
        ("Fernerkundung (Satellit/Luftbild)", 2),
        ("GIS-Datenmodelle & Layer", 2),
        ("Thematische Karten & Visualisierung", 1),
    ],
}

_SCHEMA = """{
  "category": "Geographie",
  "topic": "Länder, Hauptstädte & Flaggen|Flüsse, Seen & Meere|Gebirge, Inseln & Relief|Humangeographie & Städte|Klima, Biome & Naturregionen|Kartographie & GIS",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

# Schwierigkeitsbänder
_DIFF_BANDS = [
    ((1, 2), "SEHR LEICHT (1–2): sehr bekanntes Grundlagenwissen, klare Distraktoren; keine Fachsprache nötig.", 0.75),
    ((3, 4), "LEICHT (3–4): grundlegende Begriffe/Konzepte mit kurzem Kontext; einfache Beispiele.", 0.75),
    ((5, 6), "MITTEL (5–6): Verknüpfung mehrerer Konzepte; knappe, präzise Begriffsabgrenzungen.", 0.75),
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
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „Geographie“, Thema „{topic}“ (Deutsch).
{sub_hint}Ziel-Schwierigkeit: {target_difficulty}/10 – {band_note}

Vorgaben:
- Verständlich für Laien; Fachbegriffe nur wenn nötig und in der Erklärung kurz erläutern.
- Fokus erlaubt auf Hauptstädte, Flüsse, Gebirge etc., aber mit kurzem Kontext (z. B. „welche Hauptstadt liegt an diesem Fluss?“, „welcher Staat grenzt hier an?“ statt reine Listenabfrage).
- Keine reinen Trivia-Listen („Welche ist die Hauptstadt von X?“ ohne Kontext) und keine „alle/keine der oben“-Optionen.
- Keine Rechnungen oder langen Herleitungen; qualitative/konzeptionelle Prüfung reicht.
- Vier plausible Antwortoptionen (A–D), genau eine korrekt.
- Erklärung 2–3 Sätze: kurz, präzise, hilfreich; bei Ortsnamen ggf. Lagehinweis (Region/Nachbarländer/Flussverlauf).
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
    Wird vom Core mit target_difficulty (1..10) und mode ("normal"|"schwer"|"geo") aufgerufen.
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
