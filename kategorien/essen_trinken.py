# kategorien/essen_trinken.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional, List, Tuple
from openai import OpenAI

CATEGORY_NAME = "Essen und Trinken"

# Top-Level-Themen mit Gewichten (bleiben wie gehabt)
_TOPICS: dict[str, int] = {
    "Küche international": 40,
    "Ernährung": 30,
    "Getränke": 15,
    "Kulinarische Geschichte": 15,
}

# Neue: Subtopics pro Top-Level-Topic (name, gewicht) – NUR als Prompt-Hinweis, nicht im JSON ausgeben
_SUBTOPICS: dict[str, List[Tuple[str, int]]] = {
    "Küche international": [
        ("Italien: regionale Küchen (Süditalien/Norditalien), DOP/IGP-Bezüge", 3),
        ("Ostasien: China/Japan/Korea – Grundtechniken & Leitprodukte (Soja, Reis, Fermentation)", 3),
        ("Südostasien: Thailand/Vietnam/Indonesien – Balance süß-sauer-salzig-scharf, Kräuter", 2),
        ("Nahost & Levante: Mezze, Gewürze, Tahina, Zatar", 2),
        ("Lateinamerika: Mais, Bohnen, Chili – regionale Variationen (Mexiko/Peru/Brasilien)", 2),
        ("Afrika: Maghreb/Äthiopien/Westafrika – Teff, Injera, Erdnuss, Couscous", 2),
        ("Südasien: Indien/Pakistan/Sri Lanka – Masalas, Garmethoden, regionale Unterschiede", 2),
        ("Mitteleuropa & DACH: Brot- und Knödelkultur, Wurstspezialitäten, g.g.A./g.U.", 1),
        ("Streetfood & Fusionsküche: Globalisierung, Hybridgerichte, Authentizität vs. Adaption", 1),
        ("Vegetarisch/Vegan weltweit: Proteinalternativen, traditionelle pflanzliche Küchen", 1),
    ],
    "Ernährung": [
        ("Makronährstoffe & Energiebilanz: Protein, Fett, Kohlenhydrate – Funktionen & Beispiele", 3),
        ("Vitamine & Mineralstoffe: Mangel/Überversorgung, Quellen, Bioverfügbarkeit", 3),
        ("Ernährungsformen: mediterran, vegetarisch, vegan, low-carb – Evidenz & typische Fehler", 2),
        ("Lebensmittelsicherheit & Hygiene: HACCP, Kreuzkontamination, Kerntemperaturen (qualitativ)", 2),
        ("Kennzeichnung & Allergene: EU-Allergenliste, Nährwertangaben, Claims", 2),
        ("Nachhaltigkeit & Food Waste: Saisonalität, CO₂-Fußabdruck, Resteküche", 2),
        ("Sensorik & Texturen: Grundgeschmäcker, Mundgefühl, Maillard-Reaktion (allgemein)", 1),
    ],
    "Getränke": [
        ("Kaffee: Anbaugebiete, Varietäten, Röstgrade, Brühmethoden", 3),
        ("Tee: Camellia sinensis – Grün/Schwarz/Oolong/Weiß, Aufgussparameter", 2),
        ("Bier: Rohstoffe, Brauprozess, Bierstile (Lager/Ale/Weizen/Stout)", 2),
        ("Wein: Rebsorten, Terroir, Ausbau – Grundbegriffe, g.U./g.g.A.", 2),
        ("Spirituosen: Destillation, Kategorien (Whisky/Rum/Gin), Herkunftsschutz", 2),
        ("Fermentierte Alkoholfreie: Kombucha/Kefir, Limonaden, Shrubs", 1),
        ("Wasser: Mineralisierung, Sensorik, regionaler Charakter", 1),
    ],
    "Kulinarische Geschichte": [
        ("Kolumbianischer Austausch: Tomate, Kartoffel, Chili – Verbreitung & Auswirkungen", 3),
        ("Gewürzhandel & Seidenstraße: Pfeffer, Zimt, Muskat – Handelsrouten & Einfluss", 2),
        ("Schutzsiegel & Herkunft: g.U./g.g.A./TSG – Beispiele & Bedeutung", 2),
        ("Industrialisierung & Konservierung: Dosen, Kühlung, Pasteurisierung – Gesellschaftseffekte", 2),
        ("Migration & Hybridküchen: Diaspora, Kreolisierung, Globalisierung von Gerichten", 2),
        ("Esskultur & Tischsitten: Rituale, Etikette, gesellschaftlicher Kontext", 1),
        ("Regionale Brot- & Käsekulturen: Handwerk, Reifung, regionale Profile", 1),
    ],
}

