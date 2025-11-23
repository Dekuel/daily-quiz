"""
Aktualisiert latest.json und catalog.json für die neue Ordnerstruktur.
Ändert Pfade von quizzes/2025-11-08/ zu quizzes/2025/11/08/
"""
import json
import os
from pathlib import Path

def convert_path(old_path):
    """Konvertiert alte Pfadstruktur zu neuer."""
    if not old_path.startswith('quizzes/'):
        return old_path
    
    # Entferne 'quizzes/' Prefix
    remainder = old_path[8:]  # len('quizzes/') = 8
    
    # Suche nach Datum-Pattern: YYYY-MM-DD
    parts = remainder.split('/')
    if len(parts) > 0:
        date_part = parts[0]
        if '-' in date_part and len(date_part) == 10:  # YYYY-MM-DD Format
            year, month, day = date_part.split('-')
            # Rekonstruiere Pfad mit neuer Struktur
            new_remainder = '/'.join([year, month, day] + parts[1:])
            return f'quizzes/{new_remainder}'
    
    return old_path

# Verarbeite latest.json
quizzes_dir = Path(__file__).parent / "quizzes"
latest_path = quizzes_dir / "latest.json"

if latest_path.exists():
    print("=== Aktualisiere latest.json ===")
    try:
        latest = json.load(open(latest_path, 'r', encoding='utf-8'))
        
        # Aktualisiere Pfade
        if 'paths' in latest and isinstance(latest['paths'], dict):
            updated = False
            for mode, path in latest['paths'].items():
                new_path = convert_path(path)
                if new_path != path:
                    print(f"  {mode}: {path} -> {new_path}")
                    latest['paths'][mode] = new_path
                    updated = True
            
            if updated:
                with open(latest_path, 'w', encoding='utf-8') as f:
                    json.dump(latest, f, ensure_ascii=False, indent=2)
                print("✅ latest.json aktualisiert")
            else:
                print("ℹ️ Keine Änderungen nötig in latest.json")
    except Exception as e:
        print(f"❌ Fehler: {e}")

# Verarbeite catalog.json
catalog_path = quizzes_dir / "catalog.json"

if catalog_path.exists():
    print("\n=== Aktualisiere catalog.json ===")
    try:
        catalog = json.load(open(catalog_path, 'r', encoding='utf-8'))
        
        updated = False
        for entry in catalog:
            if 'paths' in entry and isinstance(entry['paths'], dict):
                for mode, path in entry['paths'].items():
                    new_path = convert_path(path)
                    if new_path != path:
                        entry['paths'][mode] = new_path
                        updated = True
        
        if updated:
            with open(catalog_path, 'w', encoding='utf-8') as f:
                json.dump(catalog, f, ensure_ascii=False, indent=2)
            print(f"✅ catalog.json aktualisiert ({len(catalog)} Einträge)")
        else:
            print("ℹ️ Keine Änderungen nötig in catalog.json")
    except Exception as e:
        print(f"❌ Fehler: {e}")

print("\n✅ Update abgeschlossen!")
