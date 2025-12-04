# kategorien/popkultur.py
# -*- coding: utf-8 -*-
import os, sys, re, json, time, random, importlib, importlib.util
from types import ModuleType
from typing import Optional, List, Tuple, Dict, Any

try:
    from openai import OpenAI
    client = OpenAI()
except (ImportError, Exception):
    client = None

CATEGORY_NAME = "Pop-Kultur"

# ──────────────────────────────────────────────────────────────────────────────
# sys.path-Bootstrap
# ──────────────────────────────────────────────────────────────────────────────
_THIS = os.path.abspath(__file__)
_DIR  = os.path.dirname(_THIS)

_CANDIDATE_ROOTS = [
    os.path.abspath(os.path.join(_DIR, "..")),
    os.path.abspath(os.path.join(_DIR, "..", "..")),
    os.path.abspath(os.getcwd()),
]

def _ensure_root_on_syspath() -> Optional[str]:
    for root in _CANDIDATE_ROOTS:
        if os.path.isdir(os.path.join(root, "Unterkategorien")):
            if root not in sys.path:
                sys.path.insert(0, root)
            return root
    for root in _CANDIDATE_ROOTS:
        kat_dir = os.path.join(root, "kategorien")
        if os.path.isdir(os.path.join(kat_dir, "Unterkategorien")):
            if kat_dir not in sys.path:
                sys.path.insert(0, kat_dir)
            return kat_dir
    return None

_PROJECT_ANCHOR = _ensure_root_on_syspath()

def _fs_debug() -> str:
    bases = []
    if _PROJECT_ANCHOR:
        bases.append(_PROJECT_ANCHOR)
        k = os.path.join(_PROJECT_ANCHOR, "kategorien")
        if os.path.isdir(k):
            bases.append(k)
    else:
        bases.append(_DIR)

    lines = []
    for base in bases:
        pkg = os.path.join(base, "Unterkategorien")
        rp  = os.path.join(pkg, "PopKultur")
        lines.append(f"Base: {base}")
        lines.append(f"  - Exists {pkg}: {os.path.isdir(pkg)}")
        lines.append(f"  - Exists {rp}: {os.path.isdir(rp)}")
        if os.path.isdir(pkg):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(pkg,'__init__.py'))}")
        if os.path.isdir(rp):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(rp,'__init__.py'))}")
            for mod in ("film_kino", "serien_streaming", "gaming", "social_media", "youtube_influencer"):
                lines.append(f"    - {mod}.py: {os.path.isfile(os.path.join(rp, mod + '.py'))}")
    lines.append("sys.path (head):")
    for p in sys.path[:6]:
        lines.append("  * " + p)
    return "\n".join(lines)

# ──────────────────────────────────────────────────────────────────────────────
# Oberthemen & Gewichte + Bucket-Gewichte (1–4 / 5–7 / 8–10)
# ──────────────────────────────────────────────────────────────────────────────
_TOPICS: Dict[str, int] = {
    "Film & Kino": 30,
    "Serien & Streaming": 25,
    "Gaming": 20,
    "Social Media & Internet": 15,
    "YouTube & Influencer": 10,
}

_TOPIC_WEIGHTS_BY_BUCKET: Dict[str, Dict[str, int]] = {
    "1-4": {
        "Film & Kino": 25,
        "Serien & Streaming": 30,
        "Gaming": 25,
        "Social Media & Internet": 12,
        "YouTube & Influencer": 8,
    },
    "5-7": {
        "Film & Kino": 30,
        "Serien & Streaming": 25,
        "Gaming": 20,
        "Social Media & Internet": 15,
        "YouTube & Influencer": 10,
    },
    "8-10": {
        "Film & Kino": 35,
        "Serien & Streaming": 25,
        "Gaming": 20,
        "Social Media & Internet": 12,
        "YouTube & Influencer": 8,
    },
}

def _bucket_for(d: int) -> str:
    if d <= 4: return "1-4"
    if d <= 7: return "5-7"
    return "8-10"

