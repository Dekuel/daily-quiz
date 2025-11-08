# -*- coding: utf-8 -*-
"""
Language plugin (English wrapper for `Sprache`).

This module adapts the logic of `kategorien/sprache.py` but exposes English
topic names and prompts. It reuses the existing Unterkategorien/Sprache
submodules (which contain German-named files) and maps them to English
topic labels so the EN-generation path can call `kategorien.language`.

The public API is `generate_one(past_texts: List[str], target_difficulty: Optional[int], mode: Optional[str]) -> dict | None`.
"""

from __future__ import annotations
import os, sys, re, json, time, random, importlib, importlib.util
from types import ModuleType
from typing import Optional, List, Tuple, Dict, Any
from openai import OpenAI

CATEGORY_NAME = "Language"

# The code intentionally mirrors the implementation in `kategorien/sprache.py`.
# It uses the same Unterkategorien modules, but exposes English topic names.

_THIS = os.path.abspath(__file__)
_DIR = os.path.dirname(_THIS)

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
        rp = os.path.join(pkg, "Sprache")
        lines.append(f"Base: {base}")
        lines.append(f"  - Exists {pkg}: {os.path.isdir(pkg)}")
        lines.append(f"  - Exists {rp}: {os.path.isdir(rp)}")
        if os.path.isdir(pkg):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(pkg,'__init__.py'))}")
        if os.path.isdir(rp):
            lines.append(f"    - __init__.py: {os.path.isfile(os.path.join(rp,'__init__.py'))}")
            for mod in ("grammatik", "wortherkunft", "redewendungen", "fremdsprachen"):
                lines.append(f"    - {mod}.py: {os.path.isfile(os.path.join(rp, mod + '.py'))}")
    lines.append("sys.path (head):")
    for p in sys.path[:6]:
        lines.append("  * " + p)
    return "\n".join(lines)

# English topic labels mapped to the existing submodule file names
_TOPICS: Dict[str, int] = {
    "Grammar": 10,
    "Etymology": 50,
    "Idioms": 15,
    "Foreign Languages": 25,
}

