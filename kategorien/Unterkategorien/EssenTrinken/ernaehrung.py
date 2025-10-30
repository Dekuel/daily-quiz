# -*- coding: utf-8 -*-
# Unterkategorien/EssenTrinken/ernaehrung.py
"""
Unterthemen (Subtopics) für die Disziplin „Ernährung“.
Diese Liste wird von kategorien/essen_trinken.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Allgemeinverständliche, quiz-taugliche Fragen zur Ernährung strukturieren –
von Makro-/Mikronährstoffen über Kennzeichnung & Sicherheit bis hin zu
Nachhaltigkeit und Sensorik – mit realistischen Schwierigkeitsintervallen (1–10).

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
1) Bekanntheit: Alltagswissen (z. B. Proteine) vs. Spezialwissen (z. B. Bioverfügbarkeit).
2) Komplexität: Funktionsverständnis, Verarbeitungseinfluss, Kennzeichnungslogik, Hygiene.

D. Heuristik für Gewichtung
---------------------------
Gewicht 4 = Kernfelder (Makro-/Mikronährstoffe, Lebensmittelsicherheit)
Gewicht 3 = Vertiefungen (Ernährungsformen, Bioverfügbarkeit, Nachhaltigkeit)
Gewicht 2 = Standard/Umfeld (Label, Sensorik, Haushalts-Praxis)

E. Basis-Kategorien (min=1)
---------------------------
Ermöglichen sehr einfache Zuordnungen, Begriffe & Beispiele.

Hinweis
-------
Alle Inhalte sind **allgemeinbildend** und qualitativ ausgelegt; keine
individuellen Gesundheits- oder Therapieempfehlungen.

"""