def _pick_topic_for_difficulty(d: int) -> str:
    bucket = _bucket_for(d)
    weights_map = _TOPIC_WEIGHTS_BY_BUCKET.get(bucket, _TOPICS)
    names = list(weights_map.keys())
    weights = [weights_map[n] for n in names]
    return random.choices(names, weights=weights, k=1)[0]

# Topic -> Modulpfad
_SUBMODULE_PATHS: Dict[str, str] = {
    "Film & Kino": "Unterkategorien.PopKultur.film_kino",
    "Serien & Streaming": "Unterkategorien.PopKultur.serien_streaming",
    "Gaming": "Unterkategorien.PopKultur.gaming",
    "Social Media & Internet": "Unterkategorien.PopKultur.social_media",
    "YouTube & Influencer": "Unterkategorien.PopKultur.youtube_influencer",
}

_SUBTOPICS: Dict[str, List[Dict[str, Any]]] = {}

# ──────────────────────────────────────────────────────────────────────────────
# Loader
# ──────────────────────────────────────────────────────────────────────────────
def _load_subtopics_from_module(mod: ModuleType) -> List[Dict[str, Any]]:
    if hasattr(mod, "SUBTOPICS"):
        data = getattr(mod, "SUBTOPICS")
    elif hasattr(mod, "SUBDISCIPLINES"):
        data = getattr(mod, "SUBDISCIPLINES")
    else:
        raise AttributeError("weder SUBTOPICS noch SUBDISCIPLINES gefunden")

    if not isinstance(data, list):
        raise TypeError("SUBTOPICS/SUBDISCIPLINES muss eine Liste sein")

    normed: List[Dict[str, Any]] = []
    for item in data:
        if not isinstance(item, tuple):
            raise TypeError("Eintrag muss Tuple sein")
        if len(item) == 2:
            name, w = item
            rng = (1, 10)
        elif len(item) == 3:
            name, w, rng = item
            if not (isinstance(rng, tuple) and len(rng) == 2 and all(isinstance(x, int) for x in rng)):
                raise TypeError("Range muss Tuple[int,int] sein")
        else:
            raise TypeError("Tuple-Länge 2 oder 3 erwartet")

        if not (isinstance(name, str) and isinstance(w, int)):
            raise TypeError("Format (str,int[, (int,int)]) erwartet")

        mn, mx = rng
        mn = max(1, min(10, mn))
        mx = max(1, min(10, mx))
        if mn > mx:
            mn, mx = mx, mn

        normed.append({
            "name": name,
            "weight": w,
            "min_difficulty": mn,
            "max_difficulty": mx,
        })

    return normed

def _load_all_subtopics_strict() -> Dict[str, List[Dict[str, Any]]]:
    errors: List[str] = []
    result: Dict[str, List[Dict[str, Any]]] = {}
    for topic, module_path in _SUBMODULE_PATHS.items():
        try:
            spec = importlib.util.find_spec(module_path)
        except ModuleNotFoundError:
            spec = None
        if spec is None:
            errors.append(f"[{topic}] Modul nicht gefunden: {module_path}")
            continue
        try:
            mod = importlib.import_module(module_path)
            result[topic] = _load_subtopics_from_module(mod)
        except Exception as e:
            errors.append(f"[{topic}] Import-/Ladefehler in {module_path}: {e.__class__.__name__}: {e}")
            continue

    if errors:
        raise ImportError(
            "Pop-Kultur-Plugin konnte Unterthemen nicht laden:\n"
            + "\n".join(f" - {e}" for e in errors)
            + "\n\nDateisystem-Check:\n" + _fs_debug()
        )
    return result

_SUBTOPICS = _load_all_subtopics_strict()

# ──────────────────────────────────────────────────────────────────────────────
# Auswahl-Hilfen
# ──────────────────────────────────────────────────────────────────────────────
def _pick_weighted_name(dicts: List[Dict[str, Any]]) -> Optional[str]:
    if not dicts:
        return None
    names = [d["name"] for d in dicts]
    weights = [d["weight"] for d in dicts]
    return random.choices(names, weights=weights, k=1)[0]

