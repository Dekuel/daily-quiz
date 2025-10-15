# kategorien/sprache.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional, List, Tuple
from openai import OpenAI

CATEGORY_NAME = "Sprache"

# Oberbereiche (Unterkategorien) mit Gewichten – wie bei Geschichte
_SUBCATEGORIES: dict[str, int] = {
    "Grammatik": 10,
    "Wortherkunft": 50,
    "Redewendungen": 15,
    "Fremdsprachen": 25,
}

# Gewichtete Unterthemen pro Unterkategorie (nur Prompt-Hinweis, NICHT ins JSON übernehmen)
_SUBTOPICS: dict[str, List[Tuple[str, int]]] = {
    "Grammatik": [
        ("Kasus & Rektion (Präpositionen, Verben)", 3),
        ("Satzbau & Wortstellung (Verbzweit, Nebensätze, Feldmodell)", 3),
        ("Tempus & Modus (Konjunktiv I/II, Zeitengebrauch)", 3),
        ("Kongruenz & Übereinstimmung (Subjekt–Verb, Attribute)", 2),
        ("Kommasetzung aus grammatischen Gründen (Nebensätze, Infinitive)", 2),
        ("Adjektivdeklination & Steigerung", 1),
        ("Aktiv–Passiv-Umformungen", 1),
    ],
    "Wortherkunft": [
        ("Lehn- & Fremdwörter (Latein, Französisch, Englisch)", 3),
        ("Wortbildung: Präfixe/Suffixe, Komposita", 3),
        ("Bedeutungswandel & semantische Verschiebung", 2),
        ("Etymologie geläufiger Wörter/Endungen (z. B. -chen, ur-)", 2),
        ("Falsche Freunde & Scheinverwandte", 1),
        ("Namens- & Ortsnamnetymologie (Basiswissen)", 1),
    ],
    "Redewendungen": [
        ("Bedeutung gängiger Idiome & Sprichwörter", 3),
        ("Herkunft/Metaphorik verbreiteter Wendungen", 2),
        ("Verwechslungsgefahr naher Wendungen (Nuancen)", 2),
        ("Register & Gebrauch (formell/umgangssprachlich)", 1),
        ("Regionale Varianten (D/A/CH) – Grundkenntnis", 1),
    ],
    "Fremdsprachen": [
        ("Deutsch–Englisch: False Friends & Interferenzen", 3),
        ("Wortstellung/Artikel im Vergleich (DE vs. EN/FR/ES)", 2),
        ("Höflichkeitsformen, Anrede & Modalität", 2),
        ("Lehnübersetzungen & Anglizismen im Deutschen", 2),
        ("Typische Fehlerquellen für Lernende (A2–B2)", 1),
    ],
}

_SCHEMA = """{
  "category": "Sprache",
  "subcategory": "Grammatik|Wortherkunft|Redewendungen|Fremdsprachen",
  "question": "...",
  "choices": ["A: ...", "B: ...", "C: ...", "D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

# Grobe Schwierigkeitsleitplanke – analog zu Geschichte, aber sprachspezifisch
_DIFF_GUIDE = """
- 1–3 (leicht): sehr geläufige Regeln/Idiome, Grundbegriffe; Distraktoren klar schwächer.
- 4–7 (mittel): weniger offensichtliche Fälle, feine Bedeutungsnuancen, typische Ausnahmen.
- 8–10 (schwer): seltene Wendungen, präzise Terminologie/Etymologie, eng beieinanderliegende Optionen.
"""

def _pick_weighted(pairs: List[Tuple[str, int]]) -> str:
    names, weights = zip(*pairs)
    return random.choices(list(names), weights=list(weights), k=1)[0]

def _prompt(subcategory: str, target_difficulty: int, mode: Optional[str], subtopic: Optional[str] = None) -> tuple[str, float]:
    # Temperatur leicht staffeln
    if target_difficulty <= 2:
        tier_note = "LEICHT (1–2): bekannte Regeln/Wendungen, einfache Ableitung möglich."
        temperature = 0.8
    elif target_difficulty <= 4:
        tier_note = "MITTEL (3–4): weniger bekannte, aber üblich prüfbare Inhalte."
        temperature = 0.8
    elif target_difficulty <= 6:
        tier_note = "Etwas schwerer (5–6): spezifische Details, enge Distraktoren."
        temperature = 0.8
    elif target_difficulty <= 8:
        tier_note = "Schwer (7–8): Ausnahmen/feine Nuancen, präzise Wortbedeutungen."
        temperature = 0.8
    else:
        tier_note = "Sehr schwer (9–10): seltene Wendungen, genaue Etymologien/Terminologie."
        temperature = 0.82

    sub_hint = f"- Unterthema (nur als inhaltlicher Hinweis, NICHT ins JSON übernehmen): „{subtopic}“.\n" if subtopic else ""

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „Sprache“, Unterbereich „{subcategory}“ (Deutsch).
{sub_hint}Ziel-Schwierigkeit: {target_difficulty}/10 – {tier_note}

Kontext zu Schwierigkeitsstufen:
{_DIFF_GUIDE}

Vorgaben:
- Knapp und eindeutig formulieren; Beispiel statt Metadiskussion.
- Vier plausible Antwortoptionen (A–D), genau eine korrekt; keine „alle oben/keine der oben“.
- Erklärung: 2–3 Sätze, warum die richtige Lösung stimmt; Fachbegriffe kurz laienverständlich erläutern.
- Das Feld "subcategory" im JSON enthält ausschließlich den Oberbereich („{subcategory}“). Unterthema nicht ins JSON.
- Gib ausschließlich valides JSON gemäß Schema zurück.

JSON-SCHEMA:
{_SCHEMA}
""".strip()

    return prompt, temperature

def _ask_json(prompt: str, temperature: float) -> dict | None:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Antwort ausschließlich als valides JSON, keine Zusätze."},
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
        )
        raw = r.choices[0].message.content.strip()
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception:
        return None

def _pick_subcategory() -> str:
    names, weights = list(_SUBCATEGORIES.keys()), list(_SUBCATEGORIES.values())
    return random.choices(names, weights=weights, k=1)[0]

def generate_one(
    past_texts: list[str],
    target_difficulty: Optional[int] = None,
    mode: Optional[str] = None,
) -> dict | None:
    """
    Wird vom Core mit target_difficulty (1..10) und mode ("normal"|"schwer"|"physik") aufgerufen.
    Falls target_difficulty fehlt, wähle moderaten Standardwert.
    """
    # 1) Unterkategorie wählen
    sub = _pick_subcategory()
    # 2) Unterthema als Prompt-Hinweis ziehen
    subtopic = _pick_weighted(_SUBTOPICS[sub]) if sub in _SUBTOPICS and _SUBTOPICS[sub] else None
    # 3) Zielschwierigkeit bestimmen
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3, 5, 7])
    # 4) Prompt bauen & Anfrage senden
    prompt, temp = _prompt(sub, tier, mode, subtopic=subtopic)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.8)
    if not data:
        return None

    # 5) Pflichtfelder normieren
    data["category"] = CATEGORY_NAME
    data["subcategory"] = sub          # Oberbereich erzwingen (Unterthema nie ins JSON)
    data["difficulty"] = int(data.get("difficulty", tier))

    # 6) minimale Validierung
    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str):
        return None

    # Shuffle übernimmt der Core zentral
    return data
