# -*- coding: utf-8 -*-
# Unterkategorien/Physik/quantenmechanik.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Quantenmechanik“.
Diese Liste wird von kategorien/physik.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte
"""

SUBDISCIPLINES = [
    # 1 Induktive Begründung der Wellenmechanik
    ("Grenzen der klassischen Physik", 3),                                    # 1.1
    ("Planck’sches Wirkungsquantum", 4),                                      # 1.2
    ("Wärmestrahlungsgesetze & Planck-Formel", 4),                            # 1.2.1–1.2.3
    ("Atome, Elektronen, Atomkerne (Überblick)", 2),                          # 1.3
    ("Teilbarkeit der Materie (historisch)", 2),                               # 1.3.1
    ("Elektron (Entdeckung, Eigenschaften)", 3),                               # 1.3.2
    ("Rutherford-Streuung", 3),                                               # 1.3.3
    ("Lichtwellen & Lichtquanten (Dualismus)", 4),                             # 1.4
    ("Interferenz und Beugung (Licht)", 3),                                    # 1.4.1
    ("Fraunhofer-Beugung", 2),                                                # 1.4.2
    ("Beugung am Kristallgitter", 3),                                         # 1.4.3
    ("Lichtquanten / Photonen", 4),                                           # 1.4.4
    ("Semiklassische Atommodelle (Rutherford→Bohr)", 3),                      # 1.5
    ("Versagen des Rutherford-Modells", 3),                                   # 1.5.1
    ("Bohr’sches Atommodell", 4),                                             # 1.5.2
    ("Korrespondenzprinzip (Bohr)", 3),                                       # 1.5.3

    # 2 Schrödinger-Gleichung
    ("Materiewellen (de Broglie-Idee)", 4),                                   # 2.1
    ("Wirkungswellen (Hamilton–Jacobi-Bezug)", 2),                            # 2.1.1
    ("de Broglie-Wellen", 4),                                                 # 2.1.2
    ("Doppelspaltexperiment (Materiewellen)", 4),                              # 2.1.3

    ("Wellenfunktion & statistische Interpretation", 4),                      # 2.2–2.2.1
    ("Freie Materiewelle", 3),                                                # 2.2.2
    ("Wellenpakete (Dispersion)", 3),                                         # 2.2.3
    ("Impulsraum-Darstellung der Wellenfunktion", 3),                         # 2.2.4
    ("Periodische Randbedingungen", 2),                                       # 2.2.5
    ("Mittelwerte & Schwankungen", 3),                                       # 2.2.6

    ("Impulsoperator & Orts-/Impulsdarstellung", 4),                          # 2.3–2.3.1
    ("Nicht-Vertauschbarkeit von Operatoren", 4),                             # 2.3.2
    ("Korrespondenzregel (Operatorersatz)", 3),                                # 2.3.3

    # 3 Grundlagen der Quantenmechanik (Dirac-Formalismus)
    ("Zustand / reiner Zustand (Präparation)", 3),                             # 3.1–3.1.2
    ("Observable", 3),                                                         # 3.1.3
    ("Hilbert-Raum (allgemein)", 4),                                          # 3.2.1
    ("Quadratintegrable Funktionen H=L^2", 3),                                 # 3.2.2
    ("Bra- und Ket-Vektoren; Dualraum", 4),                                   # 3.2.3
    ("Uneigentliche (Dirac-)Vektoren", 3),                                    # 3.2.4
    ("Lineare Operatoren", 3),                                                # 3.2.5
    ("Eigenwertproblem", 4),                                                  # 3.2.6
    ("Spezielle Operatoren (hermitesch, projektiv)", 3),                       # 3.2.7
    ("Operatoren als Matrizen", 2),                                           # 3.2.8

    ("Postulate der Quantenmechanik", 4),                                     # 3.3.1
    ("Messprozess & Projektionspostulat", 4),                                 # 3.3.2
    ("Verträgliche vs. nicht-verträgliche Observable", 3),                    # 3.3.3
    ("Dichtematrix (statistischer Operator)", 4),                              # 3.3.4
    ("Unbestimmtheitsrelation(en)", 4),                                       # 3.3.5

    ("Zeitentwicklung (Schrödinger-Bild)", 4),                                # 3.4.1
    ("Zeitentwicklungsoperator", 3),                                          # 3.4.2
    ("Zeitentwicklung (Heisenberg-Bild)", 4),                                  # 3.4.3
    ("Wechselwirkungsdarstellung (Dirac-Bild)", 3),                            # 3.4.4
    ("Quantentheoretische Bewegungsgleichungen", 3),                           # 3.4.5
    ("Energie–Zeit–Unschärfe", 3),                                            # 3.4.6

    ("Korrespondenzprinzip (QM↔klassisch)", 3),                               # 3.5
    ("Heisenberg-Bild & Poisson-Klammer (klass. Limit)", 3),                  # 3.5.1
    ("Orts- und Impulsdarstellung (Verknüpfung)", 3),                          # 3.5.2

    # 4 Einfache Modellsysteme
    ("1D-Potentialprobleme: allgemeine Aussagen", 3),                          # 4.1
    ("Lösung der 1D-Schrödinger-Gleichung", 3),                                # 4.1.1
    ("Wronski-Determinante", 2),                                              # 4.1.2
    ("Eigenwertspektrum (diskret/kontinuierlich)", 3),                         # 4.1.3
    ("Parität in 1D-Potentialen", 2),                                         # 4.1.4

    ("Potentialtopf: gebundene Zustände", 4),                                 # 4.2.1
    ("Potentialtopf: Streuzustände", 3),                                      # 4.2.2

    ("Potentialbarrieren & -stufen", 3),                                      # 4.3.1–4.3.2
    ("Tunneleffekt", 4),                                                      # 4.3.3
    ("Beispiel: α-Radioaktivität", 3),                                        # 4.3.4
    ("Kronig–Penney-Modell (Bänder)", 4),                                      # 4.3.5

    ("Harmonischer Oszillator: Erzeugungs-/Vernichtungsoperator", 4),         # 4.4.1
    ("Besetzungszahloperator & Eigenwertproblem", 3),                          # 4.4.2
    ("Spektrum des harmonischen Oszillators", 4),                              # 4.4.3
    ("Ortsdarstellung (Hermite-Polynome)", 3),                                 # 4.4.4
    ("Sommerfeld’sche Polynommethode", 2),                                     # 4.4.5
    ("Mehrdimensionaler harmonischer Oszillator", 3),                          # 4.4.6

    # 5 Quantentheorie des Drehimpulses
    ("Bahndrehimpuls: Operator & Kommutatoren", 4),                            # 5.1–5.1.3
    ("Eigenwertproblem des Bahndrehimpulses", 4),                              # 5.1.4
    ("Ortsdarstellung & Eigenfunktionen (sphärische Harmonische)", 4),         # 5.1.5–5.1.6
    ("Spin (allgemein)", 4),                                                   # 5.2
    ("Magnetisches Moment & Drehimpuls", 3),                                   # 5.2.2
    ("Hilbert-Raum des Spins", 3),                                            # 5.2.3
    ("Spin 1/2 (Pauli-Matrizen)", 4),                                         # 5.2.4

    ("Relativistische Theorie des Elektrons (Überblick)", 3),                  # 5.3
    ("Dirac-Gleichung", 4),                                                    # 5.3.1
    ("Dirac’scher Spinoperator", 3),                                          # 5.3.2
    ("Elektronenspin (Pauli-Theorie)", 3),                                     # 5.3.3
    ("Spin-Bahn-Wechselwirkung", 3),                                          # 5.3.4

    ("Addition von Drehimpulsen: Gesamtdrehimpuls", 4),                        # 5.4.1
    ("Quantenzahlen des Gesamtdrehimpulses", 3),                               # 5.4.2
    ("Clebsch–Gordan-Koeffizienten", 4),                                       # 5.4.3

    # 6 Zentralpotential
    ("Allgemeines & Radialgleichung", 4),                                      # 6.1–6.1.1
    ("Lösungsstruktur (radial)", 3),                                           # 6.1.2
    ("Coulomb-Potential (Wasserstoffatom): Energiespektrum", 4),               # 6.2.1
    ("Eigenfunktionen der gebundenen Zustände (Laguerre)", 4),                 # 6.2.2–6.2.3
    ("Wahrscheinlichkeiten & Erwartungswerte (H-Atom)", 3),                    # 6.2.4
    ("Kernmitbewegung; Zwei-Körper-Problem", 2),                               # 6.2.5
    ("Kugelsymmetrischer Potentialtopf (radial)", 3),                           # 6.3
    ("Bessel-Funktionen (radiale Lösungen)", 2),                                # 6.3.2
    ("Gebundene vs. Kontinuumszustände (radial)", 3),                           # 6.3.3–6.3.4
    ("Freies Teilchen (3D)", 2),                                               # 6.4

    # 7 Näherungsmethoden
    ("Variationsverfahren (Extremalprinzip)", 4),                               # 7.1–7.1.1
    ("Ritz’sches Verfahren", 3),                                               # 7.1.2
    ("Hartree-Gleichungen", 3),                                                # 7.1.3

    ("Zeitunabhängige Störungstheorie: nicht-entartete Niveaus", 4),          # 7.2.1
    ("Zeitunabhängige Störungstheorie: entartete Niveaus", 4),                 # 7.2.2
    ("Quasientartung", 2),                                                     # 7.2.3
    ("Störungstheoretische Grundformel", 3),                                   # 7.2.4
    ("Brillouin–Wigner-Störreihe", 2),                                         # 7.2.5

    ("Zeitabhängige (Dirac’sche) Störungstheorie: Grundgedanken", 3),         # 7.3.1
    ("Übergangswahrscheinlichkeit", 3),                                        # 7.3.2
    ("Fermi’s Goldene Regel", 4),                                             # 7.3.3
    ("Periodische Störungen", 2),                                             # 7.3.4

    ("Quasiklassische Näherung (WKB)", 4),                                     # 7.4.2
    ("ħ→0-Grenzfall; Klassische Umkehrpunkte", 3),                             # 7.4.1–7.4.3
    ("Langer-Verfahren", 2),                                                   # 7.4.4
    ("Phasenintegralquantisierung", 3),                                        # 7.4.5
    ("Bessel’sche Differentialgleichung (Zusatz)", 1),                          # 7.4.6

    # 8 Mehr-Teilchen-Systeme
    ("Unterscheidbare Teilchen: Produktraum & Observable", 3),                 # 8.1
    ("Systeme aus N unterscheidbaren Teilchen", 2),                            # 8.1.3

    ("Identische Teilchen: Ununterscheidbarkeit", 4),                          # 8.2.1
    ("Observable & Zustände für identische Teilchen", 3),                      # 8.2.2
    ("Hilbert-Raum & Basiszustände (sym/antisym)", 3),                          # 8.2.3–8.2.4
    ("Besetzungszahldarstellung", 4),                                          # 8.2.5
    ("Pauli-Prinzip", 4),                                                      # 8.2.6

    ("Zweite Quantisierung: Erzeugungs-/Vernichtungsoperatoren", 4),          # 8.3.1
    ("Operatoren in zweiter Quantisierung", 3),                                # 8.3.2
    ("Spezielle Operatoren (Zahl-, Hamilton-Operator)", 2),                     # 8.3.3

    ("Anwendungen: Hartree–Fock-Gleichungen", 3),                              # 8.4.1
    ("Anwendungen: Wasserstoffmolekül", 2),                                    # 8.4.2
    ("Anwendungen: Heliumatom", 2),                                            # 8.4.3

    # 9 Streutheorie
    ("Streutheorie: Grundbegriffe & Modell des Streuprozesses", 3),            # 9.1–9.1.1
    ("Formulierung des Streuproblems", 3),                                     # 9.1.2

    ("Partialwellenmethode & Zerlegung", 4),                                   # 9.2–9.2.1
    ("Streuung an der harten Kugel", 3),                                       # 9.2.2
    ("Streuung langsamer Teilchen am Potentialtopf", 3),                        # 9.2.3
    ("Resonanzstreuung", 3),                                                   # 9.2.4
    ("s-Streuung am Potentialtopf", 2),                                        # 9.2.5
    ("Integraldarstellung für Streuphasen", 2),                                 # 9.2.6

    ("Integralgleichungen der Streuung: Streuamplitude", 3),                   # 9.3.1
    ("Born’sche Reihe", 4),                                                    # 9.3.2

    ("Formale Streutheorie: Lippmann–Schwinger-Gleichung", 4),                 # 9.4.1
    ("S- und T-Matrix", 4),                                                    # 9.4.2
    ("Møller-Operatoren & Streuoperator", 3),                                  # 9.4.3–9.4.4
]
