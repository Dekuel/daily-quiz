# -*- coding: utf-8 -*-
# Unterkategorien/Sprache/redewendungen.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Redewendungen & Sprichwörter (Deutsch)“.
Diese Liste wird von kategorien/sprache.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Ein konsistentes, domänenübergreifendes Schema für Quizfragen aufzubauen,
das (1) thematisch strukturierte Kategorien liefert und (2) zu jeder
Kategorie realistische Schwierigkeits-Intervalle (1–10) definiert.

B. Skala (1–10)
---------------
1 = absolutes Grundwissen · 10 = schwerstmöglich

C. Intervall-Logik
------------------
- „Basis“-Kategorien setzen min = 1, um sehr leichte Zuordnungen zu erlauben.
- Herkunft/Etymologie & feine Bedeutungsnuancen steigen früh auf 4–7 ein und
  können bis 10 reichen.
- Register-/Regionalfragen liegen meist im Bereich 3–9.
"""

# Schwierigkeits-Skala kurz: 1=Allgemeinwissen … 10=schwerstmöglich

SUBDISCIPLINES = [
    # 1 Grundlagen & Bedeutung
    ("Bedeutung geläufiger Redewendungen – Basis (z. B. 'ins Schwarze treffen')",                        2, (1, 7)),
    ("Redewendung vs. Sprichwort – Abgrenzung & Beispiele",                                              3, (2, 8)),
    ("Wörtlich vs. übertragen – Metaphorik erkennen",                                                    3, (2, 8)),
    ("Semantische Felder: Körperteile (Hand, Kopf, Herz) in Idiomen",                                    3, (3, 9)),
    ("Semantische Felder: Tiere & Farben in Redewendungen",                                              3, (3, 9)),
    ("Phraseologismen vs. freie Kollokationen (Grundlagen)",                                             3, (3, 9)),
    ("Mehrwort-Einheiten: Fixiertheit, Substituierbarkeit, Variation",                                   2, (4, 9)),

    # 2 Herkunft & Etymologie
    ("Herkunft: Seefahrt (z. B. 'alles in einem Boot sein')",                                            4, (4, 10)),
    ("Herkunft: Handwerk & Zünfte (z. B. 'auf dem Holzweg sein')",                                       4, (4, 10)),
    ("Herkunft: Militär (z. B. 'über die Stränge schlagen')",                                            3, (4, 10)),
    ("Herkunft: Bibel & Antike (z. B. 'Auge um Auge')",                                                  3, (4, 10)),
    ("Herkunft: Recht & Handel (z. B. 'unter der Hand', 'auf eigene Faust')",                            3, (4, 10)),
    ("Herkunft: Literatur & Theater (z. B. 'den Vorhang fallen lassen')",                                3, (4, 10)),
    ("Herkunft: Jäger- & Studentensprache",                                                              2, (4, 9)),
    ("Herkunft: Technik/Medien (z. B. 'auf Sendung sein', 'Filmriss')",                                  2, (3, 9)),
    ("Volksetymologie & Irrtümer (falsche Herkunftsdeutungen)",                                          2, (5, 10)),
    ("Herkunft – Basis: typische Quellen korrekt zuordnen",                                              2, (1, 8)),

    # 3 Nuancen & Verwechslungsgefahr
    ("Feinunterschiede: 'den Nagel auf den Kopf treffen' vs. 'ins Schwarze treffen'",                    3, (4, 10)),
    ("Feinunterschiede: 'mit zweierlei Maß messen' vs. 'mit gleichen Ellen messen'",                     3, (4, 10)),
    ("Feinunterschiede: 'den Teufel an die Wand malen' vs. 'schwarzmalen'",                              3, (4, 10)),
    ("Feinunterschiede: 'jemandem über den Mund fahren' vs. 'ins Wort fallen'",                          3, (4, 10)),
    ("Feinunterschiede: 'aufs Spiel setzen' vs. 'auf dem Spiel stehen'",                                 3, (4, 10)),
    ("Bedeutungsradius & Registergrenzen (derb, salopp, euphemistisch)",                                 2, (5, 9)),

    # 4 Register & Gebrauch
    ("Register – formell vs. umgangssprachlich: geeignete Kontexte wählen",                              3, (3, 9)),
    ("Büro- & Medienfloskeln (z. B. 'Prozesse aufsetzen', 'Hebel umlegen')",                             2, (3, 8)),
    ("Höflichkeitsstrategien über Redewendungen (indirekte Sprache)",                                    2, (4, 9)),
    ("Anglizismen & calques: 'das macht Sinn', 'eine Challenge' – Bewertung",                             2, (4, 9)),
    ("Interkulturelle Stolpersteine: wörtliche Übersetzbarkeit (DE ↔ EN/FR/ES)",                         3, (4, 10)),
    ("Jugend- & Netzkultur: Meme-Redensarten, Ironie-Marker",                                            2, (3, 9)),

    # 5 Regionale Varianten (D/A/CH und mehr)
    ("Austriazismen (z. B. 'heikel' anders gebraucht, 'Gfrast') – idiomatisch",                          2, (3, 9)),
    ("Helvetismen (z. B. 'plötzlich auf Bern-Deutsch') – übertragene Wendungen",                         2, (3, 9)),
    ("Regionale Bilder: Rhein/Ruhr, Bayern, Norddeutschland – typische Idiome",                          2, (3, 9)),
    ("D/A/CH – Bedeutungsdrift gleicher Wendungen",                                                      2, (4, 9)),
    ("Regionale Varianten – Basis: zuordnen & vermeiden von Missverständnissen",                         2, (1, 8)),

    # 6 Grammatik & Form fester Wendungen
    ("Kasus & Präposition in festen Fügungen (z. B. 'auf dem Holzweg sein' – Dativ)",                    4, (3, 9)),
    ("Feste Artikel & Flexion (z. B. 'die Stirn bieten', nicht '*eine Stirn')",                          3, (3, 9)),
    ("Verbale Muster (sich etwas hinter die Ohren schreiben; jmdm. läuft die Zeit davon)",               3, (4, 9)),
    ("Trennbarkeit & Partikeln in Redensarten (z. B. 'aufziehen', 'untergehen')",                        2, (4, 9)),
    ("Plural & Numerus in Sprichwörtern (z. B. 'Viele Köche verderben den Brei')",                       2, (3, 8)),

    # 7 Bedeutungswandel & Modernisierung
    ("Politisch sensible Redewendungen – Ersatz & Kontextsensibilität",                                  3, (5, 10)),
    ("Wandel durch Medien/Technik: neue Bilder (Cloud, Algorithmus, Streaming)",                         2, (4, 9)),
    ("Lexikalisierung & Delexikalisierung (Wendung wird zu fixer Bedeutung / verblasst)",                2, (5, 9)),

    # 8 Aufgaben-/Fragetypen (Querschnitt)
    ("Zuordnen: Bedeutung ↔ Wendung – Basis",                                                             2, (1, 7)),
    ("Ursprung raten: Quelle ↔ Wendung (Seefahrt, Bibel, Militär …)",                                     2, (1, 8)),
    ("Lücken & Transformationen: korrekte Form kompletter Redewendungen",                                3, (3, 9)),
    ("Kontextwahl: welche Wendung passt? (Semantik/Pragmatik)",                                          3, (3, 9)),
    ("Falsche Freunde & Scheinäquivalente (DE–EN) bei Idiomen",                                          2, (3, 9)),
]
