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

def _prompt(title:str, content:str, url:str)->str:
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

def _ask_json(p:str)->dict|None:
    c=OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        r=c.chat.completions.create(model="gpt-4o-mini",
            messages=[{"role":"system","content":"Nur valides JSON."},{"role":"user","content":p}],
            temperature=0.7)
        raw=r.choices[0].message.content.strip()
        m=re.search(r"\{.*\}",raw,re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception:return None

def generate_one(past_texts:list[str])->dict|None:
    _ensure_cache()
    if not _CACHE:return None
    random.shuffle(_CACHE)
    for art in list(_CACHE):
        d=_ask_json(_prompt(art["title"],art["content"],art["url"]))
        time.sleep(_SLEEP)
        if not d or d.get("is_politics") is not True: continue
        q=(d.get("question") or "").strip()
        if not q: continue
        d["category"]=CATEGORY_NAME
        d["source"]={"title":art["title"],"url":art["url"]}
        return d
    return None
