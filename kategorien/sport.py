# kategorien/sport.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional
from openai import OpenAI

CATEGORY_NAME = "Sport"

_SPORTS = {
    "Fußball": 30,
    "Olympische Spiele": 20,
    "Tennis": 15,
    "Formel 1": 15,
    "Basketball": 10,
    "Sonstige": 10,
}

# -- Schema: 'topic' statt 'discipline' ---------------------------------------
_SCHEMA = """{
  "category": "Sport",
  "topic": "Fußball|Olympische Spiele|Tennis|Formel 1|Basketball|Sonstige",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

# ──────────────────────────────────────────────────────────────────────────────
# Neuer Schwierigkeitsleitfaden 1–10 (exakt nach Vorgabe)
# ──────────────────────────────────────────────────────────────────────────────
_DIFF_GUIDE = """
1 = absolutes Grundwissen (≈ 95 % der Bevölkerung in DE)
2 = sehr einfaches Grundwissen
3 = einfache Fragen (ohne schwere Thematik)
4 = leichte Fragen (Recall, einfache Anwendung)
5 = einfach–mittel (70–80 % schaffbar)
6 = mittlere Komplexität (≈ 60 % schaffbar)
7 = mittel–schwer (für Nicht-Expert:innen anspruchsvoll)
8 = schwer (deutliches Vorwissen/vertieftes Verständnis nötig)
9 = Expertenwissen (Fachkenntnisse erforderlich)
10 = schwerstmöglich (oberes Expertenniveau)
""".strip()

# Stufengenaue Beschreibung für die Prompt-Zeile
_DIFF_LEVELS: dict[int, str] = {
    1: "absolutes Grundwissen (≈ 95 % der Bevölkerung in DE)",
    2: "sehr einfaches Grundwissen",
    3: "einfache Fragen (ohne schwere Thematik)",
    4: "leichte Fragen (Recall, einfache Anwendung)",
    5: "einfach–mittel (70–80 % schaffbar)",
    6: "mittlere Komplexität (≈ 60 % schaffbar)",
    7: "mittel–schwer (für Nicht-Expert:innen anspruchsvoll)",
    8: "schwer (deutliches Vorwissen/vertieftes Verständnis nötig)",
    9: "Expertenwissen (Fachkenntnisse erforderlich)",
    10:"schwerstmöglich (oberes Expertenniveau)",
}

def _temperature_for(d: int) -> float:
    if d <= 2: return 0.75
    if d <= 4: return 0.75
    if d <= 6: return 0.75
    if d <= 8: return 0.75
    return 0.82

def _prompt(disc: str, target_difficulty: int, mode: Optional[str]) -> tuple[str, float]:
    temperature = _temperature_for(int(target_difficulty))
    level_desc = _DIFF_LEVELS.get(int(target_difficulty), "siehe Stufenleitfaden")

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „Sport“, Oberthema („topic“) „{disc}“ (Deutsch).
Ziel-Schwierigkeit: {target_difficulty}/10 – {level_desc}

Kontext zu Schwierigkeitsstufen (1–10):
{_DIFF_GUIDE}

Vorgaben:
- Allgemeines Sportwissen; vermeide tagesaktuelle Ergebnisse/Transfers (keine Datumsabhängigkeit).
- Klar verständlich für Laien, dennoch präzise.
- Vier plausible Antwortoptionen (A–D), eine korrekt; keine Optionen wie „alle oben/keine der oben“.
- Erklärung in 2–3 Sätzen, die die richtige Lösung knapp begründet.
- Setze das Feld "topic" im JSON exakt auf „{disc}“.
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


def _pick_disc() -> str:
    names, weights = list(_SPORTS.keys()), list(_SPORTS.values())
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
    disc = _pick_disc()
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3, 5, 7])
    prompt, temp = _prompt(disc, tier, mode)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.8)
    if not data:
        return None

    # Defensive Normalisierung: alte Keys -> neue Keys
    if "topic" not in data and "discipline" in data:
        data["topic"] = data.pop("discipline")

    # Pflichtfelder pflegen/normalisieren
    data["category"] = CATEGORY_NAME
    data["topic"] = disc  # Oberthema immer festschreiben
    data["difficulty"] = int(data.get("difficulty", tier))

    # minimale Validierung
    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str):
        return None

    # Shuffle passiert zentral im Core
    return data
