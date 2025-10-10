# -*- coding: utf-8 -*-
"""
Tägliches Quiz:
- 2 Politikfragen aus 5 Tagesschau-Artikeln (leicht verständlich, mit Einordnung von Personen)
- 3 zusätzliche Fragen aus zufälligen Segmenten (Sport, Geschichte, Wissenschaft, Kunst & Literatur, Sprache, Essen & Trinken)
- Duplikat-Check gegen die letzten 7 Tage (semantisch über einfache Textähnlichkeit)
- Persistenz in /quizzes/YYYY-MM-DD/bundle.json + latest.json + catalog.json
"""

import os
import re
import json
import time
import random
import string
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone, timedelta
from difflib import SequenceMatcher

from openai import OpenAI

# ============ 🔐 OpenAI ============
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# ============ ⚙️ Einstellungen ============
BASE_URL = "https://www.tagesschau.de"
NUM_FRONT_ARTICLES = 5
POLITICS_TARGET = 2
OUT_ROOT = "quizzes"
RANDOM_SEGMENTS = [
    "Sport",
    "Geschichte",
    "Wissenschaft",
    "Kunst und Literatur",
    "Sprache",
    "Essen und Trinken",
]
RANDOM_SEGMENTS_PER_DAY = 3
SLEEP_BETWEEN_CALLS = 1.5  # Sekunden, etwas sanfter für Rate Limits
DUPLICATE_SIMILARITY_THRESHOLD = 0.82  # 0..1 (je höher, desto strenger)
PAST_DAYS_TO_CHECK = 7

# ============ 🧰 Utilities ============
def _iso_date_today() -> str:
    return datetime.now().strftime("%Y-%m-%d")

def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def slugify(text: str, max_len: int = 120) -> str:
    t = re.sub(r"\s+", " ", text).strip().lower()
    t = "".join(ch for ch in t if ch in string.ascii_lowercase + string.digits + " -_")
    return t[:max_len]

def similarity(a: str, b: str) -> float:
    a = re.sub(r"\s+", " ", a).strip().lower()
    b = re.sub(r"\s+", " ", b).strip().lower()
    return SequenceMatcher(None, a, b).ratio()

def is_duplicate(candidate_q: str, corpus_questions: list[str]) -> bool:
    for q in corpus_questions:
        if similarity(candidate_q, q) >= DUPLICATE_SIMILARITY_THRESHOLD:
            return True
    return False

def load_past_questions(days: int = PAST_DAYS_TO_CHECK) -> list[dict]:
    """Lädt alle Fragen der letzten N Tage aus dem quizzes/-Ordner."""
    past = []
    if not os.path.exists(OUT_ROOT):
        return past

    # 1) Versuche catalog.json (falls vorhanden) – effizient
    catalog_path = os.path.join(OUT_ROOT, "catalog.json")
    dates = set()
    if os.path.exists(catalog_path):
        try:
            catalog = json.load(open(catalog_path, "r", encoding="utf-8"))
            cutoff = datetime.now().date() - timedelta(days=days)
            for entry in catalog:
                try:
                    d = datetime.strptime(entry.get("date", ""), "%Y-%m-%d").date()
                    if d >= cutoff:
                        dates.add(entry["date"])
                except Exception:
                    continue
        except Exception:
            pass

    # 2) Fallback: scanne Verzeichnisse
    if not dates:
        try:
            for name in os.listdir(OUT_ROOT):
                p = os.path.join(OUT_ROOT, name, "bundle.json")
                try:
                    d = datetime.strptime(name, "%Y-%m-%d").date()
                    if d >= datetime.now().date() - timedelta(days=days) and os.path.exists(p):
                        dates.add(name)
                except Exception:
                    continue
        except Exception:
            pass

    for d in sorted(dates, reverse=True):
        bundle_path = os.path.join(OUT_ROOT, d, "bundle.json")
        if os.path.exists(bundle_path):
            try:
                bundle = json.load(open(bundle_path, "r", encoding="utf-8"))
                past.extend(bundle.get("questions", []))
            except Exception:
                continue
    return past

def fetch_front_article_links(n: int = NUM_FRONT_ARTICLES) -> list[str]:
    res = requests.get(BASE_URL, timeout=15)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    links = []
    for a in soup.select("a.teaser__link"):
        href = a.get("href")
        if href and href.startswith("/") and href not in links:
            links.append(BASE_URL + href)
        if len(links) == n:
            break
    return links

def fetch_article(url: str) -> dict:
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    s = BeautifulSoup(r.text, "html.parser")
    title_tag = s.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else url
    paragraphs = s.select("p")
    content_full = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
    return {
        "url": url,
        "title": title,
        "content_full": content_full,
        "content_short": content_full[:2000],  # etwas großzügiger für besseren Kontext
    }

