# -*- coding: utf-8 -*-
# Unterkategorien/Physik/optik.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Optik“.
Diese Liste wird von kategorien/physik.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Spezialthemen
"""

SUBDISCIPLINES = [
    # 2 Licht als elektromagnetische Welle
    ("Wellengleichung und Lösungen", 4),                                 # 2.1
    ("Energie und Impuls von Licht", 4),                                 # 2.1.1
    ("Wellenpakete (Optik)", 3),                                          # 2.1.2
    ("Phasen- und Gruppengeschwindigkeit", 4),                            # 2.1.3

    # 2.2 Dispersion von Licht
    ("Frequenzabhängigkeit der Dielektrizitätskonstante", 3),            # 2.2.1
    ("Brechungsindex (Dispersion)", 4),                                   # 2.2.2
    ("Absorption von Licht", 3),                                          # 2.2.3
    ("Dispersion dichter Medien", 3),                                     # 2.2.4
    ("Brechungsindex und Absorption von Metallen", 3),                   # 2.2.5

    # 2.3 Grenzflächen
    ("Reflexions- und Brechungsgesetz", 4),                              # 2.3.1
    ("Fresnelsche Formeln (Reflexionsgrad)", 4),                          # 2.3.2
    ("Totalreflexion und evaneszente Wellen", 4),                         # 2.3.3

    # 2.4 Lichtwellenleiter / Fasern
    ("Lichtleitung durch Totalreflexion", 4),                             # 2.4.1
    ("Moden in optischen Wellenleitern", 3),                              # 2.4.2
    ("Lichtausbreitung im Hohlleiter", 2),                                # 2.4.3
    ("Moden im dielektrischen Wellenleiter", 3),                          # 2.4.4
    ("Lichtleitfasern (Grundlagen)", 4),                                  # 2.4.5
    ("Herstellung von Glasfasern", 2),                                    # 2.4.6

    # 2.5 Absorbierende & streuende Medien
    ("Reflexionsvermögen absorbierender Medien", 3),                      # 2.5.1
    ("Farbe von Gegenständen", 3),                                        # 2.5.2
    ("Streuung elektromagnetischer Wellen", 3),                           # 2.5.3

    # 3 Geometrische Optik
    ("Fermatsches Prinzip", 4),                                           # 3.1
    ("Reflexionsgesetz (geometrisch)", 4),                                # 3.1.1
    ("Brechungsgesetz aus Fermat", 4),                                    # 3.1.2
    ("Strahlenablenkung am Prisma", 3),                                   # 3.2
    ("Der Regenbogen (Dispersion + Geometrie)", 3),                       # 3.2.1

    # 3.3 Optische Abbildung
    ("Reelle und virtuelle Abbildungen", 3),                              # 3.3.1
    ("Abbildung am Kugelspiegel", 3),                                     # 3.3.2
    ("Brechende Kugelflächen", 3),                                        # 3.3.3
    ("Abbildungsgleichung für dünne Linsen", 4),                          # 3.3.4
    ("Dicke Linsen und Linsensysteme", 3),                                # 3.3.5
    ("Paraxiale Strahlen & Matrizen-Verfahren", 4),                       # 3.3.6
    ("Anwendungen der Matrizenmethode", 3),                               # 3.3.7
    ("Linsenfehler (Aberrationen)", 3),                                   # 3.3.8
    ("Begrenzungen in optischen Systemen (Apertur, Vignettierung)", 2),   # 3.3.9
    ("Design und Herstellung von Objektiven", 2),                         # 3.3.10

    # 3.4 Instrumente der geometrischen Optik
    ("Projektionsapparat", 2),                                            # 3.4.1
    ("Photographische Kamera", 3),                                        # 3.4.2
    ("Das Auge (Optik)", 3),                                              # 3.4.3
    ("Vergrößernde optische Instrumente", 3),                             # 3.4.4

    # 4 Welleneigenschaften von Licht – Beugung
    ("Huygenssches Prinzip", 3),                                          # 4.1.1
    ("Fresnelsche Beugung (qualitativ)", 3),                               # 4.1.2
    ("Fresnel–Kirchhoffsche Beugungstheorie", 3),                          # 4.2.1
    ("Fresnel vs. Fraunhofer (Übergangsbedingungen)", 3),                  # 4.2.2
    ("Fraunhofersche Beugung (allgemein)", 4),                             # 4.2.3
    ("Babinetsches Prinzip", 2),                                           # 4.2.4

    # 4.3 Spezielle Fraunhofer-Beugung
    ("Beugung am langen Spalt", 4),                                       # 4.3.1
    ("Beugung an der Rechteckblende", 3),                                  # 4.3.2
    ("Beugung an der kreisförmigen Öffnung", 3),                           # 4.3.3
    ("Beugung am Doppelspalt", 4),                                        # 4.3.4
    ("Beugung am Gitter", 4),                                             # 4.3.5
    ("Gitterspektrometer", 3),                                            # 4.3.6
    ("Beugung an mehrdimensionalen Gittern", 2),                          # 4.3.7

    # 4.4 Interferenz
    ("Kohärenz von Lichtquellen", 4),                                      # 4.4.1
    ("Interferometer (spezielle Anordnungen)", 4),                          # 4.4.2
    ("Interferenzen dünner Schichten", 4),                                  # 4.4.3
    ("Fabry–Perot-Interferometer (Vielfachinterferenzen)", 4),             # 4.4.4

    # 4.5 Anwendungen von Beugung & Interferenz
    ("Auflösungsvermögen optischer Geräte", 4),                            # 4.5.1
    ("Abbesche Bildtheorie & Fourieroptik", 4),                             # 4.5.2
    ("Holographie", 3),                                                    # 4.5.3
    ("Laser-Strahlen: Optik Gaußscher Bündel", 4),                          # 4.5.4
    ("Gaußsche Bündel & abbildende Elemente", 3),                          # 4.5.5

    # 4.6 Polarisation
    ("Polarisationszustände von Licht", 4),                                 # 4.6.1
    ("Polarisatoren", 3),                                                  # 4.6.2
    ("Doppelbrechung", 4),                                                 # 4.6.3
    ("Anwendungen der Doppelbrechung", 3),                                  # 4.6.4
    ("Induzierte Doppelbrechung", 2),                                      # 4.6.5
    ("Optische Aktivität & Faraday-Effekt", 4),                             # 4.6.6

    # 4.7 Nichtlineare Optik
    ("χ^(2)-Phänomene (zweite Ordnung)", 3),                                # 4.7.1
    ("χ^(3)-Phänomene (dritte Ordnung)", 3),                                # 4.7.2

    # 5 Quantenphänomene: Licht als Welle und Teilchen
    ("Photoeffekt (Grundlagen)", 4),                                       # 5.1
    ("Eigenschaften von Photonen", 3),                                      # 5.1.1
    ("Welle-Teilchen-Dualismus (Licht)", 4),                                 # 5.1.2
    ("Doppelspalt: Welle vs. Teilchen", 4),                                 # 5.1.3
    ("Photoeffekt in der Detektion (Nachweis)", 2),                          # 5.1.4

    # 5.2 Strahlungsgesetze und Lichtquellen
    ("Strahlungsphysikalische Größen", 3),                                  # 5.2.1
    ("Lichttechnische Größen", 2),                                          # 5.2.2
    ("Kirchhoffsches Strahlungsgesetz", 3),                                 # 5.2.3
    ("Schwarzer Strahler: Emissionsverhalten", 4),                          # 5.2.4
    ("Strahlungsgesetze (Wien, Rayleigh–Jeans)", 3),                         # 5.2.5
    ("Plancksche Strahlungsformel", 4),                                     # 5.2.6
    ("Lichtquellen für Beleuchtungszwecke", 2),                              # 5.2.7
    ("Der Laser (Prinzip & Anwendungen)", 4),                                # 5.2.8
]
