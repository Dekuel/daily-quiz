# kategorien/geschichte.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional
from openai import OpenAI

CATEGORY_NAME = "Geschichte"

_SUBPERIODS = {
    "Antike": 25,
    "Mittelalter": 25,
    "Neuzeit": 30,
    "Zeitgeschichte (ab 1945)": 20,
}

_SCHEMA = """{
  "category": "Geschichte",
  "subperiod": "Antike|Mittelalter|Neuzeit|Zeitgeschichte (ab 1945)",
  "question": "...",
  "choices": ["A: ...", "B: ...", "C: ...", "D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

_DIFF_GUIDE = """
- 1–3 (leicht): ikonische Ereignisse oder Personen, Grundwissen (z. B. römische Kaiser, große Kriege, bekannte Entdecker).
- 4–7 (mittel): weniger bekannte Zusammenhänge, Ursachen/Folgen, kulturelle Entwicklungen, einfache Datierungen.
- 8–10 (schwer): spezifische Quellen, Jahreszahlen, komplexe politische/soziale Prozesse, seltene historische Begriffe.
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
        tier_note = "Sehr Schwer (9-10): spezifische Details oder tiefe Konzepte, expertenwissen, eng verwandte Distraktoren."
        temperature = 0.8

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „Geschichte“, Unterbereich „{sub}“.
Ziel-Schwierigkeit: {target_difficulty}/10 – {tier_note}

Kontext zu Schwierigkeitsstufen:
{_DIFF_GUIDE}

Vorgaben:
- Frage auf Deutsch, verständlich formuliert.
- Keine tagesaktuellen Themen.
- Wenn Fachbegriffe vorkommen, kurz erklären.
- Vier plausible Antwortoptionen (A–D), eine korrekt.
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


def _pick_subperiod() -> str:
    names, weights = list(_SUBPERIODS.keys()), list(_SUBPERIODS.values())
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
    sub = _pick_subperiod()
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3, 5, 7])
    prompt, temp = _prompt(sub, tier, mode)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.8)
    if not data:
        return None

    data["category"] = CATEGORY_NAME
    data["subperiod"] = data.get("subperiod", sub)
    data["difficulty"] = int(data.get("difficulty", tier))

    # minimale Validierung
    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str):
        return None

    # Shuffle übernimmt der Core zentral
    return data
