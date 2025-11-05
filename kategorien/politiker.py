# -*- coding: utf-8 -*-
# Datei: kategorien/politikerquiz.py
import os, re, json, random, time, threading
from typing import Optional, Tuple, List, Dict
from openai import OpenAI
import requests

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
    "Bundesministerium für Umwelt, Naturschutz, nukleare Sicherheit und Verbraucherschutz",
    "Bundesministerium für Bildung und Forschung",
    "Bundesministerium für Wohnen, Stadtentwicklung und Bauwesen",
    "Bundesministerium für wirtschaftliche Zusammenarbeit und Entwicklung",
    "Bundesministerium der Verteidigung",
    # Nur die offizielle Schreibweise behalten:
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

# Plausible Falschantworten pro Kürzel (gleiche Initialen)
_PARTY_FALSE_EXPANSIONS: Dict[str, List[str]] = {
    "CDU": [
        "Christlich Demokratische Union",
        "Christliche Deutsche Union",
        "Christdemokratische Union",
        "Christlich Demokratische Unionisten"
    ],
    "CSU": [
        "Christlich-Soziale Union",
        "Christliche Sozial-Union",
        "Christsozialer Union",
        "Christliche Soziale Union"
    ],
    "SPD": [
        "Sozialistische Partei Deutschlands",
        "Sozialpolitische Partei Deutschlands",
        "Soziale Partei Deutschlands",
        "Sozialdemokratische Partei der Deutschen"
    ],
    "FDP": [
        "Freie Demokratische Partei Deutschlands",
        "Freidemokratische Partei",
        "Freiheitlich Demokratische Partei",
        "Freie Demokraten Partei"
    ],
    "AfD": [
        "Alternative für Demokratie",
        "Allianz für Deutschland",
        "Aktion für Deutschland",
        "Alternative freiheitlicher Demokraten"
    ],
    "BSW": [
        "Bündnis für soziale Wende",
        "Bürgerbündnis Soziale Wende",
        "Bündnis Solidarität und Wandel",
        "Bewegung für Solidarität und Wohlstand"
    ],
}

