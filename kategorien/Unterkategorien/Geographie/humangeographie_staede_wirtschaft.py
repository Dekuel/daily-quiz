# -*- coding: utf-8 -*-
# Unterkategorien/Geographie/humangeographie_staede_wirtschaft.py
"""
Unterthemen (Subtopics) für die Disziplin „Humangeographie & Städte“.
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
- Zeitvariable Inhalte (Demografie, Rangfolgen, Mieten) möglichst kontextualisieren
- Vergleichs-/Querschnittsthemen erlauben transferorientierte Fragen
"""

# Schwierigkeits-Skala kurz: 1=Allgemeinwissen … 10=schwerstmöglich.

SUBTOPICS = [
    # 1 BASIS & GRUNDLAGEN (einsteigerfreundlich)
    ("Stadtbegriffe & Abgrenzungen (Stadt, Agglomeration, Metropolregion)", 4, (2,9)),
    ("Urbanisierung vs. Suburbanisierung vs. Reurbanisierung – Grundideen", 4, (2,9)),
    ("Humangeographie – Basiswissen (Zuordnungen: Begriffe, Beispiele, Kartenlesen)", 2, (1,7)),
    ("Demografischer Übergang (Phasenmodell, Bevölkerungsdiagramme)", 3, (2,9)),

    # 2 STADTTHEORIEN & STADTFORM
    ("Stadtstrukturmodelle: Burgess, Hoyt, Harris–Ullman (Mehrkerne)", 4, (3,9)),
    ("Urban Morphology: Block-, Parzellen- & Straßennetz-Logiken", 3, (4,9)),
    ("Zentralitäts-, Rang-Größen-Regel & Primate-City-Konzept", 4, (3,9)),
    ("Funktionale Stadtgliederung & Nutzungsmischung (Wohnen/Arbeiten/Freizeit)", 3, (3,8)),

    # 3 MEGASTÄDTE, METROPOLEN & GLOBALISIERUNG
    ("Megastädte & Mega-Regionen: Definitionen, Beispiele, Herausforderungen", 4, (3,9)),
    ("Weltstädte/Global Cities (GaWC): Knoten, Netzwerke & Funktionen", 4, (4,10)),
    ("Globalisierung & Wertschöpfungsketten (HQs, Producer Services, FDI)", 3, (4,9)),
    ("Informalität & Duale Ökonomien in Metropolen des Globalen Südens", 3, (4,9)),

    # 4 WIRTSCHAFTSRÄUME, INDUSTRIE & DIENSTLEISTUNGEN
    ("Kern-Peripherie-Modelle (Friedmann, Krugman – New Economic Geography)", 4, (4,10)),
    ("Industrielle Cluster & Agglomerationsvorteile (Marshall/Porter)", 4, (4,10)),
    ("Standorttheorien (Weber, Christaller, Lösch) – Kernaussagen & Beispiele", 4, (4,10)),
    ("Sonderwirtschaftszonen, Exportzonen & Technologieparks", 3, (4,9)),
    ("Tourismusgeographie & Events (Stadtimage, Gentrifizierungseffekte)", 2, (3,8)),

    # 5 VERKEHR, LOGISTIK & INFRASTRUKTUR
    ("Verkehrsnetze & Knoten (Hubs, Korridore, Transit): Grundprinzipien", 4, (3,9)),
    ("Häfen & maritime Logistik (Hinterland, Gateway, Chokepoints)", 3, (4,9)),
    ("ÖPNV & Multimodalität (U-Bahn, S-Bahn, BRT, Rad, Fuß) – Netz-/Dichtewirkung", 3, (3,8)),
    ("Transit-Oriented Development (TOD) & 15-Minuten-Stadt", 2, (3,8)),

    # 6 WOHNEN, BODEN & STADTPOLITIK
    ("Bodenrente & Land-Wert-Gradient (Bid-Rent, Alonso–Muth–Mills)", 4, (4,10)),
    ("Gentrifizierung, Verdrängung & Mietdynamiken", 3, (3,9)),
    ("Informelle Siedlungen & Slums: Treiber, Aufwertung, Inklusion", 3, (4,9)),
    ("Stadtplanung: Flächennutzungsplanung, Zoning, Green Belts", 3, (3,9)),
    ("Partizipation, Governance & Smart City (Chancen/Risiken)", 2, (3,8)),

    # 7 SOZIALE & KULTURELLE DIMENSIONEN
    ("Segregation & Nachbarschaftseffekte (ethnisch, sozial, funktional)", 4, (4,9)),
    ("Kreative Milieus, Kulturwirtschaft & Stadtimage", 3, (3,8)),
    ("Bildung, Gesundheit & Infrastrukturzugang (Stadt–Land-Gefälle)", 2, (3,8)),

    # 8 UMWELT, KLIMA & RESILIENZ
    ("Stadtklima & Wärmeinsel-Effekt (UHI): Ursachen & Maßnahmen", 4, (3,9)),
    ("Klimaanpassung in Städten (Grün-/Blauinfrastruktur, Schwammstadt)", 3, (4,9)),
    ("Risiko & Resilienz: Vulnerabilität, Exposure, Governance (SDG 11)", 3, (4,9)),
    ("Luftqualität, Lärm & Verkehrswende – Zielkonflikte", 2, (3,8)),

    # 9 MIGRATION & BEVÖLKERUNG
    ("Migration: Push-/Pull-Faktoren, Remittances & Urbanisierung", 3, (3,9)),
    ("Binnenwanderung & Shrinking Cities (Deindustrialisierung, Alterung)", 3, (4,9)),
    ("Demografische Alterung & Versorgung (Pflege, Mobilität, Barrierefreiheit)", 2, (3,8)),

    # 10 DIGITALISIERUNG & ARBEIT
    ("Digitale Ökonomie & Plattformstädte (Gig Work, Co-Working, E-Commerce)", 3, (4,9)),
    ("Telepräsenz, Homeoffice & Suburbanisierungsimpulse", 2, (3,8)),
    ("Datenräume, Geodaten & Governance (Privacy, Bias, Überwachung)", 2, (5,9)),

    # 11 QUERSCHNITT & VERGLEICHE (Transferorientiert)
    ("Vergleich: Rang-Größen-Regel vs. Primate City (Fallbeispiele, Messgrößen)", 3, (4,9)),
    ("Vergleich: Stadtmodelle (Burgess/Hoyt/Mehrkerne) – Stärken/Schwächen", 3, (4,9)),
    ("Vergleich: Globale Hafenhierarchien & Hinterlandanbindung", 2, (4,9)),
    ("Querschnitt – Basis (Zuordnungen: Stadt–Funktion, Cluster–Region, Korridor–Verbindung)", 2, (1,7)),
]
