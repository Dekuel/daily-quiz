# kategorien/kunst_literatur.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional
from openai import OpenAI

CATEGORY_NAME = "Kunst und Literatur"

_SUB = {"Kunstgeschichte": 40, "Literatur": 40, "Musik": 20}

# ── Schema: 'topic' statt 'subtopic' ──────────────────────────────────────────
_SCHEMA = """{
  "category": "Kunst und Literatur",
  "topic": "Kunstgeschichte|Literatur|Musik",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

# ──────────────────────────────────────────────────────────────────────────────
# Neuer Schwierigkeitsleitfaden 1–10 (wie vorgegeben)
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

# Stufengenaue Beschreibung für die Promptzeile
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
    if d <= 2: return 0.8
    if d <= 4: return 0.8
    if d <= 6: return 0.8
    if d <= 8: return 0.8
    return 0.82

def _prompt(sub: str, target_difficulty: int, mode: Optional[str]) -> tuple[str, float]:
    temperature = _temperature_for(int(target_difficulty))
    level_desc = _DIFF_LEVELS.get(int(target_difficulty), "siehe Stufenleitfaden")

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „Kunst und Literatur“, Unterthema „{sub}“.
Ziel-Schwierigkeit: {target_difficulty}/10 – {level_desc}

Kontext zu Schwierigkeitsstufen (1–10):
{_DIFF_GUIDE}

Vorgaben:
- Auf Deutsch, knapp und eindeutig.
- Kulturwissen statt Datumsraterei um der Datumszahl willen; Daten nur, wenn inhaltlich sinnvoll.
- Keine Antwortoption „alle oben/keine der oben“.
- Vier plausible Optionen (A–D), genau eine korrekt.
- Erklärung: 2–3 Sätze, kurz und hilfreich (ggf. Stilrichtung/Einordnung).
- Das Feld "topic" im JSON enthält ausschließlich das Unterthema („{sub}“).
- Antworte ausschließlich mit **validem JSON** gemäß Schema.

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

    # Defensive Normalisierung: falls das Modell noch "subtopic" liefert
    if "topic" not in data and "subtopic" in data:
        data["topic"] = data.pop("subtopic")

    # In jedem Fall festschreiben, was als Ober-/Unterthema gemeint ist:
    data["topic"] = data.get("topic", sub)
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
