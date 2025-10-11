# kategorien/politik.py
# -*- coding: utf-8 -*-
"""
Politik-Plugin für den Daily Quiz Generator.

Highlights:
- Robuste Plugin-Discovery (Import bricht nicht, wenn Dependencies fehlen)
- Klare Logs (geeignet für GitHub Actions)
- News- & Trivia-Erzeugung, JSON-Extraktion auch bei "Geräusch" um das JSON
- Konfigurierbar über ENV (siehe Variablen unten)
"""

from __future__ import annotations
import os
import re
import json
import time
import random
import logging
from typing import Optional, Dict, Any, List

# ===================== Meta / Kategorie =====================
CATEGORY_NAME = "Politik"

# ===================== Optional-Dependencies =====================
_DEPS_OK = True
_DEPS_ERR: Optional[BaseException] = None
try:
    import requests
    from bs4 import BeautifulSoup
    from openai import OpenAI
except Exception as e:
    _DEPS_OK = False
    _DEPS_ERR = e

# ===================== Logging-Konfiguration =====================
_LOG_LEVEL = os.environ.get("POLITIK_LOGLEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, _LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] politik: %(message)s",
)
log = logging.getLogger("kategorien.politik")

# ===================== Konfiguration (ENV-Overrides) =====================
# OpenAI
_OPENAI_MODEL = os.environ.get("POLITIK_OPENAI_MODEL", "gpt-4o-mini")
_OPENAI_TIMEOUT = float(os.environ.get("POLITIK_OPENAI_TIMEOUT", "30"))

# HTTP / Scraper
_BASE_URL = "https://www.tagesschau.de"
_NUM_FRONT_ARTICLES = int(os.environ.get("POLITIK_NUM_FRONT_ARTICLES", "5"))
_HTTP_TIMEOUT = float(os.environ.get("POLITIK_HTTP_TIMEOUT", "20"))
_HTTP_HEADERS = {
    "User-Agent": os.environ.get(
        "POLITIK_HTTP_UA",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36 dreimodig-politik/1.0"
    )
}

# Generator
_SLEEP = float(os.environ.get("POLITIK_SLEEP_SECONDS", "1.0"))  # kleine Pause zwischen API-Aufrufen
_TRIES_PER_ITEM = int(os.environ.get("POLITIK_TRIES_PER_ITEM", "6"))

# ===================== Caches =====================
_CACHE: Optional[List[Dict[str, Any]]] = None

# ===================== Trivia-Pools =====================
_MINISTRIES_16 = [
    "Auswärtiges Amt",
    "Bundesministerium des Innern und für Heimat",
    "Bundesministerium der Justiz",
    "Bundesministerium der Finanzen",
    "Bundesministerium für Wirtschaft und Klimaschutz",
    "Bundesministerium für Arbeit und Soziales",
    "Bundesministerium für Ernährung und Landwirtschaft",
    "Bundesministerium der Verteidigung",
    "Bundesministerium für Gesundheit",
    "Bundesministerium für Familie, Senioren, Frauen und Jugend",
    "Bundesministerium für Bildung und Forschung",
    "Bundesministerium für Umwelt, Naturschutz, nukleare Sicherheit und Verbraucherschutz",
    "Bundesministerium für Digitales und Verkehr",
    "Bundesministerium für Wohnen, Stadtentwicklung und Bauwesen",
    "Bundesministerium für wirtschaftliche Zusammenarbeit und Entwicklung",
    "Bundesministerium für Kultur und Medien",
]

_HEADS_OF_GOV_COUNTRIES = [
    "Frankreich", "Italien", "Spanien", "Portugal", "Niederlande", "Belgien",
    "Österreich", "Schweiz", "Polen", "Tschechien", "Schweden", "Norwegen",
    "Dänemark", "Finnland", "Griechenland", "Ungarn", "Irland",
    "Vereinigtes Königreich", "Kanada", "USA", "Mexiko", "Brasilien",
    "Argentinien", "Südafrika", "Ägypten", "Nigeria", "Türkei",
    "Saudi-Arabien", "Israel", "Indien", "Pakistan", "Bangladesch", "Japan",
    "Südkorea", "Australien", "Neuseeland", "China", "Indonesien", "Vietnam"
]

_OTHER_KEY_FIGURES = [
    ("Präsidentin/Präsident der Europäischen Kommission", "Europäische Union"),
    ("Präsidentin/Präsident des Europäischen Rates", "Europäische Union"),
    ("Präsidentin/Präsident des Europäischen Parlaments", "Europäische Union"),
    ("Hohe Vertreterin/Hoher Vertreter der EU für Außen- und Sicherheitspolitik", "Europäische Union"),
    ("Generalsekretärin/Generalsekretär der NATO", "NATO"),
    ("Generalsekretärin/Generalsekretär der Vereinten Nationen", "Vereinte Nationen"),
    ("Präsidentin/Präsident der Europäischen Zentralbank", "Europäische Zentralbank"),
    ("Direktorin/Direktor des Internationalen Währungsfonds (IWF)", "Internationaler Währungsfonds"),
    ("Präsidentin/Präsident der Weltbank", "Weltbankgruppe"),
]

