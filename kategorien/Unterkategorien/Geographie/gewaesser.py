# -*- coding: utf-8 -*-
# Unterkategorien/Geographie/gewaesser.py
"""
Unterthemen (Subtopics) für die Disziplin „Flüsse, Seen & Meere“.
Diese Liste wird von kategorien/geographie.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Ein konsistentes, domänenübergreifendes Schema für Quizfragen aufzubauen,
das (1) thematisch strukturierte Kategorien liefert und (2) zu jeder
Kategorie realistische Schwierigkeits-Intervalle (1–10) definiert.
Das System ist so formuliert, dass es auf andere Fächer übertragbar ist.

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
1) Bekanntheit (Population Familiarity): Wie verbreitet ist Basiswissen
   zu diesem Thema in der Allgemeinbevölkerung?
2) Inhalts-/Methodenkomplexität (Conceptual/Method Complexity):
   Wie tief/spezialisiert ist das Verständnis, das Fragen typischerweise
   erfordern?

Die **untere Intervallgrenze (min)** wird primär durch *Bekanntheit*
bestimmt (erlaubt Level-1/2/3-Fragen bei populären Themen).
Die **obere Intervallgrenze (max)** wird durch *Komplexität/Expertise*
bestimmt (lässt Raum bis 9–10, wenn das Thema Tiefe hergibt).

D. Gewichte → Basis-Heuristik (nur Orientierung, kein Zwang)
------------------------------------------------------------
Gewicht 4 (Kernkonzepte): typ. (2–4, bis 9/10 möglich)
Gewicht 3 (Vertiefungen): typ. (3–5, bis 9/10 möglich)
Gewicht 2 (Standard/Umfeld): typ. (1–4, bis 8/9 möglich)
→ Tatsächliche Intervalle werden anschließend mit A/B/C kalibriert.

E. Basiskategorien (Level-1 fähig)
----------------------------------
Pro Überkategorie wird eine „Basis“-Kategorie ergänzt (z. B.
„… – Basiswissen“), die bewusst **min = 1** setzt, damit sehr leichte
Fragen (Zuordnungen, Definitionen, einfache Lagefragen) möglich sind.

F. Vergleichende & themenübergreifende Kategorien
-------------------------------------------------
Neben domänenspezifischen Kategorien werden **Querschnitts-Kategorien**
eingefügt (Vergleiche, Geografie-Relationen, Zeitachsen),
um übergreifende Fragen zu ermöglichen (z. B. „Welcher Fluss durchquert
diese Hauptstädte?“). Hinweis: Pegelstände, Gletscher- und Küstendynamik,
Seeflächen etc. sind **zeitabhängig**; Erklärungen sollten möglichst
zeitunabhängige Kontexte nutzen oder klar datieren.

G. Intervall-Setzung – Regeln
-----------------------------
1) min:
   - 1–2, wenn verbreitete Basisfragen möglich (z. B. „Mündung des Nils“,
     „Welche Meerenge?“).
   - ≥4, wenn schon Einstiegsvokabular seltener ist (z. B. Ästuardynamik).
2) max:
   - 8–10, wenn das Thema substanzielle Tiefe/Methodik besitzt.
   - 7–8, wenn Tiefe begrenzt ist (reine Zuordnung/feste Fakten).
3) Breite:
   - Breiter Bereich (z. B. (2,10)), wenn triviale bis komplexe Fragen plausibel sind.
   - Enger Bereich (z. B. (7,10)), wenn primär Spezialwissen.
4) Konsistenz:
   - Gleichartige Subkategorien (z. B. „größte/längste …“) erhalten
     vergleichbare min/max-Logik.
   - „Basis…“-Kategorien immer min = 1 (außer Domäne schließt das aus).

H. Übertragung auf andere Domänen
---------------------------------
Analog einsetzbar (z. B. Relief, Klima, Städte).

I. Frage-Design (Templates, optional)
-------------------------------------
- Recall/Zuordnung (Levels 1–3): „Wie heißt …?“, „Welche Mündung …?“,
  „Ordne Fluss–Hauptstadt zu.“
- Verständnis/Anwendung (4–6): „Warum bildet sich hier ein Delta?“, „Welche
  Folge hat eine Flussbegradigung …?“
- Transfer/Analyse (7–8): „Vergleiche Deltatypen …“, „Diskutiere die Rolle
  von Wasserscheiden …“
- Experten (9–10): „Beurteile Hypothesen zu Telekonnektionen & Abflussregimen …“

J. Konsistenz-Checkliste
------------------------
[ ] Gibt es eine „Basis…“-Kategorie mit min = 1?
[ ] Haben seltene/spezialisierte Themen min ≥ 7?
[ ] Sind gleichartige Themen vergleichbar eingestuft?
[ ] Spiegelt max die reale inhaltliche Tiefe wider (bis 8/9/10)?
[ ] Sind zeitvariable Themen als solche markiert?
"""

