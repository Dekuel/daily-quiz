# -*- coding: utf-8 -*-
# Unterkategorien/Physik/kern_und_teilchenphysik.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Kern- und Teilchenphysik“.
Diese Liste wird von kategorien/physik.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Spezialthemen
"""

SUBDISCIPLINES = [
    # 1 Hors d’œuvre
    ("Grundbausteine der Materie", 4),                              # 1.1
    ("Fundamentale Wechselwirkungen", 4),                           # 1.2
    ("Symmetrien und Erhaltungssätze", 4),                          # 1.3
    ("Experimente (Überblick)", 2),                                 # 1.4
    ("Einheiten (natürliche Einheiten)", 3),                         # 1.5

    # Teil I – Analyse: Bausteine der Materie
    # 2 Globale Eigenschaften der Kerne
    ("Atom und seine Bausteine", 3),                                # 2.1
    ("Nuklide & Nuklidkarte", 3),                                   # 2.2
    ("Parametrisierung der Bindungsenergie (Weizsäcker)", 4),       # 2.3
    ("Ladungsunabhängigkeit der Kernkraft & Isospin", 3),           # 2.4

    # 3 Stabilität der Kerne
    ("β‑Zerfall (β±, EC)", 4),                                      # 3.1
    ("α‑Zerfall", 3),                                               # 3.2
    ("Kernspaltung", 4),                                            # 3.3
    ("Zerfall angeregter Kernzustände (γ, isomer)", 3),             # 3.4

    # 4 Streuung
    ("Allgemeine Betrachtung von Streuprozessen", 3),               # 4.1
    ("Wirkungsquerschnitt & differentielle Größen", 4),             # 4.2
    ("Goldene Regel (Fermi)", 4),                                   # 4.3
    ("Feynman‑Diagramme (Streuprozesse)", 4),                       # 4.4

    # 5 Geometrische Gestalt der Kerne
    ("Kinematik der Elektronenstreuung", 3),                        # 5.1
    ("Rutherford‑Wirkungsquerschnitt", 3),                          # 5.2
    ("Mott‑Wirkungsquerschnitt", 3),                                # 5.3
    ("Kern‑Formfaktoren", 4),                                       # 5.4
    ("Inelastische Kernanregungen", 3),                             # 5.5

    # 6 Elastische Streuung am Nukleon
    ("Formfaktoren des Nukleons", 4),                               # 6.1
    ("Quasielastische Streuung", 3),                                # 6.2
    ("Ladungsradius von Pionen und Kaonen", 2),                     # 6.3

    # 7 Tiefinelastische Streuung
    ("Angeregte Nukleonzustände", 3),                               # 7.1
    ("Strukturfunktionen (F1, F2,…)", 4),                            # 7.2
    ("Partonmodell", 4),                                            # 7.3
    ("Interpretation der Strukturfunktionen (Partonmodell)", 3),    # 7.4

    # 8 Quarks, Gluonen und starke WW (QCD)
    ("Quarkstruktur der Nukleonen", 4),                             # 8.1
    ("Quarks in Hadronen (Flavor, Farbladung)", 3),                 # 8.2
    ("Quark‑Gluon‑Wechselwirkung (QCD)", 4),                         # 8.3
    ("Skalenbrechung (Scaling Violation)", 3),                       # 8.4

    # 9 e+e−‑Kollisionen
    ("Leptonpaar‑Erzeugung", 3),                                    # 9.1
    ("Resonanzen (Breit‑Wigner)", 3),                               # 9.2
    ("Nichtresonante Hadronerzeugung (R‑Verhältnis)", 3),           # 9.3
    ("Gluonenabstrahlung (Jets)", 3),                                # 9.4

    # 10 Phänomenologie der schwachen Wechselwirkung
    ("Eigenschaften der Leptonen", 3),                               # 10.1
    ("Typen der schwachen Wechselwirkung (CC/NC)", 4),              # 10.2
    ("Kopplungsstärke des geladenen Stroms (G_F)", 3),               # 10.3
    ("Quarkfamilien (CKM)", 3),                                      # 10.4
    ("Leptonische Familien", 2),                                     # 10.5
    ("Majorana‑Neutrino?", 2),                                      # 10.6
    ("Paritätsverletzung", 4),                                       # 10.7
    ("Tiefinelastische Neutrinostreuung", 3),                        # 10.8

    # 11 Austauschbosonen der schwachen WW
    ("Reelle W‑ und Z‑Bosonen", 4),                                 # 11.1
    ("Elektroschwache Vereinheitlichung (SU(2)×U(1))", 4),          # 11.2
    ("Große Vereinheitlichung (GUT)", 2),                            # 11.3

    # 12 Standardmodell
    ("Überblick: Felder, Teilchen, Symmetrien des Standardmodells", 4), # 12

    # Teil II – Synthese: Zusammengesetzte Systeme
    # 13 Quarkonia
    ("Analoga: Wasserstoff & Positronium", 2),                       # 13.1
    ("Charmonium", 3),                                               # 13.2
    ("Quark‑Antiquark‑Potential (Confinement)", 4),                  # 13.3
    ("Farbmagnetische Wechselwirkung", 3),                           # 13.4
    ("Bottonium & Toponium", 2),                                     # 13.5
    ("Zerfallskanäle schwerer Quarkonia", 2),                        # 13.6
    ("QCD‑Test aus Zerfallsbreiten", 2),                              # 13.7

    # 14 Mesonen aus leichten Quarks
    ("Meson‑Multipletts (SU(3))", 3),                                # 14.1
    ("Massen der Mesonen", 2),                                       # 14.2
    ("Zerfallskanäle (Mesonen)", 2),                                 # 14.3
    ("Zerfall des neutralen Kaons (CP‑Verletzung)", 3),              # 14.4

    # 15 Baryonen
    ("Erzeugung & Nachweis von Baryonen", 2),                        # 15.1
    ("Baryon‑Multipletts", 3),                                       # 15.2
    ("Massen der Baryonen", 2),                                      # 15.3
    ("Magnetische Momente von Baryonen", 3),                         # 15.4
    ("Semileptonische Baryon‑Zerfälle", 2),                           # 15.5
    ("Konstituentenquark‑Modell: Validität", 2),                      # 15.6

    # 16 Kernkraft
    ("Nukleon‑Nukleon‑Streuung", 3),                                 # 16.1
    ("Das Deuteron", 3),                                             # 16.2
    ("Charakter der Kernkraft", 3),                                   # 16.3

    # 17 Aufbau der Kerne
    ("Fermigasmodell", 3),                                            # 17.1
    ("Hyperkerne", 2),                                                # 17.2
    ("Schalenmodell", 4),                                             # 17.3
    ("Deformierte Kerne", 3),                                         # 17.4
    ("Spektroskopie mittels Kernreaktionen", 2),                      # 17.5
    ("β‑Zerfall des Kerns", 3),                                       # 17.6
    ("Doppelter β‑Zerfall", 2),                                       # 17.7

    # 18 Kollektive Kernanregungen
    ("Elektromagnetische Übergänge", 3),                              # 18.1
    ("Dipolschwingungen", 2),                                         # 18.2
    ("Formschwingungen", 2),                                          # 18.3
    ("Rotationszustände", 2),                                         # 18.4

    # 19 Nukleare Thermodynamik
    ("Thermodynamische Beschreibung der Kerne", 2),                   # 19.1
    ("Compoundkern & Quantenchaos", 2),                               # 19.2
    ("Phasen der Kernmaterie", 2),                                     # 19.3
    ("Frühes Universum: Teilchenphysik & Thermodynamik", 2),          # 19.4
    ("Sternentwicklung & Elementsynthese", 3),                         # 19.5

    # 20 Vielkörpersysteme der starken WW
    ("Vielkörpersysteme der starken Wechselwirkung", 2),              # 20

    # Anhang (nützlich für Fragenkontext)
    ("Beschleuniger (Arten & Prinzipien)", 2),                         # A.1
    ("Detektoren (Nachweismethoden)", 3),                              # A.2
    ("Kopplung von Drehimpulsen (J‑Kopplung)", 2),                     # A.3
    ("Naturkonstanten (Fundamentalwerte)", 2),                         # A.4
]
