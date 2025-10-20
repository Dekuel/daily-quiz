# kategorien/physik.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional, List, Tuple
from openai import OpenAI

# Import der Subthemen
from Unterkategorien.Physik.klassische_mechanik import SUBDISCIPLINES as KM_SUBS
from Unterkategorien.Physik.analytische_mechanik import SUBDISCIPLINES as AM_SUBS
from Unterkategorien.Physik.thermodynamik import SUBDISCIPLINES as TH_SUBS
from Unterkategorien.Physik.elektrodynamik import SUBDISCIPLINES as ED_SUBS
from Unterkategorien.Physik.srt import SUBDISCIPLINES as RT_SUBS
from Unterkategorien.Physik.quantenmechanik import SUBDISCIPLINES as QM_SUBS
from Unterkategorien.Physik.optik import SUBDISCIPLINES as OP_SUBS
from Unterkategorien.Physik.kernteilchen import SUBDISCIPLINES as KT_SUBS
from Unterkategorien.Physik.festkoerper import SUBDISCIPLINES as FK_SUBS
from Unterkategorien.Physik.statmech import SUBDISCIPLINES as SM_SUBS



CATEGORY_NAME = "Physik"

_PHYSIK = {
    "Klassische Mechanik": 10,
    "Thermodynamik": 10,
    "Quantenmechanik": 15,
    "Analytische Mechanik": 10,
    "Relativitätstheorie": 5,
    "Elektrodynamik": 10,
    "Optik": 10,
    "Kern- und Teilchenphysik": 10,
    "Statistische Mechanik": 10,
    "Festkörperphysik": 10,
}

# Mapping der externen Subtopic-Dateien
_SUBDISCIPLINES: dict[str, List[Tuple[str, int]]] = {
    "Klassische Mechanik": KM_SUBS,
    "Analytische Mechanik": AM_SUBS,
    "Thermodynamik": TH_SUBS,
    "Elektrodynamik": ED_SUBS,
    "Relativitätstheorie": RT_SUBS,
    "Quantenmechanik": QM_SUBS,
    "Optik": OP_SUBS,
    "Kern- und Teilchenphysik": KT_SUBS,
    "Festkörperphysik": FK_SUBS,
    "Statistische Mechanik": SM_SUBS,

}

_SCHEMA = """{
  "category": "Physik",
  "discipline": "Klassische Mechanik|Thermodynamik|Quantenmechanik|Analytische Mechanik|Relativitätstheorie|Elektrodynamik|Optik|Kern- und Teilchenphysik|Astrophysik|Festkörperphysik|berühmte Physiker",
  "subcategory": "...",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""


_DIFF_BANDS = [
    ((1, 2), "SEHR LEICHT (1–2): Alltagsphysik, anschauliche Begriffe, kaum Fachsprache.", 0.75),
    ((3, 4), "LEICHT (3–4): Grundbegriffe/Definitionen, einfache qualitative Zusammenhänge.", 0.75),
    ((5, 6), "MITTEL (5–6): Kombination mehrerer Konzepte, einfache quantitative Aussagen ohne Rechnen.", 0.75),
    ((7, 8), "ANSRUCHSVOLL (7–8): präzisere Konzepte/Fallunterscheidungen, engere Distraktoren.", 0.75),
    ((9,10), "SCHWER (9–10): tiefe Konzepte/Edge Cases, genaue Begriffsabgrenzungen", 0.78),
]

def _band_for_difficulty(target: int) -> tuple[str, float]:
    for (lo, hi), note, temp in _DIFF_BANDS:
        if lo <= target <= hi:
            return note, temp
    return "MITTEL (5–6): Kombination mehrerer Konzepte.", 0.55

def _pick_weighted(pairs: List[Tuple[str, int]]) -> str:
    names, weights = zip(*pairs)
    return random.choices(list(names), weights=list(weights), k=1)[0]

def _prompt(disc: str, target_difficulty: int, mode: Optional[str], subtopic: Optional[str] = None) -> tuple[str, float]:
    band_note, temperature = _band_for_difficulty(target_difficulty)
    sub_line = f'- Subthema: "{subtopic}"\n' if subtopic else '- Subthema: ""\n'
    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie "Physik" (Deutsch).
- Disziplin: "{disc}"
{sub_line}Ziel-Schwierigkeit: {target_difficulty}/10 – {band_note}

Vorgaben:
- Nutze das Subthema (falls nicht leer) als inhaltlichen Fokus der Frage.
- Setze "discipline" exakt auf "{disc}" und "subcategory" exakt auf das oben angegebene Subthema (oder "" wenn keins).
- Vier plausible Antwortoptionen (A–D), eine korrekt.
- Erklärung in 2–3 Sätzen: kurz, präzise, hilfreich.
- Antworte ausschließlich mit validem JSON gemäß Schema.


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
                {"role": "system", "content": "Antworte ausschließlich mit valide parsem barem JSON."},
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
    return random.choices(list(_PHYSIK.keys()), weights=list(_PHYSIK.values()), k=1)[0]

def generate_one(past_texts: list[str], target_difficulty: Optional[int] = None, mode: Optional[str] = None) -> dict | None:
    disc = _pick_disc()
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([6, 8])

    sub = None
    if disc in _SUBDISCIPLINES and _SUBDISCIPLINES[disc]:
        sub = _pick_weighted(_SUBDISCIPLINES[disc])

    prompt, temp = _prompt(disc, tier, mode, subtopic=sub)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.8)
    if not data:
        return None

    data["category"] = CATEGORY_NAME
    data["discipline"] = data.get("discipline", disc)
    data["difficulty"] = int(data.get("difficulty", tier))

    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str):
        return None

    return data
