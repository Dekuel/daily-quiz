# -*- coding: utf-8 -*-
# Unterkategorien/KunstLiteratur/kunstwissen_allgemeines.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Kunstwissen – Allgemeines“.
Diese Liste wird von kategorien/kunst_literatur.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Ein konsistentes, domänenübergreifendes Schema für Quizfragen aufzubauen,
das (1) thematisch strukturierte Kategorien liefert und (2) zu jeder
Kategorie realistische Schwierigkeits-Intervalle (1–10) definiert.
Das System ist so formuliert, dass es auf andere Fächer übertragen werden kann.

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
1) Bekanntheit (Population Familiarity)
2) Inhalts-/Methodenkomplexität (Conceptual/Method Complexity)

Die **untere Intervallgrenze (min)** wird primär durch *Bekanntheit*,
die **obere Intervallgrenze (max)** durch *Komplexität/Expertise* bestimmt.

D. Gewichte → Basis-Heuristik (nur Orientierung)
------------------------------------------------
Gewicht 4 (Kernkonzepte): typ. (2–4, bis 9/10 möglich)
Gewicht 3 (Vertiefungen): typ. (3–5, bis 9/10 möglich)
Gewicht 2 (Standard/Umfeld): typ. (1–4, bis 8/9 möglich)

E. Basiskategorien (Level-1 fähig)
----------------------------------
Pro Überkategorie wird eine „Basis“-Kategorie ergänzt, die **min = 1** setzt.

F. Vergleichende & themenübergreifende Kategorien
-------------------------------------------------
Querschnitts-Kategorien ermöglichen übergreifende Fragen (Gattungen, Medien,
Institutionen, Geografie, Zeitachse, Praktiken). Zeitvariable Themen (z. B.
Museumslandschaft, Markt) sollten „Stand: Jahr/Quelle“ berücksichtigen.

G. Intervall-Setzung – Regeln
-----------------------------
1) min: 1–2 bei verbreiteten Basisthemen; ≥4 bei Spezialthemen.
2) max: 8–10 bei substantieller Tiefe; 7–8 bei begrenzter Tiefe.
3) Breite: groß, wenn trivial bis hochkomplex plausibel; klein bei Spezial.
4) Konsistenz: Gleichartige Themen vergleichbar einstufen; „Basis…“ immer min=1.

