# kategorien/geschichte.py
# -*- coding: utf-8 -*-
import os, re, json, random, time
from typing import Optional, List, Tuple
from openai import OpenAI

CATEGORY_NAME = "Geschichte"

# Oberbereiche (Epochen) mit Gewichten
_SUBPERIODS: dict[str, int] = {
    "Antike": 25,
    "Mittelalter": 25,
    "Neuzeit": 30,
    "Zeitgeschichte (ab 1945)": 20,
}

# Neue: gewichtete Unterthemen pro Epoche (nur als Prompt-Hinweis, NICHT ins JSON übernehmen)
_SUBTOPICS: dict[str, List[Tuple[str, int]]] = {
    "Antike": [
        ("Griechische Polis & Demokratie (Athen/Sparta), Perserkriege", 3),
        ("Römische Republik & Kaiserzeit: Verfassung, Expansion, Recht", 3),
        ("Hellenismus: Alexanderreich, Kulturtransfer, Bibliothek von Alexandria", 2),
        ("Ägypten: Pharaonenzeit, Nil-Ökonomie, Monumentalbauten", 2),
        ("Antike Religionen & Mythen, Kultpraktiken", 1),
        ("Handel & Mittelmeerwelt: Kolonien, Seefahrt, Münzgeld", 1),
    ],
    "Mittelalter": [
        ("Frühmittelalter: Völkerwanderung, Frankenreich, Christianisierung", 3),
        ("Hochmittelalter: Feudalordnung, Investiturstreit, Kreuzzüge", 3),
        ("Spätmittelalter: Städte & Zünfte, Hanse, Pest & demografischer Wandel", 2),
        ("Byzanz & orthodoxe Welt, Ikonoklasmus, Kulturkontakte", 2),
        ("Islamische Blütezeit: Wissenschaft, Handel, Al-Andalus", 2),
        ("Klöster, Bildung & Scholastik, Universitäten", 1),
    ],
    "Neuzeit": [
        ("Renaissance & Humanismus: Druck, Kunst, Wissenskulturen", 3),
        ("Reformation & Konfessionalisierung, Dreißigjähriger Krieg", 3),
        ("Entdeckungen & koloniale Expansion, atlantische Verflechtungen", 2),
        ("Aufklärung & Absolutismus: Staatsverständnis, Wissenschaft", 2),
        ("Revolutionen 1776/1789/1848, Nationenbildung", 2),
        ("Industrialisierung: Arbeit, Technik, soziale Frage", 2),
        ("Imperialismus & Völkerrecht um 1900", 1),
    ],
    "Zeitgeschichte (ab 1945)": [
        ("Kalter Krieg: Blockbildung, Krisen, Entspannungspolitik", 3),
        ("Deutschland: Teilung, 1968, Friedliche Revolution, Wiedervereinigung", 3),
        ("Dekolonisation & „Dritte Welt“: Unabhängigkeitsbewegungen, Non-Alignment", 2),
        ("Europäische Integration: EG/EU, Verträge, Erweiterungen", 2),
        ("Bürgerrechts- & soziale Bewegungen (USA, Europa, weltweit)", 2),
        ("UNO & internationale Ordnung, Menschenrechte", 1),
        ("Globalisierung: Wirtschaft, Medien, Kulturtransfers", 1),
    ],
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

def _pick_weighted(pairs: List[Tuple[str, int]]) -> str:
    names, weights = zip(*pairs)
    return random.choices(list(names), weights=list(weights), k=1)[0]

def _prompt(subperiod: str, target_difficulty: int, mode: Optional[str], subtopic: Optional[str] = None) -> tuple[str, float]:
    if target_difficulty <= 2:
        tier_note = "LEICHT (1–2): bekannte Fakten, teils logisch erschließbare Antwort."
        temperature = 0.8
    elif target_difficulty <= 4:
        tier_note = "MITTEL (3–4): etwas weniger bekannte Fakten, moderate Komplexität."
        temperature = 0.8
    elif target_difficulty <= 6:
        tier_note = "Etwas schwerer (5–6): spezifische Details, eng verwandte Distraktoren."
        temperature = 0.8
    elif target_difficulty <= 8:
        tier_note = "Schwer (7–8): präzise Details oder tiefere Konzepte, enge Distraktoren."
        temperature = 0.8
    else:
        tier_note = "Sehr schwer (9–10): exakte Terminologie/Datierungen, Expertenwissen."
        temperature = 0.82

    sub_hint = f"- Unterthema (nur als inhaltlicher Hinweis, NICHT ins JSON übernehmen): „{subtopic}“.\n" if subtopic else ""

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „Geschichte“, Unterbereich „{subperiod}“ (Deutsch).
{sub_hint}Ziel-Schwierigkeit: {target_difficulty}/10 – {tier_note}

Kontext zu Schwierigkeitsstufen:
{_DIFF_GUIDE}

Vorgaben:
- Verständliche, neutrale Formulierung ohne Gegenwartsbezug; keine tagesaktuellen Themen.
- Falls Fachbegriffe nötig sind, kurz erläutern (in der Erklärung).
- Keine „alle oben/keine der oben“-Optionen; vier plausible Antworten, genau eine korrekt.
- Erklärung: 2–3 Sätze, knapp und hilfreich; ggf. Datierung/Orts-/Akteurs-Hinweis.
- Das Feld "subperiod" im JSON enthält ausschließlich den Oberbereich („{subperiod}“). Unterthema nicht ins JSON.
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
    # 1) Epoche wählen
    sub = _pick_subperiod()
    # 2) Unterthema als Prompt-Hinweis ziehen
    subtopic = _pick_weighted(_SUBTOPICS[sub]) if sub in _SUBTOPICS and _SUBTOPICS[sub] else None
    # 3) Zielschwierigkeit bestimmen
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3, 5, 7])
    # 4) Prompt bauen & Anfrage senden
    prompt, temp = _prompt(sub, tier, mode, subtopic=subtopic)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.8)
    if not data:
        return None

    # 5) Pflichtfelder normieren
    data["category"] = CATEGORY_NAME
    data["subperiod"] = sub  # Oberbereich erzwingen (Unterthema nie ins JSON)
    data["difficulty"] = int(data.get("difficulty", tier))

    # 6) minimale Validierung
    if not isinstance(data.get("question"), str) or not data["question"].strip():
        return None
    if not isinstance(data.get("choices"), list) or len(data["choices"]) != 4:
        return None
    if not isinstance(data.get("correct_answer"), str):
        return None

    # Shuffle übernimmt der Core zentral
    return data
