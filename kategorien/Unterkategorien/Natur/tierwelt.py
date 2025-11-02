# -*- coding: utf-8 -*-
# Unterkategorien/Natur/tierwelt.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Tierwelt“.
Diese Liste wird von kategorien/natur.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
"""

# Schwierigkeits-Skala kurz:
# 1=Allgemeinwissen … 10=schwerstmöglich.

SUBDISCIPLINES = [
    # 1 | Grundlagen, Systematik, Erkennung
    ("Tiere – Basisfakten (Wirbeltiere vs. Wirbellose, einfache Merkmale)", 2, (1,10)),
    ("Grundlagen der Zoologie: Baupläne & Symmetrie (radiär/bilateral)", 3, (5,10)),
    ("Systematik: Stammbäume, Klassen & Ordnungen – Grundbegriffe", 4, (5,10)),
    ("Fortpflanzungsstrategien (ovipar, vivipar, Brutpflege vs. keine)", 3, (5,10)),
    ("Sinnesleistungen im Überblick (Sehen, Hören, Geruch, Seitenlinie)", 3, (5,10)),

    # 2 | Wirbeltiere – Klassenüberblick
    ("Säugetiere: Kennzeichen (Haare, Milchdrüsen, konstante Körpertemp.)", 4, (3,10)),
    ("Vögel: Federn, Flug & Luftsäcke – Grundprinzipien", 4, (3,10)),
    ("Reptilien: Schuppenhaut, wechselwarm, Fortpflanzung", 3, (3,10)),
    ("Amphibien: Metamorphose, Hautatmung, Feuchtlebensräume", 3, (3,10)),
    ("Fische: Knorpel- vs. Knochenfische, Kiemen, Schwimmblase", 3, (3,10)),
    # ⚑ Basis
    ("Wirbeltiere – Basis (Zuordnungen: Klasse ↔ Merkmal/Beispiel)", 2, (1,9)),

    # 3 | Wirbellose – Vielfalt
    ("Insekten: Körperbau (Kopf/Thorax/Abdomen), Mundwerkzeuge, Metamorphose", 4, (5,10)),
    ("Spinnentiere (Arachnida): Cheliceren, Spinnseide, Giftapparate – Basics", 3, (5,10)),
    ("Weichtiere (Mollusca): Schnecken, Muscheln, Kopffüßer – Unterschiede", 3, (5,10)),
    ("Krebse (Crustacea): Bau, Häutung, Lebensräume (Süß-/Meerwasser)", 3, (5,10)),
    ("Stachelhäuter (Echinodermata): Wassergefäßsystem, radiale Symmetrie", 2, (7,10)),
    # ⚑ Basis
    ("Wirbellose – Basis (Alltagsbeispiele erkennen/zuordnen)", 2, (1,9)),

    # 4 | Verhalten/Ethologie
    ("Instinkt vs. Lernen: Prägung, Konditionierung, Spielverhalten", 3, (5,10)),
    ("Sozialverhalten: Dominanzhierarchien, Koalitionen, Kooperation", 3, (7,10)),
    ("Kommunikation: akustisch, chemisch, visuell; Signal-Funktion", 3, (7,10)),
    ("Revierverhalten & Territorialität; Kosten-Nutzen", 3, (7,10)),
    ("Balz & Paarungssysteme (Monogamie, Polygynie, Polyandrie)", 3, (7,10)),
    ("Elterninvestment & Brutpflege-Strategien", 3, (7,10)),
    # ⚑ Basis
    ("Verhalten – Basis (einfache Beispiele zuordnen: Balz/Ruf/Imponieren)", 2, (1,9)),

    # 5 | Ökologie & Lebensräume (tierzentriert)
    ("Nahrungsnetze & Trophieebenen (Produzent–Konsument–Destruent – tierfokus)", 3, (5,10)),
    ("Anpassungen an Kälte/Hitze: Winterschlaf, Winterruhe, Wärmeregulierung", 3, (5,10)),
    ("Wüsten-/Polar-/Höhlenfauna – spezielle Anpassungen", 3, (7,10)),
    ("Aquatische Anpassungen: Strömung, Seitenlinie, Atmung", 3, (5,10)),
    ("Inselökologie: Endemismus, Inselgigantismus/Zwergwuchs (Tierbeispiele)", 3, (8,10)),
    # ⚑ Basis
    ("Lebensräume – Basis (einfache Zuordnung Tier ↔ Habitat)", 2, (1,9)),

    # 6 | Evolution & Diversität
    ("Natürliche Selektion, sexuelle Selektion – tierische Beispiele", 4, (5,10)),
    ("Mimikry & Tarnung: Bates, Müller, Krypsis, Aposematismus", 3, (7,10)),
    ("Adaptive Radiation (z. B. Darwinfinken, Buntbarsche)", 3, (8,10)),
    ("Konvergente Evolution (Flossen/Fledermausflügel/Beutelwolf)", 3, (8,10)),
    ("Domestikation (Hund, Rind, Huhn) – Merkmale & Folgen", 2, (3,10)),
    # ⚑ Basis
    ("Evolution – Basis (einfache Begriffe/Beispiele zuordnen)", 2, (1,9)),

    # 7 | Physiologie & Bau/Funktion
    ("Atmungstypen: Kiemen, Lungen, Tracheen – Vergleich", 4, (7,10)),
    ("Kreislaufsysteme: offen vs. geschlossen; Herzbau", 3, (8,10)),
    ("Thermoregulation: ektotherm vs. endotherm; Gegenstromprinzip", 3, (8,10)),
    ("Sinnesphysiologie: Echolokation, Magnetorezeption, UV-Sicht", 3, (8,10)),
    ("Gift & Verteidigung: Toxine, Stacheln, Panzer – Funktionsweisen", 3, (7,10)),

    # 8 | Gruppen im Fokus – Säugetiere/Vögel
    ("Primaten: Merkmale, Sozialstrukturen, Beispiele (Altwelt/Neuwelt)", 3, (7,10)),
    ("Carnivora (Raubtiere): Schädel-/Zahnanpassungen, Jagdstrategien", 3, (7,10)),
    ("Cetacea (Wale/Delfine): Anpassungen ans Wasser, Kommunikation", 3, (7,10)),
    ("Ungulata (Paar-/Unpaarhufer): Hufe, Wiederkäuer, Verdauung", 3, (7,10)),
    ("Fledertiere (Chiroptera): Flug, Echo, Energetik", 3, (8,10)),
    ("Greifvögel & Eulen: Sinnesleistung, Jagd, Federspezialisationen", 3, (7,10)),
    ("Singvögel (Passeriformes): Gesang, Territorialität, Vielfalt", 2, (5,10)),
    ("Zugvögel: Navigation (Sterne, Magnetfeld), Zugrouten", 3, (7,10)),
    # ⚑ Basis
    ("Säuger/Vögel – Basis (typische Vertreter ↔ Merkmale)", 2, (1,9)),

    # 9 | Gruppen im Fokus – Reptilien/Amphibien/Fische
    ("Schlangen & Echsen: Häutung, Giftzähne, Autotomie", 3, (7,10)),
    ("Schildkröten & Krokodile: Panzer/Brutpflege/Temperaturabh. Geschlechtsbestimmung", 3, (8,10)),
    ("Amphibien: Giftstoffe (Tetrodotoxin etc.), Hautatmung, Laichgewässer", 3, (7,10)),
    ("Knorpelfische (Haie/Rochen): Elektrorezeption, Placoidschuppen", 3, (8,10)),
    ("Knochenfische: Schwimmblase, Schuppenformen, Laichstrategien", 3, (7,10)),
    # ⚑ Basis
    ("Reptilien/Amphibien/Fische – Basis (Erkennung/Zuordnung)", 2, (1,9)),

    # 10 | Insekten & soziale Systeme
    ("Sozialinsekten: Eusozialität (Bienen, Ameisen, Termiten), Kastenwesen", 4, (8,10)),
    ("Bestäubung & Bestäuber-Netzwerke (Tierperspektive)", 3, (5,10)),
    ("Schwärmen, Tänze, Pheromone – Kommunikation bei Insekten", 3, (7,10)),
    ("Metamorphose: holometabol vs. hemimetabol – Vorteile/Nachteile", 3, (7,10)),
    # ⚑ Basis
    ("Insekten – Basis (Larve, Puppe, Adult – einfache Gegenüberstellung)", 2, (1,9)),

    # 11 | Mensch–Tier & Schutz
    ("Wildtiermanagement & Konflikte (z. B. Großraubtiere, Stadtfauna)", 2, (5,10)),
    ("Naturschutz: Rote Listen, CITES, Schutzstrategien (tierzentriert)", 3, (5,10)),
    ("Invasive Tierarten: Beispiele, Wirkungen, Management", 3, (7,10)),
    ("Tierhaltung & Wohlergehen (Grundprinzipien, 5 Freiheiten)", 2, (3,10)),
    # ⚑ Basis
    ("Schutz & Nutzung – Basis (einfache Konzepte/Beispiele)", 2, (1,10)),

    # 12 | Fortgeschrittene Vertiefungen & Vergleiche
    ("Fortbewegung: Laufen, Springen, Fliegen, Schwimmen – Energetik/Anpassung", 3, (8,10)),
    ("Ernährungsweisen: Herbivor/Omnivor/Karnivor/Spezialisten – Gebiss/Darm", 3, (7,10)),
    ("Lebenszyklen & Lebensgeschichten (r/K-Strategen, Itero-/Semelparität)", 3, (8,10)),
    ("Vergleich: Sinnesmodalitäten (Fledermaus vs. Eule vs. Hai)", 3, (8,10)),
    # ⚑ Basis
    ("Vergleich – Basis (Nahrungstypen ↔ Tierbeispiele)", 2, (1,10)),
]
