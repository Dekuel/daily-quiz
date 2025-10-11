# -*- coding: utf-8 -*-
"""
Daily Quiz Generator (zweimodig):
- Modi: "normal" und "schwer"
- Politik-Fragen werden pro Modus separat über das Politik-Plugin generiert (Ziel: 2)
- Weitere Fragen über Kategorien-Plugins in ./kategorien/ (je Aufruf genau 1 Frage)
- Dedupe ggü. Vergangenheit (7 Tage), innerhalb eines Modus, und zwischen den Modi (tagesweit)
- Schwierigkeit pro Modus via Gewichten
- Persistenz:
  quizzes/YYYY-MM-DD/bundle.normal.json
  quizzes/YYYY-MM-DD/bundle.schwer.json
  latest.json -> { "latest_date": "...", "paths": {"normal": "...", "schwer": "..."} }
  catalog.json -> [{ "date": "...", "paths": {"normal": "...", "schwer": "..."} }, ...]
"""

from __future__ import annotations
import os
import re
import json
import random
import importlib
import pkgutil
from datetime import datetime, timezone, timedelta
from difflib import SequenceMatcher
from typing import Callable, Dict, List, Optional

# ===================== Konfiguration =====================

OUT_ROOT = "quizzes"
PAST_DAYS_TO_CHECK = 7

# Wie viele Politikfragen pro Modus?
POLITICS_TARGET = 2

# Wie viele Nicht-Politik-Kategorien pro Modus?
RANDOM_SEGMENTS_PER_DAY = 3

# Kategorie-Name des Politik-Plugins
POLITICS_CATEGORY_NAME = "Politik"

# Schwierigkeit-Gewichte (Schlüssel = Difficulty 1..10, Wert = Gewicht)
DIFFICULTY_WEIGHTS: Dict[str, Dict[int, int]] = {
    # vom Nutzer vorgegeben
    "schwer": {10: 13, 9: 15, 8: 20, 7: 17, 6: 11, 5: 9, 4: 6, 3: 4, 2: 3, 1: 2},
    # Vorschlag für "normal" (anpassbar)
    "normal": {10: 3, 9: 5, 8: 8, 7: 10, 6: 14, 5: 18, 4: 16, 3: 12, 2: 8, 1: 6},
}

# Text-Ähnlichkeitsschwelle für Dedupe
SIM_THRESHOLD = 0.82


# ===================== Utilities =====================

def _iso_date_today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "")).strip().lower()


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, _norm(a), _norm(b)).ratio()


def is_duplicate(candidate_q: str, corpus_questions: List[str], threshold: float = SIM_THRESHOLD) -> bool:
    cand = _norm(candidate_q)
    for q in corpus_questions:
        if similarity(cand, q) >= threshold:
            return True
    return False


def weighted_choice(weights: Dict[int, int]) -> int:
    # weights: {difficulty: weight}
    if not weights:
        return 5
    # sort optional – nicht notwendig für random.choices, aber deterministischer
    items = sorted(weights.items(), key=lambda x: x[0])
    keys = [k for k, _ in items]
    vals = [w for _, w in items]
    return random.choices(keys, weights=vals, k=1)[0]


# ===================== Vergangenheit laden =====================

def load_past_questions(days: int = PAST_DAYS_TO_CHECK) -> List[dict]:
    """
    Lädt Fragen aus bundle.json, bundle.normal.json, bundle.schwer.json der letzten N Tage.
    """
    past: List[dict] = []
    if not os.path.exists(OUT_ROOT):
        return past

    cutoff = datetime.now().date() - timedelta(days=days)
    dates = set()

    # bevorzugt catalog.json
    catalog_path = os.path.join(OUT_ROOT, "catalog.json")
    if os.path.exists(catalog_path):
        try:
            catalog = json.load(open(catalog_path, "r", encoding="utf-8"))
            for entry in catalog:
                try:
                    d = datetime.strptime(entry.get("date", ""), "%Y-%m-%d").date()
                    if d >= cutoff:
                        dates.add(entry["date"])
                except Exception:
                    continue
        except Exception:
            pass

    # Fallback: Verzeichnisse scannen
    if not dates:
        try:
            for name in os.listdir(OUT_ROOT):
                p = os.path.join(OUT_ROOT, name)
                try:
                    d = datetime.strptime(name, "%Y-%m-%d").date()
                    if d >= cutoff and os.path.isdir(p):
                        dates.add(name)
                except Exception:
                    continue
        except Exception:
            pass

    for d in sorted(dates, reverse=True):
        for fname in ("bundle.json", "bundle.normal.json", "bundle.schwer.json"):
            bundle_path = os.path.join(OUT_ROOT, d, fname)
            if os.path.exists(bundle_path):
                try:
                    bundle = json.load(open(bundle_path, "r", encoding="utf-8"))
                    past.extend(bundle.get("questions", []))
                except Exception:
                    continue

    return past


