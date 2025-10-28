# -*- coding: utf-8 -*-
# Unterkategorien/Geographie/kartographie_gis.py
"""
Unterthemen (Subtopics) für die Disziplin „Kartographie & GIS“.
Diese Liste wird von kategorien/geographie.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Kurzleitfaden
==========================================================================

Skala (1–10):
1 = absolutes Grundwissen … 10 = schwerstmöglich (Expertenniveau)

Zwei Achsen:
- Bekanntheit (Population Familiarity)
- Inhalts-/Methodenkomplexität (Conceptual/Method Complexity)

Gewichte (Heuristik):
- 4 = Kernkonzepte (typ. 2–4, bis 9/10 möglich)
- 3 = Vertiefungen (typ. 3–5, bis 9/10 möglich)
- 2 = Standard/Umfeld (typ. 1–4, bis 8/9 möglich)

Regeln:
- Mindestens eine „Basis…“-Kategorie mit min=1
- Zeitvariable Inhalte (Standards/Softwareversionen) möglichst neutral formulieren
- Vergleichs-/Querschnittsthemen erlauben Transfer- und Anwendungsfragen
"""

# Schwierigkeits-Skala kurz: 1=Allgemeinwissen … 10=schwerstmöglich.

SUBTOPICS = [
    # 1 BASIS & GRUNDLAGEN
    ("Kartographie – Basiswissen (Zuordnungen: Maßstab, Legende, Nordpfeil, Projektion)", 2, (1,7)),
    ("Maßstab, Generalisierung & Genauigkeit (Konzept & Beispiele)", 4, (2,9)),
    ("Kartennetzentwürfe (Projektionen): Flächen-/Winkel-/Längen­treue", 4, (3,9)),
    ("Koordinaten & Referenzsysteme (Geographisch vs. Projektion, EPSG-Grundideen)", 4, (3,9)),
    ("Kartensymbologie & visuelle Variablen (Position, Größe, Form, Helligkeit, Textur)", 3, (3,9)),

    # 2 PROJEKTIONEN & DATUM
    ("Geodätische Datums & Ellipsoide (WGS84 vs. ETRS89 – Grundprinzipien)", 3, (4,9)),
    ("Projektionstypen im Vergleich (Mercator, Lambert, Albers, UTM) – Eignung nach Zweck", 3, (3,9)),
    ("Verzerrungsanalyse & Tissot’sche Indikatrix – Interpretation", 2, (5,9)),

    # 3 GIS-DATENMODELLE & DATEIFORMATE
    ("Vektor vs. Raster – Topologie, Attribute, Auflösung, Zellenwert", 4, (2,9)),
    ("Topologische Beziehungen (adjazent, enthaltend, schneidend) – DE-9IM-Grundidee", 3, (4,9)),
    ("Datenformate & Strukturen (Shapefile, GeoPackage, GeoJSON, TIFF) – Einsatzszenarien", 3, (3,9)),
    ("Metadaten & Qualitätsmerkmale (Herkunft, Maßstab, Genauigkeit, Aktualität)", 3, (3,9)),

    # 4 RÄUMLICHE ANALYSE & GEOPROCESSING
    ("Puffer, Verschneidung, Vereinigen, Clip – typische Workflows", 4, (3,9)),
    ("Räumliche Abfragen & Join-Typen (Attribut-/Spatial-Join)", 3, (3,9)),
    ("Dichte- & Hotspot-Analysen (Kernel Density, Getis-Ord – Konzept)", 2, (5,9)),
    ("Netzwerkanalyse (Wege, Isochronen, Erreichbarkeit) – Grundprinzipien", 3, (4,9)),

    # 5 HÖHENMODELLE & RASTERANALYSE
    ("DGM/DOM/DSM – Unterschiede, Ableitungen (Hangneigung, Exposition, Krümmung)", 3, (4,9)),
    ("Interpolation (IDW, Kriging – Konzept & Anwendungsfälle, ohne Mathe)", 2, (5,9)),
    ("Viewshed/Line-of-Sight & Hydrologische Ableitungen (Flow Accumulation)", 3, (5,9)),

    # 6 FERNERKUNDUNG (satellitär & luftgestützt)
    ("Spektralkanäle & Indizes (NDVI/NDWI/NDBI – Interpretation, Anwendungsbeispiele)", 3, (4,9)),
    ("Auflösungstypen (räumlich, spektral, radiometrisch, temporal)", 3, (3,9)),
    ("Klassifikation (überwacht vs. unüberwacht – Grundideen)", 2, (5,9)),

    # 7 KARTENTYPEN & THEMATISCHE VISUALISIERUNG
    ("Choroplethen vs. Proportional-Symbole vs. Isolinien – Eignung & Fallstricke", 4, (3,9)),
    ("Klassierungsverfahren (Equal Interval, Quantile, Jenks) – Vergleich & Wirkung", 3, (4,9)),
    ("Kartendesign & Lesbarkeit (Kontrast, Hierarchie, Labeling, Farbe – Grundsätze)", 3, (3,9)),

    # 8 WEB-MAPPING & DIENSTE
    ("Kachelprinzip & Web-Merkmale (XYZ/TMS, Tile-Pyramide) – Grundideen", 2, (4,9)),
    ("OGC/Web-Dienste (WMS, WFS, WMTS, WCS) – Zweck & Unterschiede", 3, (4,9)),
    ("Client- vs. Serverseitige Darstellung, Vektor-Tiles – Konzepte", 2, (5,9)),

    # 9 GEODATENMANAGEMENT & ETHIK
    ("Geodaten-Infrastruktur (Kataloge, Lizenzen, Open Data) – Prinzipien", 2, (3,8)),
    ("Geoprivacy & Ethik (Location Tracking, Aggregation, Re-Identifikation)", 2, (5,9)),
    ("Datenqualität & Unsicherheit kommunizieren (Legende, Maßstab, Disclaimer)", 2, (3,8)),

    # 10 ANWENDUNGEN & QUERSCHNITT
    ("Lagebestimmung & GNSS-Grundlagen (Positionsfehler, Korrekturen – konzeptuell)", 3, (3,9)),
    ("Multikriterielle Eignungsanalyse (MCDA) – Workflow & Kartenkommunikation", 2, (5,9)),
    ("Querschnitt – Basis (Kartensymbole zuordnen, Projektion nach Zweck wählen)", 2, (1,7)),
]
