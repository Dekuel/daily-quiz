# -*- coding: utf-8 -*-
# Unterkategorien/Geschichte/neuzeit.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Neuzeit“.
Diese Liste wird von kategorien/geschichte.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
"""

SUBDISCIPLINES = [
    # 1 Periodisierung & Grundzüge
    ("Neuzeit: Periodisierung & Epochenüberblick", 7, (3,10)),
    ("Frühe Neuzeit (ca. 1500–1800)", 7, (3,10)),
    ("Neuere Geschichte (19. Jahrhundert)", 7, (3,10)),
    ("Neueste Geschichte (20.–21. Jahrhundert)", 7, (3,10)),
    ("Quellenkunde, Methoden & Historiographie", 5, (5,10)),
    ("Basis – Neuzeit allgemein (Zeitstrahl, Grundbegriffe, Leitereignisse)", 3, (1,10)),

    # 2 Reformation, Konfessionalisierung & Religionskonflikte
    ("Reformation: Luther, Zwingli, Calvin", 7, (3,10)),
    ("Gegenreformation & Trienter Konzil", 7, (5,10)),
    ("Konfessionalisierung & Staatsbildung", 5, (7,10)),
    ("Religionskriege in Frankreich & Niederlanden", 5, (7,10)),
    ("Dreißigjähriger Krieg & Westfälischer Frieden", 7, (5,10)),
    ("Basis – Reformation (Akteure, Begriffe, Daten)", 3, (1,10)),

    # 3 Staat, Herrschaft & Diplomatie in der Frühen Neuzeit
    ("Absolutismus & Hofgesellschaft (z. B. Ludwig XIV.)", 7, (5,10)),
    ("Stehendes Heer, Militärrevolution, Festungen", 5, (7,10)),
    ("Fiskalstaat, Bürokratie & Verwaltung", 5, (7,10)),
    ("Völkerrecht & europäisches Staatensystem", 5, (7,10)),
    ("Aufklärung: Ideen, Öffentlichkeit, Salons", 7, (5,10)),
    ("Basis – Frühe Neuzeit (Herrschaft, Heer, Öffentlichkeit)", 3, (1,10)),

    # 4 Wissenschaft, Technik & Medienwandel
    ("Wissenschaftliche Revolution (Kopernikus–Newton)", 7, (5,10)),
    ("Akademien, Gelehrtennetzwerke, Enzyklopädien", 5, (7,10)),
    ("Buchdruck, Presse & Zensur", 5, (5,10)),
    ("Technikgeschichte (Uhr, Dampfmaschine, Elektrizität)", 5, (5,10)),
    ("Medizingeschichte (Anatomie, Impfungen)", 3, (3,10)),
    ("Basis – Wissenschaft/Technik (Erfinder, Geräte, Begriffe)", 3, (1,10)),

    # 5 Entdeckungen, Kolonialismus & atlantische Welt
    ("Entdeckungsfahrten & erste Globalisierung", 7, (5,10)),
    ("Iberische Imperien & Konkurrenz der Mächte", 5, (7,10)),
    ("Atlantikhandel & Plantagensystem", 5, (7,10)),
    ("Transatlantischer Sklavenhandel & Sklaverei", 7, (5,10)),
    ("Indigene Gesellschaften & Kolonialbegegnungen", 5, (7,10)),
    ("Basis – Atlantische Welt (Routen, Waren, Akteure)", 3, (1,10)),

    # 6 Revolutionen & Verfassungsstaat
    ("Amerikanische Revolution & Verfassung", 7, (3,10)),
    ("Französische Revolution & Menschenrechte", 7, (3,10)),
    ("Haitianische Revolution & Sklavenemanzipation", 5, (7,10)),
    ("Napoleonische Zeit & Neuordnung Europas", 7, (5,10)),
    ("Revolutionen 1830/1848 & Liberalismus", 7, (5,10)),
    ("Basis – Revolutionen (Chronologie, Konzepte, Personen)", 3, (1,10)),

    # 7 Industrie, Arbeit & Gesellschaft im 19. Jahrhundert
    ("Industrialisierung: Phasen, Sektoren, Regionen", 7, (5,10)),
    ("Urbanisierung, Migration & soziale Frage", 7, (5,10)),
    ("Arbeiterbewegung, Gewerkschaften, Sozialgesetzgebung", 7, (5,10)),
    ("Kapitalismus, Banken & Unternehmensformen", 5, (7,10)),
    ("Wissen, Patente & technische Netzwerke (Eisenbahn, Telegraf)", 5, (5,10)),
    ("Basis – Industrialisierung (Maschinen, Orte, Begriffe)", 3, (1,10)),

    # 8 Nationenbildung, Imperialismus & Weltverkehr
    ("Nationalstaatsbildung: Deutschland & Italien", 7, (5,10)),
    ("Imperialismus & Kolonialreiche des 19. Jh.", 7, (5,10)),
    ("Weltwirtschaft & Goldstandard", 5, (7,10)),
    ("Globaler Handel, Migration & Diasporas", 5, (5,10)),
    ("Wissenschaftliche Expeditionen & Weltmessen", 3, (3,10)),
    ("Basis – Nation & Imperium (Karten, Daten, Schlüsselbegriffe)", 3, (1,10)),

    # 9 Kultur, Bildung & Lebenswelten (1500–1900)
    ("Bildungsexpansion, Universitäten & Alphabetisierung", 5, (5,10)),
    ("Kunst- und Kulturströmungen (Renaissance–Realismus)", 5, (5,10)),
    ("Religion, Säkularisierung & Frömmigkeit", 5, (5,10)),
    ("Familie, Geschlecht & Körpergeschichte", 5, (5,10)),
    ("Wohnen, Konsum & materielle Kultur", 3, (3,10)),
    ("Basis – Kultur/Lebenswelten (Stile, Epochen, Beispiele)", 3, (1,10)),

    # 10 Erster Weltkrieg & Zwischenkriegszeit
    ("Erster Weltkrieg: Ursachen, Verlauf, Folgen", 7, (5,10)),
    ("Heimatfront, Kriegswirtschaft & Totalisierung", 5, (7,10)),
    ("Friedensschlüsse & Neuordnung (Versailles)", 5, (7,10)),
    ("Zwischenkriegszeit: Krisen & Kultur (1920er)", 5, (5,10)),
    ("Autoritarismus, Faschismus & Stalinismus", 7, (5,10)),
    ("Basis – Erster Weltkrieg & Zwischenkriegszeit (Begriffe, Daten)", 3, (1,10)),

    # 11 Zweiter Weltkrieg & Gewaltgeschichte
    ("Zweiter Weltkrieg: globaler Verlauf", 7, (5,10)),
    ("Holocaust & nationalsozialistische Verbrechen", 7, (5,10)),
    ("Widerstand, Kollaboration & Befreiung", 5, (5,10)),
    ("Kriegsende, Vertreibungen & Nachkriegsordnung", 5, (5,10)),
    ("Kriegsverbrechen, Prozesse & Erinnerungskultur", 5, (5,10)),
    ("Basis – Zweiter Weltkrieg (Schauplätze, Akteure, Begriffe)", 3, (1,10)),

    # 12 Kalter Krieg, Blockbildung & Dekolonisation
    ("Kalter Krieg: Bipolarität & Konfliktzonen", 7, (5,10)),
    ("NATO, Warschauer Pakt & Rüstungsdynamiken", 5, (7,10)),
    ("Dekolonisation in Asien & Afrika", 7, (5,10)),
    ("Blockfreie Bewegung & Entwicklungspolitik", 3, (5,10)),
    ("Teilung & Wiedervereinigung Deutschlands", 7, (3,10)),
    ("Basis – Kalter Krieg & Dekolonisation (Karten, Daten, Begriffe)", 3, (1,10)),

    # 13 Zeitgeschichte seit 1970
    ("Europäische Integration (EG/EU) & Erweiterungen", 7, (5,10)),
    ("Neoliberale Wende, Globalisierung & Finanzmärkte", 5, (7,10)),
    ("Menschenrechte, NGOs & transnationale Bewegungen", 5, (5,10)),
    ("Technologischer Wandel: Digitalität & Internet", 5, (3,10)),
    ("Umweltgeschichte & Klimapolitik", 5, (5,10)),
    ("Migration, Multikulturalität & Populismus", 5, (5,10)),
    ("Erinnerungskulturen & Geschichtspolitik", 5, (5,10)),
    ("Basis – Zeitgeschichte (Begriffe, Organisationen, Ereignisse)", 3, (1,10)),

    # 14 Recht, Staat & Gesellschaft im 20./21. Jahrhundert
    ("Wohlfahrtsstaat & soziale Sicherungssysteme", 7, (5,10)),
    ("Internationale Organisationen (UNO, WTO, IWF)", 5, (5,10)),
    ("Völkerrecht, Menschenrechtsschutz & Strafgerichte", 5, (7,10)),
    ("Mediengeschichte: Radio, TV, Social Media", 5, (3,10)),
    ("Wissenschaft, Medizin & Ethik (Atom, Genetik, KI)", 3, (5,10)),
    ("Basis – Recht, Staat & Gesellschaft (Begriffe, Institutionen)", 3, (1,10)),
]
