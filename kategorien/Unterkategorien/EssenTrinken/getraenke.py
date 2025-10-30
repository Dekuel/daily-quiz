# -*- coding: utf-8 -*-
# Unterkategorien/EssenTrinken/getraenke.py
"""
Unterthemen (Subtopics) für die Disziplin „Getränke“.
Diese Liste wird von kategorien/essen_trinken.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Fragen zu Herkunft, Verarbeitung, Stilen, Sensorik und Schutzsystemen
von Getränken (alkoholisch & alkoholfrei) so strukturieren, dass sowohl
einfache Zuordnungen als auch tiefe Fachfragen (1–10) möglich sind.

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
1) Bekanntheit: Alltags- vs. Spezialwissen (z. B. „Espresso“ vs. „Carbonic Maceration“).
2) Komplexität: Verarbeitung, Fermentation, Appellationen, Chemie, Sensorik.

D. Heuristik für Gewichtung
---------------------------
Gewicht 4 = Kernbereiche mit großer Tiefe (Kaffee, Tee, Bier, Wein, Spirituosen)
Gewicht 3 = große Themenkomplexe / Stile / Methoden mittlerer Tiefe
Gewicht 2 = Basiswissen, Randfelder, Trends, Service & rechtliche Einordnung

E. Basis-Kategorien
-------------------
Pro Hauptbereich gibt es „… – Basisfakten“ (min = 1) für sehr leichte Fragen.

"""

SUBTOPICS = [
    # ──────────────────────────────────────────────────────────────────────
    # Kaffee
    # ──────────────────────────────────────────────────────────────────────
    ("Kaffee: Pflanzenarten & Herkunft (Arabica/Robusta, Anbaugebiete)", 4, (2,9)),
    ("Aufbereitung: washed/natural/honey & Auswirkungen auf Sensorik", 4, (3,9)),
    ("Röstgrade & Chemie: Maillard, Röstaromen, Entgasung", 3, (4,9)),
    ("Brühmethoden: Espresso, Filter, Immersion, Druckprofile", 3, (3,9)),
    ("Extraktion & Parameter: Mahlgrad, Ratio, Temperatur, TDS (qualitativ)", 3, (4,9)),
    # Basis
    ("Kaffee – Basisfakten (Espresso vs. Filter, typische Begriffe)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Tee
    # ──────────────────────────────────────────────────────────────────────
    ("Tee: Camellia sinensis – Grün/Schwarz/Oolong/Weiß/Gelb/Pu-Erh", 4, (2,9)),
    ("Oxidation, Röstung & Fixierung: Herstellschritte & Effekte", 3, (3,9)),
    ("Aufgussparameter: Temperatur, Zeit, Wasserhärte (qualitativ)", 3, (2,8)),
    ("Herkünfte & Stile: China, Japan, Indien, Taiwan, Sri Lanka", 3, (3,8)),
    # Basis
    ("Tee – Basisfakten (Sorten erkennen, einfache Aufgussregeln)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Bier
    # ──────────────────────────────────────────────────────────────────────
    ("Bier: Rohstoffe & Brauprozess (Malz, Hopfen, Hefe, Wasser)", 4, (2,9)),
    ("Bierstile: Lager, Ale, Weizen, Stout, IPA – Profil & Unterschiede", 3, (2,8)),
    ("Gärung & Hefe: unter-/obergärig, Ester/Phenole (qualitativ)", 3, (3,9)),
    ("Hopfengaben & Bittere (IBU, Kalthopfung – qualitativ)", 2, (3,8)),
    # Basis
    ("Bier – Basisfakten (Stile zuordnen, Reinheitsgebot – einfach)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Wein
    # ──────────────────────────────────────────────────────────────────────
    ("Wein: Rebsorten & Terroir (Klimazonen, Böden, Stilistik)", 4, (3,9)),
    ("Weinausbau: Edelstahl, Holz, Reifung, Batonnage, Malolaktik (qualitativ)", 3, (4,9)),
    ("Schaumwein-Methoden: traditionell/tank/ancestral – Unterschiede", 3, (4,9)),
    ("Appellationen & Schutz: g.U./g.g.A., AOP/DOC/DOCG, Prädikate", 3, (3,9)),
    # Basis
    ("Wein – Basisfakten (trocken/lieblich, Rebsorten, Regionen – einfach)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Spirituosen & Mixology
    # ──────────────────────────────────────────────────────────────────────
    ("Whisky/Whiskey: Rohstoffe, Pot/Column Still, Reifung, Regionen", 4, (4,9)),
    ("Rum: Melasse vs. Agricole, Stilwelten & Herkunftsschutz", 3, (4,9)),
    ("Gin: Botanicals, London Dry vs. New Western, Aromatisierung", 3, (3,9)),
    ("Agaven-Spirituosen: Tequila vs. Mezcal (Arten, Öfen, NOM/CRT)", 3, (4,9)),
    ("Brände/Geiste/Liköre: Kategorien & Zucker-/Aromaregeln (qualitativ)", 2, (4,9)),
    ("Cocktails: Grundfamilien (Sour, Old Fashioned, Highball, Martini) – Balance", 2, (2,8)),
    # Basis
    ("Spirituosen – Basisfakten (Hauptkategorien, typische Rohstoffe)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Fermentierte alkoholfreie Getränke & regionale Spezialitäten
    # ──────────────────────────────────────────────────────────────────────
    ("Kombucha, Wasserkefir, Rejuvelac: Fermentation & Säureprofil (qualitativ)", 3, (3,8)),
    ("Sake & Shochu/Soju: Reis-/Getreidevergärung, Koji, Stile", 3, (4,9)),
    ("Cider & Perry: Apfel/Birne – Stilistik, Restsüße, Herkunft", 2, (3,8)),
    ("Kvass, Boza, Ayran, Lassi: regionale Getränke & Kulturen", 2, (2,8)),
    # Basis
    ("Fermentierte Alkoholfreie – Basisfakten (Kombucha/Kefir – einfach)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Wasser, Kakao & Erfrischungsgetränke
    # ──────────────────────────────────────────────────────────────────────
    ("Wasser: Mineralisierung, Härte, Mündgefühl & Pairing (qualitativ)", 2, (2,7)),
    ("Kakao/Schokolade als Getränk: Bohnen, Conchieren, Trinkschokolade", 2, (2,8)),
    ("Erfrischungsgetränke & Shrubs: Sirup, Säure, Kohlensäure (qualitativ)", 2, (1,6)),
    ("Alkoholfrei-Trend & Zero-Proof: Destillate ohne Alkohol, Bitters, Aperitif-Profile", 2, (2,7)),
    # Basis
    ("Wasser & Softdrinks – Basisfakten (Sprudel/still, einfache Zuordnungen)", 2, (1,5)),

    # ──────────────────────────────────────────────────────────────────────
    # Querschnitt & Service
    # ──────────────────────────────────────────────────────────────────────
    ("Sensorik: Aromenrad, Grundgeschmäcker, Fehlerbilder (Brett/Skunk/OT)", 3, (3,9)),
    ("Service & Glasformen: Temperaturbereiche, Dekantieren (qualitativ)", 2, (2,7)),
    ("Lebensmittelsicherheit & Alkohol: ABV, Pasteurisation, Hygiene (qualitativ)", 2, (2,7)),
    ("Recht & Kennzeichnung: EU-Allergene, Alkoholangaben, Geografische Herkunft", 2, (3,8)),
    # Basis
    ("Getränke – Basisvergleiche (Kategorie ↔ Rohstoff/Region zuordnen)", 2, (1,5)),
]
