# kategorien/kunst_literatur.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional
from openai import OpenAI

CATEGORY_NAME = "Kunst und Literatur"

_SUB = {"Kunstgeschichte": 40, "Literatur": 40, "Musik": 20}

_SCHEMA = """{
  "category": "Kunst und Literatur",
  "subtopic": "Kunstgeschichte|Literatur|Musik",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

_DIFF_GUIDE = """
- 1–3 (leicht): sehr bekannte Werke/Autor:innen/Komponist:innen, ikonische Stile oder Epochenmerkmale.
- 4–7 (mittel): weniger offensichtliche Zuordnungen, Werk-Kontexte, Gattungen, Motive, stilistische Kennzeichen.
- 8–10 (schwer): spezifische Jahreszahlen/Erstveröffentlichungen, Einflüsse, Fachbegriffe, Detailwissen zu Schulen/Techniken.
"""

def _prompt(sub: str, target_difficulty: int, mode: Optional[str]) -> tuple[str, float]:
    if target_difficulty <= 2:
        tier_note = "LEICHT (1–2): bekannte Fakten,teils logisch erschließbare Antwort."
        temperature = 0.8
    elif target_difficulty <= 4:
        tier_note = "MITTEL (3-4): etwas weniger bekannte Fakten, moderate Komplexität."
        temperature = 0.8
    elif target_difficulty<= 6:
        tier_note = "Etwas schwerer (5-6): spezifische Details, oder etwas tiefere Konzepte eng verwandte Distraktoren."
        temperature = 0.8
    elif target_difficulty<= 8:
        tier_note = "Schwer (7-8): spezifische Details oder tiefe Konzepte, eng verwandte Distraktoren."
        temperature = 0.8
    else:
        tier_note = "sehr Schwer (9-10): spezifische Details oder tiefe Konzepte, expertenwissen, eng verwandte Distraktoren."
        temperature = 0.8


    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „Kunst und Literatur“, Unterthema „{sub}“.
Ziel-Schwierigkeit: {target_difficulty}/10 – {tier_note}

Kontext zu Schwierigkeitsstufen:
{_DIFF_GUIDE}

Vorgaben:
- Auf Deutsch, knapp und eindeutig.
- Kulturwissen statt Datumsraterei um der Datumszahl willen; Daten nur, wenn inhaltlich sinnvoll.
- Keine Antwortoption „alle oben/keine der oben“.
- Vier plausible Optionen (A–D), genau eine korrekt.
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
                {"role": "system", "content": "Antworte ausschließlich mit valide parsem barem JSON (ohne Text außerhalb des JSON)."},
                {"role": "user", "content": p},
            ],
            temperature=temperature,
        )
        raw = r.choices[0].message.content.strip()
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception:
        return None


def _pick_sub() -> str:
    names, weights = list(_SUB.keys()), list(_SUB.values())
    return random.choices(names, weights=weights, k=1)[0]


def generate_one(
    past_texts: list[str],
    target_difficulty: Optional[int] = None,
    mode: Optional[str] = None,
) -> dict | None:
    """
    Wird vom Core mit target_difficulty (1..10) und mode ("normal"|"schwer"|"physik") aufgerufen.
    Fallback, falls target_difficulty fehlt: moderater Zielwert.
    """
    sub = _pick_sub()
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3, 5, 7])
    prompt, temp = _prompt(sub, tier, mode)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.8)
    if not data:
        return None

    # Pflichtfelder pflegen
    data["category"] = CATEGORY_NAME
    data["subtopic"] = data.get("subtopic", sub)
    data["difficulty"] = int(data.get("difficulty", tier))

    # minimale Validierung
    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str):
        return None

    # Antworten werden zentral im Core gemischt
    return data
