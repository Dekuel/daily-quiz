# -*- coding: utf-8 -*-
# Unterkategorien/Sport/fußball.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Fußball“ – *angepasste Schwierigkeitsintervalle*.
Die Anpassung folgt der Regel: 2→+1, 3→+2, 4–9→+3, Deckel bei 10 (1 und 10 unverändert).
"""

SUBDISCIPLINES = [
    # 1 Allgemeines & Grundlagen
    ('Fußball: Grundbegriffe, Feld, Positionen', 4, (1, 10)),
    ('Regeln & Schiedsrichterwesen (inkl. Abseits, VAR)', 4, (1, 10)),
    ('Taktiken & Formationen (4-3-3, 4-2-3-1, Pressingarten)', 3, (5, 10)),
    ('Statistiken & Analytics (xG, PPDA, Zonen, Set-Pieces)', 3, (8, 10)),
    ('Geschichte des Fußballs (Ursprünge, IFAB, Professionalisierung)', 3, (3, 10)),
    ('Stadien, Spielfeldmaße & Infrastruktur', 2, (1, 10)),
    ('Transfers, Marktwerte & Financial Fairplay', 2, (3, 10)),
    ('Fan-Kultur, Rivalitäten & Derbys', 2, (1, 10)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ('Fußball – Basisfakten (Begriffe, Spielfeld, Trikotnummern, Pokalnamen)', 2, (1, 10)),

    # 2 Rekorde & Funfacts
    ('Rekorde (Tore, Titel, Serien, Alters-/Geschwindigkeitsrekorde)', 3, (1, 10)),
    ('Funfacts & Kurioses (Spitznamen, Maskottchen, legendäre Szenen)', 2, (1, 10)),

    # 3 Nationalmannschaften (allgemein)
    ('Nationalmannschaften: Struktur, FIFA/UEFA/CONMEBOL', 4, (3, 10)),
    ('Turniere der Nationalteams (EM, Copa América, AFCON, Asien-/Gold-Cup)', 3, (3, 10)),
    # ⚑ einfache Kategorie
    ('Nationalmannschaften – Basis (Flaggen, Spitznamen, Trikotfarben)', 2, (1, 10)),

    # 4 Weltmeisterschaften
    ('FIFA-Weltmeisterschaften – Historie & Siegerlisten', 4, (1, 10)),
    ('Weltmeisterschaften – Stars, Torschützenkönige, Rekordspiele', 3, (3, 10)),
    ('Weltmeisterschaften – Taktiktrends & Innovationen', 3, (7, 10)),
    # ⚑ einfache Kategorie
    ('Weltmeisterschaften – Basis (Gastgeber, Endspiel-Orte, Pokal)', 2, (1, 10)),

    # 5 UEFA Champions League
    ('Champions League – Geschichte & Modus', 4, (3, 10)),
    ('Champions League – Rekorde & Meilensteine', 3, (3, 10)),
    ('Champions League – legendäre Spiele & Finalserien', 3, (5, 10)),
    # ⚑ einfache Kategorie
    ('Champions League – Basis (Hymne, Pokalname, Gruppen/K.-o.-Phase)', 2, (1, 10)),

    # 6 Bundesliga (Deutschland)
    ('Bundesliga – Geschichte, Modus & DFL', 4, (3, 10)),
    ('Bundesliga – Vereine, Stadien & Derbys', 3, (1, 10)),
    ('Bundesliga – Rekorde (Meister, Tore, Serien)', 3, (3, 10)),
    ('DFB-Pokal & Supercup', 2, (1, 10)),
    # ⚑ einfache Kategorie
    ('Bundesliga – Basis (Gründungsjahr, Schale, Traditionsklubs)', 2, (1, 10)),

    # 7 Premier League (England)
    ('Premier League – Geschichte & Modus', 4, (3, 10)),
    ('Premier League – Vereine, Stadien & Rivalitäten', 3, (1, 10)),
    ('Premier League – Rekorde & Ikonen', 3, (3, 10)),
    # ⚑ einfache Kategorie
    ('Premier League – Basis (Logo, Ball, Boxing Day)', 2, (1, 10)),

    # 8 LaLiga (Spanien)
    ('LaLiga – Geschichte & Modus', 4, (3, 10)),
    ('LaLiga – Vereine, Stadien & Clásicos/Derbies', 3, (1, 10)),
    ('LaLiga – Rekorde & Ikonen', 3, (3, 10)),
    # ⚑ einfache Kategorie
    ('LaLiga – Basis (Trophäe, Spitznamen, Copa del Rey)', 2, (1, 10)),

    # 9 Serie A (Italien)
    ('Serie A – Geschichte & Modus', 4, (3, 10)),
    ('Serie A – Vereine, Stadien & Rivalitäten', 3, (1, 10)),
    ('Serie A – Rekorde & Ikonen', 3, (3, 10)),
    # ⚑ einfache Kategorie
    ('Serie A – Basis (Scudetto, Coppa Italia, Derby d\'Italia)', 2, (1, 10)),

    # 10 Sonstige Ligen (Auswahl)
    ('Sonstige Ligen – Ligue 1 (Frankreich): Geschichte, Vereine, Rekorde', 3, (3, 10)),
    ('Sonstige Ligen – Eredivisie (NLD), Primeira Liga (POR)', 2, (3, 10)),
    ('Sonstige Ligen – Südeuropa & Osteuropa (Türkei, Griechenland, Balkans)', 2, (5, 10)),
    ('Sonstige Ligen – MLS (USA/Kanada), Liga MX (MEX)', 2, (5, 10)),
    ('Sonstige Ligen – Brasilien/Argentinien (Brasileirão, Primera División)', 3, (5, 10)),
    ('Sonstige Ligen – Asien & Afrika (J1 League, K League, CAF-Ligen)', 2, (5, 10)),
    # ⚑ einfache Kategorie (Sammelzuordnung)
    ('Ligen – Basis (Länderzuordnung, Trophäennamen, Verbände)', 2, (1, 10)),

    # 11 Pokal- & Europawettbewerbe (weitere)
    ('Europa League & Conference League – Modus, Rekorde', 3, (3, 10)),
    ('UEFA-Supercup & Klub-WM', 2, (3, 10)),

    # 12 Frauenfußball
    ('Frauenfußball – Weltmeisterschaften & EM', 3, (3, 10)),
    ('Frauenfußball – Ligen & Rekorde (z. B. Frauen-Bundesliga, NWSL, WSL)', 2, (3, 10)),
    # ⚑ einfache Kategorie
    ('Frauenfußball – Basis (Pokalnamen, Ikonische Spielerinnen)', 2, (1, 10)),

    # 13 Deutschland – Nationalteam (Beispiel-Detailtiefe)
    ('DFB-Team – Geschichte & Turniere', 3, (3, 10)),
    ('DFB-Team – Spielerlegenden & Trainer', 2, (3, 10)),
    # ⚑ einfache Kategorie
    ('DFB-Team – Basis (Adler, Trikotfarben, Spitzname)', 2, (1, 10)),

    # 14 Schiedsrichter, Regeln & Verbände
    ('IFAB & Regelhistorie (inkl. Hands-/Abseitsinterpretation)', 3, (7, 10)),
    ('VAR, Torlinientechnik & Technologien', 3, (6, 10)),

    # 15 Medizin, Training & Nachwuchs
    ('Sportmedizin & Verletzungen (ACL, Muskelverletzungen, Return-to-Play)', 2, (5, 10)),
    ('Trainingslehre & Periodisierung (Mikro-/Meso-/Makrozyklen)', 3, (7, 10)),
    ('Nachwuchs & Akademien (Talentsichtung, U-Teams, Leihsysteme)', 2, (3, 10)),

    # 16 Ökonomie & Recht
    ('Vereinsstrukturen, 50+1, Eigner-/Mitgliedermodelle', 2, (5, 10)),
    ('Sponsoring, Medienrechte & Stadionfinanzierung', 2, (5, 10)),

    # 17 Taktik-Vertiefungen
    ('Pressing-/Gegenpressing-Modelle & Aufbauzonen', 3, (8, 10)),
    ('Standards (Ecken/Freistöße) – Muster & Varianten', 3, (7, 10)),
    ('Positionsspiel & Rollen (Inverted Fullback, Regista, Raumdeuter)', 3, (8, 10)),

    # 18 Daten & Analyse-Vertiefung
    ('Metriken & Modelle (xG/xA, Non-shot xG, xT, Packing)', 3, (9, 10)),
    ('Scouting & Datenrekrutierung (KPIs, Alterskurven)', 2, (7, 10)),

    # 19 Kultur, Medien & Gesellschaft
    ('Fankultur & Ultras, Choreos, Hymnen', 2, (1, 10)),
    ('Fußball & Politik/Gesellschaft (WM-Vergaben, Menschenrechte)', 2, (5, 10)),
    ('Journalismus & Kommentartraditionen', 2, (1, 10)),

    # 20 Gaming & Sonstiges
    ('eFootball/Simulationen (Karrieremodus, Ultimate Team, Taktik-Meta)', 2, (1, 10)),
    ('Schiedsrichterzeichen & Kommunikation', 2, (3, 10)),

    # ⚑ globale Sammel-Basis (Level-1 möglich)
    ('Fußball – Weltweit Basis: Trophäenformen, Vereinswappen, Spitznamen, Derbys', 2, (1, 10)),
]
