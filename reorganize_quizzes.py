import os
import shutil
from pathlib import Path

# Basis-Verzeichnis
quizzes_dir = Path(__file__).parent / "quizzes"

# Alle Verzeichnisse im quizzes-Ordner durchgehen
for item in quizzes_dir.iterdir():
    if item.is_dir() and item.name.startswith("2025-"):
        # Datum parsen (Format: 2025-10-27)
        date_parts = item.name.split("-")
        if len(date_parts) == 3:
            year, month, day = date_parts
            
            # Neuen Pfad erstellen: quizzes/2025/10/27/
            new_path = quizzes_dir / year / month / day
            new_path.mkdir(parents=True, exist_ok=True)
            
            # Alle Dateien aus dem alten Ordner in den neuen verschieben
            for file in item.iterdir():
                shutil.move(str(file), str(new_path / file.name))
                print(f"Moved: {file.name} -> {new_path}")
            
            # Alten Ordner löschen
            item.rmdir()
            print(f"Removed old directory: {item.name}")

print("\nReorganization complete!")
print("\nNew structure:")
# Zeige die neue Struktur
for year_dir in sorted(quizzes_dir.iterdir()):
    if year_dir.is_dir() and year_dir.name.isdigit():
        print(f"  {year_dir.name}/")
        for month_dir in sorted(year_dir.iterdir()):
            if month_dir.is_dir():
                day_count = len([d for d in month_dir.iterdir() if d.is_dir()])
                print(f"    {month_dir.name}/ ({day_count} days)")
