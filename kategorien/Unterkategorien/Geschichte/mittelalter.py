# -*- coding: utf-8 -*-
# Unterkategorien/Geschichte/mittelalter.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Mittelalter“.
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
    ("Mittelalter: Periodisierung & Epochenüberblick", 4),                    # 1
    ("Spätantike → Frühmittelalter (Transformation)", 4),                      # 1.1
    ("Frühmittelalter (ca. 500–1050)", 4),                                     # 1.2
    ("Hochmittelalter (ca. 1050–1250)", 4),                                    # 1.3
    ("Spätmittelalter (ca. 1250–1500)", 4),                                    # 1.4
    ("Quellenkunde & Geschichtsschreibung (Annalen, Chroniken)", 3),          # 1.5
    ("Raumkonzepte: lateinisches Europa, Byzanz, islamische Welt", 3),        # 1.6

    # 2 Frühmittelalterliche Herrschaften
    ("Völkerwanderung & Reichsbildungen", 3),                                  # 2.1
    ("Merowinger & Frankenreich", 3),                                          # 2.2
    ("Karolinger & karolingische Renaissance", 4),                             # 2.3
    ("Reichsidee & Kaiserkrönung 800", 3),                                     # 2.3.1
    ("Teilungen (Verdun 843) & Nachfolgereiche", 3),                           # 2.3.2
    ("Ottonen, Salier, Staufer (Regnum Teutonicum)", 4),                       # 2.4
    ("Angelsachsen & Normannen (1066)", 3),                                    # 2.5
    ("Skandinavien: Christianisierung & Reichsbildung", 2),                    # 2.6

    # 3 Kirche, Religion & Frömmigkeit
    ("Christianisierung Europas", 4),                                          # 3.1
    ("Klosterwesen: Benediktiner, Zisterzienser, Cluny", 4),                   # 3.2
    ("Bettelorden: Franziskaner & Dominikaner", 3),                            # 3.3
    ("Investiturstreit & Kirchenreformen (Gregor VII.)", 4),                   # 3.4
    ("Papsttum, Konzilien & Kirchenrecht", 3),                                 # 3.5
    ("Frömmigkeitsformen, Reliquienkult, Pilgerwesen", 3),                     # 3.6
    ("Häresien & Inquisition (Albigenser, Waldenser)", 3),                     # 3.7
    ("Judentum im mittelalterlichen Europa", 3),                               # 3.8
    ("Islamische Theologie & Gelehrsamkeit (Überblick)", 2),                   # 3.9

    # 4 Kreuzzüge & Kontaktzonen
    ("Kreuzzüge: Ursachen, Verlauf, Folgen", 4),                               # 4.1
    ("Erster Kreuzzug & Lateinische Staaten", 3),                              # 4.1.1
    ("Dritter Kreuzzug & Saladin", 3),                                         # 4.1.2
    ("Vierter Kreuzzug & Lateinisches Kaiserreich", 2),                        # 4.1.3
    ("Reconquista auf der Iberischen Halbinsel", 4),                           # 4.2
    ("Byzanz: Kontinuität & Konflikte", 3),                                    # 4.3
    ("Handelskontakte: Levante, Italien, Hanseraum", 3),                       # 4.4
    ("Mongolenreich & Europa", 2),                                             # 4.5

    # 5 Herrschaft, Recht & Politik
    ("Feudalismus & Lehnswesen (Debatten, Modelle)", 4),                       # 5.1
    ("Königtum, Fürstenmacht & Reichsverfassung", 4),                          # 5.2
    ("Städte, Stadtrechte & Kommunalbewegungen", 4),                           # 5.3
    ("Recht: Gewohnheitsrecht, Sachsenspiegel, kanonisches Recht", 3),         # 5.4
    ("Rittertum & Hofkultur", 3),                                              # 5.5
    ("Turniere, Ehrenkodex, Minne", 2),                                        # 5.5.1
    ("Hundertjähriger Krieg", 4),                                              # 5.6
    ("Burgundische Machtpolitik", 2),                                          # 5.7
    ("Schottland, Wales & Irland im Mittelalter", 2),                          # 5.8
    ("Osteuropa: Piasten, Árpáden, Kiewer Rus", 2),                            # 5.9

    # 6 Wirtschaft, Gesellschaft & Umwelt
    ("Agrarrevolution des Hochmittelalters (Dreifelderwirtschaft)", 4),        # 6.1
    ("Bevölkerungswachstum & Binnenkolonisation", 3),                          # 6.2
    ("Gilden & Zünfte, Arbeit & Löhne", 3),                                    # 6.3
    ("Fernhandel: Hanse, Champagne-Messen, Mittelmeerhandel", 4),              # 6.4
    ("Münz- & Geldwesen, Banken (Medici, Fugger – spät)", 2),                  # 6.5
    ("Ländliche Gesellschaft & Grundherrschaft", 4),                            # 6.6
    ("Familiensysteme, Ehe & Erbrecht", 2),                                    # 6.7
    ("Ernährung, Klima & Umwelt (Mittelalterliche Warmzeit)", 3),              # 6.8
    ("Stadt-Land-Beziehungen", 2),                                             # 6.9

    # 7 Kultur, Bildung & Wissenschaft
    ("Romanik & Gotik (Architektur, Skulptur)", 4),                            # 7.1
    ("Bildung: Domschulen, Universitäten (Bologna, Paris, Oxford)", 4),        # 7.2
    ("Scholastik (Thomas von Aquin, Ockham)", 4),                              # 7.3
    ("Literatur: Epen, Artusstoff, Minnesang", 3),                              # 7.4
    ("Buchkultur, Skriptorien & Pergament", 3),                                # 7.5
    ("Musik & Liturgie", 2),                                                   # 7.6
    ("Wissenschaft: Medizin, Astronomie, Naturkunde", 3),                      # 7.7
    ("Übersetzungsbewegungen (Toledo, Sizilien)", 3),                          # 7.8
    ("Technik: Mühlen, Uhr, Brille, Schiffbau", 3),                            # 7.9

    # 8 Krankheit, Krisen & Wandel
    ("Pest (Schwarzer Tod) & demografische Folgen", 4),                        # 8.1
    ("Hungersnöte & Preisrevolutionen (spätmittelalterlich)", 3),              # 8.2
    ("Soziale Unruhen: Jacquerie, Ciompi, Bauernkriege (Vorläufe)", 3),        # 8.3
    ("Religiöse Krisen & Schisma (Avignon, Konziliarismus)", 4),               # 8.4
    ("Militärischer Wandel: Langbogen, Söldnerheere", 3),                      # 8.5
    ("Staatsbildung & Verwaltung (England, Frankreich)", 3),                   # 8.6
    ("Frühe Entdeckungen & Seewege (Vorstufen)", 2),                           # 8.7

    # 9 Alltag, Mentalitäten & Rechtspraxis
    ("Alltagsleben: Wohnen, Ernährung, Kleidung, Hygiene", 3),                 # 9.1
    ("Geschlechterrollen & Frauen in der Stadt/auf dem Land", 3),              # 9.2
    ("Kindheit, Jugend & Lebenszyklen", 2),                                     # 9.3
    ("Kriminalität, Strafen & Gerichtspraxis", 3),                              # 9.4
    ("Feste, Bräuche & Jahreslauf", 2),                                        # 9.5
    ("Randgruppen: Bettler, Außenseiter, Minderheiten", 2),                    # 9.6

    # 10 Außereuropäische Bezüge (Vergleich & Austausch)
    ("Islamische Reiche: Umayyaden, Abbasiden, Andalusien", 4),                # 10.1
    ("Fatimiden, Mamluken & osmanische Anfänge", 3),                           # 10.2
    ("Byzantinisches Reich (lange Dauer, Kulturtransfer)", 4),                 # 10.3
    ("Ostasien: Song/Yuan, Technik- und Wissensaustausch", 2),                 # 10.4
    ("Transkontinentale Netzwerke: Seidenstraße & Gewürzhandel", 3),           # 10.5

    # 11 Übergang zur Frühen Neuzeit & Nachwirkungen
    ("Renaissance & Humanismus (Italien, Nordalpen)", 4),                      # 11.1
    ("Buchdruck (Gutenberg) & Medienwandel", 4),                               # 11.2
    ("Reformation: Vorläufer (Hus, Wyclif)", 3),                               # 11.3
    ("Entdeckungsfahrten & Globalisierungsschub", 3),                          # 11.4
    ("Kontinuitäten/Brüche 1500 (‚Mittelalterbild‘)", 3),                      # 11.5
]
