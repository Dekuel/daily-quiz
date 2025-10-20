# -*- coding: utf-8 -*-
# Unterkategorien/Geschichte/antike.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Antike“.
Diese Liste wird von kategorien/geschichte.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte
"""

SUBDISCIPLINES = [
    # 1 Frühantike Hochkulturen
    ("Frühantike Hochkulturen (Überblick)", 4),                              # 1
    ("Mesopotamien: Sumerer, Babylonier, Assyrer", 4),                        # 1.1
    ("Ägypten: Altes, Mittleres und Neues Reich", 4),                         # 1.2
    ("Pharaonentum & göttliche Herrschaft", 3),                               # 1.2.1
    ("Pyramidenbau & Grabkultur", 3),                                         # 1.2.2
    ("Schriftentwicklung: Keilschrift & Hieroglyphen", 3),                    # 1.3
    ("Rechtssysteme (z. B. Codex Hammurapi)", 3),                             # 1.4
    ("Handel & frühe Stadtstaaten", 2),                                       # 1.5
    ("Frühe Wissenschaften (Astronomie, Mathematik)", 2),                     # 1.6

    # 2 Griechenland
    ("Antikes Griechenland (Überblick)", 4),                                  # 2
    ("Mykenische & minoische Kultur", 3),                                     # 2.1
    ("Dunkle Jahrhunderte & Entstehung der Polis", 3),                        # 2.2
    ("Polis-System: Athen & Sparta", 4),                                      # 2.3
    ("Demokratie in Athen", 4),                                               # 2.3.1
    ("Spartanisches System & Heloten", 3),                                    # 2.3.2
    ("Perserkriege", 4),                                                      # 2.4
    ("Peloponnesischer Krieg", 4),                                            # 2.5
    ("Griechische Kolonisation", 3),                                          # 2.6
    ("Hellenistische Zeit (Alexander der Große)", 4),                         # 2.7
    ("Kultur & Philosophie der Antike (Griechenland)", 4),                    # 2.8
    ("Mythologie & Religion", 3),                                             # 2.9
    ("Architektur & Kunst (Tempel, Skulptur)", 3),                            # 2.10
    ("Philosophen: Sokrates, Platon, Aristoteles", 4),                        # 2.11
    ("Wissenschaft & Mathematik (Euklid, Archimedes)", 3),                    # 2.12
    ("Olympische Spiele & Panhellenismus", 2),                                # 2.13

    # 3 Römische Geschichte
    ("Römische Antike (Überblick)", 4),                                       # 3
    ("Frühzeit & Königszeit Roms", 3),                                        # 3.1
    ("Römische Republik", 4),                                                 # 3.2
    ("Senat & Magistrate", 3),                                                # 3.2.1
    ("Ständekämpfe (Patrizier vs. Plebejer)", 3),                             # 3.2.2
    ("Ausdehnung Italiens & Punische Kriege", 4),                             # 3.3
    ("Hannibal & Rom-Karthago-Konflikt", 3),                                  # 3.3.1
    ("Krise der Republik & Bürgerkriege", 4),                                 # 3.4
    ("Caesar, Pompeius, Crassus (Triumvirat)", 3),                            # 3.4.1
    ("Übergang zur Kaiserzeit (Augustus)", 4),                                # 3.5
    ("Römisches Kaiserreich: Prinzipat & Dominat", 4),                        # 3.6
    ("Pax Romana", 3),                                                        # 3.6.1
    ("Römische Armee & Verwaltung", 3),                                       # 3.7
    ("Provinzsystem & Romanisierung", 3),                                     # 3.8
    ("Recht & Gesellschaft (Zwölftafelgesetz, ius civile)", 4),               # 3.9
    ("Sklaverei & soziale Strukturen", 3),                                    # 3.10
    ("Kaiserzeit: Nero bis Commodus", 2),                                     # 3.11
    ("Spätantike & Völkerwanderung", 3),                                      # 3.12
    ("Untergang des Weströmischen Reichs", 4),                                # 3.13

    # 4 Kultur, Wissenschaft und Alltag
    ("Alltag in der Antike", 3),                                              # 4.1
    ("Familie & Frauenrolle", 2),                                             # 4.1.1
    ("Bildung & Erziehung (paideia)", 3),                                     # 4.1.2
    ("Religion & Kulte (Mysterienkulte, Isis, Mithras)", 3),                  # 4.2
    ("Philosophie der Spätantike (Stoiker, Epikureer)", 3),                   # 4.3
    ("Literatur (Epen, Tragödien, Komödien)", 3),                             # 4.4
    ("Rhetorik & Geschichtsschreibung", 3),                                   # 4.5
    ("Architektur & Städtebau (Forum, Amphitheater)", 4),                     # 4.6
    ("Technik & Ingenieurskunst (Aquädukte, Straßenbau)", 3),                 # 4.7
    ("Wissenschaftliche Errungenschaften (Medizin, Astronomie)", 2),          # 4.8
    ("Kleidung, Ernährung, Hygiene", 2),                                      # 4.9

    # 5 Antike im Mittelmeerraum & Kontaktzonen
    ("Handel & Wirtschaft im Mittelmeerraum", 3),                             # 5.1
    ("Phönizier & Karthago", 3),                                              # 5.2
    ("Etrusker & frühes Italien", 2),                                         # 5.3
    ("Kelten & Germanen im Kontakt mit Rom", 3),                              # 5.4
    ("Persisches Großreich (Achaimeniden)", 4),                               # 5.5
    ("Hellenistische Königreiche (Ptolemäer, Seleukiden)", 3),                # 5.6
    ("Beziehungen Rom–Orient", 3),                                            # 5.7
    ("Afrika & Nubien in der Antike", 2),                                     # 5.8
    ("China & Seidenstraße (frühe Kontakte)", 2),                             # 5.9

    # 6 Übergänge und Nachwirkungen
    ("Übergang von Antike zu Mittelalter", 4),                                # 6.1
    ("Christianisierung & Konstantin der Große", 4),                          # 6.2
    ("Spätantike Philosophie (Neuplatonismus)", 3),                           # 6.3
    ("Byzanz als Fortsetzung der Antike", 3),                                 # 6.4
    ("Römisches Erbe im Mittelalter", 3),                                     # 6.5
    ("Rezeption der Antike in Renaissance & Humanismus", 3),                  # 6.6
    ("Antikenbild in der Moderne", 2),                                        # 6.7
]
