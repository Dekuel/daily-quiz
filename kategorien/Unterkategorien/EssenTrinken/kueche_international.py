# -*- coding: utf-8 -*-
# Unterkategorien/EssenTrinken/kueche_international.py
"""
Unterthemen (Subtopics) für die Disziplin „Küche international“.
Diese Liste wird von kategorien/essen_trinken.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Ein konsistentes, domänenübergreifendes Schema für Quizfragen aufzubauen,
das (1) thematisch strukturierte Kategorien liefert und (2) zu jeder
Kategorie realistische Schwierigkeits-Intervalle (1–10) definiert.

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

C. Zwei Achsen der Schwierigkeit
--------------------------------
1) Bekanntheit (Population Familiarity): Wie verbreitet ist Basiswissen?
2) Inhalts-/Methodenkomplexität: Wie tief/technisch ist das Verständnis?

Die **untere Intervallgrenze (min)** wird primär durch *Bekanntheit*
bestimmt (Level-1/2-Fragen bei sehr populären Küchen).
Die **obere Intervallgrenze (max)** durch *Komplexität/Expertise*
(z. B. regionale DOP/AOP, spezifische Garmethoden, Fermentationen).

D. Gewichte → grobe Heuristik
-----------------------------
Gewicht 4 (Kernfelder, global präsent), 3 (Vertiefungen), 2 (Standard/Umfeld).
Die tatsächlichen Intervalle sind gemäß A–C kalibriert.

E. Basis-Kategorien (Level-1 fähig)
-----------------------------------
Je Makroregion gibt es eine „… – Basisfakten“-Kategorie (min = 1), um sehr
leichte Fragen (Zuordnungen, typische Gerichte/Produkte) zu ermöglichen.

F. Vergleichende & Querschnittskategorien
-----------------------------------------
Zur internationalen Küche gehören auch Transfer-Themen (Streetfood, Fusion,
pflanzliche Traditionen, Schutzsiegel), die regionenübergreifende Fragen
ermöglichen.

G. Intervall-Setzung – Regeln
-----------------------------
- min: 1–2 bei populären Themen (Italien, Japan, Mexiko etc.)
- max: bis 9–10, wenn viel Tiefe (Regionalküchen, Schutzsiegel, Techniken)
- Breite: groß (1–9/10) für Küchen mit Populär- und Expertenaspekten
- Konsistenz: Gleichartige Subkategorien erhalten vergleichbare min/max
- „Basis…“-Kategorien stets min = 1

"""

# Schwierigkeits-Skala kurz:
# 1=Allgemeinwissen … 10=schwerstmöglich.

