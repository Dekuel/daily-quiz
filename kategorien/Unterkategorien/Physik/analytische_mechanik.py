# -*- coding: utf-8 -*-
# Unterkategorien/Physik/analytische_mechanik.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Analytische Mechanik“.
Diese Liste wird von kategorien/physik.py importiert und dient nur als Datenquelle
für die Subthema-Auswahl im Prompt. Die Gewichte sind heuristisch:
- 4 = Kernkonzepte / besonders fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Randnotizen / Kontext
"""

SUBDISCIPLINES = [
    # 1 Lagrange-Mechanik
    ("Zwangsbedingungen & generalisierte Koordinaten", 4),                 # 1.1
    ("Holonome Zwangsbedingungen", 3),                                     # 1.1.1
    ("Nicht-holonome Zwangsbedingungen", 3),                               # 1.1.2

    ("d’Alembert’sches Prinzip", 4),                                       # 1.2
    ("Lagrange-Gleichungen", 4),                                           # 1.2.1 / 1.3.3
    ("Einfache Anwendungen der Lagrange-Gleichungen", 3),                  # 1.2.2
    ("Verallgemeinerte Potentiale", 3),                                    # 1.2.3
    ("Reibung in der Lagrange-Formulierung", 2),                           # 1.2.4
    ("Nicht-holonome Systeme (Lagrange)", 3),                               # 1.2.5
    ("Methode der Lagrange’schen Multiplikatoren (Zwangskräfte)", 4),      # 1.2.6

    ("Hamilton’sches Prinzip (Prinzip der stationären Wirkung)", 4),      # 1.3
    ("Formulierung des Hamilton’schen Prinzips", 3),                       # 1.3.1
    ("Elemente der Variationsrechnung", 3),                                # 1.3.2
    ("Erweiterungen des Hamilton’schen Prinzips", 2),                      # 1.3.4

    ("Erhaltungssätze in der Lagrange-Mechanik", 4),                        # 1.4
    ("Noether-Idee: Homogenität der Zeit ⇒ Energieerhaltung", 4),          # 1.4.1
    ("Homogenität des Raumes ⇒ Impulserhaltung", 4),                        # 1.4.2
    ("Isotropie des Raumes ⇒ Drehimpulserhaltung", 4),                      # 1.4.3

    # 2 Hamilton-Mechanik
    ("Legendre-Transformation (L→H)", 4),                                   # 2.1
    ("Kanonische Gleichungen (Hamilton-Gleichungen)", 4),                   # 2.2
    ("Hamilton-Funktion (Hamiltonian)", 4),                                 # 2.2.1
    ("Einfache Beispiele in Hamilton-Formulierung", 3),                    # 2.2.2

    ("Wirkungsprinzipien (Überblick)", 3),                                  # 2.3
    ("Modifiziertes Hamilton’sches Prinzip", 3),                            # 2.3.1
    ("Prinzip der kleinsten Wirkung", 3),                                   # 2.3.2
    ("Fermat’sches Prinzip (Optik-Bezug)", 2),                              # 2.3.3
    ("Jacobi-Prinzip (verkürzte Wirkung)", 3),                              # 2.3.4

    ("Poisson-Klammer (Definition & Bedeutung)", 4),                        # 2.4
    ("Darstellungsräume (q,p) und Funktionenräume", 2),                     # 2.4.1
    ("Fundamentale Poisson-Klammern", 4),                                   # 2.4.2
    ("Formale Eigenschaften (Bilinearität, Antisymmetrie, Jacobi)", 3),     # 2.4.3
    ("Integrale der Bewegung & Involution", 3),                             # 2.4.4
    ("Bezug zur Quantenmechanik (Kommutator ↔ Poisson)", 3),               # 2.4.5

    ("Kanonische Transformationen (Motivation)", 3),                        # 2.5 / 2.5.1
    ("Erzeugende Funktion (vier Typen)", 4),                                # 2.5.2
    ("Äquivalente Formen der erzeugenden Funktion", 3),                     # 2.5.3
    ("Beispiele kanonischer Transformationen", 3),                          # 2.5.4
    ("Kriterien für Kanonizität (Symplektizität)", 3),                      # 2.5.5

    # 3 Hamilton-Jacobi-Theorie
    ("Hamilton–Jacobi-Gleichung (HJ)", 4),                                  # 3.1
    ("Lösungsmethode der HJ-Theorie", 3),                                   # 3.2
    ("Hamilton’sche charakteristische Funktion S", 3),                      # 3.3
    ("Separation der Variablen in HJ", 3),                                  # 3.4

    ("Wirkungs- und Winkelvariable (Action-Angle)", 4),                     # 3.5
    ("Periodische Systeme & Winkelvariable", 3),                            # 3.5.1–3.5.2
    ("Kepler-Problem (HJ/AA-Formalismus)", 4),                              # 3.5.3
    ("Entartung (degenerate Systeme)", 2),                                   # 3.5.4
    ("Bohr–Sommerfeld-Quantisierung (historisch)", 3),                      # 3.5.5

    ("Übergang zur Wellenmechanik (klassisch → QM)", 3),                    # 3.6
    ("Wellengleichung der klassischen Mechanik (Hamilton–Jacobi ↔ eikonal)", 2), # 3.6.1
    ("Einschub über Lichtwellen (Optikbezug)", 2),                           # 3.6.2
    ("Ansatz der Wellenmechanik (de Broglie/Schrödinger-Idee)", 3),          # 3.6.3
]
