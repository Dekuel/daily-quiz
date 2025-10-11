# kategorien/sprache.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional
from openai import OpenAI

CATEGORY_NAME = "Sprache"

_THEMES = {
    "Grammatik": 30,
    "Wortherkunft": 30,
    "Redewendungen": 25,
    "Fremdsprachen": 15,
}

_SCHEMA = """{
  "category": "Sprache",
  "topic": "Grammatik|Wortherkunft|Redewendungen|Fremdsprachen",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

# Schwierigkeitsbänder (feiner als nur leicht/mittel/schwer)
_DIFF_BANDS = [
    ((1, 2), "SEHR LEICHT (1–2): allgemein bekannte Regeln/Begriffe, sehr klare Distraktoren.", 0.75),
    ((3, 4), "LEICHT (3–4): grundlegende Grammatik/Wortbedeutungen, geläufige Redewendungen.", 0.75),
    ((5, 6), "MITTEL (5–6): weniger offensichtliche Ableitungen, Etymologie-Hinweise, feinere Grammatikfälle.", 0.75),
    ((7, 8), "ANSPRUCHSVOLL (7–8): seltenere Wendungen, genaue Bedeutungsnuancen, Ausnahmen/Regelkonflikte.", 0.75),
    ((9,10), "SCHWER (9–10): historische Etymologien, regionale Varietäten, knappe Fachtermini korrekt abgrenzen.", 0.82),
]

def _band_for_difficulty(target: int) -> tuple[str, float]:
    t = int(target)
    for (lo, hi), note, temp in _DIFF_BANDS:
        if lo <= t <= hi:
            return note, temp
    return "MITTEL (5–6): weniger offensichtliche Ableitungen, feinere Grammatikfälle.", 0.55

def _prompt(topic: str, target_difficulty: int, mode: Optional[str]) -> tuple[str, float]:
    band_note, temperature = _band_for_difficulty(target_difficulty)

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „Sprache“, Thema „{topic}“ (Deutsch).
Ziel-Schwierigkeit: {target_difficulty}/10 – {band_note}

Vorgaben:
- Knapp und eindeutig formulieren; Beispiele statt Metadiskussion.
- Wenn Fachbegriff vorkommt, in der Erklärung kurz und laienverständlich erläutern.
- Vier plausible Antwortoptionen (A–D), genau eine korrekt; vermeide „alle oben/keine der oben“.
- Erklärung in 2–3 Sätzen, warum die richtige Lösung stimmt.
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


def _pick_theme() -> str:
    names, weights = list(_THEMES.keys()), list(_THEMES.values())
    return random.choices(names, weights=weights, k=1)[0]


def generate_one(
    past_texts: list[str],
    target_difficulty: Optional[int] = None,
    mode: Optional[str] = None,
) -> dict | None:
    """
    Wird vom Core mit target_difficulty (1..10) und mode ("normal"|"schwer"|"physik") aufgerufen.
    Fallback bei fehlender target_difficulty: moderater Zielwert.
    """
    topic = _pick_theme()
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3, 5, 7])
    prompt, temp = _prompt(topic, tier, mode)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.8)
    if not data:
        return None

    # Pflichtfelder pflegen/normalisieren
    data["category"] = CATEGORY_NAME
    data["topic"] = data.get("topic", topic)
    data["difficulty"] = int(data.get("difficulty", tier))

    # minimale Validierung
    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str):
        return None

    # Shuffle der Antworten passiert zentral im Core
    return data
