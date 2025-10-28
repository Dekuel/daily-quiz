# -*- coding: utf-8 -*-
# Unterkategorien/Geographie/staedte_laender_flaggen.py
"""
Subtopics für das Oberthema „Städte, Länder & Flaggen“ (ohne Hauptstädte).
Ziel: Von sehr einfachen Zuordnungen (min=1) bis zu analytischen/vergleichenden
Fragen (bis 9/10). Keine aktuellen Politik-/Tagesbezüge nötig.

Gewichte (Heuristik):
- 4 = Kernkonzepte/tragende Themen
- 3 = Vertiefungen/typische Anwendungen
- 2 = Basis/Umfeld (einsteigerfreundlich)
"""

SUBTOPICS = [
    # 1 BASIS & ORIENTIERUNG
    ("Länder–Kontinent–Region: einfache Zuordnungen (ohne Hauptstädte)", 2, (1,7)),
    ("Küsten- vs. Binnenstaaten, Insel- vs. Festlandstaaten – Erkennen & Beispiele", 3, (2,8)),
    ("Sprachfamilien & Schriften (lateinisch, kyrillisch, arabisch, Devanagari …) – Grundzuordnung", 2, (2,8)),
    ("Zeitzonen & Datumsgrenze – einfache Lage- und Zuordnungsfragen", 2, (2,7)),

    # 2 LÄNDER & GRENZEN (KEINE HAUPTSTÄDTE)
    ("Nachbarländer & Grenzverläufe (Natürliche Grenzen, Flüsse, Gebirge)", 4, (3,9)),
    ("Binnenex-/Enklaven & Sonderfälle (Baarle, Llivia, Kaliningrad, Lesotho)", 3, (5,10)),
    ("Geteilte Inseln & Inselgruppen (Borneo, Hispaniola, Neuguinea)", 3, (3,9)),
    ("Pene-En-/Exklaven & Korridore (z. B. Nahwa, Bir Tawil, Suwałki-Korridor – konzeptuell)", 2, (6,10)),
    ("Längste/markante Landesgrenzen (USA–Kanada, Russland–Kasachstan) – Lage & Charakter", 2, (3,8)),
    ("Historische Umbenennungen von Ländern & Regionen (ohne aktuelle Politik)", 2, (4,8)),

    # 3 STÄDTE (NICHT HAUPTSTÄDTE)
    ("Wichtige Hafenstädte & Seehandelsknoten (z. B. Rotterdam, Antwerpen, Santos, Busan)", 4, (3,9)),
    ("Großstädte an Flüssen/Seen/Meeresbuchten (z. B. New Orleans, Hamburg, Chongqing)", 3, (3,8)),
    ("Industriestädte & Cluster (Ruhrgebiet, Donbas, Detroit, Shenzhen – Funktion & Lage)", 3, (4,9)),
    ("Touristische Metropolen & Kulturerbe (z. B. Venedig, Cusco, Marrakesch)", 2, (2,8)),
    ("Agglomerationen & polyzentrische Regionen (Randstad, Rhein-Ruhr, Pearl River Delta)", 3, (4,9)),
    ("Stadtumbenennungen & Kontinuitäten (z. B. Mumbai/Bombay, Ho-Chi-Minh-Stadt/Saigon)", 2, (4,9)),
    ("Städtepaare über Grenzen (Zwillingsstädte, Grenzmetropolen)", 2, (4,8)),

    # 4 FLAGGENKUNDE (VEXILLOLOGIE)
    ("Flaggen – Basiszuordnungen (Farbe–Symbol–Land), ohne Hauptstädte", 2, (1,7)),
    ("Musterfamilien & Farbcodes: Panarabisch, Panafrikanisch, Nordisches Kreuz, Trikoloren", 4, (3,9)),
    ("Symbole & Bedeutungen (Sterne, Sichel, Sonne, Wappen) – typische Beispiele", 3, (3,8)),
    ("Ähnliche Flaggen unterscheiden (Rumänien/Chad; Indonesien/Monaco; Irland/Côte d’Ivoire)", 3, (3,9)),
    ("Flaggen mit besonderen Proportionen/Asymmetrien (Nepal, Schweiz, Katar) – Besonderheiten", 2, (3,8)),
    ("Farbsymbolik & Regionenbezug (Meer, Wüste, Wald, Berge) – vorsichtig kontextualisiert", 2, (3,8)),

    # 5 INSELN, HALBINSELN & REGIONEN (OHNE HAUPTSTÄDTE)
    ("Große Inseln & Inselgruppen (Madagaskar, Borneo, Sumatra, Honshu, Sulawesi) – Zuordnung", 3, (2,8)),
    ("Halbinseln & Isthmi (Skandinavische, Iberische, Arabische Halbinsel; Isthmus von Panama/Suez)", 3, (3,8)),
    ("Physisch-geografische Großräume vs. politische Einheiten (Skandinavien ≠ Norden Europas)", 2, (4,8)),

    # 6 VERKEHR & HANDEL (GEOGRAFISCHER FOKUS)
    ("Seewege & Chokepoints (Suez, Malakka, Hormus, Bosporus) – Lage & Funktion", 4, (4,9)),
    ("Kontinentale Landbrücken & Korridore (Transsib, Eurasische Korridore) – grobe Verortung", 3, (4,9)),
    ("Große Luft-/See-Hubs (Cargo/Passengers) – Zuordnung & Standortfaktoren", 2, (4,8)),

    # 7 VERGLEICH & QUERSCHNITT
    ("Vergleich: Küstenstaat vs. Binnenstaat – typische Wirtschafts-/Infrastrukturmuster", 3, (3,8)),
    ("Vergleich: Inselstaaten nach Region – Risiken/Chancen (Tourismus, Handel)", 2, (3,8)),
    ("Querschnitt – Basis (Stadt ↔ Gewässer/Relief; Land ↔ Nachbarn; Flagge ↔ Musterfamilie)", 2, (1,7)),
]