# ============ 🧠 Prompting ============
POLITICS_JSON_SCHEMA = """{
  "is_politics": true,
  "category": "Politik",
  "question": "...",
  "choices": ["A: ...", "B: ...", "C: ...", "D: ..."],
  "correct_answer": "A",
  "explanation": "...",
  "source": {"title": "...", "url": "..."}
}"""


def build_politics_prompt(title: str, content_short: str, url: str) -> str:
    return f"""
Du bist ein deutscher Nachrichten-Quizgenerator.

AUFGABE:
- Prüfe, ob der folgende Text überwiegend POLITIK betrifft (Regierung, Wahlen, Parlamente, Ministerien, Parteien, Staats- und Regierungschefs, internationale Politik, EU, UN, Gesetzgebung, Sicherheits-/Außenpolitik).
- Wenn JA, erzeuge genau EINE Multiple-Choice-Frage (A–D, eine richtig).
- Formuliere die FRAGE so, dass sie für Menschen verständlich ist, die die Nachrichten nicht verfolgt haben:
  * Baue kurze EINORDNUNGEN direkt in die Frage ein (z. B. „… Bundeskanzler Olaf Scholz (Deutschland) …”, „… EU-Kommissionspräsidentin Ursula von der Leyen …”).
  * Nenne bei erstmaliger Erwähnung von Personen ihren Titel/Funktion/Land, bei Organisationen kurz ihre Rolle.
- Die Erklärung (2–3 Sätze) soll die richtige Antwort einordnen (Kontext, Bedeutung).
- Die Frage sollte nach dem Ereignis selbst fragen


GIB AUSSCHLIESSLICH valides JSON gemäß Schema zurück (keine zusätzlichen Zeichen, keine Markdown-Formatierung). 
Wenn der Text KEINE Politik ist, gib folgendes JSON zurück: {{"is_politics": false}}

TEXT:
---
Titel: {title}
Inhalt: {content_short}
Quelle: {url}
---

JSON-SCHEMA:
{POLITICS_JSON_SCHEMA}
""".strip()

GENERAL_JSON_SCHEMA = """{
  "category": "Sport|Geschichte|Wissenschaft|Kunst und Literatur|Sprache|Essen und Trinken",
  "question": "...",
  "choices": ["A: ...", "B: ...", "C: ...", "D: ..."],
  "correct_answer": "A",
  "explanation": "2–3 Sätze, kurz und hilfreich."
}"""


def build_general_prompt(category: str) -> str:
    return f"""
Erzeuge eine Multiple-Choice-Frage (A–D, eine richtig) zur Kategorie „{category}“ in deutscher Sprache.
Anforderungen:
- Verständlich für Laien.
- Keine tagesaktuellen Nachrichten nötig (zeitlos oder langlebig).
- Wenn Fachbegriffe vorkommen, erkläre sie kurz in der FRAGE selbst, außer die Frage fragt nach dem Begriff selbst (Klammer oder kurze Einordnung).
- Gib AUSSCHLIESSLICH valides JSON gemäß Schema zurück, ohne Kommentare, ohne Markdown.

JSON-SCHEMA:
{GENERAL_JSON_SCHEMA}
""".strip()

