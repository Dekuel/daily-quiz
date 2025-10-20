# -*- coding: utf-8 -*-
# Unterkategorien/Physik/elektrodynamik.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Elektrodynamik“.
Diese Liste wird von kategorien/physik.py importiert und dient nur als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder ergänzende Mathematik
"""

SUBDISCIPLINES = [
    # 1 Mathematische Vorbereitungen
    ("Dirac’sche δ-Funktion", 3),
    ("Taylor-Entwicklung für Felder", 2),
    ("Flächenintegrale (orientierte Flächen)", 3),
    ("Integraldarstellung der Divergenz", 3),
    ("Integraldarstellung der Rotation", 3),
    ("Gauß’scher Satz", 4),
    ("Stokes’scher Satz", 4),
    ("Green’sche Sätze", 3),
    ("Zerlegungs- und Eindeutigkeitssatz (Vektoranalysis)", 2),

    # 2 Elektrostatik
    ("Ladungen und Ströme", 3),
    ("Coulomb’sches Gesetz & elektrisches Feld", 4),
    ("Maxwell-Gleichungen der Elektrostatik", 4),
    ("Feldverhalten an Grenzflächen", 3),
    ("Elektrostatische Feldenergie", 3),

    ("Plattenkondensator", 4),
    ("Kugelkondensator", 3),
    ("Zylinderkondensator", 3),
    ("Der Dipol & Dipolfeld", 4),
    ("Dipolschicht & Quadrupol", 3),
    ("Multipolentwicklung", 4),
    ("Wechselwirkung einer Ladungsverteilung mit äußerem Feld", 3),

    ("Randwertprobleme der Elektrostatik (Laplace-Gleichung)", 4),
    ("Klassifikation der Randbedingungen", 3),
    ("Green’sche Funktion", 3),
    ("Methode der Bildladungen", 4),
    ("Separation der Variablen & orthogonale Funktionen", 3),
    ("Laplace-Gleichung in Kugelkoordinaten", 3),
    ("Potential einer Punktladung, Multipolmomente", 3),

    ("Elektrostatik der Dielektrika", 4),
    ("Makroskopische Feldgrößen (D, E, P)", 4),
    ("Molekulare Polarisierbarkeit", 3),
    ("Randwertprobleme & Energie in Dielektrika", 3),

    # 3 Magnetostatik
    ("Elektrischer Strom (Definition & Kontinuitätsgleichung)", 4),
    ("Biot–Savart-Gesetz", 4),
    ("Maxwell-Gleichungen der Magnetostatik", 4),
    ("Vektorpotential", 3),
    ("Magnetisches Moment", 3),
    ("Kraft & Drehmoment auf Stromverteilungen", 3),
    ("Magnetostatik in Materie", 4),
    ("Makroskopische Feldgrößen (B, H, M)", 3),
    ("Einteilung magnetischer Stoffe (dia-/para-/ferro-)", 4),
    ("Feldverhalten an Grenzflächen", 3),

    # 4 Elektrodynamik
    ("Maxwell-Gleichungen (vollständig)", 4),
    ("Faraday’sches Induktionsgesetz", 4),
    ("Maxwell’sche Ergänzung des Ampèreschen Gesetzes", 4),
    ("Elektromagnetische Potentiale (φ, A)", 4),
    ("Feldenergie & Feldimpuls", 3),

    ("Gegen- und Selbstinduktion", 4),
    ("Magnetische Feldenergie (Dichte)", 3),
    ("Wechselströme & Schwingkreise", 4),
    ("Resonanz & Schaltvorgänge", 3),

    # 4.3 Elektromagnetische Wellen
    ("Homogene Wellengleichung", 4),
    ("Ebene Wellen & Polarisation", 4),
    ("Wellenpakete & Kugelwellen", 3),
    ("Fourier-Reihen & -Integrale in der Wellenausbreitung", 3),
    ("Energietransport in Wellenfeldern (Poynting-Vektor)", 4),
    ("Wellenausbreitung in Leitern", 3),
    ("Reflexion & Brechung elektromagnetischer Wellen", 4),
    ("Interferenz & Beugung elektromagnetischer Wellen", 4),
    ("Beugung am Schirm & Poisson’scher Fleck", 3),

    # 4.4 Funktionentheorie (für Feldlösungen)
    ("Komplexe Funktionen & Integralsätze", 3),
    ("Reihen komplexer Funktionen", 2),
    ("Residuensatz", 3),

    # 4.5 Erzeugung elektromagnetischer Wellen
    ("Inhomogene Wellengleichung", 3),
    ("Zeitlich oszillierende Quellen", 3),
    ("Elektrische Dipolstrahlung", 4),
    ("Quadrupol- und magnetische Dipolstrahlung", 3),
    ("Bewegte Punktladungen & Liénard–Wiechert-Potentiale", 4),
]
