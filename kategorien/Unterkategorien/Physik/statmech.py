# -*- coding: utf-8 -*-
# Unterkategorien/Physik/statistische_mechanik.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Statistische Mechanik“.
Diese Liste wird von kategorien/physik.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Spezialthemen
"""

SUBDISCIPLINES = [
    # 1. Grundlagen
    ("Einleitung & Zielsetzung der Statistischen Mechanik", 2),                 # 1.1
    ("Wahrscheinlichkeitstheorie: Dichten & charakteristische Funktion", 3),    # 1.2.1
    ("Zentraler Grenzwertsatz", 3),                                            # 1.2.2
    ("Klassische Ensembles: Phasenraum & Verteilungsfunktion", 4),             # 1.3.1
    ("Liouville-Gleichung", 4),                                                # 1.3.2
    ("Quantenstatistik: Dichtematrix (rein/gemischt)", 4),                      # 1.4.1
    ("Von-Neumann-Gleichung", 3),                                              # 1.4.2
    ("Binomial- & Poisson-Verteilung (Exkurs)", 2),                             # *1.5.1
    ("Dichtematrix von Teilsystemen (Reduktion)", 2),                           # *1.5.2

    # 2. Gleichgewichtsensemble
    ("Mikrokanonisches Ensemble: Verteilungsfunktion & Dichtematrix", 4),      # 2.2.1
    ("Klassisches ideales Gas (mikrokanonisch)", 3),                             # 2.2.2
    ("Entropie: Definition & Extremaleigenschaft", 4),                           # 2.3.1/2
    ("Entropie im mikrokanonischen Ensemble", 3),                               # 2.3.3
    ("Temperaturdefinition aus Energieaustausch", 4),                            # 2.4.1
    ("Fluktuationen makroskopischer Größen", 3),                                # 2.4.2
    ("Äußere Parameter & Druck", 3),                                           # 2.4.3
    ("Nicht wechselwirkende Systeme: Ideales Gas", 3),                          # 2.5.1
    ("Kanonisches Ensemble: Dichtematrix & Zustandssumme", 4),                  # 2.6.1
    ("Maxwell-Verteilung & barometrische Höhenformel", 3),                      # 2.6.2
    ("Entropie im kanonischen Ensemble & Extremalität", 3),                    # 2.6.3
    ("Virialsatz & Äquipartition (Gleichverteilungssatz)", 4),                  # 2.6.4
    ("Thermodynamische Größen aus dem kanonischen Ensemble", 3),               # 2.6.5
    ("Großkanonisches Ensemble: Dichtematrix & Potential", 4),                  # 2.7.2
    ("Thermodynamische Größen (großkanonisch)", 3),                             # 2.7.3
    ("Klassisches ideales Gas (großkanonisch)", 3),                              # 2.7.4

    # 3. Thermodynamik
    ("Potentiale & Hauptsätze der Gleichgewichtsthermodynamik", 4),            # 3.1
    ("Legendre-Transformation", 4),                                            # 3.1.2
    ("Gibbs-Duhem-Relation (homogene Systeme)", 3),                             # 3.1.3
    ("Ableitungen thermodynamischer Größen & Maxwell-Relationen", 4),          # 3.2.2
    ("Jacobi-Determinante (Wechsel der Variablen)", 2),                         # 3.2.3
    ("Fluktuationen & thermodynamische Ungleichungen", 3),                      # 3.3
    ("Absolute vs. empirische Temperatur", 2),                                  # 3.4
    ("Thermodynamische Prozesse (Begriffe)", 2),                                # 3.5.1
    ("Irreversible Expansion (Gay-Lussac)", 3),                                 # 3.5.2
    ("Statistische Begründung der Irreversibilität", 4),                         # 3.5.3
    ("Reversible Vorgänge & Adiabatengleichung", 3),                            # 3.5.4/5
    ("Erster & Zweiter Hauptsatz (reversibel/irreversibel)", 4),                 # 3.6.1
    ("Carnot- und allgemeine Kreisprozesse", 4),                                # 3.7.2/3
    ("Phasen von Einstoffsystemen & Clausius–Clapeyron", 4),                    # 3.8/3.8.2
    ("Tripelpunkt & Konvexität/ Konkavität freier Energien", 3),               # 3.8.3/4
    ("Gibbs-Phasenregel; Mehrkomponenten-Gleichgewichte", 4),                  # 3.9.2
    ("Massenwirkungsgesetz (chem. Gleichgewicht)", 3),                          # 3.9.3

    # 4. Ideale Quanten-Gase
    ("Großkanonisches Potential (Quanten-Gase)", 4),                            # 4.1
    ("Klassischer Grenzfall (z ≪ 1)", 3),                                       # 4.2
    ("Ideales Fermi-Gas: Grundzustand & starke Entartung", 4),                  # 4.3.1/2
    ("Bose–Einstein-Kondensation (BEC)", 4),                                    # 4.4
    ("Photonengas & Plancksches Strahlungsgesetz", 4),                          # 4.5.3
    ("Teilchenzahlfluktuationen: Fermi vs. Bose", 2),                           # *4.5.5
    ("Phononen in Festkörpern: harmonischer Hamilton-Operator", 3),            # 4.6.1
    ("Phonon-Thermodynamik (Debye u. a.)", 3),                                  # 4.6.2
    ("Phononen/Rotonen in He II: Anregungen & Thermik", 2),                    # 4.7.1/2

    # 5. Reale Gase, Flüssigkeiten & Lösungen
    ("Ideales Molekülgas: Zustandssumme (Rot./Vib.)", 3),                       # 5.1 ff.
    ("Virialentwicklung & 2. Virialkoeffizient (klass./quant.)", 4),            # 5.3.2/5.3.3
    ("Van-der-Waals-Gleichung & Maxwell-Konstruktion", 4),                     # 5.4/5.4.2
    ("Gesetz korrespondierender Zustände & kritischer Punkt", 3),               # 5.4.3/4
    ("Verdünnte Lösungen: chem. Potentiale & osmotischer Druck", 3),            # 5.5.1/2
    ("Gefrierpunktserniedrigung/Siedepunktserhöhung", 2),                       # 5.5.4

    # 6. Magnetismus (statmech)
    ("Kanonische Dichtematrix & Thermodynamik magnetischer Systeme", 3),       # 6.1
    ("Diamagnetismus (atomar)", 2),                                             # 6.2
    ("Paramagnetismus ungekoppelter Momente (Curie-Gesetz)", 3),                # 6.3
    ("Pauli-Paramagnetismus", 3),                                               # 6.4
    ("Ferromagnetismus: Austausch & Ising-MF", 4),                              # 6.5.1/2
    ("Korrelationsfunktion & Suszeptibilität; Ornstein–Zernike", 3),            # 6.5.3/4
    ("Dipolwechselwirkung, interne/äußere Felder; Domänen", 2),                 # 6.6/6.6.4
    ("Anwendungen: Polymere/Negative Temperaturen", 2),                         # 6.7.1/2

    # 7. Phasenübergänge, RG & Perkolation
    ("Phasenübergänge & kritische Phänomene (Überblick)", 4),                   # 7.1
    ("Symmetriebrechung; Ehrenfest-Klassifikation", 3),                         # 7.1.1
    ("Universalität & Skalenhypothese (statisch)", 4),                           # 7.1.3/7.2
    ("Kritische Exponenten & Skalengesetze", 4),                                 # 7.2.1/7.3.4
    ("RG-Ideen: Ising 1D/2D & Dezimierung", 3),                                 # 7.3.2/3
    ("Ginzburg–Landau-Funktional & -Nähe", 3),                                  # 7.4.1/2/3
    ("Perkolation: Phänomen, Theorie & Skalen", 3),                              # 7.5 ff.

    # 8. Brownsche Bewegung & FP-Gleichungen
    ("Langevin-Gleichungen (frei & mit Kraftfeld)", 4),                          # 8.1
    ("Fokker–Planck aus Langevin; Smoluchowski-Gleichung", 4),                  # 8.2
    ("Anwendungen: Reaktionen, kritische Dynamik", 3),                           # 8.3

    # 9. Boltzmann-Gleichung
    ("Herleitung der Boltzmann-Gleichung", 4),                                   # 9.2
    ("H-Theorem, Irreversibilität & lokale Maxwell-Verteilung", 4),             # 9.3.1/3
    ("Erhaltungssätze & Hydrodynamik im lokalen Gleichgewicht", 3),             # 9.3.4/5
    ("Linearisierte Boltzmann-Gleichung & Relaxationszeit", 2),                  # 9.4/9.5.1

    # 10. Irreversibilität & Relaxation zum Gleichgewicht
    ("Wiederkehrzeit & Poincaré-Rekurrenz", 2),                                  # 10.2
    ("Mikro→Makro: Ursprung irreversibler Gleichungen", 3),                      # 10.3
    ("Gibbs- vs. Boltzmann-Entropie & Zeitentwicklung", 3),                      # 10.6
    ("Zeitumkehr & Gasexpansion; Störungen der Trajektorien", 2),                # 10.7

    # Anhänge (ausgewählte Kernideen)
    ("Dritter Hauptsatz (Nernstsches Theorem): Konsequenzen", 3),               # A
    ("Klassischer Grenzfall & Quantenkorrekturen (Virial)", 2),                  # B
    ("Riemannsche ζ-Funktion & Bernoulli-Zahlen (Anwendungen)", 1),             # D
    ("Ginzburg–Landau-Funktional: Herleitung", 2),                               # E
    ("Transfermatrix-Methode (Ising etc.)", 2),                                   # F
    ("Integrale mit Maxwell-Verteilung (Technik)", 1),                            # G
    ("Hydrodynamik & Kubo-Formalismus (Übersicht)", 2),                          # H
]
