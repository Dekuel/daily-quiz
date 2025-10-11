# kategorien/politik.py
# -*- coding: utf-8 -*-
import os, re, json, time, random, requests
from bs4 import BeautifulSoup
from openai import OpenAI

CATEGORY_NAME = "Politik"
_BASE_URL = "https://www.tagesschau.de"
_NUM_FRONT_ARTICLES = 5
_SLEEP = 1.0
_CACHE: list[dict] | None = None

# === Trivia-Pools ===
_MINISTRIES_16 = [
    # exakt 16, gleichwahrscheinlich
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
    # Auswahl bekannter/stabiler Pools; beliebig erweiterbar
    "Frankreich", "Italien", "Spanien", "Portugal", "Niederlande", "Belgien",
    "Österreich", "Schweiz", "Polen", "Tschechien", "Schweden", "Norwegen",
    "Dänemark", "Finnland", "Griechenland", "Ungarn", "Irland",
    "Vereinigtes Königreich", "Kanada", "USA", "Mexiko", "Brasilien",
    "Argentinien", "Südafrika", "Ägypten", "Nigeria", "Türkei",
    "Saudi-Arabien", "Israel", "Indien", "Pakistan", "Bangladesch", "Japan",
    "Südkorea", "Australien", "Neuseeland", "China", "Indonesien", "Vietnam"
]

_OTHER_KEY_FIGURES = [
    # Rolle + Organisation (Frage fragt nach der aktuellen Person)
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

def _fetch_front_links(n=_NUM_FRONT_ARTICLES) -> list[str]:
    r = requests.get(_BASE_URL, timeout=15)
    r.raise_for_status()
    s = BeautifulSoup(r.text, "html.parser")
    out=[]
    for a in s.select("a.teaser__link"):
        h=a.get("href")
        if h and h.startswith("/") and h not in out:
            out.append(_BASE_URL+h)
        if len(out)==n:break
    return out

def _fetch_article(u: str) -> dict:
    r = requests.get(u, timeout=20)
    r.raise_for_status()
    s = BeautifulSoup(r.text,"html.parser")
    title = s.find("h1").get_text(strip=True) if s.find("h1") else u
    paras = [p.get_text(strip=True) for p in s.select("p") if p.get_text(strip=True)]
    return {"url":u,"title":title,"content":"\n".join(paras)[:2000]}

def _ensure_cache():
    global _CACHE
    if _CACHE is not None: return
    _CACHE=[]
    try:
        for u in _fetch_front_links():
            try:_CACHE.append(_fetch_article(u))
            except Exception:continue
    except Exception:pass

def _prompt_news(title:str, content:str, url:str)->str:
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
"""

def _prompt_trivia_ministry(ministry:str)->str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D) auf Deutsch.
Thema: Wer ist derzeit die/der Bundesminister/in des Ressorts "{ministry}" in Deutschland?
Liefere plausible Distraktoren (echte deutsche Politiker/innen, aber nicht amtierend für dieses Ressort).
Erklärung: 2–3 Sätze Einordnung zur/ zum Amtsinhaber/in (Partei, Zuständigkeiten).
Wenn du unsicher bist oder die Information veraltet sein könnte, gib {{ "is_politics": false }} zurück.
JSON:
{"is_politics":true,"category":"Politik","question":"Wer ist derzeit Bundesminister/in für {ministry}?","choices":["A: ...","B: ...","C: ...","D: ..."],"correct_answer":"A","explanation":"...","source":{"title":"Amtsinhaber/in {ministry}","url":"https://www.bundesregierung.de"}} 
"""

def _prompt_trivia_head_of_gov(country:str)->str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D) auf Deutsch.
Thema: Wer ist (Stand heute) Regierungschef/in von {country}?
Nutze die korrekte Amtsbezeichnung (z. B. Premierminister/in, Ministerpräsident/in, Präsident/in) je nach Land.
Erklärung: 2–3 Sätze Einordnung (Partei/Koalition, grobe Amtszeit).
Wenn du unsicher bist, gib {{ "is_politics": false }} zurück.
JSON:
{"is_politics":true,"category":"Politik","question":"Wer ist aktuell Regierungschef/in von {country}?","choices":["A: ...","B: ...","C: ...","D: ..."],"correct_answer":"A","explanation":"...","source":{"title":"Regierungschef/in {country}","url":"https://www.wikipedia.org"}} 
"""

def _prompt_trivia_other(role:str, org:str)->str:
    return f"""
Erzeuge EINE Multiple-Choice-Frage (A–D) auf Deutsch.
Thema: Wer bekleidet aktuell die Position "{role}" bei {org}?
Erklärung: 2–3 Sätze Einordnung (Rolle, Zuständigkeiten, Amtsantritt soweit bekannt).
Wenn du unsicher bist, gib {{ "is_politics": false }} zurück.
JSON:
{"is_politics":true,"category":"Politik","question":"Wer ist aktuell {role} ({org})?","choices":["A: ...","B: ...","C: ...","D: ..."],"correct_answer":"A","explanation":"...","source":{"title":"{role} – {org}","url":"https://www.wikipedia.org"}} 
"""

def _ask_json(p:str)->dict|None:
    c=OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        r=c.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"system","content":"Nur valides JSON."},{"role":"user","content":p}],
            temperature=0.7,
        )
        raw=r.choices[0].message.content.strip()
        m=re.search(r"\{.*\}",raw,re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception:
        return None

def _generate_from_news()->dict|None:
    _ensure_cache()
    if not _CACHE: return None
    random.shuffle(_CACHE)
    for art in list(_CACHE):
        d=_ask_json(_prompt_news(art["title"],art["content"],art["url"]))
        time.sleep(_SLEEP)
        if not d or d.get("is_politics") is not True: 
            continue
        if not (d.get("question") or "").strip():
            continue
        d["category"]=CATEGORY_NAME
        d["source"]={"title":art["title"],"url":art["url"]}
        return d
    return None

def _generate_trivia()->dict|None:
    # Verteilung innerhalb der Trivia-Hälfte:
    # 55% Ministerium, 30% Regierungschef, 15% andere Schlüsselperson
    r = random.random()
    if r < 0.55:
        ministry = random.choice(_MINISTRIES_16)
        return _ask_json(_prompt_trivia_ministry(ministry))
    elif r < 0.55 + 0.30:
        country = random.choice(_HEADS_OF_GOV_COUNTRIES)
        return _ask_json(_prompt_trivia_head_of_gov(country))
    else:
        role, org = random.choice(_OTHER_KEY_FIGURES)
        return _ask_json(_prompt_trivia_other(role, org))

def generate_one(past_texts:list[str])->dict|None:
    """
    50%: Tagesschau-Artikel (wie bisher)
    50%: Trivia (55% Ministerium, 30% Regierungschef, 15% sonstige Rolle)
    """
    use_news = (random.random() < 0.5)
    # Versuche bis zu einige Male, um ein valides Ergebnis zu bekommen
    tries = 6
    for _ in range(tries):
        d = _generate_from_news() if use_news else _generate_trivia()
        time.sleep(_SLEEP)
        if d and d.get("is_politics") is True and (d.get("question") or "").strip():
            d["category"]=CATEGORY_NAME
            # Standardquelle setzen, falls Trivia keine gesetzt hat
            if "source" not in d or not d["source"]:
                d["source"]={"title":"Politik-Trivia","url":"https://www.bundesregierung.de"}
            return d
        # Beim nächsten Versuch Modus wechseln (News <-> Trivia), um Hänger zu vermeiden
        use_news = not use_news
    return None
