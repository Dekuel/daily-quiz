# -*- coding: utf-8 -*-
# Datei: kategorien/politikerquiz.py
import os, re, json, random, time, threading
from typing import Optional, Tuple, List, Dict
from openai import OpenAI
import requests
from functools import lru_cache

CATEGORY_NAME = "Politiker"

# =====================================================================
#                      FESTE LISTEN (gleichverteilt auswählen)
# =====================================================================

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

_WICHTIGE_LAENDER: List[str] = [
    "USA", "Vereinigtes Königreich", "Frankreich", "Deutschland", "Italien",
    "Spanien", "Kanada", "Japan", "Indien", "China",
    "Brasilien", "Südafrika", "Türkei", "Mexiko", "Australien", "Ukraine", "Argentinien"
]

_WICHTIGE_ORGS: List[str] = [
    "Vereinte Nationen",
    "NATO",
    "Europäische Zentralbank",
    "Europäische Kommission",
    "Europarat",
    "Internationaler Währungsfonds",
    "Weltbank",
    "Weltgesundheitsorganisation",
    "OECD",
    "Welthandelsorganisation",
    "OSZE",
    "Internationaler Gerichtshof",
    "Federal Reserve",
]

_CHANCELLOR_TERMS: List[Dict[str, str]] = [
    {"amtszeit": "1949–1963", "kanzler": "Konrad Adenauer"},
    {"amtszeit": "1963–1966", "kanzler": "Ludwig Erhard"},
    {"amtszeit": "1966–1969", "kanzler": "Kurt Georg Kiesinger"},
    {"amtszeit": "1969–1974", "kanzler": "Willy Brandt"},
    {"amtszeit": "1974–1982", "kanzler": "Helmut Schmidt"},
    {"amtszeit": "1982–1998", "kanzler": "Helmut Kohl"},
    {"amtszeit": "1998–2005", "kanzler": "Gerhard Schröder"},
    {"amtszeit": "2005–2021", "kanzler": "Angela Merkel"},
    {"amtszeit": "2021–", "kanzler": "Olaf Scholz"},
]

_PARTY_ACRONYMS: Dict[str, str] = {
    "CDU": "Christlich Demokratische Union Deutschlands",
    "CSU": "Christlich-Soziale Union in Bayern",
    "SPD": "Sozialdemokratische Partei Deutschlands",
    "FDP": "Freie Demokratische Partei",
    "AfD": "Alternative für Deutschland",
    "BSW": "Bündnis Sahra Wagenknecht – Vernunft und Gerechtigkeit",
}

_DE_SEATS: List[Dict[str, str]] = [
    {"institution": "Bundesregierung (Regierungssitz)", "stadt": "Berlin"},
    {"institution": "Bundestag (Plenarsitz)", "stadt": "Berlin"},
    {"institution": "Bundesrat (Plenarsaal)", "stadt": "Berlin"},
    {"institution": "Bundesverfassungsgericht", "stadt": "Karlsruhe"},
    {"institution": "Bundesgerichtshof (BGH)", "stadt": "Karlsruhe"},
    {"institution": "Deutsche Bundesbank – Zentrale", "stadt": "Frankfurt am Main"},
    {"institution": "Europäische Zentralbank (EZB) – Sitz in DE", "stadt": "Frankfurt am Main"},
]

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
#                         SCHNITTSTELLEN / KONFIG
# =====================================================================

_WIKIPEDIA_API = "https://{lang}.wikipedia.org/w/api.php"
_WIKIDATA_SPARQL = "https://query.wikidata.org/sparql"
_HTTP_TIMEOUT = 10
_CACHE_PATH = os.environ.get("POLQUIZ_CACHE_FILE", "politikerquiz_cache.json")
_cache_lock = threading.Lock()
_memory_cache: Dict[str, Dict[str, str]] = {}  # key -> {"value": "...", "ts": 1700000000}

def _load_cache_from_disk():
    global _memory_cache
    if not os.path.exists(_CACHE_PATH):
        return
    try:
        with open(_CACHE_PATH, "r", encoding="utf-8") as f:
            _memory_cache = json.load(f)
    except Exception:
        pass