# ===================== Utils =====================
def _is_true(v) -> bool:
    if v is True:
        return True
    if isinstance(v, str) and v.strip().lower() in {"true", "wahr", "ja", "1"}:
        return True
    if v in (1,):
        return True
    return False


def _extract_first_json_block(text: str) -> Optional[str]:
    """Extrahiert den ersten {...}-Block, toleriert Markdown-Codefences."""
    if not text:
        return None
    m = re.search(r"```(?:json)?\s*({.*?})\s*```", text, flags=re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(1)
    m = re.search(r"\{.*\}", text, flags=re.DOTALL)
    return m.group(0) if m else None


def _validate_payload(d: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    if not isinstance(d, dict):
        return None
    if not _is_true(d.get("is_politics")):
        return None
    q = (d.get("question") or "").strip()
    choices = d.get("choices") or []
    ans = (d.get("correct_answer") or "").strip()
    if not q or not isinstance(choices, list) or len(choices) < 4 or ans not in {"A", "B", "C", "D"}:
        return None
    # Normalize Pflichtfelder
    d["category"] = CATEGORY_NAME
    if "source" not in d or not d["source"]:
        d["source"] = {"title": "Politik-Trivia", "url": "https://www.bundesregierung.de"}
    return d

# ===================== Scraper =====================
def _fetch_front_links(n=_NUM_FRONT_ARTICLES) -> List[str]:
    try:
        r = requests.get(_BASE_URL, headers=_HTTP_HEADERS, timeout=_HTTP_TIMEOUT)
        r.raise_for_status()
    except Exception as e:
        log.warning("Tagesschau Frontpage nicht erreichbar: %s", e)
        return []
    s = BeautifulSoup(r.text, "html.parser")
    out: List[str] = []
    links = s.select("a.teaser__link")
    log.debug("Gefundene Teaser-Links: %d", len(links))
    for a in links:
        h = a.get("href")
        if h and h.startswith("/") and h not in out:
            out.append(_BASE_URL + h)
        if len(out) == n:
            break
    if not out:
        log.warning("Kein Link via Selektor 'a.teaser__link' gefunden – HTML-Struktur geändert?")
    return out


def _fetch_article(u: str) -> Dict[str, Any]:
    r = requests.get(u, headers=_HTTP_HEADERS, timeout=_HTTP_TIMEOUT)
    r.raise_for_status()
    s = BeautifulSoup(r.text, "html.parser")
    title = (s.find("h1").get_text(strip=True) if s.find("h1") else u)
    paras = [p.get_text(strip=True) for p in s.select("p") if p.get_text(strip=True)]
    content = "\n".join(paras)[:2000]
    return {"url": u, "title": title, "content": content}


def _ensure_cache():
    global _CACHE
    if _CACHE is not None:
        return
    _CACHE = []
    urls = _fetch_front_links()
    if not urls:
        log.warning("Keine Frontpage-Artikel gesammelt – News-Modus wird vermutlich 0 liefern.")
    for u in urls:
        try:
            _CACHE.append(_fetch_article(u))
        except Exception as e:
            log.debug("Artikel konnte nicht geladen werden (%s): %s", u, e)
            continue
    log.info("News-Cache aufgebaut: %d Artikel", len(_CACHE or []))

# ===================== Prompts =====================
def _prompt_news(title: str, content: str, url: str) -> str:
    return f"""
Du bist ein deutscher Nachrichten-Quizgenerator.
Erzeuge EINE Multiple-Choice-Frage (A–D) aus folgendem Tagesschau-Artikel, falls er Politik behandelt.
Füge Kurz-Einordnungen zu Personen hinzu.
Erklärung: 2–3 Sätze Einordnung.
Wenn keine Politik: {{ "is_politics": false }}
TEXT:
Titel: {title}
Inhalt: {content}
Quelle: {url}
JSON-Schema:
{{"is_politics":true,"category":"Politik","question":"...","choices":["A: ...","B: ...","C: ...","D: ..."],"correct_answer":"A","explanation":"...","source":{"title":"...","url":"..."}}}
""".strip()


def _prompt_trivia_ministry(ministry: str) -> str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D) auf Deutsch.
Thema: Wer ist derzeit die/der Bundesminister/in des Ressorts "{ministry}" in Deutschland?
Liefere plausible Distraktoren (echte deutsche Politiker/innen, aber nicht amtierend für dieses Ressort).
Erklärung: 2–3 Sätze Einordnung zur/zum Amtsinhaber/in (Partei, Zuständigkeiten).
Wenn du unsicher bist oder die Information veraltet sein könnte, gib {{ "is_politics": false }} zurück.
JSON:
{{"is_politics":true,"category":"Politik","question":"Wer ist derzeit Bundesminister/in für {ministry}?","choices":["A: ...","B: ...","C: ...","D: ..."],"correct_answer":"A","explanation":"...","source":{"title":"Amtsinhaber/in {ministry}","url":"https://www.bundesregierung.de"}}}
""".strip()


def _prompt_trivia_head_of_gov(country: str) -> str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D) auf Deutsch.
Thema: Wer ist (Stand heute) Regierungschef/in von {country}?
Nutze die korrekte Amtsbezeichnung je nach Land.
Erklärung: 2–3 Sätze Einordnung (Partei/Koalition, grobe Amtszeit).
Wenn du unsicher bist, gib {{ "is_politics": false }} zurück.
JSON:
{{"is_politics":true,"category":"Politik","question":"Wer ist aktuell Regierungschef/in von {country}?","choices":["A: ...","B: ...","C: ...","D: ..."],"correct_answer":"A","explanation":"...","source":{"title":"Regierungschef/in {country}","url":"https://www.wikipedia.org"}}}
""".strip()


def _prompt_trivia_other(role: str, org: str) -> str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D) auf Deutsch.
Thema: Wer bekleidet aktuell die Position "{role}" bei {org}?
Erklärung: 2–3 Sätze Einordnung (Rolle, Zuständigkeiten, Amtsantritt soweit bekannt).
Wenn du unsicher bist, gib {{ "is_politics": false }} zurück.
JSON:
{{"is_politics":true,"category":"Politik","question":"Wer ist aktuell {role} ({org})?","choices":["A: ...","B: ...","C: ...","D: ..."],"correct_answer":"A","explanation":"...","source":{"title":"{role} – {org}","url":"https://www.wikipedia.org"}}}
""".strip()

# ===================== OpenAI Helper =====================
def _ask_json(prompt: str) -> Optional[Dict[str, Any]]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        log.warning("OPENAI_API_KEY fehlt – OpenAI-Aufrufe werden übersprungen.")
        return None
    try:
        client = OpenAI(api_key=api_key, timeout=_OPENAI_TIMEOUT)
        r = client.chat.completions.create(
            model=_OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "Gib ausschließlich valides JSON ohne Erklärtext zurück."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )
        raw = (r.choices[0].message.content or "").strip()
        if not raw:
            log.debug("OpenAI leere Antwort.")
            return None
        jb = _extract_first_json_block(raw)
        if not jb:
            log.debug("Kein JSON-Block extrahiert. Volltext (gekürzt): %r", raw[:200])
            return None
        try:
            data = json.loads(jb)
        except Exception as e:
            log.debug("JSON-Parse-Fehler: %s – Payload (gekürzt): %r", e, jb[:200])
            return None
        valid = _validate_payload(data)
        if not valid:
            log.debug("JSON verworfen (keine Politik/inkomplett).")
        return valid
    except Exception as e:
        log.warning("OpenAI-Aufruf fehlgeschlagen: %s", e)
        return None

# ===================== Generatoren =====================
def _generate_from_news() -> Optional[Dict[str, Any]]:
    _ensure_cache()
    if not _CACHE:
        return None
    arts = list(_CACHE)
    random.shuffle(arts)
    for art in arts:
        log.debug("News-Versuch mit: %s", art.get("title"))
        d = _ask_json(_prompt_news(art["title"], art["content"], art["url"]))
        time.sleep(_SLEEP)
        if d:
            # Quelle auf den Artikel setzen
            d["source"] = {"title": art["title"], "url": art["url"]}
            log.info("Politikfrage aus News generiert: %s", d.get("question")[:80])
            return d
    log.info("Keine geeignete Politik-News gefunden.")
    return None


def _generate_trivia() -> Optional[Dict[str, Any]]:
    r = random.random()
    if r < 0.55:
        ministry = random.choice(_MINISTRIES_16)
        prompt = _prompt_trivia_ministry(ministry)
        log.debug("Trivia-Ministerium: %s", ministry)
    elif r < 0.85:
        country = random.choice(_HEADS_OF_GOV_COUNTRIES)
        prompt = _prompt_trivia_head_of_gov(country)
        log.debug("Trivia-Regierungschef: %s", country)
    else:
        role, org = random.choice(_OTHER_KEY_FIGURES)
        prompt = _prompt_trivia_other(role, org)
        log.debug("Trivia-andere Rolle: %s / %s", role, org)
    d = _ask_json(prompt)
    if d:
        log.info("Politikfrage aus Trivia generiert: %s", d.get("question")[:80])
    return d

# ===================== Public API =====================
def generate_one(past_texts: List[str]) -> Optional[Dict[str, Any]]:
    """
    50%: Tagesschau-Artikel
    50%: Trivia
    Mehrere Versuche; wechselt zwischen News/Trivia, um Hänger zu vermeiden.
    """
    if not _DEPS_OK:
        log.warning("Politik-Plugin deaktiviert: fehlende Dependencies: %r", _DEPS_ERR)
        return None

    use_news = (random.random() < 0.5)
    tries = _TRIES_PER_ITEM
    for i in range(tries):
        mode = "News" if use_news else "Trivia"
        log.debug("generate_one Versuch %d/%d (%s)", i + 1, tries, mode)
        d = _generate_from_news() if use_news else _generate_trivia()
        time.sleep(_SLEEP)
        if d:
            d["category"] = CATEGORY_NAME  # sicherheitshalber
            return d
        use_news = not use_news

    log.warning("generate_one: Keine Politikfrage generiert (nach %d Versuchen).", tries)
    return None
