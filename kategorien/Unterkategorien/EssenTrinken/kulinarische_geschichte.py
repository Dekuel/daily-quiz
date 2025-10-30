# -*- coding: utf-8 -*-
# Unterkategorien/EssenTrinken/kulinarische_geschichte.py
"""
Unterthemen (Subtopics) für die Disziplin „Kulinarische Geschichte“.
Diese Liste wird von kategorien/essen_trinken.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Historische und kulturgeschichtliche Entwicklungen der Ernährung
verständlich abbilden – von frühen Agrartraditionen bis zur globalisierten
Industrieküche. Das System definiert für jede Unterkategorie realistische
Schwierigkeitsintervalle (1–10).

B. Skala (1–10) – Bedeutung
---------------------------
1 = absolutes Grundwissen (≈ 95 % der Bevölkerung in DE)
2 = sehr einfaches Grundwissen
3 = einfache Fragen (ohne schwere Thematik)
4 = leichte Fragen (Recall, einfache Anwendung)
5 = einfach–mittel (70–80 % schaffbar)
6 = mittlere Komplexität (≈ 60 % schaffbar)
7 = mittel–schwer (für Nicht-Expert:innen anspruchsvoll)
8 = schwer (deutliches Vorwissen/vertieftes Verständnis nötig)
9 = Expertenwissen (Fachkenntnisse erforderlich)
10 = schwerstmöglich (oberes Expertenniveau)

C. Schwierigkeitsachsen
-----------------------
1) Bekanntheit: wie stark verbreitet ist das Basiswissen (z. B. Kartoffel aus Amerika)?
2) Komplexität: wie viel Kontextwissen über Handel, Gesellschaft, Technik ist nötig?

D. Heuristik für Gewichtung
---------------------------
Gewicht 4 = Schlüsselereignisse oder zentrale Entwicklungen  
Gewicht 3 = größere Themenkomplexe mit mittlerer Tiefe  
Gewicht 2 = begleitende Aspekte, regionale Beispiele, Alltagskultur

E. Struktur
-----------
Die Kulinarische Geschichte umfasst:
- Frühe Landwirtschaft & Domestikation
- Handelsnetze & Kolonialismus
- Industrialisierung & Technik
- Migration & Globalisierung
- Schutzsysteme & Herkunftskennzeichnung
- Esskultur, Rituale, Gesellschaft

F. Intervall-Logik
------------------
- min niedrig (1–3) bei allgemein bekannten Epochen & Produkten
- max hoch (8–10) bei historischen Prozessen, wirtschaftlichen Folgen, Quellenwissen
- Basis-Kategorien (min=1) für einfache Zuordnungen & Datierungen

"""

