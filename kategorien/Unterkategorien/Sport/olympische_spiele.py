# -*- coding: utf-8 -*-
# Unterkategorien/Sport/olympische_spiele.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Olympische Spiele“.
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
- Zeitabhängige Inhalte (aktuelle Meister/Topstars) nur als **optional-historische**
  Orientierung; keine tagesaktuellen Abfragen.
- Fokus: Formate, Regeln, Geschichte, Strukturen, Ethik, Symbolik.
"""

SUBTOPICS = [
    # 1 Grundlagen & Struktur
    ("Olympische Bewegung: IOC, NOKs & IFs – Rollen & Zuständigkeiten", 4, (7, 10)),
    ("Sommer- vs. Winterspiele: Disziplinstruktur, Zyklen, Programme", 4, (5, 10)),
    ("Qualifikationssysteme: Quotenplätze, Normen, Weltranglisten (Überblick)", 4, (8, 10)),
    ("Olympische Werte & Charta: Fair Play, Neutralität, Amateurismus/Professionalisierung", 3, (8, 10)),
    # ⚑ Basis
    ("Olympia – Basisfakten (alle 4 Jahre, Ringe, Fackellauf, Eröffnungs-/Abschlussfeier)", 2, (1, 10)),

    # 2 Geschichte & Meilensteine
    ("Antike Spiele in Olympia: Disziplinen, Ablauf, Gesellschaftskontext", 3, (7, 10)),
    ("Moderne Wiederbelebung (Pierre de Coubertin) & frühe Ausgaben", 3, (7, 10)),
    ("Bedeutende Epochen: Globalisierung, Fernsehen, Kommerzialisierung", 3, (8, 10)),
    ("Boykotte, Politik & Olympia – Fallstudien (zeitlos)", 3, (9, 10)),
    # ⚑ Basis
    ("Historie – Basis: erste Moderne Spiele, Symbole, ikonische Momente (Zuordnung)", 2, (1, 10)),

    # 3 Symbole, Rituale & Identität
    ("Olympische Ringe, Motto & Flagge: Bedeutung & Entstehung", 4, (5, 10)),
    ("Fackellauf & Olympisches Feuer: Ursprung, Staffel, Entzündung", 3, (5, 10)),
    ("Eröffnungs- & Abschlusszeremonie: Protokoll, Einmarsch, Eid", 3, (5, 10)),
    ("Maskottchen & Design (Piktogramme, Look of the Games)", 2, (3, 10)),
    # ⚑ Basis
    ("Symbolik – Basis: Ringe, Flagge, Feuer (Zuordnungen & Begriffe)", 2, (1, 10)),

    # 4 Sportarten & Wettkampfformen (Sommer)
    ("Leichtathletik bei Olympia: Programm, Finals, Mehrkämpfe (Überblick)", 4, (5, 10)),
    ("Schwimmen & Aquatics (Schwimmen, Wasserspringen, Wasserball, Synchr.)", 4, (7, 10)),
    ("Turnen (Artistik/Rhythmisch/Trampolin): Geräte, Finals, Teams", 3, (7, 10)),
    ("Kampfsport (Judo, Ringen, Taekwondo, Boxen): Klassen, Wertung, Format", 3, (8, 10)),
    ("Mannschaftssport (HB/VB/Basketball/7er-Rugby): Turnierformate", 3, (7, 10)),
    # ⚑ Basis
    ("Sommer – Basis: Sportart → typische Disziplin/Ort (Zuordnung)", 2, (1, 10)),

    # 5 Sportarten & Wettkampfformen (Winter)
    ("Ski Alpin & Nordisch: Disziplinen, Startmodi, Kombiformate", 4, (7, 10)),
    ("Eisschnelllauf & Shorttrack: Distanzen, Heats, Zeit-/Zeitstrafen", 3, (7, 10)),
    ("Eiskunstlauf & Eistanz: Wertungssysteme (GOE, Komponenten) – Überblick", 3, (8, 10)),
    ("Biathlon & Skispringen: Strafrunden, Wind-/Gate-Kompensation, Teams", 3, (8, 10)),
    # ⚑ Basis
    ("Winter – Basis: Sportart → Disziplin/Ort (Zuordnung)", 2, (1, 10)),

    # 6 Formate, Setzsysteme & Medaillen
    ("Finalwege & Heats: Vorlauf, Halbfinale, Finale – sportartspezifisch", 4, (7, 10)),
    ("Medaillenwertung & Nationenrankings: Zählweisen, Kontroversen", 3, (8, 10)),
    ("Mixed- & Team-Events: Einführungen, Ziele, Beispiele", 3, (7, 10)),
    ("Jugendspiele & Quali-Events (Kontinentalspiele, Weltmeisterschaften)", 2, (5, 10)),
    # ⚑ Basis
    ("Medaillen – Basis: Gold/Silber/Bronze, Podest, Flower Ceremony", 2, (1, 10)),

    # 7 Fairness, Sicherheit & Dopingprävention
    ("Anti-Doping-Strukturen: WADA, TUE, Testing-Pools, CAS-Fälle (überblick)", 4, (9, 10)),
    ("Schutz der Integrität: Manipulationsprävention, Wettbetrug, Whistleblowing", 3, (9, 10)),
    ("Athlet:innenwohl: Heat Policies, Concussion Protocols, Safeguarding", 3, (8, 10)),
    # ⚑ Basis
    ("Fair Play – Basis: Doping-Verbote, Grundprinzipien, Meldepflicht (Zuordnung)", 2, (1, 10)),

    # 8 Hosting, Organisation & Nachhaltigkeit
    ("Vergabeprozesse: Kandidaturphasen, Evaluationskriterien, Host City Contract", 4, (8, 10)),
    ("Infrastruktur & Legacy: Venues, Athletendorf, Nachnutzung", 3, (8, 10)),
    ("Nachhaltigkeit & Klima: CO₂-Bilanzen, temporäre Bauten, Mobilität", 3, (8, 10)),
    ("Sicherheit, Volunteers & Logistik: Akkreditierung, Flüsse, Notfallkonzepte", 3, (8, 10)),
    # ⚑ Basis
    ("Organisation – Basis: Wer vergibt? Was ist ein NOK? (Zuordnungen)", 2, (1, 10)),

    # 9 Gleichstellung & Inklusion
    ("Gender Equity: Programmparität, Mixed Events, Quoten", 3, (8, 10)),
    ("Paralympics & Deaflympics: Abgrenzung, Klassifikationsprinzipien (Überblick)", 3, (8, 10)),
    ("Inklusion & Barrierefreiheit: Venue-Design, Broadcasting, Regelanpassungen", 2, (5, 10)),
    # ⚑ Basis
    ("Inklusion – Basis: Piktogramme, Klassifikations-Idee (Zuordnung)", 2, (1, 10)),

    # 10 Rekorde, Ikonen & Turniergeschichte (zeitlos)
    ("Olympische Rekorde & Meilensteine (zeitlos-historisch, sportartenübergreifend)", 3, (7, 10)),
    ("Ikonische Athlet:innen & Teams (Sommer/Winter) – Überblick", 3, (7, 10)),
    ("Legendäre Wettkämpfe & Wendepunkte (zeitlos erzählt)", 2, (5, 10)),
    # ⚑ Basis
    ("Ikonen – Basis: Athlet:in → Sportart (Zuordnung, zeitlos)", 2, (1, 10)),

    # 11 Regeländerungen & Programmentwicklung
    ("Aufnahme/Abwahl von Sportarten: Kriterien, Beispiele, Debatten", 3, (8, 10)),
    ("Regelinnovationen: Video Assist, Zeitformate, Mixed-Team-Förderung", 3, (8, 10)),
    ("Amateurismus → Professionalisierung: Folgen für Teilnahme & Leistung", 3, (9, 10)),
    # ⚑ Basis
    ("Programm – Basis: neue/alte Sportarten (Zuordnung, Beispiele)", 2, (1, 10)),

    # 12 Medien, Vermarktung & Kultur
    ("Rundfunkrechte & Broadcasting: Scheduling, Primetime, Digitalformate", 3, (8, 10)),
    ("Sponsoring & TOP-Programm: Rechtekategorien, Ambush-Marketing", 3, (9, 10)),
    ("Fankultur & Hospitality: Ticketing, Fan-Zonen, Kulturprogramme", 2, (5, 10)),
    # ⚑ Basis
    ("Kultur – Basis: Symbole, Hymnen, Piktogramme (Zuordnungen)", 2, (1, 10)),

    # 13 Samples für sportartspezifische Deep-Dives (optional)
    ("Leichtathletik (olympisch): Qualinormen vs. Weltrangliste – Beispiele", 4, (8, 10)),
    ("Schwimmen (olympisch): Vorläufe, Halbfinals, Finals – Seedings & Bahnen", 3, (8, 10)),
    ("Turnen (olympisch): D- und E-Note, Finals by Apparatus – Überblick", 3, (9, 10)),
    # ⚑ Basis
    ("Deep-Dive – Basis: Disziplin → Wettkampfform (Zuordnung)", 2, (1, 10)),
]
