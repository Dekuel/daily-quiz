# -*- coding: utf-8 -*-
# Unterkategorien/KunstLiteratur/musikgeschichte_epochen.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Musikgeschichte & Epochen“.
Diese Liste wird von kategorien/kunst_literatur.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Ein konsistentes, epochenübergreifendes Schema zur Systematisierung von Themen
der Musikgeschichte. Es soll (1) historische Entwicklungen, (2) Stilmerkmale
und (3) bedeutende Komponist:innen erfassen, um Quizfragen von Basis- bis
Expertenniveau zu ermöglichen.

B. Skala (1–10) – Bedeutung
---------------------------
1 = populäres Allgemeinwissen (Mozart, Beethoven, Klassik als Epoche)  
4–6 = mittleres Bildungswissen (Stile, Begriffe, nationale Schulen)  
9–10 = Expertenwissen (Analyse, Werkkunde, Stilästhetik, Musiktheorie-Kontext)

C. Struktur
-----------
- Frühformen & Mittelalter
- Renaissance & Barock
- Klassik & Romantik
- Moderne & Zeitgenössische Musik
- Vergleichende, theoretische und interkulturelle Perspektiven
"""

# Schwierigkeits-Skala kurz (zur Laufzeit nutzbar):
# 1=Allgemeinwissen … 10=schwerstmöglich.

SUBDISCIPLINES = [
    # 1 Frühformen & Mittelalter
    ("Anfänge der Musikgeschichte: Antike & frühe Notation", 4, (5,10)),
    ("Gregorianischer Choral & mittelalterliche Mehrstimmigkeit", 4, (5,10)),
    ("Minnesang, Troubadours & höfische Musiktraditionen", 3, (3,10)),
    ("Kirchliche & weltliche Musik im Mittelalter", 3, (3,10)),
    # ⚑ einfache Kategorie
    ("Frühmusik – Basis (Gregorianik, Mittelalter, frühe Instrumente)", 2, (1,10)),

    # 2 Renaissance (15.–16. Jh.)
    ("Renaissance – Merkmale (Imitation, Polyphonie, Vokalstil)", 4, (3,10)),
    ("Meister der Renaissance (Josquin, Palestrina, Lasso)", 4, (3,10)),
    ("Instrumentalmusik & Tanzformen", 3, (3,10)),
    ("Musik im Humanismus: Textausdruck & Madrigal", 3, (5,10)),
    # ⚑ einfache Kategorie
    ("Renaissance – Basis (Komponisten & Stilmerkmale)", 2, (1,10)),

    # 3 Barock (ca. 1600–1750)
    ("Barock – Stilmerkmale (Generalbass, Affektenlehre, Kontrapunkt)", 4, (3,10)),
    ("Bach, Händel & Vivaldi – zentrale Vertreter", 4, (1,10)),
    ("Oper & Oratorium im Barock", 3, (5,10)),
    ("Instrumentalmusik: Concerto, Suite, Fuge", 3, (5,10)),
    ("Musikzentren: Italien, Frankreich, Deutschland", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Barock – Basis (Formen, Komponisten, Gattungen)", 2, (1,10)),

    # 4 Klassik (ca. 1750–1820)
    ("Wiener Klassik – Haydn, Mozart, Beethoven", 4, (1,10)),
    ("Formprinzipien: Sonatenhauptsatz, Symphonie, Streichquartett", 3, (5,10)),
    ("Oper der Klassik (Mozart, Gluck)", 3, (5,10)),
    ("Musikästhetik der Aufklärung (Maß, Harmonie, Vernunft)", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Klassik – Basis (Epochenbegriff, Hauptkomponisten, Formen)", 2, (1,10)),

    # 5 Romantik (ca. 1820–1900)
    ("Romantik – Ausdruck, Gefühl, nationale Schulen", 4, (3,10)),
    ("Sinfonische Dichtung & Programmmusik (Liszt, Berlioz)", 3, (5,10)),
    ("Oper der Romantik (Wagner, Verdi, Bizet)", 3, (3,10)),
    ("Virtuosenkult & Salonmusik (Chopin, Paganini, Clara Schumann)", 3, (3,10)),
    ("Spätromantik & Übergang zur Moderne (Mahler, Strauss)", 3, (5,10)),
    # ⚑ einfache Kategorie
    ("Romantik – Basis (Komponisten, Gattungen, Leitmotive)", 2, (1,10)),

    # 6 Moderne (20. Jh.)
    ("Moderne & Avantgarde (Atonalität, Dodekaphonie, Neue Musik)", 4, (5,10)),
    ("Expressionismus & Zweite Wiener Schule (Schönberg, Berg, Webern)", 4, (7,10)),
    ("Impressionismus & Symbolismus (Debussy, Ravel)", 3, (5,10)),
    ("Neoklassizismus & Stravinsky", 3, (5,10)),
    ("Jazz-Einflüsse & Popularmusik der Moderne", 2, (3,10)),
    # ⚑ einfache Kategorie
    ("Moderne – Basis (Stilrichtungen & Hauptvertreter)", 2, (1,10)),

    # 7 Zeitgenössische Musik (1950–heute)
    ("Serielle Musik, Aleatorik & elektronische Komposition", 3, (7,10)),
    ("Minimal Music & Konzeptkunst (Reich, Glass, Cage)", 3, (5,10)),
    ("Neue Musikformen & Crossover (Film, Games, Multimedia)", 2, (5,10)),
    ("Globalisierung & außereuropäische Einflüsse", 2, (5,10)),
    ("Klangkunst & Soundscape", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Zeitgenössisch – Basis (Stilrichtungen & Komponisten)", 2, (1,10)),

    # 8 Musikkulturen & interkulturelle Strömungen
    ("Musik außereuropäischer Kulturen (afrikanisch, arabisch, asiatisch)", 3, (3,10)),
    ("Tradition & Moderne: Weltmusik & Fusion", 2, (5,10)),
    ("Volksmusik & nationale Stile (Folk, Chanson, Flamenco)", 2, (3,10)),
    # ⚑ einfache Kategorie
    ("Weltmusik – Basis (Stil, Herkunft, Instrumente)", 2, (1,10)),

    # 9 Theoretische & formale Aspekte
    ("Musikalische Formenlehre (Fuge, Sonate, Rondo, Variation)", 3, (5,10)),
    ("Instrumentenkunde & Orchesterentwicklung", 3, (3,10)),
    ("Notationssysteme & Musikschrift", 2, (5,10)),
    ("Harmonielehre & Kontrapunkt (historisch)", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Formen & Instrumente – Basis (Begriffe, Zuordnungen)", 2, (1,10)),

    # 10 Vergleichende & übergreifende Themen
    ("Epochenvergleich (Barock vs. Klassik vs. Romantik)", 2, (5,10)),
    ("Musik & Gesellschaft (Kirche, Hof, Öffentlichkeit, Medien)", 2, (5,10)),
    ("Musikgeschichte & Zeitgeist (Kunstströmungen, Philosophie)", 2, (5,10)),
    ("Kanon & Rezeption (wie entsteht musikalisches Erbe?)", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Vergleich – Basis (Epoche–Komponist–Werk zuordnen)", 2, (1,10)),
]
