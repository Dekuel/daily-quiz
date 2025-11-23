"""
Test-Script um die neue Ordnerstruktur zu validieren.
"""
import os
import json
from pathlib import Path

# Prüfe die neue Struktur
quizzes_dir = Path(__file__).parent / "quizzes"

print("=== Neue Ordnerstruktur ===")
print(f"Quizzes-Verzeichnis: {quizzes_dir}\n")

# Zähle Dateien in der neuen Struktur
total_days = 0
total_files = 0

if quizzes_dir.exists():
    for year_dir in sorted(quizzes_dir.iterdir()):
        if year_dir.is_dir() and year_dir.name.isdigit():
            print(f"📅 Jahr {year_dir.name}:")
            for month_dir in sorted(year_dir.iterdir()):
                if month_dir.is_dir() and month_dir.name.isdigit():
                    days = [d for d in month_dir.iterdir() if d.is_dir() and d.name.isdigit()]
                    day_count = len(days)
                    total_days += day_count
                    
                    # Zähle Dateien pro Monat
                    files_in_month = 0
                    for day_dir in days:
                        files_in_day = len([f for f in day_dir.iterdir() if f.is_file() and f.suffix == '.json'])
                        files_in_month += files_in_day
                    
                    total_files += files_in_month
                    print(f"  Monat {month_dir.name}: {day_count} Tage, {files_in_month} JSON-Dateien")

print(f"\n📊 Gesamt: {total_days} Tage mit {total_files} JSON-Dateien")

# Prüfe latest.json
latest_path = quizzes_dir / "latest.json"
if latest_path.exists():
    print("\n=== latest.json ===")
    try:
        latest = json.load(open(latest_path, 'r', encoding='utf-8'))
        print(f"Letztes Datum: {latest.get('latest_date')}")
        print("Pfade:")
        for mode, path in latest.get('paths', {}).items():
            print(f"  {mode}: {path}")
            # Prüfe ob Datei existiert
            full_path = quizzes_dir.parent / path
            exists = "✅" if full_path.exists() else "❌"
            print(f"    {exists} Existiert: {full_path.exists()}")
    except Exception as e:
        print(f"Fehler beim Lesen von latest.json: {e}")

# Prüfe catalog.json
catalog_path = quizzes_dir / "catalog.json"
if catalog_path.exists():
    print("\n=== catalog.json ===")
    try:
        catalog = json.load(open(catalog_path, 'r', encoding='utf-8'))
        print(f"Anzahl Einträge: {len(catalog)}")
        print(f"Neuester Eintrag: {catalog[0].get('date') if catalog else 'N/A'}")
        print(f"Ältester Eintrag: {catalog[-1].get('date') if catalog else 'N/A'}")
    except Exception as e:
        print(f"Fehler beim Lesen von catalog.json: {e}")

print("\n✅ Struktur-Check abgeschlossen!")
