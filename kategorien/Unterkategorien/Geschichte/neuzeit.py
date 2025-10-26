# -*- coding: utf-8 -*-
# Unterkategorien/Geschichte/neuzeit.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Neuzeit“.
Diese Liste wird von kategorien/geschichte.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Einheitliche Skala & Struktur
==========================================================================
- Skala 1–10: 1 = Allgemeinwissen, 10 = Expertenwissen
- min = Bekanntheit (Population Familiarity)
- max = inhaltliche/methodische Tiefe (Conceptual Depth)
- „Basis…“-Kategorien haben immer min = 1 (Zuordnung, Namen, einfache Fakten)
- Nicht-Basis-Themen können i. d. R. bis 10 gehen (Vertiefbarkeit durch Forschung)
"""

SUBDISCIPLINES = [
    # 1 Periodisierung & Grundzüge
    ("Neuzeit: Periodisierung & Epochenüberblick", 4, (2,10)),                   # 1
    ("Frühe Neuzeit (ca. 1500–1800)", 4, (2,10)),                                # 1.1
    ("Neuere Geschichte (19. Jahrhundert)", 4, (2,10)),                          # 1.2
    ("Neueste Geschichte (20.–21. Jahrhundert)", 4, (2,10)),                     # 1.3
    ("Quellenkunde, Methoden & Historiographie", 3, (3,10)),                     # 1.4
    # ⚑ Basis
    ("Basis – Neuzeit allgemein (Zeitstrahl, Grundbegriffe, Leitereignisse)", 2, (1,7)),

    # 2 Reformation, Konfessionalisierung & Religionskonflikte
    ("Reformation: Luther, Zwingli, Calvin", 4, (2,10)),                          # 2.1
    ("Gegenreformation & Trienter Konzil", 4, (3,10)),                             # 2.2
    ("Konfessionalisierung & Staatsbildung", 3, (4,10)),                           # 2.3
    ("Religionskriege in Frankreich & Niederlanden", 3, (4,10)),                   # 2.4
    ("Dreißigjähriger Krieg & Westfälischer Frieden", 4, (3,10)),                  # 2.5
    # ⚑ Basis
    ("Basis – Reformation (Akteure, Begriffe, Daten)", 2, (1,7)),

    # 3 Staat, Herrschaft & Diplomatie in der Frühen Neuzeit
    ("Absolutismus & Hofgesellschaft (z. B. Ludwig XIV.)", 4, (3,10)),             # 3.1
    ("Stehendes Heer, Militärrevolution, Festungen", 3, (4,10)),                   # 3.2
    ("Fiskalstaat, Bürokratie & Verwaltung", 3, (4,10)),                           # 3.3
    ("Völkerrecht & europäisches Staatensystem", 3, (4,10)),                       # 3.4
    ("Aufklärung: Ideen, Öffentlichkeit, Salons", 4, (3,10)),                      # 3.5
    # ⚑ Basis
    ("Basis – Frühe Neuzeit (Herrschaft, Heer, Öffentlichkeit)", 2, (1,7)),

    # 4 Wissenschaft, Technik & Medienwandel
    ("Wissenschaftliche Revolution (Kopernikus–Newton)", 4, (3,10)),               # 4.1
    ("Akademien, Gelehrtennetzwerke, Enzyklopädien", 3, (4,10)),                   # 4.2
    ("Buchdruck, Presse & Zensur", 3, (3,10)),                                     # 4.3
    ("Technikgeschichte (Uhr, Dampfmaschine, Elektrizität)", 3, (3,10)),           # 4.4
    ("Medizingeschichte (Anatomie, Impfungen)", 2, (2,9)),                         # 4.5
    # ⚑ Basis
    ("Basis – Wissenschaft/Technik (Erfinder, Geräte, Begriffe)", 2, (1,7)),

    # 5 Entdeckungen, Kolonialismus & atlantische Welt
    ("Entdeckungsfahrten & erste Globalisierung", 4, (3,10)),                      # 5.1
    ("Iberische Imperien & Konkurrenz der Mächte", 3, (4,10)),                     # 5.2
    ("Atlantikhandel & Plantagensystem", 3, (4,10)),                                # 5.3
    ("Transatlantischer Sklavenhandel & Sklaverei", 4, (3,10)),                    # 5.4
    ("Indigene Gesellschaften & Kolonialbegegnungen", 3, (4,10)),                  # 5.5
    # ⚑ Basis
    ("Basis – Atlantische Welt (Routen, Waren, Akteure)", 2, (1,7)),

    # 6 Revolutionen & Verfassungsstaat
    ("Amerikanische Revolution & Verfassung", 4, (2,10)),                          # 6.1
    ("Französische Revolution & Menschenrechte", 4, (2,10)),                       # 6.2
    ("Haitianische Revolution & Sklavenemanzipation", 3, (4,10)),                  # 6.3
    ("Napoleonische Zeit & Neuordnung Europas", 4, (3,10)),                        # 6.4
    ("Revolutionen 1830/1848 & Liberalismus", 4, (3,10)),                          # 6.5
    # ⚑ Basis
    ("Basis – Revolutionen (Chronologie, Konzepte, Personen)", 2, (1,7)),

    # 7 Industrie, Arbeit & Gesellschaft im 19. Jahrhundert
    ("Industrialisierung: Phasen, Sektoren, Regionen", 4, (3,10)),                 # 7.1
    ("Urbanisierung, Migration & soziale Frage", 4, (3,10)),                       # 7.2
    ("Arbeiterbewegung, Gewerkschaften, Sozialgesetzgebung", 4, (3,10)),           # 7.3
    ("Kapitalismus, Banken & Unternehmensformen", 3, (4,10)),                      # 7.4
    ("Wissen, Patente & technische Netzwerke (Eisenbahn, Telegraf)", 3, (3,10)),   # 7.5
    # ⚑ Basis
    ("Basis – Industrialisierung (Maschinen, Orte, Begriffe)", 2, (1,7)),

    # 8 Nationenbildung, Imperialismus & Weltverkehr
    ("Nationalstaatsbildung: Deutschland & Italien", 4, (3,10)),                   # 8.1
    ("Imperialismus & Kolonialreiche des 19. Jh.", 4, (3,10)),                     # 8.2
    ("Weltwirtschaft & Goldstandard", 3, (4,10)),                                   # 8.3
    ("Globaler Handel, Migration & Diasporas", 3, (3,10)),                          # 8.4
    ("Wissenschaftliche Expeditionen & Weltmessen", 2, (2,9)),                      # 8.5
    # ⚑ Basis
    ("Basis – Nation & Imperium (Karten, Daten, Schlüsselbegriffe)", 2, (1,7)),

    # 9 Kultur, Bildung & Lebenswelten (1500–1900)
    ("Bildungsexpansion, Universitäten & Alphabetisierung", 3, (3,10)),            # 9.1
    ("Kunst- und Kulturströmungen (Renaissance–Realismus)", 3, (3,10)),            # 9.2
    ("Religion, Säkularisierung & Frömmigkeit", 3, (3,10)),                         # 9.3
    ("Familie, Geschlecht & Körpergeschichte", 3, (3,10)),                          # 9.4
    ("Wohnen, Konsum & materielle Kultur", 2, (2,9)),                               # 9.5
    # ⚑ Basis
    ("Basis – Kultur/Lebenswelten (Stile, Epochen, Beispiele)", 2, (1,7)),

    # 10 Erster Weltkrieg & Zwischenkriegszeit
    ("Erster Weltkrieg: Ursachen, Verlauf, Folgen", 4, (3,10)),                     # 10.1
    ("Heimatfront, Kriegswirtschaft & Totalisierung", 3, (4,10)),                   # 10.2
    ("Friedensschlüsse & Neuordnung (Versailles)", 3, (4,10)),                      # 10.3
    ("Zwischenkriegszeit: Krisen & Kultur (1920er)", 3, (3,10)),                    # 10.4
    ("Autoritarismus, Faschismus & Stalinismus", 4, (3,10)),                        # 10.5
    # ⚑ Basis
    ("Basis – Erster Weltkrieg & Zwischenkriegszeit (Begriffe, Daten)", 2, (1,7)),

    # 11 Zweiter Weltkrieg & Gewaltgeschichte
    ("Zweiter Weltkrieg: globaler Verlauf", 4, (3,10)),                              # 11.1
    ("Holocaust & nationalsozialistische Verbrechen", 4, (3,10)),                    # 11.2
    ("Widerstand, Kollaboration & Befreiung", 3, (3,10)),                            # 11.3
    ("Kriegsende, Vertreibungen & Nachkriegsordnung", 3, (3,10)),                   # 11.4
    ("Kriegsverbrechen, Prozesse & Erinnerungskultur", 3, (3,10)),                  # 11.5
    # ⚑ Basis
    ("Basis – Zweiter Weltkrieg (Schauplätze, Akteure, Begriffe)", 2, (1,7)),

    # 12 Kalter Krieg, Blockbildung & Dekolonisation
    ("Kalter Krieg: Bipolarität & Konfliktzonen", 4, (3,10)),                       # 12.1
    ("NATO, Warschauer Pakt & Rüstungsdynamiken", 3, (4,10)),                       # 12.2
    ("Dekolonisation in Asien & Afrika", 4, (3,10)),                                 # 12.3
    ("Blockfreie Bewegung & Entwicklungspolitik", 2, (3,9)),                         # 12.4
    ("Teilung & Wiedervereinigung Deutschlands", 4, (2,10)),                         # 12.5
    # ⚑ Basis
    ("Basis – Kalter Krieg & Dekolonisation (Karten, Daten, Begriffe)", 2, (1,7)),

    # 13 Zeitgeschichte seit 1970
    ("Europäische Integration (EG/EU) & Erweiterungen", 4, (3,10)),                 # 13.1
    ("Neoliberale Wende, Globalisierung & Finanzmärkte", 3, (4,10)),                # 13.2
    ("Menschenrechte, NGOs & transnationale Bewegungen", 3, (3,10)),                # 13.3
    ("Technologischer Wandel: Digitalität & Internet", 3, (2,10)),                  # 13.4
    ("Umweltgeschichte & Klimapolitik", 3, (3,10)),                                  # 13.5
    ("Migration, Multikulturalität & Populismus", 3, (3,10)),                        # 13.6
    ("Erinnerungskulturen & Geschichtspolitik", 3, (3,10)),                          # 13.7
    # ⚑ Basis
    ("Basis – Zeitgeschichte (Begriffe, Organisationen, Ereignisse)", 2, (1,7)),

    # 14 Recht, Staat & Gesellschaft im 20./21. Jahrhundert
    ("Wohlfahrtsstaat & soziale Sicherungssysteme", 4, (3,10)),                     # 14.1
    ("Internationale Organisationen (UNO, WTO, IWF)", 3, (3,10)),                   # 14.2
    ("Völkerrecht, Menschenrechtsschutz & Strafgerichte", 3, (4,10)),               # 14.3
    ("Mediengeschichte: Radio, TV, Social Media", 3, (2,10)),                        # 14.4
    ("Wissenschaft, Medizin & Ethik (Atom, Genetik, KI)", 2, (3,9)),                # 14.5
    # ⚑ Basis
    ("Basis – Recht, Staat & Gesellschaft (Begriffe, Institutionen)", 2, (1,7)),
]
