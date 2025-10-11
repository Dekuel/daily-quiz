# kategorien/physik.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional
from openai import OpenAI

CATEGORY_NAME = "Physik"

# Themen mit Gewichten (Summe beliebig; Verteilung via random.choices)
_PHYSIK = {
    "Klassische Mechanik": 10,
    "Thermodynamik": 10,
    "Quantenmechanik": 10,
    "Analytische Mechanik": 10,
    "Relativitätstheorie": 10,
    "Elektrodynamik": 10,
    "Optik": 10,
    "Kern- und Teilchenphysik": 10,
    "Astrophysik": 10,
    "Festkörperphysik": 10,
}

_SCHEMA = """{
  "category": "Physik",
  "discipline": "Klassische Mechanik|Thermodynamik|Quantenmechanik|Analytische Mechanik|Relativitätstheorie|Elektrodynamik|Optik|Kern- und Teilchenphysik|Astrophysik|Festkörperphysik|berühmte Physiker",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

# Leitplanken je Schwierigkeitsbereich:
# Wir unterscheiden 5 Bänder (2er-Schritte), damit 8≠9≈10 etc. fühlbar wird.
_DIFF_BANDS = [
    ( (1, 2), "SEHR LEICHT (1–2): Alltagsphysik, anschauliche Begriffe, kaum Fachsprache.", 0.75 ),
    ( (3, 4), "LEICHT (3–4): Grundbegriffe/Definitionen, einfache qualitative Zusammenhänge.", 0.75 ),
    ( (5, 6), "MITTEL (5–6): Kombination mehrerer Konzepte, einfache quantitative Aussagen ohne Rechnen.", 0.75 ),
    ( (7, 8), "ANSRUCHSVOLL (7–8): präzisere Konzepte/Fallunterscheidungen, engere Distraktoren.", 0.75 ),
    ( (9,10), "SCHWER (9–10): tiefe Konzepte/Edge Cases, genaue Begriffsabgrenzungen, keine Herleitungen nötig.", 0.78 ),
]

def _band_for_difficulty(target: int) -> tuple[str, float]:
    t = int(target)
    for (lo, hi), note, temp in _DIFF_BANDS:
        if lo <= t <= hi:
            return note, temp
    # Fallback
    return "MITTEL (5–6): Kombination mehrerer Konzepte.", 0.55

def _prompt(disc: str, target_difficulty: int, mode: Optional[str]) -> tuple[str, float]:
    band_note, temperature = _band_for_difficulty(target_difficulty)

    # Physik-spezifische Anforderungen:
    # - Keine Rechnungen/Herleitungen notwendig (kein Latex), aber inhaltlich korrekt.
    # - Qualitativ/konzeptionell prüfen; ggf. kleine Zahlen-/Größenordnungen nur zur Einordnung.
    # - Distraktoren plausibel und fachlich nahe, ohne „alle oben/keine der oben“.
    # - Erklärung kurz und präzise (2–3 Sätze), verständlich für Laien/Studierende.
    # - Höhere Difficulty ⇒ engere Distraktoren und präzisere Begrifflichkeiten.
    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „Physik“, Disziplin „{disc}“ (Deutsch).
Ziel-Schwierigkeit: {target_difficulty}/10 – {band_note}

Vorgaben:
- Allgemeinverständliche, fachlich korrekte Formulierung; keine Formelumstellungen/Rechenwege.
- Qualitative/konzeptionelle Prüfung; Zahlen nur zur Orientierung (keine Herleitung).
- Vier plausible Antwortoptionen (A–D), eine korrekt; keine Antwort wie „alle oben/keine der oben“.
- Erklärung in 2–3 Sätzen: kurz, präzise, hilfreich.
- Gib ausschließlich valides JSON gemäß Schema zurück.

JSON-SCHEMA:
{_SCHEMA}
""".strip()

    return prompt, temperature


def _ask_json(p: str, temperature: float) -> dict | None:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        r = client.chat.completions.create(
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
    names, weights = list(_PHYSIK.keys()), list(_PHYSIK.values())
    return random.choices(names, weights=weights, k=1)[0]


def generate_one(
    past_texts: list[str],
    target_difficulty: Optional[int] = None,
    mode: Optional[str] = None,
) -> dict | None:
    """
    Wird vom Core mit target_difficulty (1..10) und mode ("physik" oder andere) aufgerufen.
    Falls target_difficulty fehlt, wählen wir einen mittel-nach-oben Zielwert, da Physik-Set insgesamt anspruchsvoller sein soll.
    """
    disc = _pick_disc()
    # Physik tendenziell schwerer: fallback 6/8 statt 3/5/7
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([6, 8])
    prompt, temp = _prompt(disc, tier, mode)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.8)
    if not data:
        return None

    # Pflichtfelder setzen/normalisieren
    data["category"] = CATEGORY_NAME
    data["discipline"] = data.get("discipline", disc)
    data["difficulty"] = int(data.get("difficulty", tier))

    # minimale Validierung
    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str):
        return None

    # Shuffle der Antworten übernimmt der Core zentral
    return data