SUBTOPICS = [
    # ──────────────────────────────────────────────────────────────────────
    # Frühgeschichte & Agrarrevolution
    # ──────────────────────────────────────────────────────────────────────
    ("Neolithische Revolution: Domestikation von Getreide & Vieh", 4, (2,9)),
    ("Frühe Fermentation & Haltbarmachung (Brot, Bier, Käse)", 3, (3,9)),
    ("Antike Küche: Rom, Griechenland, Ägypten – Luxus vs. Alltag", 3, (3,8)),
    ("Handel & Luxusgüter in der Antike (Wein, Olivenöl, Gewürze)", 3, (3,8)),
    # Basis
    ("Frühe Ernährung – Basisfakten (erste Nutzpflanzen, Brot, Bier)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Mittelalter & Frühneuzeit
    # ──────────────────────────────────────────────────────────────────────
    ("Mittelalterliche Tafelkultur & Klosterküche", 3, (3,8)),
    ("Gewürzhandel & Seidenstraße: Pfeffer, Zimt, Muskat", 4, (3,9)),
    ("Salz & Konservierungstechniken – ökonomische Bedeutung", 3, (3,8)),
    ("Essensrituale & Standesunterschiede (Europa)", 2, (2,7)),
    # Basis
    ("Mittelalter – Basisfakten (Hauptnahrungsmittel, Fastenzeiten, Tafelsitten)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Neuzeit & Kolonialismus
    # ──────────────────────────────────────────────────────────────────────
    ("Kolumbianischer Austausch: Tomate, Kartoffel, Chili, Mais", 4, (2,9)),
    ("Zucker, Kaffee & Kakao: Plantagenwirtschaft & Sklavenhandel", 4, (3,9)),
    ("Koloniale Gewürzpolitik: Niederländer, Portugiesen, Briten", 3, (4,9)),
    ("Globalisierung der Ernährung: Tee, Tabak, Zuckertrias", 3, (3,8)),
    ("Migration von Rezepturen & Hybridküchen (Kreolisierung, Nikkei, Chifa)", 3, (3,9)),
    # Basis
    ("Frühe Neuzeit – Basisfakten (neue Produkte aus Amerika, Entdeckungszeit)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # 18.–19. Jahrhundert: Industrialisierung & Moderne
    # ──────────────────────────────────────────────────────────────────────
    ("Industrialisierung & Konservierung: Pasteurisierung, Dosen, Kühlung", 4, (3,9)),
    ("Nahrungsmittelindustrie & Massenproduktion (Maggi, Nestlé, Kellogg)", 3, (4,9)),
    ("Technische Innovationen: Mühle, Raffination, Kühlkette", 3, (3,9)),
    ("Ernährung im 19. Jh.: Bürgertum, Arbeiterküche, Hauswirtschaft", 2, (2,8)),
    # Basis
    ("Industrialisierung – Basisfakten (erste Konserven, Pasteur, Kälte)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # 20.–21. Jahrhundert: Globalisierung, Konsum & Nachhaltigkeit
    # ──────────────────────────────────────────────────────────────────────
    ("Globalisierung & Fast Food (McDonaldization, Convenience, Kritik)", 4, (2,9)),
    ("Ernährungswissenschaft & Diättrends (Kalorien, Vitamine, Light-Produkte)", 3, (3,9)),
    ("Nachhaltigkeit & Slow Food: Ursprung, Prinzipien, CO₂-Bilanz", 3, (3,9)),
    ("Food Waste & Recyclingküche", 2, (2,8)),
    ("Schutzsiegel & Herkunftsbezeichnungen (g.U., g.g.A., TSG)", 3, (3,9)),
    # Basis
    ("Moderne Ernährung – Basisfakten (Fast Food, Bio, Fair Trade)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Kulturelle & soziale Dimension
    # ──────────────────────────────────────────────────────────────────────
    ("Esskultur & Tischsitten: Rituale, Etikette, gesellschaftliche Codes", 3, (2,8)),
    ("Feste & Feiertage: symbolische Speisen, religiöse Bezüge", 3, (2,8)),
    ("Geschlechterrollen & Küche: Arbeitsteilung, Wandel, Feminismus", 2, (3,8)),
    ("Medien & Kochbücher: Rezeptsammlungen, Fernsehen, Influencer", 2, (2,8)),
    # Basis
    ("Esskultur – Basisfakten (Rituale, typische Feste, Tischsitten)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Querschnitt & Vergleich
    # ──────────────────────────────────────────────────────────────────────
    ("Vergleich: Kolonialprodukte & heutige Handelsstrukturen", 3, (4,9)),
    ("Migration & Essen als Identitätsmarker", 3, (3,9)),
    ("Technikgeschichte: von Feuerstelle bis Molekularküche", 3, (3,9)),
    ("Wandel der Mahlzeitenstruktur (Frühstück–Abendessen–Snacking)", 2, (2,8)),
    ("Kulturelle Aneignung & Authentizität in der Küche", 3, (4,9)),
    # Basis
    ("Kulinarische Geschichte – Basisvergleiche (Epochen, Produkte, Erfindungen)", 2, (1,5)),
]
