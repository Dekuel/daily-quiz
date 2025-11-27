# -*- coding: utf-8 -*-
"""
Kategorie: Alltag & Gesellschaft

Fokussiert auf praktisches Alltagswissen zu Arbeit, Wohnen, Verkehr,
Gesundheit, Bildung und Familie. Zielgruppe: breites Publikum ab 16 Jahren.
"""

from __future__ import annotations
import os
import random
from typing import Optional, Tuple, List

# OpenAI-Client (falls vorhanden)
try:
    from openai import OpenAI
    client = OpenAI()
except (ImportError, Exception):
    client = None


def _discover_subtopics(subcat_name: str) -> List[Tuple[str, int, Tuple[int, int]]]:
    """Lädt SUBTOPICS aus Unterkategorien/Alltag_Gesellschaft/<subcat_name>.py"""
    here = os.path.dirname(__file__)
    repo = os.path.abspath(os.path.join(here, ".."))
    subcat_dir = os.path.join(repo, "Unterkategorien", "Alltag_Gesellschaft")
    subcat_file = os.path.join(subcat_dir, f"{subcat_name}.py")

    if not os.path.isfile(subcat_file):
        return []

    ns = {}
    with open(subcat_file, "r", encoding="utf-8") as f:
        exec(f.read(), ns)

    subtopics = ns.get("SUBTOPICS", [])
    if not isinstance(subtopics, list):
        return []

    return subtopics


def _pick_weighted_topic(topics: List[Tuple[str, int, Tuple[int, int]]]) -> Tuple[str, Tuple[int, int]]:
    """Wählt ein Topic mit Gewichtung aus: (topic_name, weight, (min_diff, max_diff))"""
    if not topics:
        return ("Alltagswissen", (3, 6))
    
    weights = [w for (_, w, _) in topics]
    chosen = random.choices(topics, weights=weights, k=1)[0]
    return (chosen[0], chosen[2])


def _get_difficulty_examples(difficulty: int, main_topic: str) -> str:
    """Gibt konkrete Beispiele für Schwierigkeitslevel."""
    
    examples_map = {
        "Arbeit & Beruf": {
            (1, 3): "z.B. 'Was gehört in einen Lebenslauf?', 'Was ist eine Krankmeldung?'",
            (4, 6): "z.B. 'Wie lange ist die gesetzliche Kündigungsfrist?', 'Was ist ein Arbeitszeugnis?'",
            (7, 10): "z.B. 'Welche Kündigungsfristen gelten bei Betriebsratsmitgliedern?', 'Was ist eine Direktversicherung?'"
        },
        "Wohnen & Lifestyle": {
            (1, 3): "z.B. 'Was sind Nebenkosten?', 'Was ist eine Kaution?'",
            (4, 6): "z.B. 'Wer zahlt die Grundsteuer?', 'Was ist eine Mietpreisbremse?'",
            (7, 10): "z.B. 'Welche Fristen gelten für Nebenkostenabrechnungen?', 'Was ist eine WEG-Umlage?'"
        },
        "Verkehr & Mobilität": {
            (1, 3): "z.B. 'Bei welcher Ampelphase muss man halten?', 'Was ist ein Zebrastreifen?'",
            (4, 6): "z.B. 'Wie schnell darf man innerorts fahren?', 'Was kostet Falschparken?'",
            (7, 10): "z.B. 'Welche Vorfahrtsregeln gelten bei abgeknickter Vorfahrt?', 'Was ist der Unterschied zwischen Vollkasko und Teilkasko?'"
        },
        "Gesundheit & Medizin": {
            (1, 3): "z.B. 'Was ist ein Hausarzt?', 'Wie oft sollte man Zähneputzen?'",
            (4, 6): "z.B. 'Was sind Vorsorgeuntersuchungen?', 'Wie funktioniert eine Krankschreibung?'",
            (7, 10): "z.B. 'Was ist der Unterschied zwischen GKV und PKV?', 'Welche Zuzahlungen gibt es bei Medikamenten?'"
        },
        "Bildung & Schulsystem": {
            (1, 3): "z.B. 'Was ist ein Abitur?', 'Was ist eine Grundschule?'",
            (4, 6): "z.B. 'Was ist der Numerus Clausus?', 'Wie funktioniert BAföG?'",
            (7, 10): "z.B. 'Welche Schulformen gibt es in Deutschland?', 'Was ist ein duales Studium?'"
        },
        "Familie & Beziehungen": {
            (1, 3): "z.B. 'Was ist Kindergeld?', 'Was ist eine Heirat?'",
            (4, 6): "z.B. 'Wie lange bekommt man Elterngeld?', 'Was ist ein Ehevertrag?'",
            (7, 10): "z.B. 'Wie wird das Sorgerecht bei Scheidung geregelt?', 'Was ist ein Berliner Testament?'"
        },
    }
    
    for topic_key, ranges in examples_map.items():
        if topic_key.lower() in main_topic.lower():
            for (min_d, max_d), example_text in ranges.items():
                if min_d <= difficulty <= max_d:
                    return example_text
    
    # Fallback
    if difficulty <= 3:
        return "z.B. Allgemeinwissen, das die meisten kennen"
    elif difficulty <= 6:
        return "z.B. Faktenwissen, das man aus Erfahrung oder Medien kennt"
    else:
        return "z.B. Detailwissen oder rechtliche Feinheiten"


