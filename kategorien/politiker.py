# -*- coding: utf-8 -*-
# Datei: kategorien/politikerquiz.py
import os, re, json, random, time
from typing import Optional, Tuple, List, Dict
from openai import OpenAI

CATEGORY_NAME = "Politiker"

# =====================================================================
#                      FESTE LISTEN (gleichverteilt auswählen)
# =====================================================================

# 16 Bundesministerien (nur Titel; Personen liefert GPT)
# Hinweis: Die folgende Liste enthält zweimal ein Verkehrsministerium
# mit vertauschter Wortreihenfolge (so wie im Original).
_MINISTERIEN: List[str] = [
    "Auswärtiges Amt",
    "Bundesministerium des Innern und für Heimat",
    "Bundesministerium der Justiz",
    "Bundesministerium der Finanzen",
    "Bundesministerium für Wirtschaft und Klimaschutz",
    "Bundesministerium für Arbeit und Soziales",
    "Bundesministerium für Ernährung und Landwirtschaft",
    "Bundesministerium für Familie, Senioren, Frauen und Jugend",
    "Bundesministerium für Gesundheit",
    "Bundesministerium für Verkehr und Digitales",
    "Bundesministerium für Umwelt, Naturschutz, nukleare Sicherheit und Verbraucherschutz",
    "Bundesministerium für Bildung und Forschung",
    "Bundesministerium für Wohnen, Stadtentwicklung und Bauwesen",
    "Bundesministerium für wirtschaftliche Zusammenarbeit und Entwicklung",
    "Bundesministerium der Verteidigung",
    "Bundesministerium für Digitales und Verkehr",
]

# „Wichtige Länder“ (gleichverteilt; Person liefert GPT)
_WICHTIGE_LAENDER: List[str] = [
    "USA", "Vereinigtes Königreich", "Frankreich", "Deutschland", "Italien",
    "Spanien", "Kanada", "Japan", "Indien", "China",
    "Brasilien", "Südafrika", "Türkei", "Mexiko", "Australien", "Ukraine", "Argentinien"
]

# Bedeutende Organisationen (Person liefert GPT)
_WICHTIGE_ORGS: List[str] = [
    "Vereinte Nationen (UN)",
    "NATO",
    "Europäische Zentralbank (EZB)",
    "Europäische Kommission",
    "Europarat",
    "Internationaler Währungsfonds (IWF)",
    "Weltbank",
    "Weltgesundheitsorganisation (WHO)",
    "Organisation für wirtschaftliche Zusammenarbeit und Entwicklung (OECD)",
    "Welthandelsorganisation (WTO)",
    "Organisation für Sicherheit und Zusammenarbeit in Europa (OSZE)",
    "Internationaler Gerichtshof (IGH)",
]

# Bundeskanzler nach Amtszeit (stabil)
_CHANCELLOR_TERMS: List[Dict[str, str]] = [
    {"amtszeit": "1949–1963", "kanzler": "Konrad Adenauer"},
    {"amtszeit": "1963–1966", "kanzler": "Ludwig Erhard"},
    {"amtszeit": "1966–1969", "kanzler": "Kurt Georg Kiesinger"},
    {"amtszeit": "1969–1974", "kanzler": "Willy Brandt"},
    {"amtszeit": "1974–1982", "kanzler": "Helmut Schmidt"},
    {"amtszeit": "1982–1998", "kanzler": "Helmut Kohl"},
    {"amtszeit": "1998–2005", "kanzler": "Gerhard Schröder"},
    {"amtszeit": "2005–2021", "kanzler": "Angela Merkel"},
    {"amtszeit": "2021–2025", "kanzler": "Olaf Scholz"},
]

# Parteikürzel (stabil)
_PARTY_ACRONYMS: Dict[str, str] = {
    "CDU": "Christlich Demokratische Union Deutschlands",
    "CSU": "Christlich-Soziale Union in Bayern",
    "SPD": "Sozialdemokratische Partei Deutschlands",
    "FDP": "Freie Demokratische Partei",
    "AfD": "Alternative für Deutschland",
    "BSW": "Bündnis Sahra Wagenknecht – Vernunft und Gerechtigkeit",
}

# Sitze in Deutschland (Institution → Stadt) – stabil
_DE_SEATS: List[Dict[str, str]] = [
    {"institution": "Bundesregierung (Regierungssitz)", "stadt": "Berlin"},
    {"institution": "Bundestag (Plenarsitz)", "stadt": "Berlin"},
    {"institution": "Bundesrat (Plenarsaal)", "stadt": "Berlin"},
    {"institution": "Bundesverfassungsgericht", "stadt": "Karlsruhe"},
    {"institution": "Bundesgerichtshof (BGH)", "stadt": "Karlsruhe"},
    {"institution": "Deutsche Bundesbank – Zentrale", "stadt": "Frankfurt am Main"},
    {"institution": "Europäische Zentralbank (EZB) – Sitz in DE", "stadt": "Frankfurt am Main"},
]

