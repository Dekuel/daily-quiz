# -*- coding: utf-8 -*-
# Unterkategorien/Geographie/naturkatastrophen_georisiken.py
"""
Unterthemen (Subtopics) für die Disziplin „Naturkatastrophen & Georisiken“.
Diese Liste wird von kategorien/geographie.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

Kurzleitfaden:
- Skala 1–10: 1=Allgemeinwissen … 10=oberes Expertenniveau
- Zwei Achsen: Bekanntheit (wie vertraut) & Komplexität (Tiefe/Methodik)
- Gewichte (Heuristik): 4=Kern, 3=Vertiefung, 2=Umfeld
- Mindestens eine Basis-Kategorie (min=1) für sehr leichte Zuordnungen
- Zeitvariable Inhalte (Häufigkeiten, Schadenssummen) vermeiden oder einordnen
"""

# Schwierigkeits-Skala kurz: 1=Allgemeinwissen … 10=schwerstmöglich.

SUBTOPICS = [
    # 1 BASIS & BEGRIFFE
    ("Begriffe: Gefahr (Hazard), Exposition, Vulnerabilität, Risiko – Grundverständnis", 4, (2,9)),
    ("Naturkatastrophen – Basis (Zuordnungen: Prozess ↔ Beispielregion ↔ typische Folgen)", 2, (1,7)),
    ("Sendai-Framework & Risikokreislauf (Prevention–Preparedness–Response–Recovery)", 3, (4,9)),

    # 2 TEKTONISCHE GEFAHREN
    ("Erdbeben: Plattengrenzen (Subduktion/Transform), Magnitude vs. Intensität, Baugrundeffekte", 4, (4,10)),
    ("Tsunamis: Auslöser (Seebeben, Hangrutsch, Vulkan), Laufwege, Küstengefährdung", 3, (5,10)),
    ("Vulkanismus: Vulkantypen (Strato/Schild/Caldera), Eruptionstypen & Risiken (Lava, Pyroklastik, Lahar)", 4, (4,10)),
    ("Geothermale & vulkanisch-tektonische Sekundärgefahren (Gase, Aschewolken, Flugverkehr)", 2, (5,9)),

    # 3 HYDRO-METEOROLOGISCHE GEFAHREN
    ("Tropische Wirbelstürme: Entstehung, Zugbahnen, Sturmflut & Niederschlagsrisiken", 4, (4,10)),
    ("Starkregen, Sturzfluten & Flusshochwasser: Einzugsgebiete, Versiegelung, Retention", 4, (3,9)),
    ("Dürre & Hitzewellen: Fernwirkungen (ENSO/NAO), Bodenfeuchte, Landwirtschaft & Gesundheit", 3, (4,9)),
    ("Konvektive Unwetter: Hagel, Downbursts, Tornados – Bedingungen & räumliche Muster", 2, (4,8)),

    # 4 GRAVITATIVE & KRYOSPHÄRE-BEZOGENE PROZESSE
    ("Hangrutschungen & Massenbewegungen: Trigger (Niederschlag, Beben), Lithologie, Relief", 4, (4,10)),
    ("Lawinen (Trocken/Nass), Permafrost & Tauprozesse – alpine Risiken & Schutzmaßnahmen", 3, (4,9)),
    ("Gletscherseeausbrüche (GLOFs) & proglaziale Dynamiken – Indikatoren & Hotspots", 3, (5,10)),

    # 5 KÜSTEN & MEERESNAHE RISIKEN
    ("Küstenerosion & Überflutung: Wellen, Tiden, Meeresspiegel, Subsidenz", 3, (4,9)),
    ("Deltagebiete: Landgewinnung vs. Setzung, Zyklon-/Sturmflutgefährdung", 3, (4,9)),
    ("Korallenriffe & Mangroven als natürlicher Küstenschutz – Leistungen & Grenzen", 2, (3,8)),

    # 6 KOMBINIERTE/VERKETTETE EREIGNISSE (COMPOUND EVENTS)
    ("Mehrfachgefahren & Kaskaden (z. B. Beben→Tsunami→Natech): Risikoaufsummierung", 3, (5,10)),
    ("Gleichzeitigkeit & Abhängigkeiten (Compound Flooding: Fluss + Sturmflut + Starkregen)", 3, (5,10)),

    # 7 ERKENNUNG, MODELLIERUNG & FRÜHWARNUNG
    ("Monitoring & Fernerkundung: seismisch, GNSS, Radar, Satellit – konzeptioneller Einsatz", 3, (4,9)),
    ("Gefahren- & Risikokarten: Hazard Curves, Return Periods, Szenarien, Unsicherheiten", 4, (5,10)),
    ("Frühwarnsysteme & Schwellenwerte (Lead Time, False Alarms, Last-Mile-Kommunikation)", 3, (4,9)),

    # 8 STADT, INFRASTRUKTUR & WIRTSCHAFT
    ("Urbanes Risiko: Dichte, Baualter, kritische Infrastrukturen (Energie, Verkehr, Wasser)", 3, (4,9)),
    ("Baurichtlinien, Erdbeben-/Windlastnormen & Retrofit – Grundprinzipien", 3, (5,9)),
    ("Versicherung, Rückversicherung & Katastrophenbonds – Risikotransfer (konzeptionell)", 2, (5,9)),

    # 9 ANPASSUNG, MANAGEMENT & GOVERNANCE
    ("Prävention vs. Schutz vs. Vorsorge: harte/weiße/Grün-Blau-Maßnahmen", 3, (3,9)),
    ("Zonierung, Landnutzung & No-Build-Areas (Dammbruchszenarien, Setzungsgebiete)", 3, (4,9)),
    ("Partizipation, Risiko-Kommunikation & soziale Verwundbarkeit (inkl. Gender/Armut)", 2, (3,8)),

    # 10 QUERSCHNITT & BASIS-VERGLEICHE
    ("Vergleich: Subduktionszone vs. Transformstörung – Gefahrenprofile & Beispiele", 3, (4,9)),
    ("Vergleich: Delta- vs. Gebirgsfluss – Hochwassertypen & Steuerfaktoren", 3, (4,9)),
    ("Querschnitt – Basis (Zuordnungen: Prozess ↔ Warnsymbol ↔ geeignete Maßnahme)", 2, (1,7)),
]
