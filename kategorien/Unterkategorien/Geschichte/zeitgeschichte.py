# -*- coding: utf-8 -*-
# Unterkategorien/Geschichte/zeitgeschichte.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Zeitgeschichte“.
Diese Liste wird von kategorien/geschichte.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte
"""

SUBDISCIPLINES = [
    # 1 Definition, Quellen & Methodik
    ("Zeitgeschichte: Begriff, Abgrenzung & Methodik", 4),                     # 1
    ("Zeithistorische Quellen & Oral History", 4),                             # 1.1
    ("Zeitzeugenarbeit & Erinnerungskultur", 3),                               # 1.2
    ("Medien, Öffentlichkeit & Geschichtspolitik", 3),                         # 1.3
    ("Historische Sozialforschung & Digital Humanities", 2),                   # 1.4

    # 2 Zweiter Weltkrieg & seine Folgen
    ("Zweiter Weltkrieg (1939–1945): Gesamtüberblick", 4),                     # 2.1
    ("Kriegsverlauf in Europa, Asien & Afrika", 3),                            # 2.2
    ("Holocaust & nationalsozialistische Verbrechen", 4),                      # 2.3
    ("Kriegsende, Kapitulation & Nachkriegsordnung", 4),                       # 2.4
    ("Flucht, Vertreibung & Neuanfang", 3),                                    # 2.5
    ("Wiederaufbau & Besatzungszonen", 3),                                     # 2.6

    # 3 Deutschland nach 1945
    ("Gründung von BRD & DDR (1949)", 4),                                      # 3.1
    ("Politische Systeme: Demokratie & Sozialismus", 4),                       # 3.2
    ("Wirtschaftswunder & soziale Marktwirtschaft", 4),                        # 3.3
    ("Sowjetische Besatzungszone & SED-Herrschaft", 3),                        # 3.4
    ("Berlin-Frage & Mauerbau", 4),                                            # 3.5
    ("Kalter Krieg im geteilten Deutschland", 4),                              # 3.6
    ("Opposition & Bürgerrechtsbewegung in der DDR", 3),                       # 3.7
    ("Wiedervereinigung 1989/90", 4),                                          # 3.8
    ("Transformation & Erinnerung an die DDR", 3),                             # 3.9

    # 4 Kalter Krieg & Weltpolitik 1945–1990
    ("Kalter Krieg: globale Struktur & Bipolarität", 4),                       # 4.1
    ("Marshallplan & Wiederaufbau Westeuropas", 3),                            # 4.2
    ("Koreakrieg, Vietnamkrieg & Stellvertreterkonflikte", 4),                 # 4.3
    ("Kuba-Krise & Atomare Abschreckung", 3),                                  # 4.4
    ("Entspannungspolitik & KSZE-Prozess", 3),                                 # 4.5
    ("UNO, NATO, Warschauer Pakt", 3),                                         # 4.6
    ("Ende des Kalten Krieges & Zusammenbruch der UdSSR", 4),                  # 4.7

    # 5 Dekolonisation & Dritte Welt
    ("Dekolonisation in Asien & Afrika", 4),                                   # 5.1
    ("Indien, Algerien, Kongo & Vietnam", 3),                                  # 5.2
    ("Blockfreie Bewegung & Bandung-Konferenz", 3),                            # 5.3
    ("Entwicklungspolitik & Nord-Süd-Konflikt", 3),                            # 5.4
    ("Postkoloniale Perspektiven", 2),                                         # 5.5

    # 6 Gesellschaft & Kultur nach 1945
    ("Sozialstaat & Konsumgesellschaft", 4),                                   # 6.1
    ("68er-Bewegung & neue soziale Bewegungen", 4),                            # 6.2
    ("Frauenbewegung & Geschlechterrollenwandel", 3),                          # 6.3
    ("Bildungsreformen & Bildungsexpansion", 3),                               # 6.4
    ("Jugendkulturen & Populärkultur", 3),                                     # 6.5
    ("Religion, Säkularisierung & Wertewandel", 3),                            # 6.6
    ("Migration & Multikulturalität", 4),                                      # 6.7
    ("Gesundheitsgeschichte & Biopolitik", 2),                                 # 6.8

    # 7 Internationale Ordnung & Globalisierung (seit 1990)
    ("Globalisierung: Ökonomie, Kommunikation, Mobilität", 4),                 # 7.1
    ("Europäische Integration (Maastricht, EU-Erweiterung)", 4),               # 7.2
    ("USA als Hegemon & Globalpolitik nach 1991", 3),                          # 7.3
    ("Kriege im Nahen Osten & Terrorismus", 4),                                # 7.4
    ("9/11 & ‚Krieg gegen den Terror‘", 4),                                    # 7.5
    ("China, Russland & neue Großmachtkonflikte", 3),                          # 7.6
    ("Internationale Organisationen (UNO, WTO, WHO)", 3),                      # 7.7
    ("Flucht, Migration & geopolitische Krisen", 3),                           # 7.8

    # 8 Umwelt, Technik & Wissenschaft
    ("Atomzeitalter & Kernenergie", 3),                                        # 8.1
    ("Raumfahrt & Wissenschaftswettlauf", 3),                                  # 8.2
    ("Technologische Revolution (Computer, Internet)", 4),                     # 8.3
    ("Umweltbewegung & Klimawandel", 4),                                       # 8.4
    ("Ernährung, Medizin & Biotechnologie", 3),                                # 8.5
    ("Energiekrisen & Nachhaltigkeit", 3),                                     # 8.6

    # 9 Erinnerung, Medien & politische Kultur
    ("Vergangenheitsbewältigung & Erinnerungskultur", 4),                      # 9.1
    ("Gedenkstätten, Denkmäler & Musealisierung", 3),                          # 9.2
    ("Medienwandel: Fernsehen, Internet, Social Media", 4),                    # 9.3
    ("Politische Kommunikation & Fake News", 3),                               # 9.4
    ("Geschichtspolitik & kollektives Gedächtnis", 4),                         # 9.5

    # 10 Zeitgeschichte im 21. Jahrhundert
    ("Finanzkrise 2008 & Eurokrise", 4),                                       # 10.1
    ("Arabischer Frühling & autoritäre Regime", 3),                            # 10.2
    ("Klimakrise & Fridays for Future", 3),                                    # 10.3
    ("COVID-19-Pandemie & Gesellschaft", 4),                                   # 10.4
    ("Krieg in der Ukraine (ab 2022)", 4),                                     # 10.5
    ("Künstliche Intelligenz & digitale Transformation", 3),                   # 10.6
    ("Polarisierung & Populismus", 3),                                         # 10.7
    ("Globale Zukunftsfragen & Szenarien", 2),                                 # 10.8
]