# Sitze international (Organisation → Stadt) – stabil
_INTL_SEATS: List[Dict[str, str]] = [
    {"organisation": "Vereinte Nationen (UN) – Hauptquartier", "stadt": "New York"},
    {"organisation": "NATO – Hauptsitz", "stadt": "Brüssel"},
    {"organisation": "Internationaler Gerichtshof (IGH)", "stadt": "Den Haag"},
    {"organisation": "Europäischer Gerichtshof (EuGH)", "stadt": "Luxemburg"},
    {"organisation": "Europarat – Sitz", "stadt": "Straßburg"},
    {"organisation": "OSZE – Sekretariat", "stadt": "Wien"},
    {"organisation": "OECD – Hauptsitz", "stadt": "Paris"},
    {"organisation": "WTO – Sitz", "stadt": "Genf"},
]

# =====================================================================
#                         SCHEMA & KONFIG
# =====================================================================

_SCHEMA = """{
  "category": "Politik",
  "discipline": "Ministerien (DE)|Regierungschefs (Welt)|Org-Personen|Bundeskanzler (Amtszeit)|Parteikürzel (DE)|Grundrechte (DE)|Sitze (DE)|Sitze (International)",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

# Prozentverteilung (summe = 100) – Auswahl erfolgt LOKAL per random.choices
_WEIGHTS = [
    ("minister_de_gpt", 38),
    ("regierungschefs_gpt", 13),
    ("org_person_gpt", 10),
    ("kanzler_zeit_local", 5),
    ("partei_kuerzel_local", 7),
    ("grundrechte_gpt", 10),
    ("sitze_de_local", 8),
    ("sitze_intl_local", 10),
]

# GPT-Temperatur: fester Wert, da Schwierigkeit irrelevant
_GPT_TEMPERATURE = 0.72

# =====================================================================
#                       GPT-Helfer (striktes JSON)
# =====================================================================

def _ask_json(prompt: str, temperature: float = _GPT_TEMPERATURE) -> dict | None:
    """
    GPT dient NUR zur sprachlichen Formulierung der Frage/Erklärung.
    Zufall (Kategorie/Seed/Antwortmischung) passiert komplett lokal.
    """
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Antworte ausschließlich mit valide parsem barem JSON (kein Text außerhalb des JSON)."},
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
        )
        raw = (r.choices[0].message.content or "").strip()
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception:
        return None

# =====================================================================
#                 NEU: LOKALES Mischen & Normalisieren
# =====================================================================

_LETTERS = ["A", "B", "C", "D"]

def _extract_choice_text(choice: str) -> str:
    # akzeptiert "A: Text" oder nur "Text"
    parts = choice.split(":", 1)
    return parts[1].strip() if len(parts) == 2 else choice.strip()

def _format_choices(choice_texts: List[str]) -> List[str]:
    return [f"{_LETTERS[i]}: {choice_texts[i]}" for i in range(4)]

def _shuffle_choices_and_fix_answer(data: dict) -> dict:
    """
    Erwartet data['choices'] (A–D) und data['correct_answer'].
    Wir extrahieren die reinen Texte, bestimmen die korrekte, mischen lokal und setzen den Buchstaben neu.
    Primärannahme: GPT liefert die richtige Antwort bei 'A'. Fallback: correct_answer-Feld.
    """
    if not isinstance(data, dict):
        return data
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return data

    choice_texts = [_extract_choice_text(c) for c in data["choices"]]

    # Standard: korrekt ist A
    correct_idx = 0
    # Fallback: respektiere vorhandenes Feld (falls GPT sich nicht an Vorgabe hält)
    if isinstance(data.get("correct_answer"), str) and data["correct_answer"] in _LETTERS:
        correct_idx = _LETTERS.index(data["correct_answer"])

    flags = [i == correct_idx for i in range(4)]
    pairs = list(zip(choice_texts, flags))
    random.shuffle(pairs)

    shuffled_texts = [t for (t, _) in pairs]
    shuffled_flags = [f for (_, f) in pairs]
    new_correct_idx = shuffled_flags.index(True)

    data["choices"] = _format_choices(shuffled_texts)
    data["correct_answer"] = _LETTERS[new_correct_idx]
    return data

# =====================================================================
#                 GPT-Prompts (mit "A ist korrekt")
# =====================================================================

def _prompt_gpt_from_choice(discipline: str, seed_text: str) -> str:
    """Wir geben NUR die gewählte Entität (Ministerium/Land/Organisation) vor.
    GPT soll die Frage/Erklärung formulieren und die richtige Antwort unter A listen.
    """
    if discipline == "Ministerien (DE)":
        task = f"Erzeuge eine Frage: Wer ist (allgemein, ohne Datum) Bundesminister(in) für „{seed_text}“?"
    elif discipline == "Regierungschefs (Welt)":
        task = f"Erzeuge eine Frage: Wer ist (allgemein) Regierungschef von „{seed_text}“?"
    elif discipline == "Org-Personen":
        task = f"Erzeuge eine Frage: Wer ist (allgemein) die/der oberste Amtsinhaber(in) der Organisation „{seed_text}“?"
    else:
        task = f"Erzeuge eine Frage basierend auf: {seed_text}"

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (Deutsch) zur Kategorie „Politik“, Disziplin „{discipline}“.

Aufgabe:
- {task}
- Vier plausible Antwortoptionen A–D.
- WICHTIG: Setze die KORREKTE Antwort IMMER bei A. B–D sind plausible Distraktoren.
- NEUTRAL formulieren; keine datumsabhängigen Fakten in der Frage.
- Gib ausschließlich valides JSON gemäß diesem Schema aus (kein Text außerhalb):

{_SCHEMA}
""".strip()
    return prompt