# Vom Core werden Antworten ohnehin gemischt; wir geben trotzdem sauber gelabeltes JSON zurück.
_SCHEMA = """{
  "category": "Essen und Trinken",
  "topic": "Küche international|Ernährung|Getränke|Kulinarische Geschichte",
  "question": "...",
  "choices": ["A: ...","B: ...","C: ...","D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

# Leitplanken je Schwierigkeit (1..10)
DIFF_GUIDE = """
- 1–3 (leicht): sehr bekanntes Alltagswissen; Distraktoren klar unterscheidbar.
- 4–7 (mittel): weniger offensichtliche Fakten, regionale Besonderheiten, einfache Zahlenbereiche.
- 8–10 (schwer): spezifische Herkunft/Etmythologie/geschützte Herkunftsbezeichnungen, rare Zubereitungen;
  Distraktoren plausibel und nah dran.
"""

def _pick_weighted(pairs: List[Tuple[str, int]]) -> str:
    names, weights = zip(*pairs)
    return random.choices(list(names), weights=list(weights), k=1)[0]

def _prompt(topic: str, target_difficulty: int, mode: Optional[str], subtopic: Optional[str] = None) -> tuple[str, float]:
    # Temperatur moderat einheitlich; könnte optional je Tier variiert werden
    if target_difficulty <= 2:
        tier_note = "LEICHT (1–2): bekannte Fakten, teils logisch erschließbar."
        temperature = 0.8
    elif target_difficulty <= 4:
        tier_note = "MITTEL (3–4): weniger bekannte Fakten, moderate Komplexität."
        temperature = 0.8
    elif target_difficulty <= 6:
        tier_note = "Etwas schwerer (5–6): spezifischere Details, eng verwandte Distraktoren."
        temperature = 0.8
    elif target_difficulty <= 8:
        tier_note = "Schwer (7–8): präzise Details oder tiefere Konzepte, enge Distraktoren."
        temperature = 0.8
    else:
        tier_note = "Sehr schwer (9–10): Expertenwissen, exakte Terminologie, engste Distraktoren."
        temperature = 0.82

    sub_hint = f"- Subthema (nur als inhaltlicher Hinweis, NICHT ins JSON übernehmen): „{subtopic}“.\n" if subtopic else ""

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, eine richtig) zur Kategorie „Essen und Trinken“, Thema „{topic}“ (Deutsch).
{sub_hint}Ziel-Schwierigkeit: {target_difficulty}/10 – {tier_note}
Kontext zu Schwierigkeitsstufen:
{DIFF_GUIDE}

Anforderungen:
- Keine reinen Rezeptschritte; Fokus auf Ursprung, Geschichte, Zutatenkunde, Bezeichnungen, Geographie, Schutzsiegel.
- Formuliere knapp, eindeutig, ohne Insider-Begriffe, ohne „alle oben“/„keine der oben“.
- Vier Antwortoptionen (A–D). Genau EINE ist korrekt; die anderen drei müssen plausibel sein.
- Erklärung 2–3 Sätze: kurz, präzise, hilfreich; bei Herkunft ggf. kurzer Lage-/Kulturhinweis.
- Das Feld "topic" im JSON enthält ausschließlich das Oberthema („{topic}“). Subthema nicht gesondert ausgeben.
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
                {"role": "system", "content": "Antworte ausschließlich mit valide parsem barem JSON (keine Erklärtexte außerhalb des JSON)."},
                {"role": "user", "content": p},
            ],
            temperature=temperature,
        )
        raw = r.choices[0].message.content.strip()
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception:
        return None

def generate_one(past_texts: list[str], target_difficulty: Optional[int] = None, mode: Optional[str] = None) -> dict | None:
    """
    Wird vom Core mit target_difficulty (1..10) und mode ("normal"|"schwer"|"physik") aufgerufen.
    Falls target_difficulty fehlt, ziehen wir lokal einen moderaten Zielwert (Kompatibilität).
    """
    # 1) Top-Level-Topic ziehen
    t = random.choices(list(_TOPICS.keys()), weights=list(_TOPICS.values()), k=1)[0]
    # 2) Optionales Subtopic (nur für den Prompt)
    sub = _pick_weighted(_SUBTOPICS[t]) if t in _SUBTOPICS and _SUBTOPICS[t] else None
    # 3) Zielschwierigkeit
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3, 5, 7])
    # 4) Frage generieren
    prompt, temp = _prompt(t, tier, mode, subtopic=sub)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.8)
    if not data:
        return None

    # Pflichtfelder pflegen/normalisieren
    data["category"] = CATEGORY_NAME
    data["topic"] = t  # Oberthema erzwingen (Subtopic nie ins JSON)
    data["difficulty"] = int(data.get("difficulty", tier))

    # Sanity check: choices & correct_answer vorhanden
    choices = data.get("choices")
    correct = data.get("correct_answer")
    if not isinstance(choices, list) or len(choices) != 4 or not isinstance(correct, str):
        return None

    # Fragen-Text prüfen
    qtext = (data.get("question") or "").strip()
    if not qtext:
        return None

    # Plugin selbst mischt nicht – der Core mischt später tagesweit konsistent.
    return data
