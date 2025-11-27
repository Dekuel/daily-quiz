# -*- coding: utf-8 -*-
from __future__ import annotations

"""
Generate-only-one-category script.

Examples (deiner Struktur ohne /scripts):
    python generate_category_only.py --category natur --count 20 --mode normal
    python generate_category_only.py -c natur -n 20 -m random -o out/natur.20.json --shuffle
"""

import os, sys, re, json, random, argparse, importlib, pkgutil, traceback
from datetime import datetime
from typing import Dict, List, Optional
from difflib import SequenceMatcher

# ──────────────────────────────────────────────────────────────────────────────
# Repo-Root robust ermitteln: gehe nach oben, bis ein Ordner "kategorien" gefunden wird
# ──────────────────────────────────────────────────────────────────────────────
def _find_repo_root(start: str) -> str:
    d = os.path.abspath(start)
    for _ in range(5):  # max. 5 Ebenen nach oben
        if os.path.isdir(os.path.join(d, "kategorien")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    return os.path.abspath(os.path.join(os.path.dirname(start), ".."))

HERE = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = _find_repo_root(HERE)
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

# ──────────────────────────────────────────────────────────────────────────────
# Konfiguration / Defaults
# ──────────────────────────────────────────────────────────────────────────────
DIFFICULTY_WEIGHTS: Dict[str, Dict[int, int]] = {
    "schwer": {10: 16, 9: 17, 8: 21, 7: 16, 6: 11, 5: 9, 4: 6, 3: 4, 2: 0, 1: 0},
    "normal": {10: 0, 9: 0, 8: 10, 7: 10, 6: 14, 5: 18, 4: 16, 3: 12, 2: 10, 1: 10},
    "physik": {10: 3, 9: 5, 8: 8, 7: 10, 6: 14, 5: 18, 4: 16, 3: 12, 2: 8, 1: 6},
    "random": {10: 10, 9: 10, 8: 10, 7: 10, 6: 10, 5: 10, 4: 10, 3: 10, 2: 10, 1: 10},
}
SIM_THRESHOLD = 0.82  # Dedupe-Schwelle innerhalb dieses Runs

_SUBCATEGORY_ALIASES = [
    "subcategory", "subtopic", "sub_topic",
    "subdiscipline", "sub_discipline",
    "unterkategorie", "unter_kategorie",
]

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ──────────────────────────────────────────────────────────────────────────────
# Utils
# ──────────────────────────────────────────────────────────────────────────────
def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "")).strip().lower()

def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, _norm(a), _norm(b)).ratio()

def is_duplicate(candidate_q: str, corpus: List[str], threshold: float = SIM_THRESHOLD) -> bool:
    cand = _norm(candidate_q)
    for q in corpus:
        if similarity(cand, q) >= threshold:
            return True
    return False

def weighted_choice(weights: Dict[int, int]) -> int:
    if not weights:
        return 5
    items = sorted(weights.items(), key=lambda x: x[0])
    keys = [k for k, _ in items]
    vals = [w for _, w in items]
    return random.choices(keys, weights=vals, k=1)[0]

def pick_target_difficulty_for_mode(mode: str) -> int:
    weights = DIFFICULTY_WEIGHTS.get(mode) or DIFFICULTY_WEIGHTS["normal"]
    return int(weighted_choice(weights))

def _harmonize_question_metadata(q: dict) -> None:
    if not isinstance(q, dict):
        return
    if "subcategory" not in q:
        for k in _SUBCATEGORY_ALIASES:
            v = q.get(k)
            if isinstance(v, str) and v.strip():
                q["subcategory"] = v.strip()
                break

def _strip_letter_prefix(s: str) -> str:
    return re.sub(r"^[A-D]\s*[:\)\]\.-]\s*", "", s.strip(), flags=re.IGNORECASE)

def _apply_letter_prefixes(choices: List[str]) -> List[str]:
    return [f"{LETTERS[i]}: {choices[i]}" for i in range(len(choices))]