SUBTOPICS = [
    # ──────────────────────────────────────────────────────────────────────
    # Europa – Süd & West
    # ──────────────────────────────────────────────────────────────────────
    ("Italien: Regionen, Klassiker & DOP/IGP (Nord vs. Süd)", 4, (2,10)),
    ("Frankreich: Saucen, Regionen & AOP/AOC (Bistros bis Haute Cuisine)", 4, (3,10)),
    ("Spanien & Portugal: Tapas/Petiscos, Iberico, Bacalhau, DOC", 3, (2,9)),
    ("Mittelmeer: Olivenöl, Kräuterprofile & Meeresküche (Vergleich)", 2, (1,7)),
    # Basis
    ("Südeuropa – Basisfakten (typische Gerichte, Zutaten, Käse/Schinken)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Europa – Mitteleuropa & DACH / Ost & Nord
    # ──────────────────────────────────────────────────────────────────────
    ("Mitteleuropa & DACH: Brotkultur, Knödel, Wurst & g.g.A./g.U.", 3, (2,8)),
    ("Balkan & Osteuropa: Eintöpfe, Teigwaren, Käse- & Paprikaküche", 3, (2,8)),
    ("Nordische Küche: New Nordic, Einlegen, Wild & Fisch", 3, (3,9)),
    # Basis
    ("Europa – Basisfakten (Regionen erkennen, typische Produkte)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Nahost & Levante, Maghreb, Afrika
    # ──────────────────────────────────────────────────────────────────────
    ("Levante & Nahost: Mezze, Tahina/Zaatar, Fladenbrote", 4, (2,9)),
    ("Maghreb: Couscous, Harissa, Pastilla, Tajine-Traditionen", 3, (3,8)),
    ("Äthiopien & Horn von Afrika: Injera, Berbere, Niter Kibbeh", 3, (4,9)),
    ("West-/Zentral-/Südliches Afrika: Jollof, Erdnuss, Maniok, Braise", 3, (3,9)),
    # Basis
    ("Afrika & Levante – Basisfakten (Gewürze, Brote, Signature-Dishes)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Südasien, Zentralasien
    # ──────────────────────────────────────────────────────────────────────
    ("Indien: Regionale Masalas, Tandoor, Tiffin-Kultur (Nord/Süd/Ost/West)", 4, (3,10)),
    ("Pakistan & Bangladesch: Karahi, Biryani-Profile, Fisch- & Senfsaat", 3, (4,9)),
    ("Sri Lanka & Malediven: Curryblätter, Kokos, Hoppers/Pol Sambol", 2, (3,8)),
    ("Zentralasien: Plov/Pilaw, Teigwaren, Nomadenprägungen", 2, (3,8)),
    # Basis
    ("Südasien – Basisfakten (Grundgewürze, Brotsorten, Garmethoden)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Ostasien
    # ──────────────────────────────────────────────────────────────────────
    ("China: Regionalküchen (Sichuan, Kanton, Jiangsu, Shandong) & Techniken", 4, (2,10)),
    ("Japan: Dashi/Umami, Sushi/Sashimi, Fermentation (Miso/Shoyu)", 4, (3,10)),
    ("Korea: Hansik-Prinzipien, Kimchi-Ökosystem & Gochujang/Doenjang", 3, (3,9)),
    # Basis
    ("Ostasien – Basisfakten (Grundtechniken, Grundprodukte, Reis/Soja)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Südostasien
    # ──────────────────────────────────────────────────────────────────────
    ("Thailand: Balance süß–sauer–salzig–scharf, Kräuter & Pasten", 4, (2,9)),
    ("Vietnam: Kräuterfrische, Fischsauce, Pho/Bun/Com – Nord/Süd", 4, (2,9)),
    ("Indonesien/Malaysia/Singapur: Sambal, Rendang, Nasi Lemak, Peranakan", 3, (3,9)),
    ("Philippinen: Adobo, Sinigang, Lechon – Einflüsse & Säureprofile", 2, (3,8)),
    # Basis
    ("Südostasien – Basisfakten (Kräuter, Saucen, Grundgerichte)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Amerika – Nord, Mittel, Süd & Karibik
    # ──────────────────────────────────────────────────────────────────────
    ("Mexiko: Mais/Chili/Bohnen, Moles, regionale Vielfalt (Oaxaca/Yucatán)", 4, (2,10)),
    ("Anden & Peru: Ceviche, Kartoffelvielfalt, Aji & Nikkei-Einflüsse", 3, (3,9)),
    ("Brasilien: Feijoada, Farofa, Dendê, Regionalvielfalt (Nord/Nordost/Süd)", 3, (3,9)),
    ("Karibik: Kreolisierung, Callaloo/Jerk, Rumküche", 2, (3,8)),
    ("Nordamerika: BBQ-Regionen, Diner- & Soul-Food-Traditionen", 2, (2,8)),
    # Basis
    ("Amerika – Basisfakten (Maiswege, Chili, Bohnen, Signature-Dishes)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Ozeanien & Pazifik / Diaspora
    # ──────────────────────────────────────────────────────────────────────
    ("Ozeanien & Pazifik: Hangi, Meeresfrüchte, Wurzeln & Taro", 2, (3,8)),
    ("Diaspora & Migration: Kreolisierung, Nikkei, Chifa, Indo-Caribbean", 3, (3,9)),
    # Basis
    ("Pazifik & Diaspora – Basisfakten (Techniken, Zutaten, Hybridgerichte)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Querschnitt & Vergleich
    # ──────────────────────────────────────────────────────────────────────
    ("Schutzsiegel international: DOP/AOP/IGP/g.U./g.g.A. – Vergleich & Beispiele", 3, (3,9)),
    ("Streetfood weltweit: Zubereitungsprinzipien & Authentizität vs. Adaption", 3, (2,8)),
    ("Vegetarisch/vegan traditionell: Hülsenfrüchte, Tofu/Tempeh, Jackfruit", 2, (2,8)),
    ("Getreide & Grundnahrungen: Reis, Mais, Weizen, Hirse – regionale Rollen", 2, (1,7)),
    ("Würz- und Fettprofile im Vergleich (Olivenöl, Ghee, Schmalz, Palmöl, Erdnuss)", 2, (3,8)),
    # Basis (einfacher Vergleich)
    ("Küche international – Basisvergleiche (Gericht - Land/Region zuordnen)", 2, (1,7)),
]