def _save_cache_to_disk():
    try:
        with _cache_lock, open(_CACHE_PATH, "w", encoding="utf-8") as f:
            json.dump(_memory_cache, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

_load_cache_from_disk()

def _cache_get(key: str, max_age_sec: int = 60 * 60 * 24 * 7) -> Optional[str]:
    ent = _memory_cache.get(key)
    if not ent:
        return None
    if time.time() - ent.get("ts", 0) > max_age_sec:
        return None
    return ent.get("value")

def _cache_set(key: str, value: str) -> None:
    _memory_cache[key] = {"value": value, "ts": time.time()}
    _save_cache_to_disk()

# =====================================================================
#                       WIKIDATA / WIKIPEDIA HELFER
# =====================================================================

def _wikipedia_title_to_qid(title_de: str, lang: str = "de") -> Optional[str]:
    """
    Holt die Wikidata-QID zu einem deutschen Wikipedia-Titel/Begriff.
    Funktioniert gut mit offiziellen Namen wie 'Bundesministerium der Finanzen'.
    """
    key = f"qid:{lang}:{title_de}"
    cached = _cache_get(key)
    if cached:
        return cached
    try:
        r = requests.get(
            _WIKIPEDIA_API.format(lang=lang),
            params={
                "action": "query",
                "format": "json",
                "prop": "pageprops",
                "ppprop": "wikibase_item",
                "titles": title_de,
                "redirects": 1,
            },
            timeout=_HTTP_TIMEOUT,
        )
        r.raise_for_status()
        data = r.json()
        pages = data.get("query", {}).get("pages", {})
        for _, page in pages.items():
            qid = page.get("pageprops", {}).get("wikibase_item")
            if qid:
                _cache_set(key, qid)
                return qid
    except Exception:
        return None
    return None

def _sparql_first_label(query: str, lang: str = "de") -> Optional[str]:
    """
    Führt SPARQL aus und gibt das erste ?whoLabel als String zurück.
    """
    key = f"sparql:{hash(query)}:{lang}"
    cached = _cache_get(key, max_age_sec=6 * 60 * 60)  # 6h
    if cached:
        return cached
    try:
        headers = {
            "Accept": "application/sparql-results+json",
            "User-Agent": "PolitikerQuiz/1.0 (https://example.org)"
        }
        r = requests.get(
            _WIKIDATA_SPARQL,
            params={"query": query},
            headers=headers,
            timeout=_HTTP_TIMEOUT,
        )
        r.raise_for_status()
        j = r.json()
        bindings = j.get("results", {}).get("bindings", [])
        if not bindings:
            return None
        label = bindings[0].get("whoLabel", {}).get("value")
        if label:
            _cache_set(key, label)
            return label
    except Exception:
        return None
    return None

def _get_head_of_organization_name(qid: str) -> Optional[str]:
    # P169: Leiter/in / CEO / 'head of the organization'
    query = f"""
    SELECT ?whoLabel WHERE {{
      wd:{qid} wdt:P169 ?who .
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "de,en". }}
    }}
    LIMIT 1
    """
    return _sparql_first_label(query)

def _get_head_of_government_name(country_qid: str) -> Optional[str]:
    # P6: head of government
    query = f"""
    SELECT ?whoLabel WHERE {{
      wd:{country_qid} wdt:P6 ?who .
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "de,en". }}
    }}
    LIMIT 1
    """
    return _sparql_first_label(query)

# Bequeme Resolver (nehmen einen DE-Namen, finden QID automatisch)
def resolve_minister_name(ministry_name_de: str) -> Optional[str]:
    qid = _wikipedia_title_to_qid(ministry_name_de)
    if not qid:
        return None
    return _get_head_of_organization_name(qid)

def resolve_org_head(org_name_de: str) -> Optional[str]:
    qid = _wikipedia_title_to_qid(org_name_de)
    if not qid:
        return None
    return _get_head_of_organization_name(qid)

def resolve_head_of_government(country_name_de: str) -> Optional[str]:
    # Wikipedia-Titel ist in der Regel identisch mit dem Landesnamen (DE),
    # Redirects werden vom API-Call gehandhabt.
    qid = _wikipedia_title_to_qid(country_name_de)
    if not qid:
        return None
    return _get_head_of_government_name(qid)

# =====================================================================
#                       GPT-Formulierung (unverändert)
# =====================================================================

_GPT_TEMPERATURE = 0.72

_SCHEMA = """{
  "category": "Politik",
  "discipline": "Ministerien (DE)|Regierungschefs (Welt)|Org-Personen|Bundeskanzler (Amtszeit)|Parteikürzel (DE)|Grundrechte (DE)|Sitze (DE)|Sitze (International)",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

def _ask_json(prompt: str, temperature: float = _GPT_TEMPERATURE) -> dict | None:
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
#                 LOKALES Mischen & Normalisieren
# =====================================================================

_LETTERS = ["A", "B", "C", "D"]

def _extract_choice_text(choice: str) -> str:
    parts = choice.split(":", 1)
    return parts[1].strip() if len(parts) == 2 else choice.strip()

def _format_choices(choice_texts: List[str]) -> List[str]:
    return [f"{_LETTERS[i]}: {choice_texts[i]}" for i in range(4)]

def _shuffle_choices_and_fix_answer(data: dict) -> dict:
    if not isinstance(data, dict):
        return data
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return data

    choice_texts = [_extract_choice_text(c) for c in data["choices"]]

    # Standard: korrekt ist A (wir setzen es ohnehin vorher manuell)
    correct_idx = 0
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
#                 GPT-Prompts (A ist korrekt)
# =====================================================================

def _prompt_gpt_from_choice(discipline: str, seed_text: str, correct_name: Optional[str]) -> str:
    if discipline == "Ministerien (DE)":
        task = (f"Erzeuge eine Frage: Wer ist (ohne Datum nennen) Bundesminister(in) für „{seed_text}“?")
    elif discipline == "Regierungschefs (Welt)":
        task = (f"Erzeuge eine Frage: Wer ist (neutral, ohne Datum) Regierungschef von „{seed_text}“?")
    elif discipline == "Org-Personen":
        task = (
            "Erzeuge eine Frage: Wie heißt (neutral) die/der amtierende oberste Amtsinhaber(in) "
            f"der Organisation „{seed_text}“ (z. B. Generalsekretär(in), Präsident(in), Direktor(in))? "
            "Antwortoptionen ausschließlich als Personennamen."
        )
    else:
        task = f"Erzeuge eine Frage basierend auf: {seed_text}"

    # wichtiger Hinweis für A=korrekt
    correct_hint = f"Die korrekte Antwort lautet: {correct_name or 'N/A'}."
    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (Deutsch) zur Kategorie „Politik“, Disziplin „{discipline}“.

Aufgabe:
- {task}
- Vier plausible Antwortoptionen A–D.
- WICHTIG: Setze die KORREKTE Antwort IMMER bei A. B–D sind plausible Distraktoren.
- Verwende keine konkreten Datumsangaben in Frage/Erklärung.
- {correct_hint}
- Gib ausschließlich valides JSON gemäß diesem Schema aus:

{_SCHEMA}
""".strip()
    return prompt

def _prompt_grundrechte() -> str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (Deutsch) zur Kategorie „Politik“, Disziplin „Grundrechte (DE)“.

Vorgaben:
- Thema: „Was ist KEIN Grundrecht im Sinne des Grundgesetzes (GG)?“.
- Vier plausible Antwortoptionen A–D, KORREKTE Antwort IMMER bei A; kein „alle/keine der oben“.
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
    opts = [correct] + distractors[:3]
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
        "question": f"Wofür steht das Parteikürzel „{kuerzel}““ in Deutschland?",
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
#           GPT-basierte Generatoren mit LIVE-Antwort (Wikidata)
# =====================================================================

def _gen_minister_de_gpt() -> dict | None:
    ministerium = random.choice(_MINISTERIEN)
    correct_name = resolve_minister_name(ministerium)  # LIVE
    prompt = _prompt_gpt_from_choice("Ministerien (DE)", ministerium, correct_name)
    data = _ask_json(prompt)
    if not data:
        return None
    # Setze A explizit auf die live ermittelte Person (falls vorhanden)
    if correct_name:
        # Ersetze A-Text
        choices = data.get("choices", [])
        if isinstance(choices, list) and len(choices) == 4:
            # setze A:
            choices_texts = [_extract_choice_text(c) for c in choices]
            choices_texts[0] = correct_name
            data["choices"] = _format_choices(choices_texts)
            data["correct_answer"] = "A"
    return _shuffle_choices_and_fix_answer(data)

def _gen_regierungschefs_gpt() -> dict | None:
    land = random.choice(_WICHTIGE_LAENDER)
    correct_name = resolve_head_of_government(land)  # LIVE
    prompt = _prompt_gpt_from_choice("Regierungschefs (Welt)", land, correct_name)
    data = _ask_json(prompt)
    if not data:
        return None
    if correct_name:
        choices = data.get("choices", [])
        if isinstance(choices, list) and len(choices) == 4:
            choices_texts = [_extract_choice_text(c) for c in choices]
            choices_texts[0] = correct_name
            data["choices"] = _format_choices(choices_texts)
            data["correct_answer"] = "A"
    return _shuffle_choices_and_fix_answer(data)

def _gen_org_person_gpt() -> dict | None:
    org = random.choice(_WICHTIGE_ORGS)
    correct_name = resolve_org_head(org)  # LIVE
    prompt = _prompt_gpt_from_choice("Org-Personen", org, correct_name)
    data = _ask_json(prompt)
    if not data:
        return None
    if correct_name:
        choices = data.get("choices", [])
        if isinstance(choices, list) and len(choices) == 4:
            choices_texts = [_extract_choice_text(c) for c in choices]
            choices_texts[0] = correct_name
            data["choices"] = _format_choices(choices_texts)
            data["correct_answer"] = "A"
    return _shuffle_choices_and_fix_answer(data)

def _gen_grundrechte_gpt() -> dict | None:
    data = _ask_json(_prompt_grundrechte())
    return _shuffle_choices_and_fix_answer(data) if data else None

# =====================================================================
#                              PUBLIC API
# =====================================================================

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

def _pick_weighted_type() -> str:
    names, weights = zip(*_WEIGHTS)
    return random.choices(names, weights=weights, k=1)[0]

def generate_one(
    past_texts: List[str],
    target_difficulty: Optional[int] = None,
    mode: Optional[str] = None,
) -> dict | None:
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

    data["category"] = CATEGORY_NAME
    data["difficulty"] = 1

    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str) or data["correct_answer"] not in ("A","B","C","D"):
        return None

    return data