def _shuffle_answers_in_question(q: dict) -> None:
    field = None
    if isinstance(q.get("choices"), list):
        field = "choices"
    elif isinstance(q.get("options"), list):
        field = "options"
    elif isinstance(q.get("answers"), list):
        field = "answers"
    if not field:
        return

    opts = list(q[field])
    if not opts:
        return

    correct_idx = None
    for k in ("answer_index", "correct_index", "correctIndex"):
        if isinstance(q.get(k), int):
            correct_idx = q[k]
            break

    if correct_idx is None and isinstance(q.get("correct_answer"), str):
        try:
            correct_idx = LETTERS.index(q["correct_answer"].strip().upper())
        except ValueError:
            pass

    if correct_idx is None and isinstance(opts[0], dict) and "correct" in opts[0]:
        correct_idx = next((i for i, c in enumerate(opts) if c.get("correct")), None)

    if correct_idx is None or not (0 <= correct_idx < len(opts)):
        return

    def normalize_choice(x):
        if isinstance(x, str):
            return _strip_letter_prefix(x)
        if isinstance(x, dict) and "text" in x:
            return _strip_letter_prefix(str(x["text"]))
        return x

    normalized = [normalize_choice(x) for x in opts]
    idxs = list(range(len(opts)))
    random.shuffle(idxs)
    new_correct = idxs.index(correct_idx)

    if isinstance(opts[0], dict) and "correct" in opts[0]:
        new_opts = []
        for i, old_i in enumerate(idxs):
            item = dict(opts[old_i])
            if "text" in item:
                item["text"] = normalized[old_i]
            item["correct"] = (i == new_correct)
            new_opts.append(item)
        q[field] = new_opts
    else:
        relabeled = _apply_letter_prefixes([normalized[old_i] for old_i in idxs])
        q[field] = relabeled

    q["answer_index"] = new_correct
    q["correct_index"] = new_correct
    q["correctIndex"] = new_correct
    q["correct_answer"] = LETTERS[new_correct]

# ──────────────────────────────────────────────────────────────────────────────
# Archiv (kategorieweise) - analog zu generate_quiz.py
# ──────────────────────────────────────────────────────────────────────────────
ARCHIVE_DIRS = {
    "normal": "Fragen leicht",
    "schwer": "Fragen schwer",
}

def _sanitize_filename(name: str) -> str:
    """Rudimentär: Leerzeichen -> Unterstrich; nur Buchstaben/Ziffern/_/-/Umlaute/ß"""
    base = re.sub(r"\s+", "_", name.strip())
    base = re.sub(r"[^A-Za-z0-9_\-ÄÖÜäöüß]", "", base)
    return base or "Unbekannt"

def _load_json_list(path: str) -> List[dict]:
    """Lädt existierende Fragen aus einer JSON-Datei."""
    if not os.path.exists(path):
        return []
    try:
        data = json.load(open(path, "r", encoding="utf-8"))
        if isinstance(data, dict) and isinstance(data.get("questions"), list):
            return list(data["questions"])
        if isinstance(data, list):
            return list(data)
    except Exception:
        pass
    return []