# Schwierigkeits-Skala kurz (zur Laufzeit nutzbar):
# 1=Allgemeinwissen … 10=schwerstmöglich.

SUBTOPICS = [
    # 1 Allgemeines & Grundlagen
    ("Hydrologischer Kreislauf & Grundbegriffe (Quelle, Mündung, Einzugsgebiet, Abflussregime)", 4, (2,9)),
    ("Flussmorphologie: Mäander, Prall-/Gleithang, Flusslaufstadien", 4, (3,9)),
    ("Wasserscheiden & Kontinentale Hauptwasserscheiden", 4, (3,9)),
    ("Mündungsformen: Delta vs. Ästuar (Prozesse & Beispiele)", 3, (4,9)),
    ("Seen-Typen: glazial, tektonisch, vulkanisch, Karst – Entstehung & Beispiele", 3, (3,9)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Gewässer – Basiswissen (Zuordnungen/Definitionen: Fluss–Meer, See–Land, Meerenge–Lage)", 2, (1,7)),

    # 2 Flüsse (global & kontinental)
    ("Längste Flüsse & Rangfolgen (Amazonas, Nil, Jangtse, Mississippi, Jenissei)", 4, (2,9)),
    ("Große Stromsysteme & Nebenflüsse (Einzugsgebiete, Abfluss, Sedimentfracht)", 3, (4,9)),
    ("Flüsse durch Hauptstädte & Metropolräume (Lage-/Verkehrsbezüge)", 3, (2,8)),
    ("Trockentäler/Wadis & episodische Abflüsse (Aridgebiete)", 2, (4,8)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Flüsse – Basisfakten (Quelle–Mündung, Anrainerstaaten, Durchflossene Länder)", 2, (1,7)),

    # 3 Seen & Binnenmeere
    ("Größte Seen nach Fläche/Volumen (Kaspisches Meer, Baikalsee, Superiorsee)", 4, (2,9)),
    ("Endorheische Becken & Salzseen (Kaspisches Meer, Totes Meer, Aralsee)", 3, (3,9)),
    ("Gletscherseen & proglaziale Prozesse (Moränenstau, GLOFs – zeitabhängig)", 3, (5,10)),
    ("Karstseen & Dolinen (z. B. Plitvicer Seen)", 2, (3,8)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Seen – Basisfakten (Lage, Abflusslosigkeit, Inseln auf Seen)", 2, (1,7)),

    # 4 Meere, Ozeane & Küsten
    ("Rand- & Binnenmeere (Mittelmeer, Ostsee, Schwarzes Meer) – Austausch & Salzgehalt", 3, (4,9)),
    ("Meerengen & Chokepoints (Malakka, Hormus, Bosporus, Bab al-Mandab) – Geografiebezug", 3, (4,9)),
    ("Küstenformen: Fjord, Ria, Kliff, Haff, Düneninseln – Genese & Beispiele", 3, (3,9)),
    ("Korallenriffe & Schelfe – Entstehung, Bedingungen, Beispiele", 2, (4,8)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Meere – Basisfakten (Zuordnung Meer–Ozean–Meerenge, Anrainer, Becken)", 2, (1,7)),

    # 5 Mensch–Gewässer–Interaktion
    ("Stauseen & Wasserkraft (große Dämme, Speicherbewirtschaftung) – Chancen/Risiken", 3, (4,9)),
    ("Kanäle & Wasserwege (Panama, Suez, Nord-Ostsee-Kanal) – Geografische Wirkung", 3, (3,9)),
    ("Hochwasserschutz, Flussbegradigungen & Renaturierung – Raumplanung", 3, (4,9)),
    ("Eutrophierung & Verschmutzung (Seen/Flüsse) – Ursachen & Folgen", 2, (3,8)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Nutzung – Basis (Trinkwasser, Bewässerung, Schifffahrt, Fischerei) – Zuordnungen", 2, (1,7)),

    # 6 Vergleichende & Querschnitts-Themen
    ("Kontinentale Vergleiche: längste Flüsse, größte Seen, bedeutende Deltas", 3, (3,9)),
    ("Wasserscheiden Europas & Abfluss in Nord-/Ostsee, Atlantik, Mittelmeer, Schwarzes Meer", 3, (3,9)),
    ("Telekonnektionen & Abflussregime (ENSO/NAO) – Einfluss auf Hochwasser/Dürre", 2, (5,10)),
    ("UNESCO-Welterbe & Schutzgebiete mit Gewässerbezug (Nationalparks, Ramsar) – Beispiele", 2, (3,8)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Querschnitt – Basis (Fluss–Stadt–Meer-Zuordnungen, Kontinent-Listen)", 2, (1,7)),
]