def _choose_subdiscipline(topic: str, target_difficulty: int) -> Optional[str]:
    entries = _SUBTOPICS.get(topic, [])
    eligible = [d for d in entries if d["min_difficulty"] <= target_difficulty <= d["max_difficulty"]]
    if eligible:
        return _pick_weighted_name(eligible)
    for delta in (1, 2, 3):
        eligible = [d for d in entries if (d["min_difficulty"] - delta) <= target_difficulty <= (d["max_difficulty"] + delta)]
        if eligible:
            return _pick_weighted_name(eligible)
    return _pick_weighted_name(entries)

# ──────────────────────────────────────────────────────────────────────────────
# Prompting & Schema
# ──────────────────────────────────────────────────────────────────────────────
_SCHEMA = """{
  "category": "Pop-Kultur",
  "topic": "Film & Kino|Serien & Streaming|Gaming|Social Media & Internet|YouTube & Influencer",
  "question": "...",
  "choices": ["A: ...", "B: ...", "C: ...", "D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 Sätze, kurz und hilfreich.",
  "difficulty": 1
}"""

_DIFF_GUIDE = """
1 = absolutes Grundwissen (≈ 95 % der Bevölkerung in DE)
2 = sehr einfaches Grundwissen
3 = einfache Fragen (ohne schwere Thematik)
4 = leichte Fragen (Recall, einfache Anwendung)
5 = einfach–mittel (70–80 % schaffbar)
6 = mittlere Komplexität (≈ 60 % schaffbar)
7 = mittel–schwer (für Nicht-Expert:innen anspruchsvoll)
8 = schwer (deutliches Vorwissen/vertieftes Verständnis nötig)
9 = Expertenwissen (Fachkenntnisse erforderlich)
10 = schwerstmöglich (oberes Expertenniveau)
""".strip()

_DIFF_LEVELS: Dict[int, str] = {
    1: "absolutes Grundwissen (≈ 95 % der Bevölkerung in DE)",
    2: "sehr einfaches Grundwissen",
    3: "einfache Fragen (ohne schwere Thematik)",
    4: "leichte Fragen (Recall, einfache Anwendung)",
    5: "einfach–mittel (70–80 % schaffbar)",
    6: "mittlere Komplexität (≈ 60 % schaffbar)",
    7: "mittel–schwer (für Nicht-Expert:innen anspruchsvoll)",
    8: "schwer (deutliches Vorwissen/vertieftes Verständnis nötig)",
    9: "Expertenwissen (Fachkenntnisse erforderlich)",
    10:"schwerstmöglich (oberes Expertenniveau)",
}

def _temperature_for(d: int) -> float:
    return 0.8 + (0.02 if d >= 9 else 0.0)

def _get_difficulty_examples(d: int) -> str:
    """Konkrete Beispiele für die jeweilige Schwierigkeitsstufe."""
    if d <= 2:
        return """
Beispiele für Stufe {d}:
- "In welchem Film sagt Darth Vader 'Ich bin dein Vater'?" (Star Wars - jeder kennt es)
- "Welche Konsole hat Nintendo 2017 veröffentlicht?" (Switch - sehr bekannt)
- "Auf welcher Plattform werden Kurzvideos mit Musik geteilt?" (TikTok)
""".format(d=d)
    elif d <= 4:
        return """
Beispiele für Stufe {d}:
- "Wer spielt Iron Man im Marvel Cinematic Universe?" (Robert Downey Jr.)
- "In welcher Serie kämpfen Jon Snow und Daenerys Targaryen?" (Game of Thrones)
- "Welches Spiel hat den Kreativ-Modus 'Creative'?" (Minecraft/Fortnite)
""".format(d=d)
    elif d <= 6:
        return """
Beispiele für Stufe {d}:
- "Welcher Regisseur führte Regie bei Inception und Interstellar?" (Christopher Nolan)
- "Welche Netflix-Serie spielt in der fiktiven Stadt Hawkins?" (Stranger Things)
- "Welches Spiel gewann 2020 den Game of the Year Award?" (The Last of Us Part II)
""".format(d=d)
    elif d <= 8:
        return """
Beispiele für Stufe {d}:
- "In welchem Jahr gewann 'Parasite' als erster nicht-englischsprachiger Film den Oscar?" (2020)
- "Welcher Schauspieler spielte in 'Breaking Bad' den Anwalt Saul Goodman?"
- "Welches Indie-Game gilt als Wegbereiter für das Roguelike-Genre?" (vertieftes Wissen)
""".format(d=d)
    else:
        return """
Beispiele für Stufe {d}:
- "Welche Kamera wurde für 'Blade Runner 2049' hauptsächlich verwendet?" (Expertenwissen)
- "Welcher Algorithmus bestimmt primär das YouTube-Ranking?" (technisches Wissen)
- "In welchem Jahr erschien der erste Ego-Shooter 'Wolfenstein 3D'?" (Spezialwissen)
""".format(d=d)