def ask_openai_json(prompt: str) -> dict | None:
    """Robuste JSON-Antwort einfordern und parsen. Bei Fehlern -> None."""
    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",  # kleines, günstiges Modell mit gutem JSON-Verhalten
            messages=[
                {"role": "system", "content": "Du gibst ausschließlich valides JSON zurück."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )
        raw = resp.choices[0].message.content.strip()
        # Herauslösen des ersten/letzten {...} Blocks, falls das Modell doch mal drumherum Text liefert
        m = re.search(r"\{.*\}", raw, flags=re.DOTALL)
        if m:
            raw = m.group(0)
        return json.loads(raw)
    except Exception:
        return None

# ============ 🧩 Pipeline ============
def generate_politics_questions(articles: list[dict], past_questions_texts: list[str]) -> list[dict]:
    """Versucht aus Artikeln genau POLITIK-Fragen zu generieren, dedupliziert ggü. Vergangenheit & untereinander."""
    candidates = []
    for art in articles:
        prompt = build_politics_prompt(art["title"], art["content_short"], art["url"])
        data = ask_openai_json(prompt)
        time.sleep(SLEEP_BETWEEN_CALLS)
        if not data or data.get("is_politics") is not True:
            continue
        # Normieren & anreichern
        qtext = data.get("question", "").strip()
        if not qtext:
            continue
        if is_duplicate(qtext, past_questions_texts):
            # Duplikat ggü. Vergangenheit -> verwerfen
            continue
        data["category"] = "Politik"
        data["source"] = {"title": art["title"], "url": art["url"]}
        data["difficulty"] = random.randint(1, 10)
        candidates.append(data)

    # Untereinander deduplizieren
    final = []
    for c in candidates:
        if not any(similarity(c["question"], x["question"]) >= DUPLICATE_SIMILARITY_THRESHOLD for x in final):
            final.append(c)

    # Auf Zielzahl trimmen
    return final[:POLITICS_TARGET]

def regenerate_until_unique(generator_fn, target_count: int, past_texts: list[str], max_tries: int = 8) -> list[dict]:
    """Hilfsfunktion für Random-Segmente: generiert bis target erreicht oder Versuche erschöpft."""
    out = []
    tries = 0
    while len(out) < target_count and tries < max_tries:
        item = generator_fn()
        tries += 1
        if not item:
            continue
        qt = item.get("question", "").strip()
        if not qt:
            continue
        if is_duplicate(qt, past_texts) or any(similarity(qt, x["question"]) >= DUPLICATE_SIMILARITY_THRESHOLD for x in out):
            continue
        out.append(item)
    return out

def generate_random_segment_questions(past_questions_texts: list[str]) -> list[dict]:
    segments = random.sample(RANDOM_SEGMENTS, k=RANDOM_SEGMENTS_PER_DAY)
    def make_one(seg: str):
        def _gen():
            data = ask_openai_json(build_general_prompt(seg))
            time.sleep(SLEEP_BETWEEN_CALLS)
            if not data:
                return None
            data["category"] = seg  # sicherstellen
            data["difficulty"] = random.randint(1, 10)
            return data
        return _gen

    results = []
    for seg in segments:
        unique = regenerate_until_unique(make_one(seg), target_count=1, past_texts=past_questions_texts, max_tries=6)
        if unique:
            results.extend(unique)
    return results

# ============ 💾 Persistenz ============
def write_daily_bundle(quiz_list: list[dict], date_str: str | None = None):
    if not quiz_list:
        print("❌ Keine gültigen Quizfragen generiert.")
        return

    day = date_str or _iso_date_today()
    day_dir = os.path.join(OUT_ROOT, day)
    os.makedirs(day_dir, exist_ok=True)

    bundle = {
        "date": day,
        "generated_at": _now_iso(),
        "schema_version": 3,  # ↑ Version, da category/source ergänzt wurden
        "questions": quiz_list,
    }

    bundle_path = os.path.join(day_dir, "bundle.json")
    with open(bundle_path, "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=2)

    # latest.json aktualisieren
    latest_path = os.path.join(OUT_ROOT, "latest.json")
    with open(latest_path, "w", encoding="utf-8") as f:
        json.dump({"latest_date": day, "path": f"{OUT_ROOT}/{day}/bundle.json"}, f, ensure_ascii=False, indent=2)

    # catalog.json pflegen
    catalog_path = os.path.join(OUT_ROOT, "catalog.json")
    catalog = []
    if os.path.exists(catalog_path):
        try:
            with open(catalog_path, "r", encoding="utf-8") as f:
                catalog = json.load(f)
        except Exception:
            catalog = []
    entry = {"date": day, "path": f"{OUT_ROOT}/{day}/bundle.json"}
    catalog = [e for e in catalog if e.get("date") != day] + [entry]
    catalog.sort(key=lambda e: e.get("date", ""), reverse=True)
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    print(f"✅ Bundle gespeichert: {bundle_path}")
    print(f"➡️  latest.json aktualisiert: {latest_path}")
    print(f"🗂️  catalog.json aktualisiert: {catalog_path}")

# ============ 🚀 Main ============
def main():
    # 1) Vergangene Woche laden
    past = load_past_questions(PAST_DAYS_TO_CHECK)
    past_questions_texts = [q.get("question", "") for q in past if isinstance(q, dict)]

    # 2) Tagesschau-Artikel holen (5 Stück)
    links = fetch_front_article_links(NUM_FRONT_ARTICLES)
    if not links:
        print("❌ Keine Artikel gefunden.")
        return
    articles = []
    for u in links:
        try:
            articles.append(fetch_article(u))
        except Exception as e:
            print(f"⚠️ Fehler bei Artikel: {u} – {e}")
    if not articles:
        print("❌ Keine Artikelinhalte abrufbar.")
        return

    # 3) Politikfragen erzeugen (Ziel: 2)
    politics = generate_politics_questions(articles, past_questions_texts)

    # Falls weniger als 2 Politikfragen entstanden sind, fülle NICHT mit anderen Kategorien auf;
    # wir halten uns an „liest 5 Artikel und sucht 2 Politikfragen daraus“ – lieber 1 als eine unpassende.
    if len(politics) < POLITICS_TARGET:
        print(f"ℹ️ Nur {len(politics)} Politik-Frage(n) generiert – zu wenig Politik auf der Frontpage?")

    # 4) 3 zufällige Segmente -> je 1 Frage
    random_segments_questions = generate_random_segment_questions(past_questions_texts)

    # 5) Zusammenführen & Speichern
    all_questions = politics + random_segments_questions
    write_daily_bundle(all_questions)

if __name__ == "__main__":
    main()
