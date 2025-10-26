# -*- coding: utf-8 -*-
# Unterkategorien/Geschichte/mittelalter.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Mittelalter“.
Diese Liste wird von kategorien/geschichte.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Einheitliche Skala & Struktur (analog zu den Religion-/Antike-Modulen)
==========================================================================
- Skala 1–10: 1 = Allgemeinwissen, 10 = Expertenwissen
- min = Bekanntheit (Population Familiarity)
- max = inhaltliche/methodische Tiefe (Conceptual Depth)
- „Basis…“-Kategorien haben immer min = 1 (Zuordnung, Namen, einfache Fakten)
- Nicht-Basis-Themen können i. d. R. bis 10 gehen (Vertiefbarkeit durch Forschung)
"""

SUBDISCIPLINES = [
    # 1 Periodisierung & Grundzüge
    ("Mittelalter: Periodisierung & Epochenüberblick", 4, (2,10)),                 # 1
    ("Spätantike → Frühmittelalter (Transformation)", 4, (3,10)),                  # 1.1
    ("Frühmittelalter (ca. 500–1050)", 4, (2,10)),                                 # 1.2
    ("Hochmittelalter (ca. 1050–1250)", 4, (2,10)),                                # 1.3
    ("Spätmittelalter (ca. 1250–1500)", 4, (2,10)),                                # 1.4
    ("Quellenkunde & Geschichtsschreibung (Annalen, Chroniken)", 3, (4,10)),       # 1.5
    ("Raumkonzepte: lateinisches Europa, Byzanz, islamische Welt", 3, (3,10)),     # 1.6
    # ⚑ Basis
    ("Basis – Mittelalter allgemein (Begriffe, Zeitspannen, Leitereignisse)", 2, (1,7)),

    # 2 Frühmittelalterliche Herrschaften
    ("Völkerwanderung & Reichsbildungen", 3, (3,10)),                               # 2.1
    ("Merowinger & Frankenreich", 3, (3,10)),                                       # 2.2
    ("Karolinger & karolingische Renaissance", 4, (3,10)),                          # 2.3
    ("Reichsidee & Kaiserkrönung 800", 3, (3,10)),                                  # 2.3.1
    ("Teilungen (Verdun 843) & Nachfolgereiche", 3, (3,10)),                        # 2.3.2
    ("Ottonen, Salier, Staufer (Regnum Teutonicum)", 4, (3,10)),                    # 2.4
    ("Angelsachsen & Normannen (1066)", 3, (2,10)),                                 # 2.5
    ("Skandinavien: Christianisierung & Reichsbildung", 2, (2,9)),                  # 2.6
    # ⚑ Basis
    ("Basis – Frühmittelalter (Dynastien, Daten, Herrscher)", 2, (1,7)),

    # 3 Kirche, Religion & Frömmigkeit
    ("Christianisierung Europas", 4, (2,10)),                                       # 3.1
    ("Klosterwesen: Benediktiner, Zisterzienser, Cluny", 4, (3,10)),                # 3.2
    ("Bettelorden: Franziskaner & Dominikaner", 3, (3,10)),                         # 3.3
    ("Investiturstreit & Kirchenreformen (Gregor VII.)", 4, (4,10)),                # 3.4
    ("Papsttum, Konzilien & Kirchenrecht", 3, (4,10)),                               # 3.5
    ("Frömmigkeitsformen, Reliquienkult, Pilgerwesen", 3, (2,9)),                   # 3.6
    ("Häresien & Inquisition (Albigenser, Waldenser)", 3, (4,10)),                  # 3.7
    ("Judentum im mittelalterlichen Europa", 3, (3,10)),                             # 3.8
    ("Islamische Theologie & Gelehrsamkeit (Überblick)", 2, (3,9)),                 # 3.9
    # ⚑ Basis
    ("Basis – Kirche & Frömmigkeit (Orden, Ämter, Praktiken)", 2, (1,7)),

    # 4 Kreuzzüge & Kontaktzonen
    ("Kreuzzüge: Ursachen, Verlauf, Folgen", 4, (3,10)),                            # 4.1
    ("Erster Kreuzzug & Lateinische Staaten", 3, (3,10)),                           # 4.1.1
    ("Dritter Kreuzzug & Saladin", 3, (2,10)),                                      # 4.1.2
    ("Vierter Kreuzzug & Lateinisches Kaiserreich", 2, (3,9)),                      # 4.1.3
    ("Reconquista auf der Iberischen Halbinsel", 4, (3,10)),                        # 4.2
    ("Byzanz: Kontinuität & Konflikte", 3, (3,10)),                                  # 4.3
    ("Handelskontakte: Levante, Italien, Hanseraum", 3, (2,9)),                      # 4.4
    ("Mongolenreich & Europa", 2, (3,9)),                                           # 4.5
    # ⚑ Basis
    ("Basis – Kreuzzüge & Kontakte (Orte, Daten, Akteure)", 2, (1,7)),

    # 5 Herrschaft, Recht & Politik
    ("Feudalismus & Lehnswesen (Debatten, Modelle)", 4, (4,10)),                    # 5.1
    ("Königtum, Fürstenmacht & Reichsverfassung", 4, (4,10)),                       # 5.2
    ("Städte, Stadtrechte & Kommunalbewegungen", 4, (3,10)),                        # 5.3
    ("Recht: Gewohnheitsrecht, Sachsenspiegel, kanonisches Recht", 3, (3,10)),      # 5.4
    ("Rittertum & Hofkultur", 3, (2,9)),                                            # 5.5
    ("Turniere, Ehrenkodex, Minne", 2, (1,8)),                                      # 5.5.1
    ("Hundertjähriger Krieg", 4, (3,10)),                                           # 5.6
    ("Burgundische Machtpolitik", 2, (3,9)),                                        # 5.7
    ("Schottland, Wales & Irland im Mittelalter", 2, (2,9)),                        # 5.8
    ("Osteuropa: Piasten, Árpáden, Kiewer Rus", 2, (3,9)),                          # 5.9
    # ⚑ Basis
    ("Basis – Herrschaft & Recht (Ämter, Begriffe, Institutionen)", 2, (1,7)),

    # 6 Wirtschaft, Gesellschaft & Umwelt
    ("Agrarrevolution des Hochmittelalters (Dreifelderwirtschaft)", 4, (3,10)),     # 6.1
    ("Bevölkerungswachstum & Binnenkolonisation", 3, (3,10)),                       # 6.2
    ("Gilden & Zünfte, Arbeit & Löhne", 3, (2,9)),                                  # 6.3
    ("Fernhandel: Hanse, Champagne-Messen, Mittelmeerhandel", 4, (3,10)),           # 6.4
    ("Münz- & Geldwesen, Banken (Medici, Fugger – spät)", 2, (3,9)),               # 6.5
    ("Ländliche Gesellschaft & Grundherrschaft", 4, (3,10)),                         # 6.6
    ("Familiensysteme, Ehe & Erbrecht", 2, (2,9)),                                  # 6.7
    ("Ernährung, Klima & Umwelt (Mittelalterliche Warmzeit)", 3, (3,10)),           # 6.8
    ("Stadt-Land-Beziehungen", 2, (2,9)),                                           # 6.9
    # ⚑ Basis
    ("Basis – Wirtschaft & Gesellschaft (Begriffe, Beispiele)", 2, (1,7)),

    # 7 Kultur, Bildung & Wissenschaft
    ("Romanik & Gotik (Architektur, Skulptur)", 4, (2,10)),                         # 7.1
    ("Bildung: Domschulen, Universitäten (Bologna, Paris, Oxford)", 4, (3,10)),     # 7.2
    ("Scholastik (Thomas von Aquin, Ockham)", 4, (4,10)),                            # 7.3
    ("Literatur: Epen, Artusstoff, Minnesang", 3, (2,9)),                            # 7.4
    ("Buchkultur, Skriptorien & Pergament", 3, (3,10)),                              # 7.5
    ("Musik & Liturgie", 2, (2,9)),                                                 # 7.6
    ("Wissenschaft: Medizin, Astronomie, Naturkunde", 3, (3,10)),                   # 7.7
    ("Übersetzungsbewegungen (Toledo, Sizilien)", 3, (3,10)),                       # 7.8
    ("Technik: Mühlen, Uhr, Brille, Schiffbau", 3, (2,9)),                           # 7.9
    # ⚑ Basis
    ("Basis – Kultur & Bildung (Stile, Orte, Personen)", 2, (1,7)),

    # 8 Krankheit, Krisen & Wandel
    ("Pest (Schwarzer Tod) & demografische Folgen", 4, (3,10)),                     # 8.1
    ("Hungersnöte & Preisrevolutionen (spätmittelalterlich)", 3, (3,10)),           # 8.2
    ("Soziale Unruhen: Jacquerie, Ciompi, Bauernkriege (Vorläufe)", 3, (3,10)),     # 8.3
    ("Religiöse Krisen & Schisma (Avignon, Konziliarismus)", 4, (4,10)),            # 8.4
    ("Militärischer Wandel: Langbogen, Söldnerheere", 3, (3,10)),                   # 8.5
    ("Staatsbildung & Verwaltung (England, Frankreich)", 3, (3,10)),                # 8.6
    ("Frühe Entdeckungen & Seewege (Vorstufen)", 2, (2,9)),                         # 8.7
    # ⚑ Basis
    ("Basis – Krisen & Wandel (Begriffe, Daten, Folgen)", 2, (1,7)),

    # 9 Alltag, Mentalitäten & Rechtspraxis
    ("Alltagsleben: Wohnen, Ernährung, Kleidung, Hygiene", 3, (2,9)),               # 9.1
    ("Geschlechterrollen & Frauen in der Stadt/auf dem Land", 3, (3,9)),            # 9.2
    ("Kindheit, Jugend & Lebenszyklen", 2, (2,9)),                                  # 9.3
    ("Kriminalität, Strafen & Gerichtspraxis", 3, (3,10)),                           # 9.4
    ("Feste, Bräuche & Jahreslauf", 2, (1,8)),                                      # 9.5
    ("Randgruppen: Bettler, Außenseiter, Minderheiten", 2, (2,9)),                  # 9.6
    # ⚑ Basis
    ("Basis – Alltag & Mentalitäten (einfache Zuordnungen/Beispiele)", 2, (1,7)),

    # 10 Außereuropäische Bezüge (Vergleich & Austausch)
    ("Islamische Reiche: Umayyaden, Abbasiden, Andalusien", 4, (3,10)),             # 10.1
    ("Fatimiden, Mamluken & osmanische Anfänge", 3, (3,10)),                        # 10.2
    ("Byzantinisches Reich (lange Dauer, Kulturtransfer)", 4, (3,10)),              # 10.3
    ("Ostasien: Song/Yuan, Technik- und Wissensaustausch", 2, (2,9)),               # 10.4
    ("Transkontinentale Netzwerke: Seidenstraße & Gewürzhandel", 3, (3,10)),        # 10.5
    # ⚑ Basis
    ("Basis – Außereuropäische Bezüge (Regionen, Routen, Güter)", 2, (1,7)),

    # 11 Übergang zur Frühen Neuzeit & Nachwirkungen
    ("Renaissance & Humanismus (Italien, Nordalpen)", 4, (3,10)),                   # 11.1
    ("Buchdruck (Gutenberg) & Medienwandel", 4, (2,10)),                             # 11.2
    ("Reformation: Vorläufer (Hus, Wyclif)", 3, (3,10)),                             # 11.3
    ("Entdeckungsfahrten & Globalisierungsschub", 3, (3,10)),                        # 11.4
    ("Kontinuitäten/Brüche um 1500 (‚Mittelalterbild‘)", 3, (3,10)),                 # 11.5
    # ⚑ Basis
    ("Basis – Übergang & Nachwirkungen (Begriffe, Personen, Daten)", 2, (1,7)),
]