# Einzeiler zu Parteien: Ausrichtung/Gründung – für interessantere Erklärungen
_PARTY_FACTS: Dict[str, str] = {
    "CDU": "Mitte-rechts, christdemokratisch; gegründet 1945.",
    "CSU": "Bayerische Schwester der CDU; konservativ; seit 1945.",
    "SPD": "Sozialdemokratisch; gegründet 1863 (älteste Bundestagspartei).",
    "FDP": "Liberale Partei; marktwirtschaftlich und bürgerrechtlich; seit 1948.",
    "AfD": "Rechtskonservativ bis rechtspopulistisch; gegründet 2013.",
    "BSW": "Linkspopulistisches Bündnis um Sahra Wagenknecht; gegründet 2024.",
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

# Internationale Organisationen – mit Genitiv, Land und ggf. Gebäude/Ort
_INTL_SEATS: List[Dict[str, str]] = [
    {"organisation": "Vereinte Nationen (UN) – Hauptquartier", "stadt": "New York City", "land": "USA", "genitiv_full": "der Vereinten Nationen (UN)", "ort": "UN-Hauptquartier"},
    {"organisation": "NATO – Hauptsitz", "stadt": "Brüssel", "land": "Belgien", "genitiv_full": "der NATO"},
    {"organisation": "Internationaler Gerichtshof (IGH)", "stadt": "Den Haag", "land": "Niederlande", "genitiv_full": "des Internationalen Gerichtshofs (IGH)", "ort": "Friedenspalast"},
    {"organisation": "Europäischer Gerichtshof (EuGH)", "stadt": "Luxemburg", "land": "Luxemburg", "genitiv_full": "des Europäischen Gerichtshofs (EuGH)", "ort": "Kirchberg-Plateau"},
    {"organisation": "Europarat – Sitz", "stadt": "Straßburg", "land": "Frankreich", "genitiv_full": "des Europarats", "ort": "Palais de l’Europe"},
    {"organisation": "OSZE – Sekretariat", "stadt": "Wien", "land": "Österreich", "genitiv_full": "der OSZE"},
    {"organisation": "OECD – Hauptsitz", "stadt": "Paris", "land": "Frankreich", "genitiv_full": "der OECD", "ort": "Château de la Muette"},
    {"organisation": "WTO – Sitz", "stadt": "Genf", "land": "Schweiz", "genitiv_full": "der Welthandelsorganisation (WTO)", "ort": "Centre William Rappard"},
]

# Kurzbeschreibungen (Einzeiler) zu wichtigen Organisationen
_ORG_DESCRIPTIONS: Dict[str, str] = {
    "Vereinte Nationen": "Staatenbund für Frieden & Sicherheit, Menschenrechte und Entwicklung.",
    "NATO": "Verteidigungsbündnis der nordatlantischen Staaten.",
    "Europäische Zentralbank": "Zentralbank des Euroraums – Geldpolitik und Preisstabilität.",
    "Europäische Kommission": "Exekutive der EU; schlägt Gesetze vor und überwacht ihre Anwendung.",
    "Europarat": "Fördert Menschenrechte, Demokratie und Rechtsstaatlichkeit (kein EU-Organ).",
    "Internationaler Währungsfonds": "Sichert globale Finanzstabilität; Kredite und Beratung.",
    "Weltbank": "Entwicklungsfinanzierung zur Armutsminderung.",
    "Weltgesundheitsorganisation": "Koordiniert internationale Gesundheitspolitik und Standards.",
    "OECD": "Wirtschaftspolitische Zusammenarbeit und vergleichende Analysen.",
    "Welthandelsorganisation": "Regelt den Welthandel und schlichtet Handelsstreitigkeiten.",
    "OSZE": "Sicherheit und Zusammenarbeit in Europa; Wahlbeobachtung & Konfliktprävention.",
    "Internationaler Gerichtshof": "Hauptrechtsprechungsorgan der UN für Streitigkeiten zwischen Staaten.",
    "Federal Reserve": "Zentralbank der USA; Geldpolitik und Finanzaufsicht.",
    "Europäischer Gerichtshof": "Oberstes Gericht der EU zur Auslegung des EU-Rechts."
}

# =====================================================================
#                         SCHNITTSTELLEN / KONFIG
# =====================================================================

_WIKIPEDIA_API = "https://{lang}.wikipedia.org/w/api.php"
_WIKIDATA_SPARQL = "https://query.wikidata.org/sparql"
_HTTP_TIMEOUT = 15
_CACHE_PATH = os.environ.get("POLQUIZ_CACHE_FILE", "politikerquiz_cache.json")
_memory_cache: Dict[str, Dict[str, float | str]] = {}  # key -> {"value": "...", "ts": 1700000000.0}
_cache_lock = threading.Lock()

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
    if time.time() - float(ent.get("ts", 0)) > max_age_sec:
        return None
    return str(ent.get("value"))

def _cache_set(key: str, value: str) -> None:
    _memory_cache[key] = {"value": value, "ts": time.time()}
    _save_cache_to_disk()

# =====================================================================
#                       WIKIDATA / WIKIPEDIA HELFER
# =====================================================================

def _wikipedia_title_to_qid(title_de: str, lang: str = "de") -> Optional[str]:
    """
    Holt die Wikidata-QID zu einem deutschen Wikipedia-Titel/Begriff.
    Robust mit User-Agent; folgt Redirects.
    """
    key = f"qid:{lang}:{title_de}"
    cached = _cache_get(key)
    if cached:
        return cached
    try:
        headers = {
            "Accept": "application/json",
            "User-Agent": "PolitikerQuiz/1.0 (+https://example.org)"
        }
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
            headers=headers,
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
    Zwischencache: 6h.
    """
    key = f"sparql:{hash(query)}:{lang}"
    cached = _cache_get(key, max_age_sec=6 * 60 * 60)
    if cached:
        return cached
    try:
        headers = {
            "Accept": "application/sparql-results+json",
            "User-Agent": "PolitikerQuiz/1.0 (+https://example.org)"
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

# ---- Ministerien: über Positionskette (P2388 -> P1308)
def _get_ministry_head_via_position(ministry_qid: str) -> Optional[str]:
    query = f"""
    SELECT ?whoLabel WHERE {{
      wd:{ministry_qid} wdt:P2388 ?position .
      ?position wdt:P1308 ?who .
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "de,en". }}
    }}
    LIMIT 1
    """
    return _sparql_first_label(query)

# ---- Organisationen: mehrere Properties probieren + Positionskette
def _get_org_leader_any(qid: str) -> Optional[str]:
    for prop in ("P169", "P488", "P1037"):  # Leiter/CEO, Vorsitz, Direktor
        name = _sparql_first_label(f"""
        SELECT ?whoLabel WHERE {{
          wd:{qid} wdt:{prop} ?who .
          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "de,en". }}
        }} LIMIT 1
        """)
        if name:
            return name
    # Fallback: Positionskette
    return _sparql_first_label(f"""
    SELECT ?whoLabel WHERE {{
      wd:{qid} wdt:P2388 ?position .
      ?position wdt:P1308 ?who .
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "de,en". }}
    }} LIMIT 1
    """)

# ---- Staaten: Regierungschef (P6)
def _get_head_of_government_name(country_qid: str) -> Optional[str]:
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
    return _get_ministry_head_via_position(qid) or _get_org_leader_any(qid)

def resolve_org_head(org_name_de: str) -> Optional[str]:
    qid = _wikipedia_title_to_qid(org_name_de)
    if not qid:
        return None
    return _get_org_leader_any(qid)

def resolve_head_of_government(country_name_de: str) -> Optional[str]:
    qid = _wikipedia_title_to_qid(country_name_de)
    if not qid:
        return None
    return _get_head_of_government_name(qid)

# =====================================================================
#                       GPT-Formulierung
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

def _reject_if_na_or_empty(data: dict) -> bool:
    ch = data.get("choices", [])
    if not isinstance(ch, list) or len(ch) != 4:
        return True
    texts = [_extract_choice_text(c).strip().lower() for c in ch]
    return any(t in ("n/a", "k.a.", "unbekannt", "none", "") for t in texts)

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

    correct_hint = f"Die korrekte Antwort lautet: {correct_name or 'N/A'}."
    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (Deutsch) zur Kategorie „Politik“, Disziplin „{discipline}“.

Aufgabe:
- {task}
- Vier plausible Antwortoptionen A–D.
- WICHTIG: Setze die KORREKTE Antwort IMMER bei A. B–D sind plausible Distraktoren.
- Antworten MÜSSEN echte Personennamen sein. KEIN „N/A“, KEIN „unbekannt“.
- Verwende keine konkreten Datumsangaben in Frage/Erklärung.
- {correct_hint}
- Gib ausschließlich valides JSON gemäß diesem Schema aus:

{_SCHEMA}
""".strip()
    return prompt

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
    pool_false = _PARTY_FALSE_EXPANSIONS.get(kuerzel, [])
    if len(pool_false) >= 3:
        distractors = random.sample(pool_false, k=3)
        choice_texts = [langname] + distractors
        letters = ["A", "B", "C", "D"]
        choices = [f"{letters[i]}: {choice_texts[i]}" for i in range(4)]
        fact = _PARTY_FACTS.get(kuerzel, f"{kuerzel}: offizielle Langform gesucht.")
        data = {
            "category": CATEGORY_NAME,
            "discipline": "Parteikürzel (DE)",
            "question": f"Wofür steht das Parteikürzel „{kuerzel}“ in Deutschland?",
            "choices": choices,
            "correct_answer": "A",
            "explanation": fact,
            "difficulty": 1,
        }
        return _shuffle_choices_and_fix_answer(data)
    else:
        pool = list(_PARTY_ACRONYMS.values())
        choices, correct_letter = _choices_from_correct_and_pool(langname, pool)
        fact = _PARTY_FACTS.get(kuerzel, "Parteibezeichnung ist offiziell festgelegt.")
        data = {
            "category": CATEGORY_NAME,
            "discipline": "Parteikürzel (DE)",
            "question": f"Wofür steht das Parteikürzel „{kuerzel}“ in Deutschland?",
            "choices": choices,
            "correct_answer": correct_letter,
            "explanation": fact,
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

# --- Grundrechte (DE): stabil & lokal (kein GPT)
_GRUNDRECHTE_RECHTE = [
    "Das Recht auf Meinungsfreiheit",
    "Die Glaubens- und Gewissensfreiheit",
    "Die Versammlungsfreiheit",
    "Die Unverletzlichkeit der Wohnung",
    "Die allgemeine Handlungsfreiheit",
    "Die Berufsfreiheit",
    "Der Gleichheitssatz vor dem Gesetz",
]

_GRUNDRECHTE_KEIN_RECHT = [
    "Das Recht auf ein bedingungsloses Grundeinkommen",
    "Das Recht auf unbegrenzten Waffenbesitz",
    "Das Recht auf kostenlosen Wohnraum",
    "Das Recht auf ein eigenes Auto",
    "Das Recht auf kostenlose Urlaubsreisen",
]

def _gen_grundrechte_local() -> dict | None:
    correct = random.choice(_GRUNDRECHTE_KEIN_RECHT)
    distractors = random.sample(_GRUNDRECHTE_RECHTE, k=3)
    choices_texts = [correct] + distractors
    letters = ["A","B","C","D"]
    choices = [f"{letters[i]}: {choices_texts[i]}" for i in range(4)]
    data = {
        "category": CATEGORY_NAME,
        "discipline": "Grundrechte (DE)",
        "question": "Was ist KEIN Grundrecht im Sinne des Grundgesetzes (GG)?",
        "choices": choices,
        "correct_answer": "A",
        "explanation": "Die Grundrechte im GG schützen Freiheit und Würde; Sozialleistungen sind dort nicht als Grundrechte festgeschrieben.",
        "difficulty": 1,
    }
    return _shuffle_choices_and_fix_answer(data)

# =====================================================================
#           GPT-basierte Generatoren mit LIVE-Antwort (Wikidata)
# =====================================================================

def _gen_with_live_answer(discipline: str, seed_picker, resolver, max_tries=4) -> dict | None:
    for _ in range(max_tries):
        seed = seed_picker()
        correct_name = resolver(seed)
        if not correct_name:
            continue
        prompt = _prompt_gpt_from_choice(discipline, seed, correct_name)
        data = _ask_json(prompt)
        if not data:
            continue
        choices = data.get("choices", [])
        if isinstance(choices, list) and len(choices) == 4:
            texts = [_extract_choice_text(c) for c in choices]
            texts[0] = correct_name
            data["choices"] = _format_choices(texts)
            data["correct_answer"] = "A"
        if _reject_if_na_or_empty(data):
            continue
        return _shuffle_choices_and_fix_answer(data)
    return None

def _gen_minister_de_gpt() -> dict | None:
    return _gen_with_live_answer(
        "Ministerien (DE)",
        seed_picker=lambda: random.choice(_MINISTERIEN),
        resolver=resolve_minister_name
    )

def _gen_regierungschefs_gpt() -> dict | None:
    return _gen_with_live_answer(
        "Regierungschefs (Welt)",
        seed_picker=lambda: random.choice(_WICHTIGE_LAENDER),
        resolver=resolve_head_of_government
    )

# Eigene Variante für Org-Personen, damit die Erklärung eine Org-Kurzbeschreibung enthält
def _gen_org_person_gpt() -> dict | None:
    max_tries = 4
    for _ in range(max_tries):
        seed = random.choice(_WICHTIGE_ORGS)  # Organisationsname
        correct_name = resolve_org_head(seed)
        if not correct_name:
            continue
        prompt = _prompt_gpt_from_choice("Org-Personen", seed, correct_name)
        data = _ask_json(prompt)
        if not data:
            continue
        # Korrekte Antwort sicherstellen
        if isinstance(data.get("choices"), list) and len(data["choices"]) == 4:
            texts = [_extract_choice_text(c) for c in data["choices"]]
            texts[0] = correct_name
            data["choices"] = _format_choices(texts)
            data["correct_answer"] = "A"
        # Erklärung mit Kurzbeschreibung der Organisation überschreiben/ergänzen
        desc = _ORG_DESCRIPTIONS.get(seed)
        if desc:
            data["explanation"] = f"{seed}: {desc}"
        if _reject_if_na_or_empty(data):
            continue
        return _shuffle_choices_and_fix_answer(data)
    return None

# =====================================================================
#                     HILFSFORMATTER FÜR SITZE (INTL)
# =====================================================================

def _format_city_land(entry: Dict[str, str]) -> str:
    city = entry.get("stadt", "").strip()
    land = entry.get("land")
    return f"{city} ({land})" if land else city

def _format_correct(entry: Dict[str, str]) -> str:
    city = entry.get("stadt", "").strip()
    land = entry.get("land")
    ort  = entry.get("ort")
    if ort and land:
        return f"{city} ({ort}, {land})"
    if land:
        return f"{city} ({land})"
    return city

def _org_base_name(raw: str) -> str:
    """
    Normalisiert Anzeige-Namen aus _INTL_SEATS['organisation'] auf den
    schlichten Organisationsnamen (ohne Klammern/Suffixe), um _ORG_DESCRIPTIONS
    nachschlagen zu können. Beispiele:
      "Vereinte Nationen (UN) – Hauptquartier" -> "Vereinte Nationen"
      "Internationaler Gerichtshof (IGH)" -> "Internationaler Gerichtshof"
    """
    if not raw:
        return ""
    left = raw.split("–", 1)[0].strip()
    # entferne Klammerzusätze wie (UN), (IGH)
    left = re.sub(r"\s*\([^)]*\)", "", left).strip()
    return left

# =====================================================================
#                 GENERATOR: SITZE (INTERNATIONAL) – ÜBERARBEITET
# =====================================================================

def _gen_sitze_intl_local() -> dict | None:
    entry = random.choice(_INTL_SEATS)

    correct_text = _format_correct(entry)
    genitiv_full = entry.get("genitiv_full") or f"der Organisation „{entry.get('organisation','')}\""

    # Distraktoren
    distractor_entries = random.sample([e for e in _INTL_SEATS if e is not entry], k=3)
    distractors = [_format_city_land(e) for e in distractor_entries]

    choice_texts = [correct_text] + distractors
    letters = ["A", "B", "C", "D"]
    choices = [f"{letters[i]}: {choice_texts[i]}" for i in range(4)]

    # Erklärung mit Kurzbeschreibung der Organisation
    base = _org_base_name(entry.get("organisation", ""))
    desc = _ORG_DESCRIPTIONS.get(base)
    explanation = f"{base}: {desc}" if desc else "Internationale Organisationen haben fest definierte Hauptsitze; die Alternativen sind Sitze anderer Organisationen."

    data = {
        "category": CATEGORY_NAME,
        "discipline": "Sitze (International)",
        "question": f"In welcher Stadt befindet sich der Hauptsitz {genitiv_full}?",
        "choices": choices,
        "correct_answer": "A",
        "explanation": explanation,
        "difficulty": 1,
    }
    return _shuffle_choices_and_fix_answer(data)

# =====================================================================
#                              PUBLIC API
# =====================================================================

_WEIGHTS = [
    ("minister_de_gpt", 40),
    ("regierungschefs_gpt", 25),
    ("org_person_gpt", 7),
    ("kanzler_zeit_local", 7),
    ("partei_kuerzel_local", 7),
    ("grundrechte_local", 0),
    ("sitze_de_local", 7),
    ("sitze_intl_local", 7),
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
        "grundrechte_local": _gen_grundrechte_local,
        "sitze_de_local": _gen_sitze_de_local,
        "sitze_intl_local": _gen_sitze_intl_local,
    }

    data = gen_map[qtype]()
    time.sleep(0.3)

    if not data:
        return None

    # Normalisierung
    data["category"] = CATEGORY_NAME
    data["difficulty"] = 1

    # Minimalvalidierung
    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str) or data["correct_answer"] not in ("A","B","C","D"):
        return None
    if _reject_if_na_or_empty(data):
        return None

    return data
