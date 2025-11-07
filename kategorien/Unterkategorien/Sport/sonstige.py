# -*- coding: utf-8 -*-
# Unterkategorien/Sport/sonstiges.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Sonstige (Sport)“.
Diese Liste wird von kategorien/sport.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

Skala 1–10 (Kurzfassung):
1 = absolutes Grundwissen (≈ 95 % in DE)
2 = sehr einfaches Grundwissen
3 = einfache Fragen
4 = leichte Anwendung
5 = einfach–mittel (70–80 % schaffbar)
6 = mittlere Komplexität
7 = mittel–schwer
8 = schwer (vertieftes Verständnis nötig)
9 = Expertenwissen
10 = schwerstmöglich

Hinweise:
- „Basis…“-Kategorien erlauben min = 1 (Zuordnungen, Symbole, einfache Regeln).
- Zeitabhängige Fragen (aktuelle Meister, Topspieler:innen) sind **optional**:
  Sie sollen den Prompt inspirieren, aber nie zwingend aktuell-datumsgebunden sein.
- Fokus auf Regeln, Geschichte, Struktur, Methodik, Sportkultur.
"""

SUBTOPICS = [
    # 1 Sportübergreifendes Allgemeinwissen & Regelkunde
    ("Sportartenkunde allgemein: Spielfelder, Geräte, Grundbegriffe", 4, (5, 10)),
    ("Punktezähl- und Wertungssysteme in verschiedenen Sportarten (Übersicht)", 4, (7, 10)),
    ("Schiedsrichterzeichen & Regelauslegung (sportübergreifend)", 3, (8, 10)),
    ("Turnier- und Ligenformate: Round Robin, K.-o.-System, Setzlisten", 3, (5, 10)),
    ("Historische Entwicklungen: Profisport, Olympia, Kommerzialisierung", 3, (5, 10)),
    # ⚑ Basis
    ("Basiswissen Sport allgemein: Zuordnungen (Sportart → Ball/Gerät/Feld), einfache Regeln", 2, (1, 10)),

    # 2 Leichtathletik
    ("Leichtathletik: Laufdisziplinen – Startregeln, Bahnen, Fehlstart", 4, (5, 10)),
    ("Leichtathletik: Sprünge & Würfe – Geräte, Zonen, Versuchszählung", 4, (7, 10)),
    ("Mehrkämpfe (Sieben-/Zehnkampf): Disziplinfolge & Wertungsprinzip", 3, (8, 10)),
    ("Weltrekorde & historische Leistungen (z. B. Bolt, Heike Drechsler)", 2, (5, 10)),
    # ⚑ Basis
    ("Leichtathletik – Basisfakten (z. B. Distanzen, Balken, Sektorwinkel)", 2, (1, 10)),

    # 3 Schwimmen & Wassersport
    ("Schwimmen: Lagen, Wenden und Startregeln", 4, (5, 10)),
    ("Rudern & Kanu: Bootsklassen, Steuerung, Start-/Zielregeln", 3, (8, 10)),
    ("Wasserball: Grundregeln, Fouls, Zeitmanagement", 3, (7, 10)),
    ("Olympische Helden & Rekordschwimmer:innen (z. B. Phelps, Ledecky)", 2, (7, 10)),
    # ⚑ Basis
    ("Wassersport – Basisfakten (Beckenlängen, Lagen, typische Distanzen)", 2, (1, 10)),

    # 4 Rückschlagsportarten (ohne Tennis)
    ("Badminton: Zählweise, Aufschlagzonen, Fehler", 4, (5, 10)),
    ("Tischtennis: Sätze, Aufschlagregeln, Let/Netz, Beläge (Überblick)", 3, (7, 10)),
    ("Squash: Court, Auslinien, Let-/Stroke-Entscheidungen", 3, (8, 10)),
    ("Weltspitze & Rekordhalter:innen (Badminton, TT, Squash – Überblick)", 2, (7, 10)),
    # ⚑ Basis
    ("Rückschlag – Basis: Spielfelder & Schläger zuordnen", 2, (1, 10)),

    # 5 Wintersport
    ("Ski Alpin: Disziplinen (SL/RS/SG/Abfahrt/Kombi), Kurssetzung, Startintervalle", 3, (7, 10)),
    ("Skispringen: Anlauf, K-Punkt/HS, Haltungsnoten & Windkompensation", 4, (8, 10)),
    ("Biathlon: Strafrunde/Strafzeit, Schießserien, Liegendschießen vs. Stehend", 4, (7, 10)),
    ("Berühmte Athlet:innen & aktuelle Weltcup-Serien (zeitunabhängig beschrieben)", 2, (7, 10)),
    # ⚑ Basis
    ("Wintersport – Basisfakten (Disziplinen, Ausrüstung, einfache Regeln)", 2, (1, 10)),

    # 6 Kampfsport & Gewichtsklassen
    ("Judo & Ringen: Wertungen, Mattenregeln", 3, (8, 10)),
    ("Boxen & Kickboxen: Runden, Punkterichter, Schutzvorschriften", 3, (8, 10)),
    ("Taekwondo/Karate: Trefferzonen, Strafkatalog (Überblick)", 2, (9, 10)),
    ("Weltmeister:innen & berühmte Kämpfer:innen (zeitlos-historisch)", 2, (7, 10)),
    # ⚑ Basis
    ("Kampfsport – Basis: Gürtel-/Graduierungssysteme & Gewichtsklassen", 2, (1, 10)),

    # 7 Handball
    ("Handball: Schrittregel, Zeitspiel, 7-Meter-Regel", 4, (7, 10)),
    ("Handball: Positionen, Abwehr-/Angriffssysteme", 3, (8, 10)),
    ("Turniergeschichte, Top-Nationen & Champions-League", 2, (7, 10)),
    # ⚑ Basis
    ("Handball – Basisfakten (Spielerzahl, Feldgröße, Tore, einfache Regeln)", 2, (1, 10)),

    # 8 Volleyball
    ("Volleyball: Rotationssystem, Rally-Point-Scoring", 4, (7, 10)),
    ("Volleyball: Block & Angriff – Technik & Fehler", 3, (8, 10)),
    ("Internationale Wettbewerbe & bekannte Spieler:innen (zeitlos)", 2, (7, 10)),
    # ⚑ Basis
    ("Volleyball – Basisfakten (Punkte, Feldgröße, Positionen)", 2, (1, 10)),

    # 9 Rugby
    ("Rugby Union vs. Rugby League: Regelunterschiede & Wertung", 4, (8, 10)),
    ("Rugby: Spielfluss, Tackling, Try-Wertung", 3, (8, 10)),
    ("Rugby: WM-Tradition & ikonische Teams (All Blacks, Springboks, England)", 2, (7, 10)),
    # ⚑ Basis
    ("Rugby – Basisfakten (Spielerzahl, Ballform, Punktarten)", 2, (1, 10)),

    # 10 Baseball / Softball
    ("Baseball: Innings, Strikes/Balls, Force/Tag Plays", 3, (7, 10)),
    ("Softball: Unterschiede zu Baseball, Spielfeldgröße, Regeln", 3, (8, 10)),
    ("MLB & historische Ikonen (Babe Ruth, Jackie Robinson, Ohtani)", 2, (8, 10)),
    # ⚑ Basis
    ("Baseball/Softball – Basis: Feldaufbau & Grundbegriffe", 2, (1, 10)),

    # 11 Eishockey
    ("Eishockey: Zonen, Abseits, Icing", 3, (7, 10)),
    ("Eishockey: Strafen, Powerplay & Wechselregeln", 3, (8, 10)),
    ("Ligen & Rekordspieler (z. B. NHL-Legenden, Stanley-Cup-Historie)", 2, (8, 10)),
    # ⚑ Basis
    ("Eishockey – Basisfakten (Puck, Drittel, Spielerzahl, Spielfeld)", 2, (1, 10)),

    # 12 Sportmedizin, Training & Anti-Doping
    ("Trainingslehre: Ausdauer-/Kraft-/Schnelligkeitstraining", 4, (5, 10)),
    ("Sporternährung: Makronährstoffe, Regeneration", 3, (3, 10)),
    ("Anti-Doping: WADA-Code, Testverfahren", 3, (9, 10)),
    ("Erfolgsfaktoren & Leistungsdiagnostik (VO2max, Laktat, Taktiktraining)", 3, (7, 10)),
    # ⚑ Basis
    ("Gesund & fair – Basis: Aufwärmen, Cool-down, Fair-Play-Grundsätze", 2, (1, 10)),

    # 13 Inklusion & Parasport
    ("Paralympischer Sport: Klassifikationsprinzipien", 3, (8, 10)),
    ("Adaptiver Sport & Inklusion: Regelanpassungen, Geräte", 2, (7, 10)),
    ("Berühmte Athlet:innen im Parasport (zeitlos)", 2, (7, 10)),
    # ⚑ Basis
    ("Parasport – Basisfakten (Kategorien, Hilfsmittel, einfache Zuordnungen)", 2, (1, 10)),

    # 14 Schach
    ("Schach: Grundregeln, Figuren und Züge", 4, (3, 10)),
    ("Schach: Eröffnungen, Mittelspielprinzipien, Mattbilder", 3, (7, 10)),
    ("Schach: Zeitformate, Notation, Taktikmotive", 3, (8, 10)),
    ("Berühmte Weltmeister & aktuelle Spitzenspieler:innen (zeitlos-historisch)", 2, (7, 10)),
    # ⚑ Basis
    ("Schach – Basisfakten (Brettaufbau, Figurenbewegungen, Ziel des Spiels)", 2, (1, 10)),

    # 15 Technik, Organisation & Großereignisse
    ("Zeitnahme & Fotofinish: Messgenauigkeit, Fehlstartsensorik", 3, (8, 10)),
    ("Video-/Technikhilfen: VAR, Hawk-Eye, Challenge-Systeme", 3, (8, 10)),
    ("Sportverbände & Wettbewerbsstrukturen (national/international)", 3, (7, 10)),
    ("Mega-Events: Bewerbungsverfahren, Austragungsformate, Nachhaltigkeit", 2, (8, 10)),
    ("Aktuelle Meister & Titelträger:innen (optionaler Kontext, nicht tagesgebunden)", 2, (7, 10)),
    # ⚑ Basis
    ("Organisation – Basis: Verband → Sportart/Disziplin zuordnen", 2, (1, 10)),
]