SUBTOPICS = [
    # ──────────────────────────────────────────────────────────────────────
    # Makronährstoffe & Energie (qualitativ)
    # ──────────────────────────────────────────────────────────────────────
    ("Makronährstoffe: Funktionen & Beispiele (Protein/Fett/Kohlenhydrate)", 4, (2,8)),
    ("Protein: essentielle Aminosäuren, biologische Wertigkeit (qualitativ)", 4, (3,9)),
    ("Fette: ungesättigt/gesättigt, Omega-3/-6, Emulsionen (qualitativ)", 3, (3,9)),
    ("Kohlenhydrate: Stärke, Zucker, Ballaststoffe – Grundverständnis", 3, (2,8)),
    ("Ballaststoffe: löslich/unlöslich, Wirkung & Quellen (qualitativ)", 3, (3,8)),
    ("Glykämischer Index/Last (GI/GL) – Konzept & Grenzen (qualitativ)", 2, (4,9)),
    # Basis
    ("Makros – Basisfakten (Zuordnungen: Nährstoff ↔ Lebensmittel)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Mikronährstoffe (qualitativ)
    # ──────────────────────────────────────────────────────────────────────
    ("Vitamine: fett-/wasserlöslich – Funktionen & Quellen (Überblick)", 4, (3,9)),
    ("Mineralstoffe & Spurenelemente: Calcium, Eisen, Zink, Jod (Überblick)", 4, (3,9)),
    ("Vitamin D, B12, Folat – Besonderheiten & Quellen (qualitativ)", 3, (4,9)),
    ("Eisen & Bioverfügbarkeit: Häm-/Nicht-Häm, Vitamin-C-Effekt (qualitativ)", 3, (4,9)),
    ("Jod/Seefisch/Algen & Salzjodierung – Einordnung (qualitativ)", 2, (3,8)),
    # Basis
    ("Mikros – Basisfakten (Vitamin-/Mineralstoff-Beispiele zuordnen)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Ernährungsformen & Muster (qualitativ, evidenzbewusst)
    # ──────────────────────────────────────────────────────────────────────
    ("Mediterranes Muster: typische Lebensmittel & Grundprinzipien", 3, (2,8)),
    ("Vegetarisch/Vegan: Proteinquellen, B12-Fokus, Jod/Eisen (qualitativ)", 3, (3,9)),
    ("Low-Carb/Low-Fat – Unterschiede & typische Fallstricke (qualitativ)", 2, (3,8)),
    ("Flexitarisch & Plant-Forward: Hülsenfrüchte, Vollkorn, Nüsse", 2, (2,7)),
    ("Sport & Ernährung (qualitativ): Timing, Flüssigkeit, Snacks", 2, (2,7)),
    # Basis
    ("Ernährungsformen – Basisfakten (Kernaussagen, typische Speisen)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Lebensmittelsicherheit & Hygiene (qualitativ)
    # ──────────────────────────────────────────────────────────────────────
    ("Küchenhygiene: Kreuzkontamination, Hand- & Flächenhygiene", 4, (2,8)),
    ("Kritische Temperaturen: Kühlkette, Warmhalten, Kerntemperaturen (qualitativ)", 4, (3,8)),
    ("HACCP-Prinzip (einfach): Gefahren erkennen & Kontrollpunkte", 3, (4,9)),
    ("Mikrobiologie alltagsnah: Keimquellen, Sporen, Reste lagern", 3, (3,8)),
    ("Allergenmanagement in der Küche (qualitativ)", 2, (3,8)),
    # Basis
    ("Sicherheit – Basisfakten (Resteküche, Mindesthaltbarkeit, Riechtest?)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Verarbeitung, Technik & Haushalt (qualitativ)
    # ──────────────────────────────────────────────────────────────────────
    ("Wärme & Nährstoffe: Schonende Garverfahren, Vitaminstabilität", 3, (3,8)),
    ("Oxidation/Bräunung: Vitamin-C-Verlust, Maillard vs. Karamell (qualitativ)", 3, (4,9)),
    ("Gefrieren & Auftauen: Kristallbildung, Qualität, Safety (qualitativ)", 2, (3,8)),
    ("Fermentation zuhause: Sauerkraut/Joghurt – Prinzipien & Hygiene", 2, (3,8)),
    ("NOVA/Verarbeitungsgrad (Konzept) – Chancen & Grenzen (qualitativ)", 2, (4,8)),
    # Basis
    ("Haushalt – Basisfakten (Kühlschrankzonen, Haltbarkeit, Reste)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Kennzeichnung, Recht & Allergene (EU-Bezug, qualitativ)
    # ──────────────────────────────────────────────────────────────────────
    ("EU-Allergenliste: Kennzeichnungspflicht & Beispiele", 4, (3,8)),
    ("Nährwerttabelle & Claims (z. B. ‚fettarm‘, ‚zuckerfrei‘) – Grundlogik", 3, (3,8)),
    ("Geografische Herkunft: g.U., g.g.A., TSG – Abgrenzung (Überblick)", 3, (3,8)),
    ("Zutatenliste: Reihenfolge, Zusatzstoffe (E-Nummern, Klassen) – qualitativ", 2, (3,8)),
    ("Front-of-Pack-Label (z. B. Nutri-Score) – Idee & Grenzen (qualitativ)", 2, (3,8)),
    # Basis
    ("Label – Basisfakten (Allergene erkennen, einfache Claims zuordnen)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Nachhaltigkeit & Food Waste (qualitativ)
    # ──────────────────────────────────────────────────────────────────────
    ("Saisonalität & Regionalität: Grundprinzipien & Beispiele", 3, (2,7)),
    ("CO₂-Fußabdruck – grobe Treiber (Transport, Kühlung, Tierprodukte)", 3, (4,8)),
    ("Food Waste: Planung, Lagerung, Resteverwertung", 3, (2,7)),
    ("Wasser- & Flächenverbrauch – qualitative Einordnung", 2, (4,8)),
    ("Verpackung & Recycling – Trade-offs (qualitativ)", 2, (3,7)),
    # Basis
    ("Nachhaltigkeit – Basisfakten (Saisongemüse, Reste-Tipps, Haltbarkeit)", 2, (1,6)),

    # ──────────────────────────────────────────────────────────────────────
    # Sensorik & Essverhalten (qualitativ)
    # ──────────────────────────────────────────────────────────────────────
    ("Grundgeschmäcker & Umami, Trigeminal (Schärfe/Kühle) – Basics", 3, (2,8)),
    ("Texturen & Mundgefühl: Crisp, Creamy, Chewy – Wirkung im Essen", 2, (2,7)),
    ("Aromenbildung: Maillard, Röstung, Fermentation (Überblick)", 2, (3,8)),
    ("Portionsgrößen & Umfeldfaktoren (Geschirr, Tempo, Ablenkung) – qualitativ", 2, (2,7)),
    # Basis
    ("Sensorik – Basisfakten (Geschmack ↔ Beispiel-Lebensmittel zuordnen)", 2, (1,5)),

    # ──────────────────────────────────────────────────────────────────────
    # Darmmikrobiom & Toleranzen (qualitativ, ohne Heilsversprechen)
    # ──────────────────────────────────────────────────────────────────────
    ("Darmmikrobiom: Vielfalt, Präbiotika/Probiotika (qualitativ)", 3, (4,9)),
    ("Laktose, Fruktose, Gluten – grundlegende Einordnung (qualitativ)", 2, (4,8)),
    ("Schärfe & Bitterkeit – Gewöhnung & kulturelle Prägung (qualitativ)", 2, (2,7)),
    # Basis
    ("Toleranzen – Basisfakten (Begriffserklärungen, einfache Beispiele)", 2, (1,6)),
]
