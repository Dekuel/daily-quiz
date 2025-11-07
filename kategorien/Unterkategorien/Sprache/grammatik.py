# -*- coding: utf-8 -*-
# Unterkategorien/Sprache/grammatik.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Grammatik (Deutsch)“.
Diese Liste wird von kategorien/sprache.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
========================================================================

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

D. Gewichte → Basis-Heuristik
-----------------------------
Gewicht 4 (Kernkonzepte)  → typ. (2–4, bis 9/10 möglich)
Gewicht 3 (Vertiefungen)  → typ. (3–5, bis 9/10 möglich)
Gewicht 2 (Standard/Umfeld) → typ. (1–4, bis 8/9 möglich)

E. „Basis…“-Kategorien (Level-1 fähig)
--------------------------------------
Je Überkategorie eine Basis-Kategorie mit min = 1 (Zuordnungen, Begriffe etc.).

F. Vergleichende/Querschnitt-Kategorien
---------------------------------------
Erlauben übergreifende Fragen (Register, Varianten D/A/CH, gesprochene Sprache).

G. Intervall-Setzung – Regeln (min/max)
---------------------------------------
Siehe Monotheismus-Beispiel; gleichartige Themen erhalten vergleichbare Logik.
"""

# Schwierigkeits-Skala kurz (zur Laufzeit nutzbar): 1=Allgemeinwissen … 10=schwerstmöglich.

SUBDISCIPLINES = [
    # 1 Grundlagen & Wortarten
    ("Wortarten – Zuordnung (Nomen, Verb, Adjektiv, Adverb, Pronomen, Artikel)",                         2, (1, 10)),
    ("Kasusfragen & Basisbegriffe (wer? wessen? wem? wen?)",                                             2, (1, 10)),
    ("Satzglieder – Erkennen (Subjekt, Prädikat, Objekt, Adverbial)",                                    4, (3, 10)),
    ("Flexion: Numerus, Genus, Kasus – Grundprinzip",                                                    3, (3, 10)),
    ("Basiswissen Grammatik: Grundbegriffe & typische Beispiele",                                        2, (1, 10)),  # ⚑ Basis

    # 2 Verben, Tempus, Modus, Diathese
    ("Tempusgebrauch im Deutschen (Präsens, Präteritum, Perfekt, Plusquamperfekt, Futur I/II)",          4, (3, 10)),
    ("Konjunktiv I/II – Formen & Gebrauch (z. B. Indirekte Rede, Irrealis)",                             4, (7, 10)),
    ("Aktiv–Passiv (Vorgangspassiv/Zustandspassiv) – Bildung & Unterschiede",                            4, (5, 10)),
    ("Verbvalenz & Rektion (Objektstruktur, Präpositionalobjekte)",                                      4, (8, 10)),
    ("Trennbare/Untrennbare Präfixverben (be-, ver-, zer-, an-, auf-, etc.)",                             3, (5, 10)),
    ("Modalverben & Ersatzformen (dürfen, können … + Umschreibungen)",                                   3, (5, 10)),
    ("Reflexive Verben & Reziprokpronomen (sich, einander)",                                             3, (5, 10)),
    ("Aspektnahe Bedeutungen im Deutschen (Aktionsarten, Resultativität)",                               2, (9, 10)),

    # 3 Nominalgruppe: Artikel, Pronomen, Adjektive
    ("Artikelgebrauch: bestimmt/unbestimmt/Nullartikel (Regeln & Ausnahmen)",                            4, (5, 10)),
    ("Pronomenklassen & -gebrauch (Personal-, Possessiv-, Demonstrativ-, Relativ-, Indefinitpronomen)",  4, (5, 10)),
    ("Adjektivdeklination (stark/schwach/gemischt) – Paradigmen & Tests",                                4, (5, 10)),
    ("Komparation & adverbiale Steigerung (so/als, wie, desto/umso)",                                    3, (5, 10)),
    ("Genitivgebrauch vs. Dativersatz (Präpositionen, feste Fügungen)",                                  3, (7, 10)),

    # 4 Satzbau & Topologisches Feldermodell
    ("Verbzweit im Hauptsatz – Prinzip & Ausnahmen (Fragen, Imperativ, Inversion)",                      4, (3, 10)),
    ("Nebensätze: Konjunktionen & Verbendstellung (weil, dass, obwohl …)",                               4, (5, 10)),
    ("Relativsätze – Relativpronomen, Kasuszuweisung & Bezüge",                                          4, (7, 10)),
    ("Infinitivkonstruktionen mit/ohne 'zu' (Ersatzinfinitiv, zu-Infinitiv)",                            3, (7, 10)),
    ("Satzklammer & Felder (Vorfeld, linke/rechte Klammer, Mittelfeld, Nachfeld)",                       4, (8, 10)),
    ("Stellungsfelder im Mittelfeld: Pronomenreihenfolge, Negation, Modalpartikeln",                     3, (8, 10)),
    ("Position der Negation (nicht, kein) & Skopus",                                                     3, (8, 10)),
    ("Informationsstruktur & Fokus (Thema/Rhema, Vorfeldbesetzung)",                                     2, (9, 10)),

    # 5 Zeichensetzung & Orthografie (grammatisch motiviert)
    ("Kommasetzung bei Nebensätzen (dass-, weil-, Relativsätze)",                                        4, (3, 10)),
    ("Kommasetzung bei Infinitiv- & Partizipgruppen",                                                    3, (5, 10)),
    ("Aufzählungen, Nachträge, Appositionen – Kommaregeln",                                              3, (3, 10)),
    ("Groß- und Kleinschreibung: Substantivierung, Anrede, Höflichkeitsform",                            3, (3, 10)),
    ("Getrennt- und Zusammenschreibung (Verb + Verb / Verb + Partikel)",                                 3, (5, 10)),
    ("ss/ß-Regeln (Vokalquantität) & typische Stolpersteine",                                            2, (3, 10)),

    # 6 Register, Variation & gesprochene Sprache
    ("Register & Stil (formell/neutral/umgangssprachlich) – grammatische Marker",                        2, (3, 10)),
    ("Regionale Varianten D/A/CH – grammatische Besonderheiten (z. B. Dativ-Ersatz)",                    2, (5, 10)),
    ("Gesprochene-Sprache-Phänomene (Verbzweitverletzungen, Ellipsen, Partikeln)",                       2, (5, 10)),
    ("Einfluss von Anglizismen auf Syntax/Morphologie (Lehnübersetzungen)",                              2, (7, 10)),

    # 7 Grammatische Semantik & Feinsinn
    ("Tempus vs. Zeitreferenz: Präsens mit Zukunftslesart, historisches Präsens",                        3, (8, 10)),
    ("Modus & Modalität: Aufforderung, Möglichkeit, Notwendigkeit – grammatische Kodierung",             3, (8, 10)),
    ("Korrelation & Kongruenz (Subjekt–Verb, Attribut–Kern)",                                            4, (5, 10)),
    ("Präpositionen & Kasusrektion – Bedeutung vs. Konvention",                                          4, (7, 10)),

    # 8 Fehlerquellen & Didaktik (lernrelevant)
    ("Typische Fehler A2–B2 (Kasus, Artikel, Satzklammer) – Diagnose & Korrektur",                       2, (3, 10)),
    ("Interferenz Deutsch–Englisch (Wortstellung, Artikel, Falsche Freunde)",                            2, (3, 10)),
    ("Minimalpaare & Kontraste (weil/denn, dass/das, wie/als) – Grammatikperspektive",                   2, (3, 10)),

    # 9 Historisches & Systematisches
    ("Grammatikmodelle (Generativ, Dependenz, Topologisches Modell) – Grundideen",                       2, (9, 10)),
    ("Morphologie: Wortbildung (Derivation, Komposition, Konversion) – Grammatikbezug",                  3, (7, 10)),
    ("Satztypen & Illokution (Aussage, Frage, Aufforderung) – grammatische Signale",                     3, (5, 10)),

    # ⚑ Basis-orientierte Querschnittskategorien (Level-1 möglich)
    ("Basis – Zuordnung: Satzarten, Wortarten, einfache Kommaregeln",                                    2, (1, 10)),
    ("Basis – Beispielanalyse: Subjekt/Prädikat/Objekt finden",                                          2, (1, 10)),
]
