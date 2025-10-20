# -*- coding: utf-8 -*-
# Unterkategorien/Physik/relativitaetstheorie.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Relativitätstheorie (SRT)“.
Diese Liste wird von kategorien/physik.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte
"""

SUBDISCIPLINES = [
    # 1 Physikalische Grundlagen
    ("Inertialsysteme (Definition und Eigenschaften)", 4),                   # 1.1
    ("Michelson–Morley-Experiment (Ätherhypothese)", 4),                     # 1.2
    ("Einsteins Postulate der SRT", 4),                                     # 1.3
    ("Lorentz-Transformation (Grundform)", 4),                              # 1.4
    ("Transformationsmatrix der Lorentz-Transformation", 3),                # 1.4.1
    ("Relativität der Gleichzeitigkeit", 4),                                # 1.4.2
    ("Zeitdilatation", 4),                                                  # 1.4.3
    ("Längenkontraktion", 4),                                               # 1.4.4
    ("Additionstheorem für Geschwindigkeiten", 3),                          # 1.4.5
    ("Lichtkegel und Minkowski-Diagramme", 4),                              # 1.5

    # 2 Kovariante vierdimensionale Formulierungen
    ("Ko- und kontravariante Tensoren (Grundbegriffe)", 3),                 # 2.1
    ("Definitionen & Rechenregeln von Tensoren", 3),                        # 2.1.1–2.1.2
    ("Differentialoperatoren in der SRT", 2),                               # 2.1.3

    ("Kovariante Formulierung der klassischen Mechanik", 4),                # 2.2
    ("Eigenzeit und Weltgeschwindigkeit", 4),                               # 2.2.1
    ("Relativistischer Impuls, Energie und Kraft", 4),                      # 2.2.2
    ("Der elastische Stoß in der SRT", 3),                                  # 2.2.3

    ("Kovariante Formulierung der Elektrodynamik", 4),                      # 2.3
    ("Kontinuitätsgleichung (vierdimensional)", 3),                         # 2.3.1
    ("Elektromagnetische Potentiale (Vierervektor)", 3),                    # 2.3.2
    ("Feldstärke-Tensor (Fμν)", 4),                                         # 2.3.3
    ("Maxwell-Gleichungen in kovarianter Form", 4),                         # 2.3.4
    ("Transformation der elektromagnetischen Felder", 4),                   # 2.3.5
    ("Lorentz-Kraft in Vierervektorform", 4),                               # 2.3.6
    ("Relativistische Elektrodynamik – Zusammenfassung der Formeln", 3),    # 2.3.7

    ("Kovariante Lagrange-Formulierung", 3),                                # 2.4
]