def _get_distractors_guide(main_topic: str) -> str:
    """Gibt Hinweise zur Erstellung plausibler Falschantworten."""
    
    guides = {
        "Arbeit & Beruf": "Nutze ähnlich klingende Begriffe (z.B. 'Arbeitsvertrag' vs. 'Tarifvertrag'), falsche Fristen oder unrealistische Gehaltszahlen.",
        "Wohnen & Lifestyle": "Nutze verwechselbare Kostenpositionen (z.B. 'Grundsteuer' vs. 'Grunderwerbssteuer'), falsche Quadratmeterpreise oder unrealistische Mieterhöhungen.",
        "Verkehr & Mobilität": "Nutze ähnliche Geschwindigkeitslimits (z.B. 30 statt 50 km/h), verwechselbare Verkehrsschilder oder falsche Bußgelder.",
        "Gesundheit & Medizin": "Nutze ähnliche Fachbegriffe (z.B. 'Krankenversicherung' vs. 'Pflegeversicherung'), falsche Impfintervalle oder unrealistische Zuzahlungen.",
        "Bildung & Schulsystem": "Nutze verwechselbare Schulformen (z.B. 'Realschule' vs. 'Gesamtschule'), falsche Abschlussnoten oder unrealistische BAföG-Sätze.",
        "Familie & Beziehungen": "Nutze verwechselbare Geldleistungen (z.B. 'Kindergeld' vs. 'Kinderfreibetrag'), falsche Elternzeit-Modelle oder unrealistische Unterhaltszahlungen.",
    }
    
    for key, guide in guides.items():
        if key.lower() in main_topic.lower():
            return guide
    
    return "Nutze plausible, aber falsche Varianten (ähnliche Zahlen, verwechselbare Begriffe, realistische aber falsche Regelungen)."


def generate_one(target_difficulty: int = 5, past_texts: Optional[List[str]] = None, mode: Optional[str] = None) -> Optional[dict]:
    """
    Generiert eine Alltags-Frage per GPT-4o-mini.
    
    Struktur:
    - 6 Hauptthemen mit je ~10-12 Subtopics
    - Gewichtetes Topic-Picking
    - Schwierigkeits-Beispiele im Prompt
    - Distraktoren-Guidance für plausible Falschantworten
    """
    if not client:
        return None

    # 1) Hauptthema auswählen (gleichgewichtet)
    main_topics = [
        ("Arbeit & Beruf", "arbeit_beruf"),
        ("Wohnen & Lifestyle", "wohnen_lifestyle"),
        ("Verkehr & Mobilität", "verkehr_mobilitaet"),
        ("Gesundheit & Medizin", "gesundheit_medizin"),
        ("Bildung & Schulsystem", "bildung_schulsystem"),
        ("Familie & Beziehungen", "familie_beziehungen"),
    ]
    
    main_topic_name, subcat_file = random.choice(main_topics)
    
    # 2) Subtopics laden und gewichtet auswählen
    subtopics = _discover_subtopics(subcat_file)
    if not subtopics:
        subtopics = [("Allgemeinwissen", 3, (3, 6))]
    
    chosen_topic, (min_diff, max_diff) = _pick_weighted_topic(subtopics)
    
    # 3) Schwierigkeit im erlaubten Bereich
    clamped_diff = max(min_diff, min(target_difficulty, max_diff))
    
    # 4) Prompt mit Beispielen und Distraktoren-Guidance
    difficulty_examples = _get_difficulty_examples(clamped_diff, main_topic_name)
    distractors_guide = _get_distractors_guide(main_topic_name)
    
    prompt = f"""Erstelle eine Multiple-Choice-Frage zum Thema "{chosen_topic}" (Kategorie: {main_topic_name}).

Schwierigkeit: {clamped_diff}/10
{difficulty_examples}

WICHTIG für Falschantworten:
{distractors_guide}

Formatierung:
- Frage: Klar und verständlich
- 4 Antwortoptionen (A-D)
- Kennzeichne die richtige Antwort mit [CORRECT]
- Keine Erklärungen, nur Frage und Antworten
- Alltagsrelevanz: Fokus auf praktisches Wissen, das im täglichen Leben nützlich ist

Beispiel-Format:
Frage: [Deine Frage]
A) [Antwort 1]
B) [Antwort 2] [CORRECT]
C) [Antwort 3]
D) [Antwort 4]"""

    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9,
            max_tokens=400,
        )
        raw = resp.choices[0].message.content.strip()
    except Exception as e:
        print(f"[alltag_gesellschaft] OpenAI-Fehler: {e}")
        return None

    # 5) Parsing
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    question_text = ""
    options = {}
    correct_key = None

    for line in lines:
        if line.lower().startswith("frage:"):
            question_text = line.split(":", 1)[1].strip()
        elif line and line[0].upper() in "ABCD" and (")" in line or ":" in line):
            key = line[0].upper()
            rest = line[1:].lstrip("):. ")
            if "[CORRECT]" in rest.upper():
                rest = rest.replace("[CORRECT]", "").replace("[correct]", "").strip()
                correct_key = key
            options[key] = rest

    if not question_text or len(options) < 4 or not correct_key:
        return None

    return {
        "question": question_text,
        "category": "Alltag & Gesellschaft",
        "subcategory": chosen_topic,
        "difficulty": clamped_diff,
        "options": options,
        "correct_answer": correct_key,
    }