_TOPIC_WEIGHTS_BY_BUCKET: Dict[str, Dict[str, int]] = {
    "1-4": dict(_TOPICS),
    "5-7": dict(_TOPICS),
    "8-10": dict(_TOPICS),
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

# Map English topic -> Unterkategorien module path (German filenames)
_SUBMODULE_PATHS: Dict[str, str] = {
    "Grammar":      "Unterkategorien.Sprache.grammatik",
    "Etymology":    "Unterkategorien.Sprache.wortherkunft",
    "Idioms":       "Unterkategorien.Sprache.redewendungen",
    "Foreign Languages": "Unterkategorien.Sprache.fremdsprachen",
}

_SUBTOPICS: Dict[str, List[Dict[str, Any]]] = {}

def _load_subtopics_from_module(mod: ModuleType) -> List[Dict[str, Any]]:
    if hasattr(mod, "SUBTOPICS"):
        data = getattr(mod, "SUBTOPICS")
    elif hasattr(mod, "SUBDISCIPLINES"):
        data = getattr(mod, "SUBDISCIPLINES")
    else:
        raise AttributeError("neither SUBTOPICS nor SUBDISCIPLINES found")

    if not isinstance(data, list):
        raise TypeError("SUBTOPICS/SUBDISCIPLINES must be a list")

    normed: List[Dict[str, Any]] = []
    for item in data:
        if not isinstance(item, tuple):
            raise TypeError("entry must be a tuple")
        if len(item) == 2:
            name, w = item
            rng = (1, 10)
        elif len(item) == 3:
            name, w, rng = item
            if not (isinstance(rng, tuple) and len(rng) == 2 and all(isinstance(x, int) for x in rng)):
                raise TypeError("range must be Tuple[int,int]")
        else:
            raise TypeError("tuple length 2 or 3 expected")

        if not (isinstance(name, str) and isinstance(w, int)):
            raise TypeError("format (str,int[, (int,int)]) expected")

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
    """
    Load subtopics but be tolerant: missing submodules are skipped and
    available topics are returned. This avoids aborting plugin import when
    some Unterkategorien files are not present.
    """
    errors: List[str] = []
    result: Dict[str, List[Dict[str, Any]]] = {}
    for topic, module_path in _SUBMODULE_PATHS.items():
        try:
            spec = importlib.util.find_spec(module_path)
        except Exception:
            spec = None
        if spec is None:
            errors.append(f"[{topic}] module not found: {module_path}")
            continue
        try:
            mod = importlib.import_module(module_path)
            try:
                result[topic] = _load_subtopics_from_module(mod)
            except Exception as e:
                errors.append(f"[{topic}] failed to parse SUBTOPICS in {module_path}: {e.__class__.__name__}: {e}")
                continue
        except Exception as e:
            errors.append(f"[{topic}] import error {module_path}: {e.__class__.__name__}: {e}")
            continue

    if errors:
        # don't raise; print a concise debug message and continue with what we have
        try:
            print("[LANGUAGE-PLUGIN] Some submodules missing or failed to load:")
            for e in errors:
                print(" - ", e)
            print("[LANGUAGE-PLUGIN] Filesystem debug:\n" + _fs_debug())
        except Exception:
            # printing must not break import
            pass

    return result

_SUBTOPICS = _load_all_subtopics_strict()

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
    for delta in (1,2,3):
        eligible = [d for d in entries if (d["min_difficulty"]-delta) <= target_difficulty <= (d["max_difficulty"]+delta)]
        if eligible:
            return _pick_weighted_name(eligible)
    return _pick_weighted_name(entries)

# Prompt schema and difficulty guide — English versions
_SCHEMA = '''{
  "category": "Language",
  "topic": "Grammar|Etymology|Idioms|Foreign Languages",
  "question": "...",
  "choices": ["A: ...", "B: ...", "C: ...", "D: ..."],
  "correct_answer": "A|B|C|D",
  "explanation": "2–3 short sentences explaining the answer.",
  "difficulty": 1
}'''

_DIFF_GUIDE = _SCHEMA  # simple placeholder; keep short for now

def _temperature_for(d: int) -> float:
    return 0.8 + (0.02 if d >= 9 else 0.0)

_JSON_OBJ_RE = re.compile(r"\{.*\}", re.DOTALL)
_CHOICE_PREFIX_RE = re.compile(r"^[A-D]:\s*", re.IGNORECASE)

def _prompt(topic: str, target_difficulty: int, mode: Optional[str], subtopic: Optional[str] = None) -> tuple[str, float]:
    temperature = _temperature_for(int(target_difficulty))
    sub_hint = f"- Subtopic (informational only): '{subtopic}'.\n" if subtopic else ""
    level_desc = f"Target difficulty: {target_difficulty}/10"
    prompt = f"""
Generate ONE multiple-choice question (A–D, exactly one correct) for category '{CATEGORY_NAME}', topic '{topic}' (English).
{sub_hint}{level_desc}

Requirements:
- Concise, clear wording.
- Four plausible answers, exactly one correct.
- Explanation: 2-3 short sentences why the answer is correct.
- Respond ONLY with valid JSON following this schema:
{_SCHEMA}
""".strip()
    return prompt, temperature

def _ask_json(prompt: str, temperature: float) -> dict | None:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    last_err = None
    for attempt in range(3):
        try:
            r = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Answer ONLY with valid JSON, no commentary."},
                    {"role": "user", "content": prompt},
                ],
                temperature=temperature,
            )
            raw = (r.choices[0].message.content or "").strip()
            m = _JSON_OBJ_RE.search(raw)
            if not m:
                raise ValueError("No JSON found in model output")
            return json.loads(m.group(0))
        except Exception as e:
            last_err = e
            time.sleep(0.3 * (attempt + 1))
    return None

def _strip_label(s: str) -> str:
    return _CHOICE_PREFIX_RE.sub("", s.strip())

def _letter_to_index(letter: str) -> Optional[int]:
    if not isinstance(letter, str) or not letter:
        return None
    L = letter.strip().upper()[:1]
    return {"A":0, "B":1, "C":2, "D":3}.get(L)

def generate_one(
    past_texts: List[str],
    target_difficulty: Optional[int] = None,
    mode: Optional[str] = None,
) -> dict | None:
    tier = int(target_difficulty) if isinstance(target_difficulty, int) else random.choice([3,5,7])
    topic = _pick_topic_for_difficulty(tier)
    subtopic = _choose_subdiscipline(topic, tier)
    prompt, temp = _prompt(topic, tier, mode, subtopic=subtopic)
    data = _ask_json(prompt, temperature=temp)
    time.sleep(0.6)
    if not data:
        return None

    q = (data.get("question") or "").strip()
    choices = data.get("choices")
    ca_raw = (data.get("correct_answer") or "").strip()
    expl = (data.get("explanation") or "").strip()
    if not q or not isinstance(choices, list) or len(choices) != 4 or not expl:
        return None

    letters = ["A","B","C","D"]
    raw_texts = [_strip_label(c) for c in choices]
    labeled = [f"{letters[i]}: {raw_texts[i]}" for i in range(4)]
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
        "topic": topic,
        "question": q,
        "choices": labeled,
        "correct_answer": ca_letter,
        "explanation": expl,
        "difficulty": int(data.get("difficulty", tier)),
    }
    for k in ("sourceTitle", "sourceUrl"):
        v = data.get(k)
        if isinstance(v, str) and v.strip():
            out[k] = v.strip()
    for k in ("options", "correctIndex", "meta"):
        out.pop(k, None)
    return out