def _get_distractors_guide() -> str:
    """Anleitung für plausible falsche Antworten."""
    return """
WICHTIG - FALSCHE ANTWORTEN (Distraktoren):
- Müssen PLAUSIBEL und NAH an der richtigen Antwort sein
- Nutze häufige Verwechslungen (z.B. ähnliche Schauspieler, verwandte Spiele)
- KEINE absurden Optionen (bei Film-Frage nicht "Banane" als Antwort)
- Mix: ähnliche Werke, gleiche Ära, verwandte Personen

GUTE Distraktoren:
"Wer führte Regie bei 'Inception'?"
A: Christopher Nolan ✓
B: Denis Villeneuve (ähnlicher Stil, könnte verwechselt werden!)
C: Ridley Scott (Sci-Fi-Regisseur, plausibel)
D: James Cameron (ebenfalls für komplexe Sci-Fi bekannt)

SCHLECHTE Distraktoren:
A: Christopher Nolan ✓
B: Steven Spielberg (völlig anderer Stil, zu offensichtlich)
C: Quentin Tarantino (macht keine Sci-Fi)
D: Walt Disney (absurd)
"""

def _prompt(topic: str, target_difficulty: int, mode: Optional[str], subtopic: Optional[str] = None) -> tuple[str, float]:
    temperature = _temperature_for(int(target_difficulty))
    level_desc = _DIFF_LEVELS.get(int(target_difficulty), "siehe Stufenleitfaden")
    sub_hint = f"- Unterthema (nur als inhaltlicher Hinweis, NICHT ins JSON übernehmen): '{subtopic}'.\n" if subtopic else ""
    
    examples = _get_difficulty_examples(target_difficulty)
    distractor_guide = _get_distractors_guide()

    prompt = f"""
Erzeuge EINE Multiple-Choice-Frage (A–D, genau eine richtig) zur Kategorie „{CATEGORY_NAME}", Oberthema „{topic}" (Deutsch).
{sub_hint}Ziel-Schwierigkeit: {target_difficulty}/10 – {level_desc}

Kontext zu Schwierigkeitsstufen (1–10):
{_DIFF_GUIDE}

{examples}

{distractor_guide}

Vorgaben:
- Neutrale, zugängliche Formulierung; keine hochakademische Sprache.
- Allgemeines Pop-Kultur-Wissen; keine ultra-aktuellen Events (Stand: max. vor 6 Monaten).
- Vier plausible Antworten, genau eine korrekt; keine „alle oben/keine der oben"-Optionen.
- Bevorzuge interessante Kontexte statt reiner Jahreszahl-Abfragen.
- Erklärung: 2–3 Sätze, knapp und hilfreich (Kontext, Fun Fact, Einordnung).
- Das Feld "topic" im JSON enthält ausschließlich das Oberthema („{topic}"). Unterthema nicht ins JSON.
- Antworte ausschließlich mit **validem JSON** gemäß Schema.
- Vermeide Fragen, in denen die richtige Lösung oder Varianten davon bereits im Fragetext vorkommen.

JSON-SCHEMA:
{_SCHEMA}
""".strip()
    return prompt, temperature

