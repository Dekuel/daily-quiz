# -*- coding: utf-8 -*-
# Unterkategorien/KunstLiteratur/kunstgeschichte_epochen.py

SUBDISCIPLINES = [
    # — VORZEIT & FRÜHE HOCHKULTUREN —
    ("Prähistorische Kunst: Höhlenmalerei & Megalithkultur", 3, (5,10)),
    ("Altägyptische Kunst: Kanon, Hieroglyphen, Grabkunst", 4, (3,10)),
    ("Mesopotamien: Sumerer, Assyrer, Babylonier – Relief & Monument", 3, (7,10)),
    ("Alte Kulturen des Mittelmeerraums (Mykene, Kreta, Phönizien)", 2, (5,10)),
    ("Frühe Hochkulturen – Basis (Pyramiden, Sphinx, Keilschrift-Reliefs)", 2, (1,8)),

    # — KLASSISCHE ANTIKE —
    ("Griechische Kunst: Archaik, Klassik, Hellenismus – Skulptur & Tempel", 4, (3,10)),
    ("Römische Kunst: Porträt, Architektur, Mosaik – Aneignung & Technik", 4, (6,10)),
    ("Vasenmalerei & Ikonographie der Antike", 3, (7,10)),
    ("Antike – Basis (Dorisch/Ionisch/Korinthisch; Parthenon; Laokoon-Gruppe)", 2, (1,8)),

    # — SPÄTANTIKE & BYZANZ —
    ("Frühchristliche Kunst & Spätantike Bildprogramme", 3, (5,10)),
    ("Byzantinische Kunst: Ikonen, Mosaiken, Hagia Sophia", 4, (6,10)),
    ("Byzanz – Basis (Goldgrund, Ikone, Mosaikmerkmale erkennen)", 2, (1,8)),

    # — ROMANIK & GOTIK —
    ("Romanik: Architektur, Portalplastik, Fresko – Symbolik & Didaxe", 4, (6,10)),
    ("Gotik: Kathedrale, Maßwerk, Glasfenster, Skulptur", 4, (3,10)),
    ("Gotik international & Spätgotik (Weicher Stil, Flügelaltäre)", 3, (5,10)),
    ("Mittelalter – Basis (Rundbogen vs. Spitzbogen; Tympanon; Glasmalerei)", 2, (1,8)),

    # — RENAISSANCE —
    ("Frühe Renaissance (Quattrocento): Perspektive, Humanismus, Werkstatt", 4, (6,10)),
    ("Hochrenaissance: Leonardo, Raffael, Michelangelo – Ideal & Harmonie", 4, (3,10)),
    ("Nordische Renaissance: Dürer, van Eyck, Holbein – Technik & Symbolik", 3, (5,10)),
    ("Venezianische Renaissance: Farbe, Atmosphäre, Tizian", 3, (5,10)),
    ("Renaissance – Basis (Mona Lisa, Letztes Abendmahl, Sixtinische Decke)", 2, (1,8)),

    # — MANIERISMUS, BAROCK, ROKOKO —
    ("Manierismus: Proportion, Virtuosität, El Greco, Bronzino", 3, (7,10)),
    ("Barock: Caravaggio, Bernini, Rubens – Lichtdramaturgie & Pathos", 4, (6,10)),
    ("Rokoko: Watteau, Boucher, Fragonard – Galanterie & Interieurkunst", 3, (5,10)),
    ("Barock/Rokoko – Basis (Chiaroscuro, Theatralik, Pastellfarben)", 2, (1,8)),

    # — KLASSIZISMUS BIS REALISMUS —
    ("Neoklassizismus: David, Ingres – Antikeideale & Moral", 3, (5,10)),
    ("Romantik: C. D. Friedrich, Turner, Delacroix – Sublimes & Gefühl", 4, (3,10)),
    ("Realismus & Naturalismus: Courbet, Millet – Gesellschaft & Alltäglichkeit", 3, (5,10)),
    ("1800–1870 – Basis (Antikezitat vs. Gefühl, Atelier- vs. Freilichtmalerei)", 2, (1,8)),

    # — IMPRESSIONISMUS & POSTIMPRESSIONISMUS —
    ("Impressionismus: Monet, Renoir, Degas – Licht, Moment, plein air", 4, (3,10)),
    ("Postimpressionismus: Cézanne, Van Gogh, Gauguin, Seurat", 4, (6,10)),
    ("Impressionismus – Basis (Seerosen, Ballett, Sonntag auf La Grande Jatte)", 2, (1,8)),

    # — JUGENDSTIL / SYMBOLISMUS / AVANTGARDEN —
    ("Symbolismus & Jugendstil/Art Nouveau: Klimt, Beardsley, Horta", 3, (5,10)),
    ("Fauvismus & früher Expressionismus: Matisse, Derain", 3, (5,10)),
    ("Expressionismus (Brücke/Blauer Reiter): Kirchner, Kandinsky, Marc", 4, (6,10)),
    ("Kubismus: Picasso, Braque – Zerlegung & Mehransicht", 4, (7,10)),
    ("Futurismus, De Stijl & Konstruktivismus", 3, (8,10)),
    ("Dada & Surrealismus: Duchamp, Dalí, Magritte – Anti-Kunst & Traum", 4, (6,10)),
    ("1900–1930 – Basis (Kubistische Formen, Surreale Motive erkennen)", 2, (1,8)),

    # — BAUHAUS & MODERNE ARCHITEKTUR —
    ("Bauhaus: Werkbund, Form follows function, Gropius/Klee/Kandinsky", 3, (7,10)),
    ("Moderne Architektur: Le Corbusier, Mies, Wright – International Style", 3, (7,10)),

    # — NACHKRIEGSMODERNE & GEGENWART —
    ("Abstrakter Expressionismus & Farbfeldmalerei: Pollock, Rothko", 3, (7,10)),
    ("Minimal Art & Konzeptkunst: Judd, LeWitt, Kosuth", 3, (8,10)),
    ("Pop Art: Warhol, Lichtenstein – Massenkultur & Reproduktion", 4, (3,10)),
    ("Postmoderne Strömungen: Appropriation, Neo-Expressionismus", 3, (8,10)),
    ("Zeitgenössische Kunst: Globalisierung, Biennalen, digitale Praktiken", 3, (7,10)),
    ("Nachkrieg & Gegenwart – Basis (Pop-Ikonen, Minimal-Formen erkennen)", 2, (1,8)),

    # — NON-WESTERN / TRANSCULTURAL (Überblick) —
    ("Islamische Kunst: Ornament, Kalligraphie, Architektur", 3, (5,10)),
    ("Ostasiatische Kunst: China/Japan/Korea – Tusche, Ukiyo-e, Zen", 3, (5,10)),
    ("Südasiatische & Südostasiatische Kunsttraditionen (Überblick)", 2, (5,10)),
    ("Afrikanische Kunst (historisch & Einflüsse auf die Moderne)", 3, (5,10)),
    ("Präkolumbische Kunst Amerikas: Maya, Azteken, Inka", 3, (7,10)),
    ("Weltkunst – Basis (Ukiyo-e, Maskenkunst, Muqarnas grob zuordnen)", 2, (1,8)),

    # — METHODEN, DISKURSE & VERGLEICHE —
    ("Stilanalyse & Epochenmerkmale (ikonische Kennzeichen)", 3, (7,10)),
    ("Ikonologie (Panofsky) & Kontextualisierung", 3, (8,10)),
    ("Transkulturalität & Global Art History (Überblick)", 2, (8,10)),
    ("Vergleich: Barock vs. Klassizismus; Impressionismus vs. Expressionismus", 3, (5,10)),
    ("Kunstmarkt, Musealisierung & Kanonkritik (Grundlagen)", 2, (7,10)),
    ("Epochenvergleich – Basis (typische Motive/Formen rasch zuordnen)", 2, (1,8)),
]