def _save_json_list(path: str, category_name: str, questions: List[dict]) -> None:
    """Speichert Fragen in eine kategorieweise JSON-Datei."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    payload = {
        "category": category_name,
        "questions": questions,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

def _append_questions_to_category_file(questions: List[dict], category_name: str, mode: str) -> None:
    """
    Hängt Fragen kategorieweise in ARCHIVE_DIRS[mode] an.
    - Nur für Modi 'normal' und 'schwer'
    - Bewahrt bisherigen Inhalt; einfache Dedupe pro Datei (identische question+category)
    """
    archive_root = ARCHIVE_DIRS.get(mode)
    if not archive_root:
        return

    fname = f"{_sanitize_filename(category_name)}.json"
    fpath = os.path.join(archive_root, fname)

    existing = _load_json_list(fpath)

    # Dedupe: keine identischen Frage-Texte in gleicher Kategorie
    seen = {(_norm(x.get("question", "")), _norm(x.get("category", ""))) for x in existing}
    merged = list(existing)
    for q in questions:
        key = (_norm(q.get("question", "")), _norm(q.get("category", "")))
        if key in seen:
            continue
        merged.append(q)
        seen.add(key)

    _save_json_list(fpath, category_name, merged)
    print(f"📁 Archiviert: {len(merged) - len(existing)} neue Fragen → {fpath}")

# ──────────────────────────────────────────────────────────────────────────────
# Plugin Discovery
# ──────────────────────────────────────────────────────────────────────────────
def discover_category_plugins() -> Dict[str, callable]:
    plugins: Dict[str, callable] = {}
    try:
        import kategorien  # package
    except Exception as e:
        print("[DISCOVERY] Paket 'kategorien' nicht gefunden:", e)
        return plugins

    pkgpath = getattr(kategorien, "__path__", None)
    if not pkgpath:
        return plugins

    for _, modname, ispkg in pkgutil.iter_modules(pkgpath):
        if ispkg:
            continue
        fqmn = f"kategorien.{modname}"
        try:
            mod = importlib.import_module(fqmn)
        except Exception as e:
            print(f"[PLUGIN-IMPORT-ERROR] {fqmn}: {e}")
            traceback.print_exc()
            print("sys.path head:", sys.path[:5])
            continue
        fn = getattr(mod, "generate_one", None)
        if callable(fn):
            plugins[modname.lower()] = fn
    return plugins

# ──────────────────────────────────────────────────────────────────────────────
# Generator
# ──────────────────────────────────────────────────────────────────────────────
def generate_only_category(category_key: str, count: int, mode: str, do_shuffle: bool) -> Dict:
    plugins = discover_category_plugins()
    if category_key not in plugins:
        raise SystemExit(f"❌ Kategorie-Plugin '{category_key}' nicht gefunden. Verfügbare: {sorted(plugins.keys())}")

    gen = plugins[category_key]
    out: List[dict] = []
    seen_texts: List[str] = []

    tries, max_tries = 0, count * 10
    while len(out) < count and tries < max_tries:
        tries += 1
        target_diff = pick_target_difficulty_for_mode(mode)
        try:
            q = gen(past_texts=[], target_difficulty=target_diff, mode=mode)
        except Exception as e:
            print(f"[WARN] Fehler in {category_key}: {e}")
            continue
        if not q:
            continue

        q.setdefault("difficulty", int(target_diff))
        q.setdefault("category", category_key)
        _harmonize_question_metadata(q)

        qt = q.get("question", "")
        if not isinstance(qt, str) or not qt.strip():
            continue
        if is_duplicate(qt, seen_texts, SIM_THRESHOLD):
            continue

        if do_shuffle:
            try:
                _shuffle_answers_in_question(q)
            except Exception:
                pass

        out.append(q)
        seen_texts.append(qt)

    payload = {
        "category": category_key,
        "mode": mode,
        "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "count": len(out),
        "questions": out,
    }
    return payload

# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(description="Generate only one category into a single JSON file.")
    ap.add_argument("-c", "--category", default="natur", help="Plugin key (module name) under ./kategorien/, e.g. 'natur'")
    ap.add_argument("-n", "--count", type=int, default=20, help="Number of questions to generate")
    ap.add_argument("-m", "--mode", default="normal", choices=["normal", "schwer", "physik", "random"], help="Difficulty profile")
    ap.add_argument("-o", "--out", default=None, help="Output path for JSON (default: out/<category>.<count>.<date>.json)")
    ap.add_argument("--shuffle", action="store_true", help="Shuffle answers within this run")
    ap.add_argument("--list", action="store_true", help="List available category plugins and exit")
    args = ap.parse_args()

    if args.list:
        plugins = discover_category_plugins()
        print("Available plugins:", ", ".join(sorted(plugins.keys())) or "(none)")
        return

    if args.out:
        out_path = args.out
    else:
        os.makedirs("out", exist_ok=True)
        stamp = datetime.now().strftime("%Y-%m-%d")
        out_path = os.path.join("out", f"{args.category}.{args.count}.{stamp}.json")

    out_dir = os.path.dirname(out_path) or "."
    os.makedirs(out_dir, exist_ok=True)

    if not os.environ.get("OPENAI_API_KEY"):
        print("⚠️  Hinweis: OPENAI_API_KEY ist nicht gesetzt. Plugins, die die OpenAI API nutzen, werden fehlschlagen.")

    payload = generate_only_category(args.category.lower(), args.count, args.mode, args.shuffle)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"✅ fertig: {out_path}  (Fragen: {payload['count']})")

    # NEU: Archivierung in Fragenordner (nur für normal/schwer)
    if args.mode in ("normal", "schwer"):
        try:
            _append_questions_to_category_file(
                payload["questions"], 
                args.category, 
                args.mode
            )
        except Exception as e:
            print(f"⚠️  Archivierung fehlgeschlagen: {e}")

if __name__ == "__main__":
    main()
