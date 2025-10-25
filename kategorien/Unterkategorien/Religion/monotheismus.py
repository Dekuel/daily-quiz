# -*- coding: utf-8 -*-
# Unterkategorien/Religion/monotheismus.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Monotheistische Religionen“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Ein konsistentes, domänenübergreifendes Schema für Quizfragen aufzubauen,
das (1) thematisch strukturierte Kategorien liefert und (2) zu jeder
Kategorie realistische Schwierigkeits-Intervalle (1–10) definiert.
Das System ist so formuliert, dass es auf andere Fächer (z. B. Physik)
übertragen werden kann.

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
„… – Basisfakten“), die bewusst **min = 1** setzt, damit sehr leichte
Fragen (Zuordnungen, Symbole, Begriffsnamen, Zählfragen) möglich sind.

F. Vergleichende & themenübergreifende Kategorien
-------------------------------------------------
Neben domänenspezifischen Kategorien werden **Querschnitts-Kategorien**
eingefügt (Vergleiche, Demografie, Geografie, Zeitachse, Praktiken),
um übergreifende Fragen zu ermöglichen (z. B. „Welche Religion hat die
zweitmeisten Anhänger weltweit?“). Hinweis: Demografie ist **zeitabhängig**;
Fragen sollten möglichst „Stand: Jahr/Quelle“ enthalten.

G. Intervall-Setzung – Regeln
-----------------------------
1) min:
   - 1–2, wenn sehr verbreitete Basisfragen möglich (z. B. heilige Bücher,
     Anzahl Evangelien, Namen großer Städte/Orte/Symbole).
   - ≥4, wenn selbst Einstiegsvokabular selten ist (z. B. Manichäismus).
2) max:
   - 8–10, wenn das Thema substantielle Tiefe/Debatten/Methodik besitzt.
   - 7–8, wenn die Tiefe begrenzt ist (reine Zuordnung/feste Fakten).
3) Breite:
   - Breiter Bereich (z. B. (2,10)), wenn sowohl triviale als auch
     hochkomplexe Fragen plausibel sind.
   - Enger Bereich (z. B. (7,10)), wenn Thema primär Spezialwissen ist.
4) Konsistenz:
   - Gleichartige Subkategorien (z. B. „heilige Schriften“ in mehreren
     Religionen) erhalten vergleichbare min/max-Logik.
   - „Basis…“-Kategorien immer min = 1 (außer Domäne schließt das aus).

H. Übertragung auf andere Fächer (z. B. Physik)
-----------------------------------------------
1) Strukturierung:
   - Grundlagen (Begriffe, Größen, Einheiten, Alltagsphänomene) → min = 1–2
   - Kernfelder (Mechanik, E-Magnetismus, Thermodynamik, Optik) → min = 2–4
   - Vertiefungen (QM, Relativität, Statistische Physik) → min = 3–6
   - Anwendungen/Methoden (Messung, Fehlerrechnung, Experimente) → min = 1–4
   - Historische/vergleichende Perspektiven → min je nach Bekanntheit
2) Beispiele Physik:
   - „Symbole/Einheiten-Basis (SI)“ → (1,7)
   - „Newtonsche Mechanik – Grundgesetze“ → (2,9)
   - „Quantenmechanik – Interpretationen“ → (6,10)
   - „Relativität – Zeitdilatation (Grundidee)“ → (2,9)
3) Querschnitte:
   - „Vergleich: Kräftearten“, „Skalen (Größenordnungen)“, „Historische
     Experimente“, „Alltagsphysik“.

I. Frage-Design (Templates, optional)
-------------------------------------
- Recall/Zuordnung (Levels 1–3): „Wie heißt …?“, „Wieviele …?“,
  „Ordne Symbol X zu.“
- Verständnis/Anwendung (4–6): „Warum …?“, „Welcher Unterschied …?“,
  „Welche Folge …?“
- Transfer/Analyse (7–8): „Vergleiche …“, „Begründe …“, „Diskutiere …“
- Forschung/Experten (9–10): „Beurteile Theorien …“, „Welche
  methodischen Grenzen …?“, „Stelle eine These auf zu …“

J. Konsistenz-Checkliste (für neue Domänen)
-------------------------------------------
[ ] Gibt es je Überkategorie eine „Basis…“-Kategorie mit min = 1?
[ ] Haben seltene/spezialisierte Themen min ≥ 7?
[ ] Sind gleichartige Themen vergleichbar eingestuft?
[ ] Spiegelt max die reale inhaltliche Tiefe wider (bis 8/9/10)?
[ ] Sind zeitvariable Themen (Demografie) als solche markiert?

