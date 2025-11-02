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
    ("Mittelalter: Periodisierung & Epochenüberblick", 7, (3,10)),                 # 1
    ("Spätantike → Frühmittelalter (Transformation)", 7, (5,10)),                  # 1.1
    ("Frühmittelalter (ca. 500–1050)", 7, (3,10)),                                 # 1.2
    ("Hochmittelalter (ca. 1050–1250)", 7, (3,10)),                                # 1.3
    ("Spätmittelalter (ca. 1250–1500)", 7, (3,10)),                                # 1.4
    ("Quellenkunde & Geschichtsschreibung (Annalen, Chroniken)", 5, (7,10)),       # 1.5
    ("Raumkonzepte: lateinisches Europa, Byzanz, islamische Welt", 5, (5,10)),     # 1.6
    # ⚑ Basis
    ("Basis – Mittelalter allgemein (Begriffe, Zeitspannen, Leitereignisse)", 3, (1,10)),

    # 2 Frühmittelalterliche Herrschaften
    ("Völkerwanderung & Reichsbildungen", 5, (5,10)),                               # 2.1
    ("Merowinger & Frankenreich", 5, (5,10)),                                       # 2.2
    ("Karolinger & karolingische Renaissance", 7, (5,10)),                          # 2.3
    ("Reichsidee & Kaiserkrönung 800", 5, (5,10)),                                  # 2.3.1
    ("Teilungen (Verdun 843) & Nachfolgereiche", 5, (5,10)),                        # 2.3.2
    ("Ottonen, Salier, Staufer (Regnum Teutonicum)", 7, (5,10)),                    # 2.4
    ("Angelsachsen & Normannen (1066)", 5, (3,10)),                                 # 2.5
    ("Skandinavien: Christianisierung & Reichsbildung", 3, (3,10)),                 # 2.6
    # ⚑ Basis
    ("Basis – Frühmittelalter (Dynastien, Daten, Herrscher)", 3, (1,10)),

    # 3 Kirche, Religion & Frömmigkeit
    ("Christianisierung Europas", 7, (3,10)),                                       # 3.1
    ("Klosterwesen: Benediktiner, Zisterzienser, Cluny", 7, (5,10)),                # 3.2
    ("Bettelorden: Franziskaner & Dominikaner", 5, (5,10)),                         # 3.3
    ("Investiturstreit & Kirchenreformen (Gregor VII.)", 7, (7,10)),                # 3.4
    ("Papsttum, Konzilien & Kirchenrecht", 5, (7,10)),                               # 3.5
    ("Frömmigkeitsformen, Reliquienkult, Pilgerwesen", 5, (3,10)),                  # 3.6
    ("Häresien & Inquisition (Albigenser, Waldenser)", 5, (7,10)),                  # 3.7
    ("Judentum im mittelalterlichen Europa", 5, (5,10)),                             # 3.8
    ("Islamische Theologie & Gelehrsamkeit (Überblick)", 3, (5,10)),                # 3.9
    # ⚑ Basis
    ("Basis – Kirche & Frömmigkeit (Orden, Ämter, Praktiken)", 3, (1,10)),

    # 4 Kreuzzüge & Kontaktzonen
    ("Kreuzzüge: Ursachen, Verlauf, Folgen", 7, (5,10)),                            # 4.1
    ("Erster Kreuzzug & Lateinische Staaten", 5, (5,10)),                           # 4.1.1
    ("Dritter Kreuzzug & Saladin", 5, (3,10)),                                      # 4.1.2
    ("Vierter Kreuzzug & Lateinisches Kaiserreich", 3, (5,10)),                     # 4.1.3
    ("Reconquista auf der Iberischen Halbinsel", 7, (5,10)),                        # 4.2
    ("Byzanz: Kontinuität & Konflikte", 5, (5,10)),                                  # 4.3
    ("Handelskontakte: Levante, Italien, Hanseraum", 5, (3,10)),                     # 4.4
    ("Mongolenreich & Europa", 3, (5,10)),                                          # 4.5
    # ⚑ Basis
    ("Basis – Kreuzzüge & Kontakte (Orte, Daten, Akteure)", 3, (1,10)),

    # 5 Herrschaft, Recht & Politik
    ("Feudalismus & Lehnswesen (Debatten, Modelle)", 7, (7,10)),                    # 5.1
    ("Königtum, Fürstenmacht & Reichsverfassung", 7, (7,10)),                       # 5.2
    ("Städte, Stadtrechte & Kommunalbewegungen", 7, (5,10)),                        # 5.3
    ("Recht: Gewohnheitsrecht, Sachsenspiegel, kanonisches Recht", 5, (5,10)),      # 5.4
    ("Rittertum & Hofkultur", 5, (3,10)),                                           # 5.5
    ("Turniere, Ehrenkodex, Minne", 3, (1,10)),                                     # 5.5.1
    ("Hundertjähriger Krieg", 7, (5,10)),                                           # 5.6
    ("Burgundische Machtpolitik", 3, (5,10)),                                       # 5.7
    ("Schottland, Wales & Irland im Mittelalter", 3, (3,10)),                       # 5.8
    ("Osteuropa: Piasten, Árpáden, Kiewer Rus", 3, (5,10)),                         # 5.9
    # ⚑ Basis
    ("Basis – Herrschaft & Recht (Ämter, Begriffe, Institutionen)", 3, (1,10)),

    # 6 Wirtschaft, Gesellschaft & Umwelt
    ("Agrarrevolution des Hochmittelalters (Dreifelderwirtschaft)", 7, (5,10)),     # 6.1
    ("Bevölkerungswachstum & Binnenkolonisation", 5, (5,10)),                       # 6.2
    ("Gilden & Zünfte, Arbeit & Löhne", 5, (3,10)),                                  # 6.3
    ("Fernhandel: Hanse, Champagne-Messen, Mittelmeerhandel", 7, (5,10)),           # 6.4
    ("Münz- & Geldwesen, Banken (Medici, Fugger – spät)", 3, (5,10)),              # 6.5
    ("Ländliche Gesellschaft & Grundherrschaft", 7, (5,10)),                         # 6.6
    ("Familiensysteme, Ehe & Erbrecht", 3, (3,10)),                                  # 6.7
    ("Ernährung, Klima & Umwelt (Mittelalterliche Warmzeit)", 5, (5,10)),           # 6.8
    ("Stadt-Land-Beziehungen", 3, (3,10)),                                          # 6.9
    # ⚑ Basis
    ("Basis – Wirtschaft & Gesellschaft (Begriffe, Beispiele)", 3, (1,10)),

    # 7 Kultur, Bildung & Wissenschaft
    ("Romanik & Gotik (Architektur, Skulptur)", 7, (3,10)),                         # 7.1
    ("Bildung: Domschulen, Universitäten (Bologna, Paris, Oxford)", 7, (5,10)),     # 7.2
    ("Scholastik (Thomas von Aquin, Ockham)", 7, (7,10)),                            # 7.3
    ("Literatur: Epen, Artusstoff, Minnesang", 5, (3,10)),                            # 7.4
    ("Buchkultur, Skriptorien & Pergament", 5, (5,10)),                              # 7.5
    ("Musik & Liturgie", 3, (3,10)),                                                # 7.6
    ("Wissenschaft: Medizin, Astronomie, Naturkunde", 5, (5,10)),                   # 7.7
    ("Übersetzungsbewegungen (Toledo, Sizilien)", 5, (5,10)),                       # 7.8
    ("Technik: Mühlen, Uhr, Brille, Schiffbau", 5, (3,10)),                          # 7.9
    # ⚑ Basis
    ("Basis – Kultur & Bildung (Stile, Orte, Personen)", 3, (1,10)),

    # 8 Krankheit, Krisen & Wandel
    ("Pest (Schwarzer Tod) & demografische Folgen", 7, (5,10)),                     # 8.1
    ("Hungersnöte & Preisrevolutionen (spätmittelalterlich)", 5, (5,10)),           # 8.2
    ("Soziale Unruhen: Jacquerie, Ciompi, Bauernkriege (Vorläufe)", 5, (5,10)),     # 8.3
    ("Religiöse Krisen & Schisma (Avignon, Konziliarismus)", 7, (7,10)),            # 8.4
    ("Militärischer Wandel: Langbogen, Söldnerheere", 5, (5,10)),                   # 8.5
    ("Staatsbildung & Verwaltung (England, Frankreich)", 5, (5,10)),                # 8.6
    ("Frühe Entdeckungen & Seewege (Vorstufen)", 3, (3,10)),                         # 8.7
    # ⚑ Basis
    ("Basis – Krisen & Wandel (Begriffe, Daten, Folgen)", 3, (1,10)),

    # 9 Alltag, Mentalitäten & Rechtspraxis
    ("Alltagsleben: Wohnen, Ernährung, Kleidung, Hygiene", 5, (3,10)),               # 9.1
    ("Geschlechterrollen & Frauen in der Stadt/auf dem Land", 5, (5,10)),            # 9.2
    ("Kindheit, Jugend & Lebenszyklen", 3, (3,10)),                                  # 9.3
    ("Kriminalität, Strafen & Gerichtspraxis", 5, (5,10)),                            # 9.4
    ("Feste, Bräuche & Jahreslauf", 3, (1,10)),                                      # 9.5
    ("Randgruppen: Bettler, Außenseiter, Minderheiten", 3, (3,10)),                  # 9.6
    # ⚑ Basis
    ("Basis – Alltag & Mentalitäten (einfache Zuordnungen/Beispiele)", 3, (1,10)),

    # 10 Außereuropäische Bezüge (Vergleich & Austausch)
    ("Islamische Reiche: Umayyaden, Abbasiden, Andalusien", 7, (5,10)),             # 10.1
    ("Fatimiden, Mamluken & osmanische Anfänge", 5, (5,10)),                        # 10.2
    ("Byzantinisches Reich (lange Dauer, Kulturtransfer)", 7, (5,10)),              # 10.3
    ("Ostasien: Song/Yuan, Technik- und Wissensaustausch", 3, (3,10)),              # 10.4
    ("Transkontinentale Netzwerke: Seidenstraße & Gewürzhandel", 5, (5,10)),        # 10.5
    # ⚑ Basis
    ("Basis – Außereuropäische Bezüge (Regionen, Routen, Güter)", 3, (1,10)),

    # 11 Übergang zur Frühen Neuzeit & Nachwirkungen
    ("Renaissance & Humanismus (Italien, Nordalpen)", 7, (5,10)),                   # 11.1
    ("Buchdruck (Gutenberg) & Medienwandel", 7, (3,10)),                             # 11.2
    ("Reformation: Vorläufer (Hus, Wyclif)", 5, (5,10)),                             # 11.3
    ("Entdeckungsfahrten & Globalisierungsschub", 5, (5,10)),                        # 11.4
    ("Kontinuitäten/Brüche um 1500 (‚Mittelalterbild‘)", 5, (5,10)),                 # 11.5
    # ⚑ Basis
    ("Basis – Übergang & Nachwirkungen (Begriffe, Personen, Daten)", 3, (1,10)),
]
