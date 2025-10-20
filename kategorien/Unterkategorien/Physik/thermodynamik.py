# -*- coding: utf-8 -*-
# Unterkategorien/Physik/thermodynamik.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Thermodynamik“.
Diese Liste wird von kategorien/physik.py importiert und dient nur als Datenquelle
für die Subthema-Auswahl im Prompt. Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Randnotizen / Kontext
"""

SUBDISCIPLINES = [
    # 1 Grundbegriffe
    ("Thermodynamische Systeme (offen/geschlossen/isoliert)", 4),             # 1.1
    ("Zustand und Gleichgewicht (makro/mikro)", 4),                            # 1.2
    ("Temperaturbegriff (thermisches Gleichgewicht)", 4),                      # 1.3
    ("Zustandsgleichungen (Überblick)", 3),                                    # 1.4
    ("Ideales Gas (Zustandsgleichung)", 4),                                    # 1.4.1
    ("Van-der-Waals-Gas (Korrekturen)", 3),                                    # 1.4.2
    ("Idealer Paramagnet (Brillouin/Langevin-Idee)", 2),                       # 1.4.3
    ("Weiß’scher Ferromagnet (mittlere Feldnäherung)", 2),                     # 1.4.4
    ("Arbeit in der Thermodynamik (p dV, generalisiert)", 4),                  # 1.5

    # 2 Hauptsätze
    ("Erster Hauptsatz & innere Energie", 4),                                  # 2.1
    ("Wärmekapazitäten (C_V, C_p, Beziehungen)", 3),                           # 2.2
    ("Adiabaten und Isothermen (Prozesse)", 3),                                # 2.3
    ("Zweiter Hauptsatz (Kelvin-Planck/Clausius)", 4),                         # 2.4
    ("Carnot-Kreisprozess & Wirkungsgrad", 4),                                 # 2.5
    ("Absolute thermodynamische Temperaturskala", 3),                          # 2.6
    ("Entropie als Zustandsgröße", 4),                                         # 2.7
    ("Einfache Folgerungen aus den Hauptsätzen", 3),                           # 2.8

    # 3 Thermodynamische Potentiale
    ("Natürliche Zustandsvariablen (U, H, F, G)", 4),                          # 3.1
    ("Legendre-Transformation (U↔H↔F↔G)", 4),                                   # 3.2
    ("Homogenitätsrelationen (Euler/Gibbs-Duhem)", 3),                          # 3.3
    ("Potentiale des idealen Gases", 3),                                       # 3.4
    ("Mischungsentropie", 3),                                                  # 3.5
    ("Joule–Thomson-Prozess (Inversionstemp.)", 3),                            # 3.6
    ("Gleichgewichtsbedingungen (allgemein)", 3),                               # 3.7
    ("Isolierte Systeme: Maximum der Entropie", 3),                            # 3.7.1
    ("Geschl. System im Wärmebad: Minimum der freien Energie F", 3),           # 3.7.2
    ("Geschl. System bei konstanten Kräften: Minimum der Enthalpie H", 3),     # 3.7.3
    ("Extremaleigenschaften von U und H", 2),                                   # 3.7.4
    ("Dritter Hauptsatz (Nernst’scher Wärmesatz)", 4),                          # 3.8

    # 4 Phasen und Phasenübergänge
    ("Phasen (Definitionen, Beispiele)", 3),                                    # 4.1
    ("Gibb’sche Phasenregel", 4),                                              # 4.1.1
    ("Dampfdruckkurve & Clausius–Clapeyron-Gleichung", 4),                     # 4.1.2
    ("Maxwell-Konstruktion (Van-der-Waals-Isothermen)", 3),                    # 4.1.3

    ("Phasenübergänge (Übersicht)", 3),                                        # 4.2
    ("Geometrische Interpretation von Phasenübergängen", 2),                   # 4.2.1
    ("Ehrenfest-Klassifikation", 3),                                           # 4.2.2
    ("Kritische Exponenten", 4),                                               # 4.2.3
    ("Exponenten-Ungleichungen (Scaling Bounds)", 3),                          # 4.2.4
    ("Skalenhypothese (Skalierungsansatz)", 3),                                # 4.2.5
]