_JSON_OBJ_RE = re.compile(r"\{.*\}", re.DOTALL)
_CHOICE_PREFIX_RE = re.compile(r"^[A-D]:\s*", re.IGNORECASE)

def _ask_json(prompt: str, temperature: float) -> dict | None:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    last_err = None
    for attempt in range(3):
        try:
            r = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Antwort ausschließlich als valides JSON, keine Zusätze."},
                    {"role": "user", "content": prompt},
                ],
                temperature=temperature,
            )
            raw = (r.choices[0].message.content or "").strip()
            m = _JSON_OBJ_RE.search(raw)
            if not m:
                raise ValueError("Kein JSON im Modell-Output gefunden")
            return json.loads(m.group(0))
        except Exception as e:
            last_err = e
            time.sleep(0.3 * (attempt + 1))
    return None

def _normalize_choice(s: str) -> str:
    return _CHOICE_PREFIX_RE.sub("", s.strip())

def _letter_to_index(letter: str) -> Optional[int]:
    if not isinstance(letter, str) or not letter:
        return None
    L = letter.strip().upper()[:1]
    return {"A":0, "B":1, "C":2, "D":3}.get(L)

# ──────────────────────────────────────────────────────────────────────────────
# Öffentliche Generator-API
# ──────────────────────────────────────────────────────────────────────────────
def generate_one(tier: int = 5, mode: Optional[str] = None) -> Optional[dict]:
    if not client:
        return None
    
    main_topics = list(_SUBTOPICS.keys())
    topic = random.choice(main_topics)
    topic_data = _SUBTOPICS[topic]
    
    bucket_for_tier = _get_tier_bucket(tier)
    main_weights = _WEIGHTS.get(bucket_for_tier, _WEIGHTS["5-7"])
    
    if topic not in main_weights:
        return None
    
    subtopic, (min_d, max_d) = _pick_weighted_subtopic(topic_data, tier)
    clamped_tier = max(min_d, min(tier, max_d))
    
    prompt_str, temp = _prompt(topic, clamped_tier, mode, subtopic)
    
    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt_str}],
            temperature=temp,
            max_tokens=600,
        )
        raw = resp.choices[0].message.content.strip()
    except Exception as e:
        print(f"[popkultur] OpenAI error: {e}")
        return None
    
    data = _parse_json(raw)
    if not data:
        return None
    
    q = data.get("question", "").strip()
    if not q:
        return None
    
    choices_raw = data.get("choices", [])
    if not isinstance(choices_raw, list) or len(choices_raw) < 4:
        return None
    
    ca_raw = data.get("correct_answer", "")
    expl = data.get("explanation", "").strip()
    
    labeled = {}
    letters = ["A", "B", "C", "D"]
    for i, ch_item in enumerate(choices_raw[:4]):
        if isinstance(ch_item, dict):
            txt = ch_item.get("text", "").strip()
        elif isinstance(ch_item, str):
            txt = ch_item.strip()
        else:
            txt = ""
        if txt:
            labeled[letters[i]] = txt
    
    if len(labeled) < 4:
        return None
    
    ca_letter = ca_raw[:1].upper() if ca_raw else "A"
    if ca_letter not in letters:
        try:
            idx = int(re.findall(r"\d", ca_raw)[0])
        except Exception:
            idx = 0
        idx = max(0, min(3, idx))
        ca_letter = letters[idx]
    
    out = {
        "category": CATEGORY_NAME,
        "subcategory": subtopic,
        "question": q,
        "options": labeled,
        "correct_answer": ca_letter,
        "difficulty": int(data.get("difficulty", tier)),
    }
    
    if expl:
        out["explanation"] = expl
    
    for k in ("sourceTitle", "sourceUrl"):
        v = data.get(k)
        if isinstance(v, str) and v.strip():
            out[k] = v.strip()
    
    return out
