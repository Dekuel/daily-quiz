# -*- coding: utf-8 -*-
# Unterkategorien/Physik/festkoerperphysik.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Festkörperphysik“.
Diese Liste wird von kategorien/physik.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Spezialthemen
"""

SUBDISCIPLINES = [
    # 2 Bindung im Festkörper
    ("Bindungstypen (Überblick)", 4),                                 # 2.1
    ("Bindungsenergie (Definition & Skalen)", 4),                      # 2.1.1
    ("Abstoßung (Kurzreichweitenteil)", 3),                            # 2.1.2
    ("Van-der-Waals-Bindung", 3),                                      # 2.2
    ("Van-der-Waals-Kräfte", 3),                                       # 2.2.1
    ("Lennard–Jones-Potential", 4),                                    # 2.2.2
    ("Bindungsenergie von Edelgaskristallen", 2),                      # 2.2.3
    ("Ionenbindung: Abschätzung & Messung", 3),                        # 2.3.1
    ("Bindungsenergie von Ionenkristallen", 3),                        # 2.3.2
    ("Kovalente Bindung", 4),                                          # 2.4
    ("Metallische Bindung", 4),                                        # 2.5
    ("Wasserstoffbrückenbindung", 2),                                  # 2.6

    # 3 Struktur der Festkörper
    ("Herstellung: Kristalle & amorphe Festkörper (Überblick)", 2),     # 3.1
    ("Einkristallherstellung (z. B. Czochralski)", 2),                  # 3.1.1
    ("Legierungen", 2),                                                 # 3.1.2
    ("Glasherstellung", 2),                                             # 3.1.3
    ("Ordnung und Unordnung", 3),                                      # 3.2
    ("Struktur der Kristalle (Überblick)", 3),                          # 3.3
    ("Translationsgitter & Kristallsysteme", 4),                        # 3.3.1
    ("Cluster & Quasikristalle", 2),                                    # 3.3.2
    ("Notation & Einfluss der Basis", 3),                               # 3.3.3
    ("Einfache Kristallgitter (sc, bcc, fcc)", 4),                      # 3.3.4
    ("Wigner–Seitz-Zelle", 3),                                          # 3.3.5
    ("Festkörperoberflächen", 3),                                       # 3.3.6
    ("Kohlenstoff-Nanoröhren", 3),                                     # 3.3.7
    ("Struktur amorpher Festkörper", 3),                                # 3.4
    ("Paarverteilungsfunktion", 3),                                     # 3.4.1

    # 4 Strukturbestimmung
    ("Strukturbestimmung: Allgemeines", 2),                             # 4.1
    ("Elementare Streutheorie", 3),                                     # 4.2
    ("Streuamplitude", 3),                                               # 4.2.1
    ("Fourier-Entwicklung von Punktgittern", 3),                        # 4.3
    ("Reziprokes Gitter", 4),                                           # 4.3.1
    ("Brillouin-Zone", 4),                                              # 4.3.2
    ("Millersche Indizes", 3),                                          # 4.3.3
    ("Streuung an Kristallen", 4),                                      # 4.4
    ("Ewald-Kugel & Bragg-Bedingung", 4),                               # 4.4.1
    ("Strukturfaktor", 4),                                              # 4.4.2
    ("Atom-Strukturfaktor", 3),                                         # 4.4.3
    ("Streuung an Oberflächen/dünnen Schichten", 3),                    # 4.4.4
    ("Phasenproblem bei Streuexperimenten", 2),                         # 4.4.5
    ("Debye–Waller-Faktor (Streuung)", 3),                               # 4.4.6
    ("Streuung an amorphen Substanzen", 2),                             # 4.5
    ("Experimentelle Methoden: Messverfahren", 3),                      # 4.6.1
    ("Messungen an Oberflächen & dünnen Filmen", 3),                    # 4.6.2

    # 5 Strukturelle Defekte
    ("Punktdefekte (Überblick)", 3),                                     # 5.1
    ("Leerstellen", 3),                                                  # 5.1.1
    ("Farbzentren", 2),                                                  # 5.1.2
    ("Zwischengitteratome", 2),                                          # 5.1.3
    ("Fremdatome", 2),                                                   # 5.1.4
    ("Atomarer Transport (Diffusion)", 3),                               # 5.1.5
    ("Ausgedehnte Defekte (Überblick)", 3),                              # 5.2
    ("Mechanische Festigkeit", 2),                                       # 5.2.1
    ("Versetzungen", 4),                                                 # 5.2.2
    ("Korngrenzen", 3),                                                  # 5.2.3
    ("Defekte in amorphen Materialien", 2),                              # 5.3
    ("Ordnungs–Unordnungs-Übergang", 3),                                # 5.4

    # 6 Gitterdynamik
    ("Elastische Eigenschaften (Überblick)", 3),                          # 6.1
    ("Spannung & Verformung", 3),                                        # 6.1.1
    ("Elastische Konstanten", 3),                                        # 6.1.2
    ("Schallwellen im Festkörper", 3),                                    # 6.1.3
    ("Gitterschwingungen: einatomige Basis", 4),                          # 6.2.1
    ("Gitterschwingungen: mehratomige Basis", 4),                         # 6.2.2
    ("Bewegungsgleichung der Gitteratome", 3),                            # 6.2.3
    ("Dynamische Streuung & Phononenquantisierung", 3),                  # 6.3.1
    ("Kohärente inelastische Neutronenstreuung", 3),                      # 6.3.2
    ("Debye–Waller-Faktor (Dynamik)", 2),                                 # 6.3.3
    ("Experimentelle Dispersionskurven", 2),                               # 6.3.4
    ("Lichtstreuung (z. B. Raman)", 2),                                   # 6.3.5
    ("Spezifische Wärmekapazität: Phonon-Zustandsdichte", 3),             # 6.4.1
    ("Debye-Näherung der spezifischen Wärme", 4),                          # 6.4.2
    ("Spezifische Wärme niederdimensionaler Systeme", 2),                 # 6.4.3
    ("Nullpunktsenergie & angeregte Phononen", 2),                        # 6.4.4
    ("Schwingungen in amorphen Festkörpern", 2),                          # 6.5
    ("Wärmekapazität von Gläsern (tiefe T)", 2),                           # 6.5.1

    # 7 Anharmonische Gittereigenschaften
    ("Zustandsgleichung & thermische Ausdehnung", 3),                     # 7.1
    ("Phonon–Phonon-Wechselwirkung (allgemein)", 3),                      # 7.2
    ("Drei-Phononen-Prozess", 3),                                         # 7.2.1
    ("Ultraschalldämpfung in Kristallen", 2),                              # 7.2.2
    ("Spontaner Phononenzerfall", 2),                                      # 7.2.3
    ("Ultraschalldämpfung in amorphen Festkörpern", 2),                    # 7.2.4
    ("Wärmetransport in dielektrischen Kristallen (Überblick)", 3),        # 7.3
    ("Ballistische Phononen", 2),                                          # 7.3.1
    ("Wärmeleitung (Phononen)", 3),                                        # 7.3.2
    ("Phonon–Phonon-Stöße", 2),                                           # 7.3.3
    ("Streuung an Defekten", 2),                                           # 7.3.4
    ("Wärmetransport in 1D-Proben", 2),                                    # 7.3.5
    ("Wärmeleitfähigkeit amorpher Festkörper", 2),                         # 7.4

    # 8 Elektronen im Festkörper
    ("Freies Elektronengas", 4),                                           # 8.1
    ("Zustandsdichte (Elektronengas)", 3),                                 # 8.1.1
    ("Fermi-Energie & Fermi-Kugel", 4),                                    # 8.1.2
    ("Spezifische Wärme der Elektronen", 3),                               # 8.2
    ("Kollektive Phänomene im Elektronengas", 3),                          # 8.3
    ("Abgeschirmtes Coulomb-Potential", 3),                                 # 8.3.1
    ("Metall–Isolator-Übergang", 3),                                       # 8.3.2
    ("Elektronen im periodischen Potential (Überblick)", 4),                # 8.4
    ("Bloch-Funktion", 4),                                                 # 8.4.1
    ("Quasi-freie Elektronen (Näherung)", 3),                               # 8.4.2
    ("Stark gebundene Elektronen (tight-binding)", 4),                      # 8.4.3
    ("Energiebänder (Überblick)", 4),                                       # 8.5
    ("Metalle und Isolatoren (Bandbild)", 4),                               # 8.5.1
    ("Brillouin-Zonen & Fermi-Flächen", 3),                                 # 8.5.2
    ("Zustandsdichte (Bänder)", 3),                                         # 8.5.3
    ("2D-hexagonale Festkörper: Graphen & Nanoröhren", 3),                  # 8.5.4

    # 9 Elektronische Transporteigenschaften
    ("Bewegungsgleichung & effektive Masse", 3),                            # 9.1
    ("Elektronen als Wellenpakete", 2),                                     # 9.1.1
    ("Ladungstransport in Bändern", 3),                                     # 9.1.2
    ("Elektronen und Löcher", 3),                                           # 9.1.3
    ("Drude-Modell", 4),                                                   # 9.2.1
    ("Sommerfeldsche Theorie", 3),                                          # 9.2.2
    ("Boltzmann-Gleichung (Transport)", 3),                                 # 9.2.3
    ("Elektrischer Ladungstransport", 3),                                   # 9.2.4
    ("Elektronstreuung", 3),                                                # 9.2.5
    ("Temperaturabhängigkeit der Leitfähigkeit", 3),                        # 9.2.6
    ("Eindimensionale Leiter", 2),                                          # 9.2.7
    ("Quantenpunkte", 2),                                                   # 9.2.8
    ("Luttinger-Flüssigkeit", 2),                                           # 9.2.9
    ("Thermische Leitfähigkeit", 2),                                        # 9.2.10
    ("Wiedemann–Franz-Gesetz", 3),                                          # 9.2.11
    ("Fermi-Funktion im stationären Gleichgewicht", 2),                     # 9.2.12
    ("Elektronen im Magnetfeld (Überblick)", 3),                            # 9.3
    ("Zyklotronresonanz", 3),                                               # 9.3.1
    ("Landau-Niveaus", 4),                                                  # 9.3.2
    ("Zustandsdichte im Magnetfeld", 3),                                    # 9.3.3
    ("De Haas–van Alphen-Effekt", 3),                                       # 9.3.4
    ("Hall-Effekt", 4),                                                     # 9.3.5
    ("Quanten-Hall-Effekt", 4),                                             # 9.3.6
    ("Quanten-Hall-Effekt in Graphen", 3),                                  # 9.3.7

    # 10 Halbleiter
    ("Intrinsische kristalline Halbleiter", 3),                              # 10.1
    ("Bandlücke & optische Absorption", 4),                                  # 10.1.1
    ("Effektive Masse von Elektronen & Löchern", 3),                        # 10.1.2
    ("Ladungsträgerdichte (intrinsisch)", 3),                               # 10.1.3
    ("Dotierung (n/p)", 4),                                                 # 10.2.1
    ("Ladungsträgerdichte & Fermi-Niveau (dotiert)", 3),                    # 10.2.2
    ("Beweglichkeit & elektrische Leitfähigkeit", 3),                        # 10.2.3
    ("Amorphe Halbleiter: Leitfähigkeit", 2),                               # 10.3.1
    ("Amorphe Halbleiter: Defektzustände", 2),                              # 10.3.2
    ("p–n-Übergang", 4),                                                    # 10.4.1
    ("Metall/Halbleiter-Kontakt (Schottky)", 3),                             # 10.4.2
    ("Heterostrukturen & Übergitter", 3),                                   # 10.4.3
    ("Bauelemente auf p–n-Basis", 4),                                       # 10.5.1
    ("Transistoren", 4),                                                    # 10.5.2
    ("Halbleiterlaser", 4),                                                 # 10.5.3

    # 11 Supraleitung
    ("Phänomenologie der Supraleitung", 3),                                 # 11.1
    ("Meißner-Effekt & London-Gleichungen", 4),                              # 11.1.1
    ("Kritisches Magnetfeld & thermodynamische Größen", 3),                 # 11.1.2
    ("Cooper-Paare", 4),                                                    # 11.2.1
    ("BCS-Grundzustand", 4),                                                # 11.2.2
    ("BCS bei endlicher Temperatur", 3),                                     # 11.2.3
    ("Nachweis der Energielücke", 3),                                       # 11.2.4
    ("Kritischer Strom & kritisches Feld", 3),                               # 11.2.5
    ("Makroskopische Wellenfunktion", 3),                                    # 11.3
    ("Flussquantisierung", 3),                                              # 11.3.1
    ("Josephson-Effekt", 4),                                                # 11.3.2
    ("Ginzburg–Landau-Theorie", 4),                                         # 11.4.1
    ("Supraleiter 2. Art & Grenzflächenenergie", 3),                         # 11.4.2
    ("Hochtemperatur-Supraleiter", 3),                                      # 11.4.3

    # 12 Magnetismus
    ("Dia- & Paramagnetismus (Überblick)", 3),                               # 12.1
    ("Diamagnetismus", 2),                                                  # 12.1.1
    ("Paramagnetismus", 3),                                                 # 12.1.2
    ("Ferromagnetismus (Überblick)", 4),                                    # 12.2
    ("Molekularfeldnäherung", 3),                                           # 12.2.1
    ("Austauschwechselwirkung (lokalisierte Elektronen)", 3),               # 12.2.2
    ("Austausch im freien Elektronengas", 2),                                # 12.2.3
    ("Band-Ferromagnetismus", 3),                                           # 12.2.4
    ("Spinwellen", 3),                                                      # 12.2.5
    ("Thermodynamik der Magnonen", 2),                                      # 12.2.6
    ("Ferromagnetische Domänen", 2),                                        # 12.2.7
    ("Ferri- & Antiferromagnetismus (Überblick)", 3),                        # 12.3
    ("Ferrimagnetismus", 2),                                                # 12.3.1
    ("Antiferromagnetismus", 3),                                            # 12.3.2
    ("Riesen-Magnetowiderstand (GMR)", 3),                                  # 12.3.3
    ("Spingläser", 2),                                                      # 12.4

    # 13 Dielektrische & optische Eigenschaften
    ("Dielektrische Funktion & optische Messungen", 3),                     # 13.1
    ("Lokales Feld & Clausius–Mossotti", 3),                                 # 13.2
    ("Elektrische Polarisation von Isolatoren (Überblick)", 3),              # 13.3
    ("Elektronische Polarisierbarkeit", 3),                                  # 13.3.1
    ("Ionenpolarisation", 3),                                               # 13.3.2
    ("Optische Phononen in Ionenkristallen", 3),                             # 13.3.3
    ("Erzwungene Schwingungen (Ionenkristalle)", 2),                          # 13.3.4
    ("Phonon-Polaritonen", 3),                                              # 13.3.5
    ("Orientierungspolarisation", 2),                                       # 13.3.6
    ("Ferroelektrizität", 3),                                               # 13.3.7
    ("Exzitonen", 3),                                                       # 13.3.8
    ("Optische Eigenschaften freier Ladungsträger (Überblick)", 3),          # 13.4
    ("Ausbreitung EM-Wellen in Metallen", 3),                                # 13.4.1
    ("Plasmonen (longitudinale Schwingungen)", 4),                           # 13.4.2
]
