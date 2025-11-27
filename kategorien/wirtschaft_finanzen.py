# -*- coding: utf-8 -*-
"""
Kategorie: Wirtschaft & Finanzen

Ausgewogen zwischen Alltagsfinanzwissen (Banking, Sparen), Börsen-/Investmentwissen
und allgemeinem Wirtschaftsverständnis (Unternehmen, Geschichte, Krypto).
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
    """Lädt SUBTOPICS aus Unterkategorien/Wirtschaft_Finanzen/<subcat_name>.py"""
    here = os.path.dirname(__file__)
    repo = os.path.abspath(os.path.join(here, ".."))
    subcat_dir = os.path.join(repo, "Unterkategorien", "Wirtschaft_Finanzen")
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
        return ("Wirtschaftswissen", (4, 7))
    
    weights = [w for (_, w, _) in topics]
    chosen = random.choices(topics, weights=weights, k=1)[0]
    return (chosen[0], chosen[2])


def _get_difficulty_examples(difficulty: int, main_topic: str) -> str:
    """Gibt konkrete Beispiele für Schwierigkeitslevel."""
    
    examples_map = {
        "Geld & Banking": {
            (1, 3): "z.B. 'Was ist ein Girokonto?', 'Was bedeutet Dispo?'",
            (4, 6): "z.B. 'Was ist ein Tagesgeldkonto?', 'Wie funktioniert Online-Banking?'",
            (7, 10): "z.B. 'Was ist die Einlagensicherung?', 'Wie funktioniert ein P-Konto?'"
        },
        "Börse & Märkte": {
            (1, 3): "z.B. 'Was ist eine Aktie?', 'Was bedeutet DAX?'",
            (4, 6): "z.B. 'Was sind ETFs?', 'Was ist eine Dividende?'",
            (7, 10): "z.B. 'Was sind Derivate?', 'Wie berechnet man das KGV?'"
        },
        "Unternehmen & Brands": {
            (1, 3): "z.B. 'Welches Logo hat Apple?', 'Wer gründete Amazon?'",
            (4, 6): "z.B. 'Was ist ein Unicorn-Startup?', 'Welche Unternehmen gehören zum DAX?'",
            (7, 10): "z.B. 'Was ist Marktkapitalisierung?', 'Welche Fusion war die größte?'"
        },
        "Wirtschaftsgeschichte": {
            (1, 3): "z.B. 'Wann wurde der Euro eingeführt?', 'Was war die Finanzkrise 2008?'",
            (4, 6): "z.B. 'Was war das Wirtschaftswunder?', 'Was war die Dotcom-Blase?'",
            (7, 10): "z.B. 'Was war Bretton Woods?', 'Welche Rolle spielte die OPEC?'"
        },
        "Kryptowährungen": {
            (1, 3): "z.B. 'Was ist Bitcoin?', 'Was sind NFTs?'",
            (4, 6): "z.B. 'Was ist eine Blockchain?', 'Wie funktioniert ein Wallet?'",
            (7, 10): "z.B. 'Was ist DeFi?', 'Wie funktioniert Proof of Work?'"
        },
    }
    
    for topic_key, ranges in examples_map.items():
        if topic_key.lower() in main_topic.lower():
            for (min_d, max_d), example_text in ranges.items():
                if min_d <= difficulty <= max_d:
                    return example_text
    
    # Fallback
    if difficulty <= 3:
        return "z.B. Basiswissen, das viele aus Medien kennen"
    elif difficulty <= 6:
        return "z.B. Wissen über Finanzprodukte oder wirtschaftliche Zusammenhänge"
    else:
        return "z.B. Detailwissen über Finanzmärkte oder komplexe Wirtschaftskonzepte"


def _get_distractors_guide(main_topic: str) -> str:
    """Gibt Hinweise zur Erstellung plausibler Falschantworten."""
    
    guides = {
        "Geld & Banking": "Nutze ähnliche Finanzprodukte (z.B. 'Tagesgeld' vs. 'Festgeld'), falsche Zinssätze oder verwechselbare Begriffe (z.B. 'Bonität' vs. 'Liquidität').",
        "Börse & Märkte": "Nutze ähnliche Indizes (z.B. 'DAX' vs. 'MDAX'), falsche Prozentwerte oder verwechselbare Fachbegriffe (z.B. 'Dividende' vs. 'Rendite').",
        "Unternehmen & Brands": "Nutze ähnliche Unternehmen (z.B. 'Amazon' vs. 'Alibaba'), falsche Gründungsjahre oder verwechselbare CEOs.",
        "Wirtschaftsgeschichte": "Nutze ähnliche Jahreszahlen (z.B. '1929' vs. '1939'), verwechselbare Krisen oder falsche Ursachen.",
        "Kryptowährungen": "Nutze ähnliche Coins (z.B. 'Bitcoin' vs. 'Bitcoin Cash'), falsche technische Details oder verwechselbare Begriffe (z.B. 'Wallet' vs. 'Exchange').",
    }
    
    for key, guide in guides.items():
        if key.lower() in main_topic.lower():
            return guide
    
    return "Nutze plausible, aber falsche Varianten (ähnliche Zahlen, verwechselbare Begriffe, realistische aber falsche Zusammenhänge)."


def generate_one(target_difficulty: int = 5, past_texts: Optional[List[str]] = None, mode: Optional[str] = None) -> Optional[dict]:
    """
    Generiert eine Wirtschafts-/Finanzfrage per GPT-4o-mini.
    
    Struktur:
    - 5 Hauptthemen mit je ~11 Subtopics
    - Gewichtetes Topic-Picking
    - Schwierigkeits-Beispiele im Prompt
    - Distraktoren-Guidance für plausible Falschantworten
    """
    if not client:
        return None

    # 1) Hauptthema auswählen (gleichgewichtet)
    main_topics = [
        ("Geld & Banking", "geld_banking"),
        ("Börse & Märkte", "boerse_maerkte"),
        ("Unternehmen & Brands", "unternehmen_brands"),
        ("Wirtschaftsgeschichte", "wirtschaftsgeschichte"),
        ("Kryptowährungen & Blockchain", "krypto_blockchain"),
    ]
    
    main_topic_name, subcat_file = random.choice(main_topics)
    
    # 2) Subtopics laden und gewichtet auswählen
    subtopics = _discover_subtopics(subcat_file)
    if not subtopics:
        subtopics = [("Wirtschaftswissen", 3, (4, 7))]
    
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
- Balance: Mix aus Alltagswissen (Banking, Sparen) und Finanzmarkt-/Wirtschaftswissen

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
        print(f"[wirtschaft_finanzen] OpenAI-Fehler: {e}")
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
        "category": "Wirtschaft & Finanzen",
        "subcategory": chosen_topic,
        "difficulty": clamped_diff,
        "options": options,
        "correct_answer": correct_key,
    }