"""

# Schwierigkeits-Skala kurz (zur Laufzeit nutzbar):
# 1=Allgemeinwissen … 10=schwerstmöglich.

SUBDISCIPLINES = [
    # 1 Allgemeines & Grundlagen
    ("Monotheismus: Begriff, Ursprung, Abgrenzung", 4, (2,10)),
    ("Abrahamitische Religionen: gemeinsame Wurzeln", 4, (2,9)),
    ("Offenbarung, Prophetie & Heilige Schriften", 4, (2,10)),
    ("Ethik & Gottesbild im Monotheismus", 3, (3,9)),
    ("Schöpfung, Erlösung, Eschatologie", 3, (3,10)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Basiswissen Monotheismus: Zuordnungen & Begriffe (z. B. Name der heiligen Schriften, Gebetsstätten)", 2, (1,7)),
    ("Globale Verbreitung & Anhängerzahlen (Basis)", 2, (1,9)),

    # 2 Judentum
    ("Judentum: Ursprung & Geschichte Israels", 4, (3,10)),
    ("Tanach (Tora, Neviim, Ketuvim)", 4, (4,10)),
    ("Tempel, Priesterschaft & Opferkult", 3, (4,10)),
    ("Rabbinisches Judentum & Talmud", 3, (5,10)),
    ("Diaspora & jüdische Identität", 3, (3,9)),
    ("Jüdische Feste & Bräuche (Pessach, Jom Kippur, Schabbat)", 3, (2,9)),
    ("Zionismus & Staat Israel", 2, (3,9)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Judentum – Basisfakten (z. B. Heilige Schrift, Sabbat, Menora)", 2, (1,7)),

    # 3 Christentum
    ("Christentum: Entstehung & frühe Kirche", 4, (3,10)),
    ("Neues Testament & Evangelien", 4, (2,9)),
    ("Jesus von Nazareth & Apostelgeschichte", 4, (2,9)),
    ("Konzile & Dogmenbildung (Nicäa, Chalcedon)", 3, (7,10)),
    ("Katholizismus, Orthodoxie & Protestantismus", 4, (2,9)),
    ("Reformation & Gegenreformation", 3, (3,9)),
    ("Christliche Liturgie, Sakramente & Heilige", 3, (3,10)),
    ("Mission, Kolonialismus & Weltkirche", 2, (3,9)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Christentum – Basisfakten (z. B. Bibel, Kreuz, Weihnachten/Ostern)", 2, (1,7)),

    # 4 Islam
    ("Islam: Ursprung & Prophet Mohammed", 4, (2,9)),
    ("Koran & Hadith", 4, (1,10)),
    ("Fünf Säulen des Islam", 4, (1,8)),
    ("Scharia & islamische Rechtsschulen", 3, (5,10)),
    ("Sunniten & Schiiten", 4, (3,9)),
    ("Kalifate & islamische Geschichte", 3, (3,9)),
    ("Sufismus (islamische Mystik)", 3, (3,10)),
    ("Islam in der Moderne & interreligiöser Dialog", 3, (3,9)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Islam – Basisfakten (z. B. Koran, Moschee, Ramadan)", 2, (1,7)),

    # 5 Bahaitum & andere monotheistische Strömungen
    ("Bahaitum: Ursprung & Lehre", 3, (4,10)),
    ("Zoroastrismus (Ahura Mazda & Dualismus)", 3, (5,10)),
    ("Manichäismus & spätantike monotheistische Bewegungen", 2, (7,10)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Weitere Strömungen – Basisfakten (Bahá’í, Zoroastrismus, Manichäismus: Gründer, Kernidee, heilige Schrift)", 2, (1,8)),

    # 6 Vergleichende Themen
    ("Gemeinsamkeiten & Unterschiede der abrahamitischen Religionen", 4, (3,10)),
    ("Monotheismus & Gewalt / Toleranz", 3, (4,10)),
    ("Frauenbilder im Monotheismus", 2, (3,9)),
    ("Monotheismus und Moderne (Säkularisierung, Pluralismus)", 3, (4,10)),
    ("Heilige Orte: Jerusalem, Mekka, Rom", 3, (2,9)),
    # ⚑ einfache Kategorien (Level-1 möglich)
    ("Vergleich – Basis: Heilige Schriften, Gebetsstätten, zentrale Feste (Zuordnungen)", 2, (1,8)),
    ("Vergleich – Demografie & Verbreitung (kontinental/länderweise, Basis)", 2, (1,9)),
]
