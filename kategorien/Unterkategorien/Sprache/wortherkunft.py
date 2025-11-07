# -*- coding: utf-8 -*-
# Unterkategorien/Sprache/wortherkunft.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Wortherkunft & Etymologie (Deutsch)“.
Diese Liste wird von kategorien/sprache.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Strukturierte Unterthemen mit realistischen Schwierigkeitsintervallen (1–10),
über die unterschiedliche Fragetypen (Zuordnung, Verständnis, Transfer) möglich sind.

B. Skala (1–10)
---------------
1 = absolutes Grundwissen · 10 = schwerstmöglich

C. Intervall-Logik (Heuristik)
------------------------------
- Basis‑Zuordnungen (Lehnwörter, einfache Präfixe/Suffixe, geläufige Beispiele) erlauben min = 1–2.
- Vertiefungen (semantischer Wandel, Volksetymologie, historische Lautgesetze) steigen ab 4–6 ein.
- Spezialfälle (Namensetymologie, sehr alte Schichten) können bis 9–10 reichen.
"""

# Schwierigkeits-Skala kurz: 1=Allgemeinwissen … 10=schwerstmöglich

SUBDISCIPLINES = [
    # 1 Grundlagen & Begriffe
    ("Was ist Etymologie? – Grundbegriffe (Erbwort, Lehnwort, Fremdwort)",                                 3, (2, 8)),
    ("Lautliche, morphologische, semantische Entwicklung – Grundüberblick",                               3, (3, 8)),
    ("Basis – Zuordnung: Alltagswörter und ihre Herkunft (lat., frz., engl., slaw.)",                     10, (1, 10)),

    # 2 Lehn- & Fremdwörter (Quellen & Zeitschichten)
    ("Latein & Romanische Sprachen (Kloster, Kirche, Verwaltung, Wissenschaft)",                          4, (3, 9)),
    ("Französisch (Adel, Mode, Küche, Militär) – Einwanderungswellen",                                    3, (3, 9)),
    ("Englisch (Technik, IT, Sport, Popkultur) – Anglizismen & Lehnübersetzungen",                        3, (2, 9)),
    ("Slawische Einflüsse (Toponyme, Landwirtschaft, Alltagslexik)",                                      3, (3, 9)),
    ("Griechisch (Wissenschaftsterminologie, Medizin) – Bildungsmorpheme",                                3, (4, 9)),
    ("Hebräisch/Jiddisch (Kultur, Religion, umgangssprachliche Ausdrücke)",                               2, (3, 8)),
    ("Türkisch & neuere Migrationseinflüsse",                                                             2, (3, 8)),
    ("Substrat- & Superstrat-Einflüsse (Kontaktzonen) – Überblick",                                       2, (5, 9)),

    # 3 Wortbildung & Morpheme
    ("Produktive Präfixe: be-, ver-, zer-, ent-, er-, miss-, ur- … – Bedeutungsspektren",                 4, (3, 9)),
    ("Produktive Suffixe: -heit/-keit, -ung, -chen/-lein, -isch/-lich …",                                 4, (3, 9)),
    ("Komposita im Deutschen (Determinativ-, Kopulativ-, Possessivkomposita)",                            3, (3, 9)),
    ("Konversion & Kurzwortbildung (Akronyme, Clippings, Blends)",                                        3, (3, 8)),
    ("Präfix- & Suffix-Polysemie (Bedeutungsfelder, Grenzfälle)",                                        2, (5, 9)),
    ("Falsche Segmentierung & Pseudo‑Morpheme (Volksetymologie der Form)",                                2, (5, 9)),

    # 4 Semantischer Wandel
    ("Bedeutungswandel: Erweiterung/Verengung, Metapher/Metonymie, Pejoration/Amelioration",             4, (4, 10)),
    ("Sinnverschiebungen durch Kulturkontakt & Medien (Beispielsammlungen)",                              3, (4, 9)),
    ("Falsche Freunde (DE–EN/FR/ES) – etymologisch begründet",                                            3, (3, 9)),
    ("Lehnübersetzungen & Scheinentlehnungen (Handy, Beamer) – Analyse",                                  3, (3, 9)),

    # 5 Lautgesetze & historische Schichten
    ("Zweite Lautverschiebung (p→pf/f, t→ts/s, k→kch/χ) – Erbwortdiagnose",                              4, (6, 10)),
    ("Grimm'sches & Vernersches Gesetz – Grundidee & Beispiele",                                          3, (6, 10)),
    ("Ablaut, Umlaut, i‑Umlaut – historische Hintergründe",                                              3, (5, 9)),
    ("Lehnwörter vs. Erbwörter – lautliche Indizien & Schreibgeschichte",                                 3, (5, 9)),

    # 6 Namenkunde (Onomastik)
    ("Personennamen: Rufname, Familienname – Herkunftstypen (Beruf, Herkunft, Patronym)",                 2, (4, 9)),
    ("Toponyme: Siedlungsnamen, Gewässernamen – typische Formanten",                                      2, (4, 9)),
    ("Marken- & Produktnamen – Motivationen, Scheinetymologien",                                          2, (3, 8)),

    # 7 Spezialthemen & Randbereiche
    ("Volksetymologie: populäre, aber falsche Erklärungen – Aufklärung",                                  2, (4, 10)),
    ("Etymologie im Wörterbuch: Duden/Grimm – Lesen & bewerten",                                         2, (3, 8)),
    ("Sprachpolitik & Purismus (Eindeutschung, Fremdwortdebatten)",                                      2, (5, 9)),

    # 8 Aufgaben-/Querschnittsformate
    ("Basis – Zuordnung: Wort → Herkunftssprache (einfach)",                                             2, (1, 7)),
    ("Zuordnung: Präfix/Suffix → Bedeutung (mittelschwer)",                                              2, (3, 9)),
    ("Analyse: Bedeutungswandel eines Begriffs an Beispielen",                                           3, (4, 9)),
    ("Diagnose: Erbwort vs. Lehnwort an Lautmerkmalen",                                                  3, (7, 10)),
]
