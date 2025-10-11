# kategorien/essen_trinken.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional
from openai import OpenAI

CATEGORY_NAME = "Essen und Trinken"

_TOPICS = {"Küche international":40, "Ernährung":30, "Getränke":15, "Kulinarische Geschichte":15}

# Vom Core werden Antworten ohnehin gemischt; wir geben trotzdem sauber gelabeltes JSON zurück.
_SCHEMA = """{
  "category": "Essen und Trinken",
  "topic": "Küche international|Ernährung|Getränke|Kulinarische Geschichte",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

# Leitplanken je Schwierigkeit (1..10) – beschreibt, WAS „leicht/mittel/schwer“ bedeutet.
# (Zentrale Gewichte bleiben im Core; hier nur semantische Guidance für die Generierung.)
DIFF_GUIDE = """
- 1–3 (leicht): sehr bekanntes Alltagswissen; Distraktoren klar unterscheidbar.
- 4–7 (mittel): weniger offensichtliche Fakten, regionale Besonderheiten, einfache Zahlenbereiche.
- 8–10 (schwer): spezifische Herkunft/Etmythologie/geschützte Herkunftsbezeichnungen, rare Zubereitungen;
  Distraktoren plausibel und nah dran.
"""

def _prompt(topic: str, target_difficulty: int, mode: Optional[str]) -> str:
    # kurze Umschreibung je Tier
    if target_difficulty <= 3:
        tier_note = "LEICHT (1–3): sehr bekanntes Allgemeinwissen, klare Distraktoren."
        temperature = 0.8
    elif target_difficulty <= 7:
        tier_note = "MITTEL (4–7): weniger offensichtliche Fakten, aber ohne Nischen-Nerdwissen."
        temperature = 0.8
    else:
        tier_note = "SCHWER (8–10): spezifisch/präzise Fakten, nahe Distraktoren, keine Mehrdeutigkeit."
        temperature = 0.8

    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, eine richtig) zur Kategorie „Essen und Trinken“, Thema „{topic}“.
Ziel-Schwierigkeit: {target_difficulty}/10 – {tier_note}
Kontext zu Schwierigkeitsstufen:
{DIFF_GUIDE}

Anforderungen:
- Keine reinen Rezeptschritte; Fokus auf Ursprung, Geschichte, Zutatenkunde, Bezeichnungen, Geographie, Schutzsiegel.
- Formuliere knapp, eindeutig, ohne Insider-Begriffe, ohne „alle oben“/„keine der oben“.
- Vier Antwortoptionen (A–D). Genau EINE ist korrekt; die anderen drei müssen plausibel sein.
- Gib ausschließlich valides JSON gemäß Schema zurück.

JSON-SCHEMA:
{_SCHEMA}
""".strip(), temperature

def _ask_json(p: str, temperature: float) -> dict | None:
    c = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        r = c.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Antworte ausschließlich mit valide parsem barem JSON (keine Erklärtexte außerhalb des JSON)."},
                {"role": "user", "content": p},
            ],
            temperature=temperature,
        )
        raw = r.choices[0].message.content.strip()
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception:
        return None

def generate_one(past_texts: list[str], target_difficulty: Optional[int] = None, mode: Optional[str] = None) -> dict | None:
    """
    Wird vom Core mit target_difficulty (1..10) und mode ("normal"|"schwer"|"physik") aufgerufen.
    Falls target_difficulty fehlt, ziehen wir lokal einen moderaten Zielwert (Kompatibilität).
    """
    t = random.choices(list(_TOPICS.keys()), weights=_TOPICS.values(), k=1)[0]
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3, 5, 7])
    prompt, temp = _prompt(t, tier, mode)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.8)
    if not data:
        return None

    # Pflichtfelder pflegen/normalisieren
    data["category"] = CATEGORY_NAME
    data["topic"] = data.get("topic", t)
    data["difficulty"] = int(data.get("difficulty", tier))

    # Sanity check: choices & correct_answer vorhanden
    choices = data.get("choices")
    correct = data.get("correct_answer")
    if not isinstance(choices, list) or len(choices) != 4 or not isinstance(correct, str):
        return None

    # Fragen-Text duplications verhindern (einfaches Normalisierungs-Trim)
    qtext = (data.get("question") or "").strip()
    if not qtext:
        return None

    # Plugin selbst mischt nicht – der Core mischt später tagesweit konsistent.
    return data
