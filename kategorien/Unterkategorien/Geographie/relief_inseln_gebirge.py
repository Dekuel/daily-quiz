# -*- coding: utf-8 -*-
# Unterkategorien/Geographie/relief_inseln_gebirge.py
"""
Unterthemen (Subtopics) für die Disziplin „Relief, Inseln & Gebirge“.
Diese Liste wird von kategorien/geographie.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Kurzleitfaden
==========================================================================

Skala (1–10):
1 = absolutes Grundwissen … 10 = schwerstmöglich (oberes Expertenniveau)

Heuristik:
- Gewicht 4 → Kernkonzepte (Struktur, Prozesse, globale Systeme)
- Gewicht 3 → Vertiefungen (Regionen, Dynamik, Geo-/Tektonik)
- Gewicht 2 → Standard/Umfeld (Zuordnungen, Basiswissen)
- Mindestens eine „Basis…“-Kategorie mit min=1 für sehr einfache Fragen

Ziele:
- Verbindung physischer Geographie (Reliefbildung, Tektonik) mit Raumwissen
- Möglichkeit sowohl für Karten- und Zuordnungsfragen (Level 1–3)
  als auch für prozessuale/deutende Fragen (Level 7–10)
"""

# Schwierigkeits-Skala kurz: 1=Allgemeinwissen … 10=schwerstmöglich.

SUBTOPICS = [
    # 1 BASIS & GRUNDLAGEN
    ("Relief – Basiswissen (Zuordnungen: Gebirge, Tiefebenen, Inselgruppen, Vulkanketten)", 5, (1,7)),
    ("Reliefenergie, Morphologie & Geomorphometrie (Höhenunterschiede, Steilheit, Talformen)", 3, (3,9)),
    ("Plattentektonik & Orogenese – Grundmechanismen (Subduktion, Kollision, Rift, Hotspot)", 4, (3,10)),
    ("Isostasie & Krustenbewegungen (Gleichgewicht, Glazialisostasie, Hebung/Senkung)", 3, (5,10)),

    # 2 GEBIRGE DER WELT
    ("Junge Faltengebirge (Alpen, Anden, Himalaya) – Entstehung, Alter, Prozesse", 4, (3,9)),
    ("Alte Gebirge (Ural, Appalachen, Skanden) – Erosionsformen & Hebungsreste", 3, (3,9)),
    ("Hochgebirgsformen: Kar, Zirkus, U-Tal, Hängegletscher – geomorphologische Merkmale", 3, (4,9)),
    ("Hochländer & Tafelländer (z. B. Dekkan, Tibet, Äthiopisches Hochland) – Genese & Nutzung", 3, (3,9)),

    # 3 INSELN & INSELBOGENE
    ("Inseln – Basiswissen (Zuordnungen: Vulkanisch, Korallen-, Kontinentalinsel)", 2, (1,7)),
    ("Vulkanische Inselbögen (z. B. Japan, Antillen, Aleuten) – Entstehung & Tektonik", 4, (4,10)),
    ("Koralleninseln & Atolle – Bildung (Darwin-Modell), Erosion & Meeresspiegelanstieg", 3, (3,9)),
    ("Inselketten & Hotspots (Hawaii, Azoren, Réunion) – Plattenbewegung & Altersabfolge", 3, (4,9)),

    # 4 PROZESSE & LANDFORMEN
    ("Verwitterung & Erosion – physikalisch, chemisch, biologisch", 4, (2,9)),
    ("Fluviale Prozesse: Täler, Deltas, Terrassen, Mäander", 4, (2,9)),
    ("Glaziale & periglaziale Formen (Moränen, Drumlins, Solifluktion, Frostmusterboden)", 4, (3,9)),
    ("Äolische Prozesse (Dünenformen, Deflation, Löss)", 3, (3,8)),
    ("Küstenrelief: Kliffs, Fjorde, Deltas, Haffs, Strandwälle", 3, (3,8)),

    # 5 GEOMORPHOLOGISCHE ZONIERUNG & REGIONALE BEISPIELE
    ("Reliefzonen Europas (Mittelgebirge, Hochgebirge, Tiefländer) – Struktur & Entstehung", 3, (2,8)),
    ("Asien: Gebirgssysteme (Himalaya, Pamir, Tian Shan) – Tektonische Bedeutung", 3, (4,9)),
    ("Afrika: Rift Valley & Hochplateaus – Tektonik & Erosion", 3, (3,9)),
    ("Amerika: Kordilleren, Appalachen, Anden – Vergleich alt/jung", 3, (3,9)),
    ("Ozeanien & Pazifik: Inselbögen, Hotspots, Korallenriffe – Überblick", 2, (2,8)),

    # 6 RISIKEN & MENSCH–UMWELT-BEZÜGE
    ("Erdrutsche, Bergstürze & Muren – Prozesse, Gefährdung, Prävention", 3, (3,9)),
    ("Gebirgsnutzung: Tourismus, Rohstoffe, Weidewirtschaft – Konflikte & Nachhaltigkeit", 3, (3,9)),
    ("Inseln als sensible Ökosysteme – Isolation, Biodiversität, Vulnerabilität", 3, (3,9)),
    ("Ressourcen & Landschaftsschutz: UNESCO-Geoparks, Bergwaldmanagement", 2, (3,8)),

    # 7 SPEZIALTHEMEN & VERGLEICHE
    ("Vergleich: Junges vs. altes Gebirge – Morphologie & Gestein", 3, (3,9)),
    ("Vergleich: Vulkanische Insel vs. Korallenatoll – Entstehung & Nutzung", 3, (3,9)),
    ("Vergleich: Reliefenergie in Gebirgen unterschiedlicher Klimazonen", 2, (4,9)),
    ("Querschnitt – Basis (Zuordnungen: Gebirge ↔ Kontinent ↔ Plattentyp)", 2, (1,7)),
]
