# -*- coding: utf-8 -*-
# Unterkategorien/Geographie/klima_biome_naturregionen.py
"""
Unterthemen (Subtopics) für die Disziplin „Klima, Biome & Naturregionen“.
Diese Liste wird von kategorien/geographie.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Kurzleitfaden
==========================================================================

Skala (1–10):
1 = absolutes Grundwissen … 10 = schwerstmöglich (Expertenniveau)

Heuristik:
- Gewicht 4 = Kernkonzepte (breit & tief, bis 9/10)
- Gewicht 3 = Vertiefungen (mittlere bis hohe Komplexität)
- Gewicht 2 = Standard/Umfeld (allgemein bekannt, bis 7–8)
- Mindestens eine „Basis…“-Kategorie mit min = 1 (z. B. einfache Zuordnungen)

Ziel:
Fragen von reinen Zuordnungen (z. B. „Wo herrscht Tropenklima?“)
bis hin zu analytischen Verständnisfragen (z. B. „Warum ist das Klima
in Westseitenlagen milder als in Ostseitenlagen?“) zu ermöglichen.
"""

# Schwierigkeits-Skala kurz: 1=Allgemeinwissen … 10=schwerstmöglich.

SUBTOPICS = [
    # 1 BASIS & KLIMASYSTEM
    ("Klima – Basiswissen (Zuordnungen: Zonen, Jahreszeiten, Passate, ITCZ)", 2, (1,7)),
    ("Witterung vs. Klima (Definitionen, Zeitmaßstab, Beispiele)", 4, (1,8)),
    ("Strahlungsbilanz der Erde & Energiehaushalt (Konzept, Einflussfaktoren)", 4, (3,9)),
    ("Atmosphärische Zirkulation (Hadley-, Ferrel-, Polarzellen, Jetstreams)", 4, (4,9)),
    ("Planetarische Wind- & Druckgürtel – Verlagerung & Jahresgang", 3, (3,9)),

    # 2 KLASSIFIKATION & KLIMADIAGRAMME
    ("Köppen-Geiger-Klassifikation (Grundtypen, Buchstabensystem, Beispiele)", 4, (3,9)),
    ("Klimadiagramme lesen & interpretieren (Niederschlag, Temperatur, Vegetation)", 4, (2,8)),
    ("Höhenklima & Temperaturgradient (adiabatisch, Gebirge, Inversion)", 3, (4,9)),
    ("Kontinentalität & Meeresnähe – Einfluss auf Temperatur & Niederschlag", 3, (3,8)),
    ("Monsune & Jahreszeitenverschiebung (Süd-/Ostasien, ITCZ-Lage)", 3, (3,9)),

    # 3 KLIMAREGIONEN & KLIMATYPEN (global)
    ("Tropisches Klima (Af/Am/Aw) – Merkmale & Vegetation", 4, (2,9)),
    ("Trockengebiete (BWh/BSh/BWk/BSk) – Ursachen & Verbreitung", 4, (2,9)),
    ("Gemäßigte Klimate (Cf/Cw/Df/Dw) – West-/Ostseitenklima im Vergleich", 4, (3,9)),
    ("Polare & subpolare Klimate (ET/EF) – Charakteristika & Anpassungen", 3, (3,9)),
    ("Gebirgsklimate (vertikale Zonation, Höhenstufen, Exposition)", 3, (3,9)),

    # 4 BIOME & VEGETATIONSZONEN
    ("Biome – Basiswissen (Zuordnungen: Regenwald, Savanne, Wüste, Steppe, Taiga, Tundra)", 2, (1,7)),
    ("Tropischer Regenwald – Struktur, Böden, Biodiversität", 4, (2,9)),
    ("Savanne & Monsunklima – Trocken-/Feuchtzeiten, Vegetation, Nutzung", 3, (2,8)),
    ("Wüsten & Halbwüsten – Arten, Ursachen, Anpassungen", 3, (2,8)),
    ("Mittelmeerklima – Hartlaubvegetation & Saisonalität", 3, (3,8)),
    ("Nadelwald & Boreale Zone – Permafrost, Boden, Lichtverhältnisse", 3, (3,9)),
    ("Tundra & Polarregionen – Vegetationsgrenzen & Anpassungen", 3, (3,8)),

    # 5 KLIMAFAKTOREN & TELEKONNEKTIONEN
    ("El Niño / La Niña (ENSO) – Ursachen, Folgen, Telekonnektionen", 3, (4,9)),
    ("NAO & PDO – Einfluss auf Temperatur- und Niederschlagsmuster", 3, (5,9)),
    ("Albedo & Rückkopplungen (Eis, Wolken, Aerosole)", 3, (5,9)),
    ("Vulkanismus & kurzzeitige Klimaeffekte (Aerosole, Abkühlung)", 2, (5,8)),

    # 6 NATURREGIONEN & GEOMORPHOLOGIE
    ("Zonale vs. azonale Naturregionen – Begriffe & Beispiele", 4, (3,9)),
    ("Relief, Böden & Klima – Zusammenhänge der Naturraumeinheiten", 3, (4,9)),
    ("Klimatische Höhenstufen & Vegetationsgradienten (Tropen bis Hochgebirge)", 3, (3,9)),
    ("Bodenbildungsprozesse (Laterit, Podsol, Schwarzerde, Tundraboden)", 3, (4,9)),

    # 7 MENSCH–UMWELT-BEZÜGE & KLIMAWANDEL
    ("Klimawandel – Grundlagen (Treibhauseffekt, anthropogene Verstärkung)", 4, (3,9)),
    ("Regionale Auswirkungen (Dürre, Gletscher, Permafrost, Vegetationszonen)", 3, (4,9)),
    ("Anpassung & Klimaschutz (SDG 13, Paris-Abkommen, Maßnahmen)", 3, (4,9)),
    ("Desertifikation & Landdegradation (Sahel, Australien, Zentralasien)", 3, (4,9)),
    ("Klimamigration & Risiko – Ursachen & regionale Muster", 2, (5,9)),

    # 8 QUERSCHNITT & VERGLEICHE
    ("Vergleich: Westseiten- vs. Ostseitenklima (Temperatur/Niederschlag)", 3, (3,8)),
    ("Vergleich: Tropische vs. gemäßigte Regenwälder – Struktur & Klima", 3, (3,9)),
    ("Vergleich: Polare vs. Gebirgsklimate – Gemeinsamkeiten & Unterschiede", 2, (3,8)),
    ("Querschnitt – Basis (Zuordnungen: Klimaform ↔ Vegetation ↔ Region)", 2, (1,7)),
]
