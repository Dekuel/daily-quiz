# -*- coding: utf-8 -*-
# Unterkategorien/Geschichte/neuzeit.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Neuzeit“.
Diese Liste wird von kategorien/geschichte.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte
"""

SUBDISCIPLINES = [
    # 1 Periodisierung & Grundzüge
    ("Neuzeit: Periodisierung & Epochenüberblick", 4),                         # 1
    ("Frühe Neuzeit (ca. 1500–1800)", 4),                                      # 1.1
    ("Neuere Geschichte (19. Jahrhundert)", 4),                                # 1.2
    ("Neueste Geschichte (20.–21. Jahrhundert)", 4),                           # 1.3
    ("Quellenkunde, Methoden & Historiographie", 3),                           # 1.4

    # 2 Reformation, Konfessionalisierung & Religionskonflikte
    ("Reformation: Luther, Zwingli, Calvin", 4),                               # 2.1
    ("Gegenreformation & Trienter Konzil", 4),                                 # 2.2
    ("Konfessionalisierung & Staatsbildung", 3),                               # 2.3
    ("Religionskriege in Frankreich & Niederlanden", 3),                       # 2.4
    ("Dreißigjähriger Krieg & Westfälischer Frieden", 4),                      # 2.5

    # 3 Staat, Herrschaft & Diplomatie in der Frühen Neuzeit
    ("Absolutismus & Hofgesellschaft (z. B. Ludwig XIV.)", 4),                 # 3.1
    ("Stehendes Heer, Militärrevolution, Festungen", 3),                       # 3.2
    ("Fiskalstaat, Bürokratie & Verwaltung", 3),                               # 3.3
    ("Völkerrecht & europäisches Staatensystem", 3),                           # 3.4
    ("Aufklärung: Ideen, Öffentlichkeit, Salons", 4),                          # 3.5

    # 4 Wissenschaft, Technik & Medienwandel
    ("Wissenschaftliche Revolution (Kopernikus–Newton)", 4),                   # 4.1
    ("Akademien, Gelehrtennetzwerke, Enzyklopädien", 3),                       # 4.2
    ("Buchdruck, Presse & Zensur", 3),                                         # 4.3
    ("Technikgeschichte (Uhr, Dampfmaschine, Elektrizität)", 3),               # 4.4
    ("Medizingeschichte (Anatomie, Impfungen)", 2),                            # 4.5

    # 5 Entdeckungen, Kolonialismus & atlantische Welt
    ("Entdeckungsfahrten & erste Globalisierung", 4),                          # 5.1
    ("Iberische Imperien & Konkurrenz der Mächte", 3),                         # 5.2
    ("Atlantikhandel & Plantagensystem", 3),                                   # 5.3
    ("Transatlantischer Sklavenhandel & Sklaverei", 4),                        # 5.4
    ("Indigene Gesellschaften & Kolonialbegegnungen", 3),                      # 5.5

    # 6 Revolutionen & Verfassungsstaat
    ("Amerikanische Revolution & Verfassung", 4),                              # 6.1
    ("Französische Revolution & Menschenrechte", 4),                           # 6.2
    ("Haitianische Revolution & Sklavenemanzipation", 3),                      # 6.3
    ("Napoleonische Zeit & Neuordnung Europas", 4),                            # 6.4
    ("Revolutionen 1830/1848 & Liberalismus", 4),                              # 6.5

    # 7 Industrie, Arbeit & Gesellschaft im 19. Jahrhundert
    ("Industrialisierung: Phasen, Sektoren, Regionen", 4),                     # 7.1
    ("Urbanisierung, Migration & soziale Frage", 4),                           # 7.2
    ("Arbeiterbewegung, Gewerkschaften, Sozialgesetzgebung", 4),               # 7.3
    ("Kapitalismus, Banken & Unternehmensformen", 3),                          # 7.4
    ("Wissen, Patente & technische Netzwerke (Eisenbahn, Telegraf)", 3),       # 7.5

    # 8 Nationenbildung, Imperialismus & Weltverkehr
    ("Nationalstaatsbildung: Deutschland & Italien", 4),                       # 8.1
    ("Imperialismus & Kolonialreiche des 19. Jh.", 4),                         # 8.2
    ("Weltwirtschaft & Goldstandard", 3),                                      # 8.3
    ("Globaler Handel, Migration & Diasporas", 3),                             # 8.4
    ("Wissenschaftliche Expeditionen & Weltmessen", 2),                        # 8.5

    # 9 Kultur, Bildung & Lebenswelten (1500–1900)
    ("Bildungsexpansion, Universitäten & Alphabetisierung", 3),                # 9.1
    ("Kunst- und Kulturströmungen (Renaissance–Realismus)", 3),                # 9.2
    ("Religion, Säkularisierung & Frömmigkeit", 3),                            # 9.3
    ("Familie, Geschlecht & Körpergeschichte", 3),                             # 9.4
    ("Wohnen, Konsum & materielle Kultur", 2),                                 # 9.5

    # 10 Erster Weltkrieg & Zwischenkriegszeit
    ("Erster Weltkrieg: Ursachen, Verlauf, Folgen", 4),                        # 10.1
    ("Heimatfront, Kriegswirtschaft & Totalisierung", 3),                      # 10.2
    ("Friedensschlüsse & Neuordnung (Versailles)", 3),                         # 10.3
    ("Zwischenkriegszeit: Krisen & Kultur (1920er)", 3),                       # 10.4
    ("Autoritarismus, Faschismus & Stalinismus", 4),                           # 10.5

    # 11 Zweiter Weltkrieg & Gewaltgeschichte
    ("Zweiter Weltkrieg: globaler Verlauf", 4),                                # 11.1
    ("Holocaust & nationalsozialistische Verbrechen", 4),                      # 11.2
    ("Widerstand, Kollaboration & Befreiung", 3),                              # 11.3
    ("Kriegsende, Vertreibungen & Nachkriegsordnung", 3),                      # 11.4
    ("Kriegsverbrechen, Prozesse & Erinnerungskultur", 3),                     # 11.5

    # 12 Kalter Krieg, Blockbildung & Dekolonisation
    ("Kalter Krieg: Bipolarität & Konfliktzonen", 4),                          # 12.1
    ("NATO, Warschauer Pakt & Rüstungsdynamiken", 3),                          # 12.2
    ("Dekolonisation in Asien & Afrika", 4),                                   # 12.3
    ("Blockfreie Bewegung & Entwicklungspolitik", 2),                          # 12.4
    ("Teilung & Wiedervereinigung Deutschlands", 4),                           # 12.5

    # 13 Zeitgeschichte seit 1970
    ("Europäische Integration (EG/EU) & Erweiterungen", 4),                    # 13.1
    ("Neoliberale Wende, Globalisierung & Finanzmärkte", 3),                   # 13.2
    ("Menschenrechte, NGOs & transnationale Bewegungen", 3),                   # 13.3
    ("Technologischer Wandel: Digitalität & Internet", 3),                     # 13.4
    ("Umweltgeschichte & Klimapolitik", 3),                                     # 13.5
    ("Migration, Multikulturalität & Populismus", 3),                          # 13.6
    ("Erinnerungskulturen & Geschichtspolitik", 3),                            # 13.7

    # 14 Recht, Staat & Gesellschaft im 20./21. Jahrhundert
    ("Wohlfahrtsstaat & soziale Sicherungssysteme", 4),                        # 14.1
    ("Internationale Organisationen (UNO, WTO, IWF)", 3),                      # 14.2
    ("Völkerrecht, Menschenrechtsschutz & Strafgerichte", 3),                  # 14.3
    ("Mediengeschichte: Radio, TV, Social Media", 3),                          # 14.4
    ("Wissenschaft, Medizin & Ethik (Atom, Genetik, KI)", 2),                  # 14.5
]