def _prompt_grundrechte() -> str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (Deutsch) zur Kategorie „Politik“, Disziplin „Grundrechte (DE)“.

Vorgaben:
- Thema: „Was ist KEIN Grundrecht im Sinne des Grundgesetzes (GG)?“.
- Vier plausible Antwortoptionen A–D, KORREKTE Antwort IMMER bei A; keine „alle/keine der oben“.
- Erklärung in 2–3 Sätzen.
- Gib ausschließlich valides JSON gemäß Schema:

{_SCHEMA}
""".strip()

# =====================================================================
#                 LOKALE GENERATOREN (stabile Wissensbereiche)
# =====================================================================

def _choices_from_correct_and_pool(correct: str, pool: List[str]) -> Tuple[List[str], str]:
    distractors = [x for x in pool if x != correct]
    random.shuffle(distractors)
    opts = [correct] + distractors[:3]  # A ist korrekt, wir mischen später lokal erneut
    letters = ["A", "B", "C", "D"]
    return [f"{letters[i]}: {opts[i]}" for i in range(4)], "A"

def _gen_kanzler_zeit_local() -> dict | None:
    entry = random.choice(_CHANCELLOR_TERMS)
    pool = [e["kanzler"] for e in _CHANCELLOR_TERMS]
    choices, correct_letter = _choices_from_correct_and_pool(entry["kanzler"], pool)
    data = {
        "category": CATEGORY_NAME,
        "discipline": "Bundeskanzler (Amtszeit)",
        "question": f"Wer war Bundeskanzler(in) der Bundesrepublik Deutschland in der Amtszeit {entry['amtszeit']}?",
        "choices": choices,
        "correct_answer": correct_letter,
        "explanation": "Historische Kanzlerschaften sind eindeutig datiert; die Alternativen sind Kanzler anderer Zeiträume.",
        "difficulty": 1,
    }
    return _shuffle_choices_and_fix_answer(data)

def _gen_partei_kuerzel_local() -> dict | None:
    kuerzel, langname = random.choice(list(_PARTY_ACRONYMS.items()))
    pool = list(_PARTY_ACRONYMS.values())
    choices, correct_letter = _choices_from_correct_and_pool(langname, pool)
    data = {
        "category": CATEGORY_NAME,
        "discipline": "Parteikürzel (DE)",
        "question": f"Wofür steht das Parteikürzel „{kuerzel}“ in Deutschland?",
        "choices": choices,
        "correct_answer": correct_letter,
        "explanation": "Parteibezeichnungen sind offiziell festgelegt; die anderen Optionen sind Bezeichnungen anderer Parteien.",
        "difficulty": 1,
    }
    return _shuffle_choices_and_fix_answer(data)

def _gen_sitze_de_local() -> dict | None:
    entry = random.choice(_DE_SEATS)
    pool = list({e["stadt"] for e in _DE_SEATS})
    choices, correct_letter = _choices_from_correct_and_pool(entry["stadt"], pool)
    data = {
        "category": CATEGORY_NAME,
        "discipline": "Sitze (DE)",
        "question": f"In welcher Stadt hat {entry['institution']} seinen/ihren Sitz (Hauptsitz/Plenarsitz)?",
        "choices": choices,
        "correct_answer": correct_letter,
        "explanation": "Bundesinstitutionen haben definierte Sitze; die anderen Städte sind Sitze anderer Institutionen.",
        "difficulty": 1,
    }
    return _shuffle_choices_and_fix_answer(data)

def _gen_sitze_intl_local() -> dict | None:
    entry = random.choice(_INTL_SEATS)
    pool = list({e["stadt"] for e in _INTL_SEATS})
    choices, correct_letter = _choices_from_correct_and_pool(entry["stadt"], pool)
    data = {
        "category": CATEGORY_NAME,
        "discipline": "Sitze (International)",
        "question": f"In welcher Stadt befindet sich der Hauptsitz/Sitz von {entry['organisation']}?",
        "choices": choices,
        "correct_answer": correct_letter,
        "explanation": "Internationale Organisationen haben feste Hauptsitze; die Alternativen sind Sitze anderer Organisationen.",
        "difficulty": 1,
    }
    return _shuffle_choices_and_fix_answer(data)

# =====================================================================
#                 GPT-basierte Generierung (Seed lokal → GPT)
# =====================================================================

def _gen_minister_de_gpt() -> dict | None:
    ministerium = random.choice(_MINISTERIEN)  # Seed lokal
    prompt = _prompt_gpt_from_choice("Ministerien (DE)", ministerium)
    data = _ask_json(prompt)
    return _shuffle_choices_and_fix_answer(data) if data else None

def _gen_regierungschefs_gpt() -> dict | None:
    land = random.choice(_WICHTIGE_LAENDER)  # Seed lokal
    prompt = _prompt_gpt_from_choice("Regierungschefs (Welt)", land)
    data = _ask_json(prompt)
    return _shuffle_choices_and_fix_answer(data) if data else None

def _gen_org_person_gpt() -> dict | None:
    org = random.choice(_WICHTIGE_ORGS)  # Seed lokal
    prompt = _prompt_gpt_from_choice("Org-Personen", org)
    data = _ask_json(prompt)
    return _shuffle_choices_and_fix_answer(data) if data else None

def _gen_grundrechte_gpt() -> dict | None:
    # Grundrechte bleibt GPT-inhaltlich; danach lokal mischen/normalisieren
    data = _ask_json(_prompt_grundrechte())
    return _shuffle_choices_and_fix_answer(data) if data else None

# =====================================================================
#                              PUBLIC API
# =====================================================================

def _pick_weighted_type() -> str:
    names, weights = zip(*_WEIGHTS)
    # Kategorieauswahl erfolgt lokal – GPT hat keinen Einfluss auf Wahrscheinlichkeiten
    return random.choices(names, weights=weights, k=1)[0]

def generate_one(
    past_texts: List[str],
    target_difficulty: Optional[int] = None,  # existiert nur für API-Kompatibilität, wird ignoriert
    mode: Optional[str] = None,               # ebenfalls ignoriert
) -> dict | None:
    """
    Erzeugt EINE Frage als JSON (Schema siehe oben).
    Verteilung: 45% Ministerien (GPT), 15% Regierungschefs (GPT), 10% Org-Personen (GPT),
                5% Kanzler (lokal), 5% Parteikürzel (lokal), 5% Grundrechte (GPT),
                5% Sitze (DE) (lokal), 10% Sitze (International) (lokal).
    Innerhalb der Listen: GLEICHE Wahrscheinlichkeit je Eintrag.
    Schwierigkeit wird nicht berücksichtigt und fix auf 1 gesetzt.

    WICHTIG: Alle Zufälle (Kategorie/Seed/Antwort-Mischen) werden lokal bestimmt.
    GPT dient nur der sprachlichen Formulierung (plus Erklärung).
    """
    qtype = _pick_weighted_type()

    gen_map = {
        "minister_de_gpt": _gen_minister_de_gpt,
        "regierungschefs_gpt": _gen_regierungschefs_gpt,
        "org_person_gpt": _gen_org_person_gpt,
        "kanzler_zeit_local": _gen_kanzler_zeit_local,
        "partei_kuerzel_local": _gen_partei_kuerzel_local,
        "grundrechte_gpt": _gen_grundrechte_gpt,
        "sitze_de_local": _gen_sitze_de_local,
        "sitze_intl_local": _gen_sitze_intl_local,
    }

    data = gen_map[qtype]()
    time.sleep(0.3)

    if not data:
        return None

    # Pflichtfelder pflegen/normalisieren
    data["category"] = CATEGORY_NAME
    data["difficulty"] = 1

    # minimale Validierung
    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str) or data["correct_answer"] not in ("A","B","C","D"):
        return None

    return data