H. Abgrenzung zu anderen Dateien
--------------------------------
Dieses Modul deckt **allgemeines Kunstwissen** ab: Terminologie, Medien-,
Methoden-, Institutions- und Marktgrundlagen. Spezifische Inhalte zu
- „Bildende Kunst & Malerei“,
- „Kunstgeschichte & Epochen“,
- „Moderne & Zeitgenössische Kunst“
werden in ihren jeweiligen Modulen behandelt und hier nur übergreifend angerissen.
"""

# Schwierigkeits-Skala kurz (zur Laufzeit nutzbar):
# 1=Allgemeinwissen … 10=schwerstmöglich.

SUBDISCIPLINES = [
    # 1 Allgemeines & Grundlagen
    ("Kunstbegriff, Funktionen & Abgrenzung (Kunst/Design/Kunsthandwerk)", 4, (2,10)),
    ("Gestaltungselemente: Linie, Fläche, Form, Farbe, Raum, Textur", 4, (1,9)),
    ("Kompositionslehre: Balance, Rhythmus, Kontrast, Hierarchie", 4, (2,10)),
    ("Farblehre – Grundlagen (Primär/Sekundär, Kontraste, Wirkung)", 3, (1,9)),
    ("Material- & Technik-Überblick (Malerei, Grafik, Plastik, Medien)", 4, (2,9)),
    ("Bildanalyse & Werkbeschreibung (Formanalyse, Kontext, Methode)", 3, (3,9)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Basiswissen Kunst: Grundbegriffe, Zuordnungen, einfache Ikonen/Signaturen", 2, (1,7)),

    # 2 Bildsysteme, Gattungen & Darstellung
    ("Perspektive & Raumdarstellung (Zentral-, Parallel-, Luftperspektive)", 3, (2,9)),
    ("Ikonografie & Symbolsprache – Grundlagen (Attribute, Allegorie)", 3, (2,9)),
    ("Klassische Gattungen – Überblick (Porträt, Landschaft, Stillleben, Historie)", 3, (2,9)),
    ("Narration im Bild: Allegorie, Metapher, Zyklus, Serien", 2, (3,8)),
    ("Abstraktion vs. Figuration: Strategien & Kriterien", 3, (3,9)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Gattungen – Basis: typische Motive & Zuordnungen", 2, (1,7)),

    # 3 Medien & Verfahren (übergreifend)
    ("Zeichnung & Druckgrafik – Verfahren & Merkmale (Radierung, Holzschnitt, Litho)", 3, (2,9)),
    ("Skulptur/Plastik: Materialien & Techniken (Stein, Bronze, Holz, Guss)", 3, (2,9)),
    ("Fotografie – Grundlagen (Aufnahme, Reproduktion, Formate)", 3, (1,9)),
    ("Installation, Performance & Medienkunst – Grundbegriffe", 2, (3,8)),
    ("Digitale & Generative Kunst (inkl. KI) – Überblick & Werklogik", 2, (4,9)),
    ("Konservierung/Restaurierung & Dokumentation (Zustand, Maßnahmen, Ethik)", 3, (3,9)),
    ("Urheberrecht, Nutzungsrechte & Lizenzen (keine Rechtsberatung)", 2, (4,8)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Medien – Basis: Verfahren wiedererkennen (z. B. Aquarell vs. Öl, Radierung vs. Holzschnitt)", 2, (1,7)),

    # 4 Institutionen, Praxis & Markt
    ("Museen, Kunsthallen, Biennalen & Off-Spaces: Formate & Rollen", 2, (2,8)),
    ("Kuratieren & Ausstellungsdesign (Konzept, Hängung, Vermittlung)", 3, (3,9)),
    ("Kunstmarkt: Galerien, Auktionshäuser, Preisbildung, Editionen", 3, (3,9)),
    ("Provenienzforschung & Kulturgutschutz (Raubkunst, Restitution)", 3, (4,9)),
    ("Sammeln & Zertifikate: Strategien, Editionen, Echtheit", 2, (3,8)),
    ("Kunstkritik & Schreiben über Kunst: Kriterien, Genres, Feuilleton", 2, (3,8)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Institutionen & Markt – Basisfakten (z. B. Aufgaben Museum/Galerie, Auktionsbegriffe)", 2, (1,7)),

    # 5 Theorie, Ästhetik & Wahrnehmung (grundlegend)
    ("Ästhetische Theorien – Überblick (Mimesis, Ausdruck, Form, Anti-Ästhetik)", 3, (4,10)),
    ("Kunst & Gesellschaft: Politik, Identität, Gender, Postkolonialität", 3, (4,9)),
    ("Wahrnehmungstheorie & Semiotik (Gestalt, Zeichen, Bedeutung)", 3, (4,9)),
    ("Original, Authentizität, Aura & Reproduktion", 3, (5,10)),
    ("Ethik in der Kunstpraxis (kulturelle Aneignung, Umgang mit Sensiblem)", 2, (4,9)),
    ("Interdisziplinäre Bezüge (Architektur, Design, Musik, Literatur)", 2, (2,8)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Theorie – Basis: zentrale Begriffe & Denkrichtungen erkennen", 2, (1,7)),

    # 6 Vergleichende & Querschnitts-Themen
    ("Vergleich: Gattungen & Medien (Eignung, Wirkung, Grenzen)", 2, (2,8)),
    ("Vergleich: Darstellungsweisen über Zeiten/Kulturen (ikonisch–realistisch–abstrakt)", 2, (3,9)),
    ("Methodenvergleich der Bildanalyse (Formalismus, Ikonologie, Sozialgeschichte)", 2, (3,8)),
    ("Berühmte Sammlungen & Museen weltweit (Basis, zeitabhängig)", 2, (1,8)),
    ("Berufsbilder im Kunstfeld (Künstler:in, Kurator:in, Restaurator:in, Vermittlung)", 2, (1,7)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Vergleich – Basis: Zuordnungen (Werk–Gattung–Medium–Institution)", 2, (1,8)),
]
