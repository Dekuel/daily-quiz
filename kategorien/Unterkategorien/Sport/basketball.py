# -*- coding: utf-8 -*-
# Unterkategorien/Sport/basketball.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Basketball“.
Diese Liste wird von kategorien/sport.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

Schwierigkeiten wurden gemäß Algorithmus angepasst:
(2→3, 3→5, 4–9→+3, 10 bleibt 10; 1 bleibt 1)

Hinweise:
- „Basis…“-Kategorien erlauben min = 1 (Zuordnungen, Symbole, einfache Regeln).
- Zeitabhängige Inhalte (Topspieler:innen, Meister) nur als optional-historischer Überblick;
  keine tagesaktuellen Abfragen (keine Saisonstände, Live-Tabellen o. Ä.).
- Fokus: Regeln, Taktik, Formate, Historie, Statistik, Entwicklung, Schiedsrichterwesen.
"""

SUBTOPICS = [
    # 1 Grundlagen & Regeln
    ("Grundregeln: Dribbling, Schrittfehler, Doppeldribbling, Aus, Rückspiel", 4, (8, 10)),
    ("Fouls & Freiwürfe: persönliche/Teamfouls, unsportliche, disqualifizierende Fouls", 4, (7, 10)),
    ("Zeitregeln: 24-Sekunden, 8-/10-Sekunden, 5-Sekunden, Overtime", 3, (7, 10)),
    # ⚑ Basis
    ("Basketball – Basisfakten (Korb, Feldlinien, Spielerzahl, Ziel des Spiels)", 2, (1, 10)),

    # 2 Positionen, Rollen & Skills
    ("Positionen & Rollen: Guard, Wing, Big – Aufgaben & Skill-Profile", 4, (8, 10)),
    ("Offensivgrundlagen: Spacing, Cuts, Screens, Give-and-Go, Post-Ups", 3, (7, 10)),
    ("Individualtechnik: Wurfmechanik, Ballhandling, Footwork (Überblick)", 3, (8, 10)),
    # ⚑ Basis
    ("Positions-Zuordnung – Basis: Spielerrolle → typische Aufgaben", 2, (1, 10)),

    # 3 Taktik & Systeme
    ("Set Plays & Offenses: Motion, Flex, Princeton, Horns, 5-Out/4-Out-1-In", 4, (8, 10)),
    ("Pick-and-Roll-Familie: Coverages (Drop, Switch, Hedge, ICE), Reads", 4, (8, 10)),
    ("Defense: Mann-Mann vs. Zonen (2-3, 3-2, Matchup), Pressing & Traps", 3, (8, 10)),
    # ⚑ Basis
    ("Taktik – Basis: Offense/Defense-Grundbegriffe (Zuordnung)", 2, (1, 10)),

    # 4 Statistik & Analytics
    ("Box Score vs. Advanced: eFG%, TS%, ORtg/DRtg, Pace", 4, (8, 10)),
    ("Shot Charts & Spacing-Analysen: 3er-Rate, Rim-Attempts, Midrange", 3, (8, 10)),
    ("Lineup- und Plus/Minus-Interpretation: Net Rating, On/Off", 3, (9, 10)),
    # ⚑ Basis
    ("Stats – Basis: Punkte, Rebounds, Assists, Steals, Blocks (Zuordnung)", 2, (1, 10)),

    # 5 Wettbewerbsformate & Ligen (zeitloser Überblick)
    ("FIBA vs. NBA-Regeln: Unterschiede (Spielfeld, 3er-Linie, Goaltending, Defensive 3s)", 4, (7, 10)),
    ("Internationale Wettbewerbe: Weltmeisterschaft, Kontinentalmeisterschaften, Olympia", 3, (7, 10)),
    ("Klubwettbewerbe: NBA, EuroLeague, nationale Ligen & Pokalformate", 3, (7, 10)),
    # ⚑ Basis
    ("Formate – Basis: K.-o.-Runde vs. Serie (Best-of-7), Round Robin (Zuordnung)", 2, (1, 10)),

    # 6 Historie & Ikonen (zeitlos)
    ("Basketballgeschichte: Naismith, Regelentwicklung, 3-Punkte-Linie, Shot Clock", 3, (7, 10)),
    ("Ikonische Teams & Dynastien (zeitloser Überblick, keine Live-Bezüge)", 3, (7, 10)),
    ("Topspieler:innen & Spielstile nach Epochen (zeitlos-historisch)", 2, (5, 10)),
    # ⚑ Basis
    ("Ikonen – Basis: Legendäre Spieler:in → Team/Ära (Zuordnung)", 2, (1, 10)),

    # 7 Wurf & Scoring
    ("Wurfauswahl & Effizienz: Rim vs. Midrange vs. 3er – Trade-offs", 4, (8, 10)),
    ("Freilauf- und ATO-Design (After Time-out): BLOB/SLOB-Konzepte", 3, (8, 10)),
    ("Endspiel-Management: 2-für-1, intentional fouling, Timeout-Nutzung", 3, (8, 10)),

    # 8 Rebounding, Transition & Possession Game
    ("Rebounding: Boxout-Techniken, Crash vs. Transition-Absicherung", 3, (7, 10)),
    ("Transition Offense/Defense: Primär-/Sekundärbreak, Crossmatches", 3, (7, 10)),
    ("Turnover-Management & Ball Security: Press Breaker, Traps schlagen", 3, (8, 10)),

    # 9 Schiedsrichterwesen & Regelinterpretation
    ("Refereeing: Kontaktkriterien, vertikaler Zylinder, Block/Charge", 4, (8, 10)),
    ("Unsportlich/Disqualifizierend: Kriterien, Clear Path, Flagrant", 3, (8, 10)),
    ("Replay & Challenge-Systeme: Review-Trigger, Unten-2-Minuten-Protokoll", 3, (8, 10)),
    # ⚑ Basis
    ("Pfiffe – Basis: Handzeichen & Standardcalls (Zuordnung)", 2, (1, 10)),

    # 10 Entwicklung, Training & Gesundheit
    ("Athletik & Skill-Entwicklung: Periodisierung, Constraints-Learning", 3, (7, 10)),
    ("Verletzungsprävention: Sprunggelenk, Knie (ACL), Laststeuerung", 3, (7, 10)),
    ("Teamkultur & Rollenakzeptanz: Leadership, Kommunikation, Buy-in", 2, (5, 10)),
    # ⚑ Basis
    ("Training – Basis: Aufwärmen, Cool-down, einfache Drills (Zuordnung)", 2, (1, 10)),

    # 11 Frauenbasketball & 3x3
    ("Frauenbasketball: Regeldifferenzen, Wettbewerbe (zeitloser Überblick)", 3, (7, 10)),
    ("3x3 Basketball: Regeln, Taktiken, Turnierformat (FIBA 3x3)", 3, (7, 10)),
    # ⚑ Basis
    ("3x3/Frauen – Basis: Ballgröße, 12-Sek.-Uhr, 21-Punkte-Ziel (Zuordnung)", 2, (1, 10)),

    # 12 Ausrüstung, Feld & Maße
    ("Spielfeld & Maße: Zonen, Restricted Area, 3er-Distanzen (FIBA/NBA)", 3, (7, 10)),
    ("Ball, Schuhe, Schutz – Materialkunde & Normen", 2, (5, 10)),
    # ⚑ Basis
    ("Maße – Basis: Linie → Bedeutung (3er, Mittellinie, Freiwurflinie)", 2, (1, 10)),

    # 13 Organisation & Wettbewerbsökonomie (zeitlos)
    ("Draft-/Kadersysteme (NBA/andere): Roster Limits, Two-Way, Salary Cap-Grundlagen", 3, (8, 10)),
    ("Spielplan & Reisen: Back-to-Backs, Belastungssteuerung, Load Management (Überblick)", 2, (5, 10)),
    ("Schiedsrichter- und Wettbewerbsorganisation: Ansetzungen, Evaluierungen", 2, (5, 10)),
    # ⚑ Basis
    ("Organisation – Basis: Serie vs. Spieltag, Heim-/Auswärts (Zuordnung)", 2, (1, 10)),
]