# ===================== Plugin Discovery =====================

def discover_category_plugins() -> Dict[str, Callable[..., Optional[dict]]]:
    """
    Findet alle Module in ./kategorien/ mit einer Funktion:
        generate_one(past_texts: list[str]) -> dict | None

    Rückgabe: Mapping { "Anzeigename": callable }
    - Anzeigename: mod.CATEGORY_NAME oder Dateiname -> Titelcase
    """
    plugins: Dict[str, Callable[..., Optional[dict]]] = {}
    try:
        import kategorien  # type: ignore
    except Exception:
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
        except Exception:
            continue
        fn = getattr(mod, "generate_one", None)
        if callable(fn):
            cname = getattr(mod, "CATEGORY_NAME", modname.replace("_", " ").title())
            plugins[cname] = fn
    return plugins


# ===================== Fragen-Generatoren =====================

def generate_random_categories(
    plugins: Dict[str, Callable[..., Optional[dict]]],
    k: int,
    past_texts: List[str],
    exclude: Optional[set[str]] = None,
) -> List[dict]:
    """
    Wählt k Kategorien (ohne exclude) und erzeugt jeweils eine Frage.
    Dedupe gegen Vergangenheit und innerhalb des Sets.
    """
    names = [n for n in plugins.keys() if not exclude or n not in exclude]
    if not names or k <= 0:
        return []

    # ziehe möglichst verschiedene Kategorien
    chosen = random.sample(names, k=min(k, len(names)))
    while len(chosen) < k:
        chosen.append(random.choice(names))

    out: List[dict] = []
    tries = 0
    while len(out) < k and tries < k * 6:
        cat = chosen[len(out)]
        tries += 1
        try:
            item = plugins[cat](past_texts=past_texts)  # -> dict | None
        except Exception:
            continue
        if not item:
            continue
        qt = _norm(item.get("question", ""))
        if not qt:
            continue
        if any(similarity(qt, x.get("question", "")) >= SIM_THRESHOLD for x in out):
            continue
        if is_duplicate(qt, past_texts, SIM_THRESHOLD):
            continue
        out.append(item)
    return out


def generate_politics_for_mode(
    plugins: Dict[str, Callable[..., Optional[dict]]],
    target: int,
    past_texts: List[str],
    day_seen: set[str],
) -> List[dict]:
    """
    Erzeugt bis zu 'target' Politikfragen für einen Modus.
    Dedupe: Vergangenheit, innerhalb dieses Sets, und 'day_seen' (andere Modi oder bereits erzeugte Fragen des Tages).
    """
    if POLITICS_CATEGORY_NAME not in plugins:
        return []

    out: List[dict] = []
    tries = 0
    while len(out) < target and tries < target * 6:
        tries += 1
        try:
            q = plugins[POLITICS_CATEGORY_NAME](past_texts=past_texts)
        except Exception:
            continue
        if not q:
            continue
        qt = _norm(q.get("question", ""))
        if not qt:
            continue
        if is_duplicate(qt, past_texts, SIM_THRESHOLD):
            continue
        if any(similarity(qt, x.get("question", "")) >= SIM_THRESHOLD for x in out):
            continue
        if any(similarity(qt, t) >= SIM_THRESHOLD for t in day_seen):
            continue
        out.append(q)

    return out


# ===================== Persistenz =====================

def write_daily_bundle(quiz_list: List[dict], mode: str, date_str: Optional[str] = None) -> Optional[str]:
    """
    Schreibt bundle.<mode>.json ins Tagesverzeichnis.
    Gibt den relative Pfad zurück oder None, wenn leer.
    """
    if not quiz_list:
        print(f"❌ Keine gültigen Quizfragen für Modus '{mode}'.")
        return None

    day = date_str or _iso_date_today()
    day_dir = os.path.join(OUT_ROOT, day)
    os.makedirs(day_dir, exist_ok=True)

    bundle = {
        "date": day,
        "generated_at": _now_iso(),
        "schema_version": 4,  # Multi-Modus + Plugins
        "mode": mode,
        "questions": quiz_list,
    }

    suffix = ".schwer.json" if mode == "schwer" else ".normal.json"
    bundle_path = os.path.join(day_dir, f"bundle{suffix}")
    with open(bundle_path, "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=2)

    print(f"✅ Bundle gespeichert ({mode}): {bundle_path}")
    return f"{OUT_ROOT}/{day}/bundle{suffix}"


def update_latest_and_catalog(paths_by_mode: Dict[str, str], date_str: Optional[str] = None) -> None:
    """
    Aktualisiert latest.json (mit beiden Pfaden) und catalog.json (Eintrag pro Datum mit beiden Pfaden).
    """
    day = date_str or _iso_date_today()

    # latest.json
    latest_path = os.path.join(OUT_ROOT, "latest.json")
    latest = {"latest_date": day, "paths": {}}
    if os.path.exists(latest_path):
        try:
            latest = json.load(open(latest_path, "r", encoding="utf-8"))
        except Exception:
            pass
    latest["latest_date"] = day
    latest.setdefault("paths", {}).update(paths_by_mode)
    with open(latest_path, "w", encoding="utf-8") as f:
        json.dump(latest, f, ensure_ascii=False, indent=2)
    print(f"➡️  latest.json aktualisiert: {latest_path}")

    # catalog.json
    catalog_path = os.path.join(OUT_ROOT, "catalog.json")
    catalog = []
    if os.path.exists(catalog_path):
        try:
            catalog = json.load(open(catalog_path, "r", encoding="utf-8"))
        except Exception:
            catalog = []
    # Eintrag ersetzen/ergänzen
    existing = next((e for e in catalog if e.get("date") == day), None)
    entry = existing or {"date": day, "paths": {}}
    entry["paths"].update(paths_by_mode)
    catalog = [e for e in catalog if e.get("date") != day] + [entry]
    catalog.sort(key=lambda e: e.get("date", ""), reverse=True)
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    print(f"🗂️  catalog.json aktualisiert: {catalog_path}")


# ===================== Orchestrierung =====================

def assign_difficulties(questions: List[dict], mode: str) -> None:
    weights = DIFFICULTY_WEIGHTS.get(mode) or DIFFICULTY_WEIGHTS["normal"]
    for q in questions:
        q["difficulty"] = int(weighted_choice(weights))


def main():
    # 0) Plugins laden
    plugins = discover_category_plugins()
    if not plugins:
        print("⚠️ Keine Plugins unter ./kategorien/ gefunden – keine Fragen generierbar.")
        return
    if POLITICS_CATEGORY_NAME not in plugins:
        print("⚠️ Politik-Plugin nicht gefunden – es werden keine Politikfragen generiert.")

    # 1) Vergangenheit (für Dedupe)
    past = load_past_questions(PAST_DAYS_TO_CHECK)
    past_texts = [q.get("question", "") for q in past if isinstance(q, dict)]

    # 2) Tagesweite Dedupe-Sammlung, um Duplikate zwischen den Modi zu vermeiden
    day_dedupe_texts: set[str] = set()

    # 3) pro Modus generieren und speichern
    saved_paths: Dict[str, str] = {}

    for mode in ("normal", "schwer"):
        # 3.1 Politik pro Modus separat
        politics = generate_politics_for_mode(
            plugins=plugins,
            target=POLITICS_TARGET,
            past_texts=past_texts,
            day_seen=day_dedupe_texts,
        )

        # 3.2 Random-Kategorien (ohne Politik)
        random_cats = generate_random_categories(
            plugins=plugins,
            k=RANDOM_SEGMENTS_PER_DAY,
            past_texts=past_texts,
            exclude={POLITICS_CATEGORY_NAME},
        )

        # 3.3 Zusammenführen
        qlist: List[dict] = politics + random_cats

        # 3.4 Optionaler Fallback: Wenn weniger als POLITICS_TARGET Politikfragen zustande kamen,
        #     fülle mit Nicht-Politik, damit die Gesamtzahl stabil bleibt.
        if len([q for q in qlist if q.get("category") == POLITICS_CATEGORY_NAME]) < POLITICS_TARGET:
            needed = POLITICS_TARGET - sum(1 for q in qlist if q.get("category") == POLITICS_CATEGORY_NAME)
            fillers = generate_random_categories(
                plugins=plugins,
                k=needed,
                past_texts=past_texts,
                exclude={POLITICS_CATEGORY_NAME},
            )
            qlist.extend(fillers)

        # 3.5 Tagesweites Dedupe-Set updaten
        for q in qlist:
            qt = _norm(q.get("question", ""))
            if qt:
                day_dedupe_texts.add(qt)

        # 3.6 Schwierigkeiten setzen
        assign_difficulties(qlist, mode)

        # 3.7 Persistieren
        saved = write_daily_bundle(qlist, mode=mode)
        if saved:
            saved_paths[mode] = saved

    # 4) latest.json + catalog.json aktualisieren
    if saved_paths:
        update_latest_and_catalog(saved_paths)


if __name__ == "__main__":
    main()
