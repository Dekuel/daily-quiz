# -*- coding: utf-8 -*-
# Unterkategorien/KunstLiteratur/klassische_werke_autoren.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Klassische Werke & Autoren“.
Diese Liste wird von kategorien/kunst_literatur.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Ein konsistentes Schema für Quizfragen, das (1) strukturierte Kategorien liefert
und (2) realistische Schwierigkeits-Intervalle (1–10) definiert. Übertragbar
auf andere Domänen.

B. Skala (1–10) – Bedeutung
---------------------------
1 = absolutes Grundwissen … 10 = schwerstmöglich (oberes Expertenniveau)

C. Zwei Achsen
--------------
(1) Bekanntheit (Population Familiarity)
(2) Inhalts-/Methodenkomplexität (Conceptual/Method Complexity)

D. Gewichte (Heuristik)
-----------------------
Gew. 4 = Kernkanon (typ. 2–4, bis 9/10 möglich)
Gew. 3 = Vertiefungen (typ. 3–5, bis 9/10 möglich)
Gew. 2 = Umfeld/Standard (typ. 1–4, bis 8/9 möglich)

E. Basiskategorien (Level-1 fähig)
----------------------------------
Je Überkategorie eine „Basis“-Kategorie mit **min = 1**.

F. Abgrenzung
-------------
Dieses Modul fokussiert auf Autor:innen, Werke, Epochen-Kanon, Formen & Motive.
Spezifische Kunstgattungen (Malerei usw.) stehen in anderen Dateien.
"""

# Schwierigkeits-Skala kurz (zur Laufzeit nutzbar):
# 1=Allgemeinwissen … 10=schwerstmöglich.

SUBDISCIPLINES = [
    # 1 Allgemeines & Grundlagen
    ("Literaturkanon: Begriff, Kriterien & Debatten", 4, (5,10)),
    ("Gattungen: Lyrik, Epik, Drama – Grundbegriffe & Abgrenzung", 4, (1,10)),
    ("Erzähltheorie – Basis (Erzähler, Fokalisierung, Zeit, Plot)", 3, (3,10)),
    ("Motiv–Topos–Mythos: Archetypen & Stofftraditionen", 3, (5,10)),
    # ⚑ einfache Kategorie (Level-1 möglich)
    ("Basiswissen Literatur: Autor–Werk–Epoche zuordnen (weltweit)", 2, (1,10)),

    # 2 Antike Klassik (Griechisch/Römisch)
    ("Griechische Tragödie & Komödie (Aischylos, Sophokles, Euripides, Aristophanes)", 4, (3,10)),
    ("Homerische Epen & epische Techniken", 4, (3,10)),
    ("Römische Klassiker (Vergil, Ovid, Horaz, Cicero, Seneca)", 4, (5,10)),
    # ⚑ einfache Kategorie
    ("Antike – Basisfakten (Autor–Werk–Gattung)", 2, (1,10)),

    # 3 Mittelalter & Frühneuzeit (Europa)
    ("Mittelalterliche Epen & Artusstoff (Nibelungenlied, Chanson de geste)", 3, (5,10)),
    ("Mystik & Didaktik (Hildegard, Meister Eckhart, MHG-Lyrik)", 2, (3,10)),
    ("Humanismus & Renaissance (Dante, Boccaccio, Petrarca, Rabelais)", 4, (3,10)),
    ("Elisabethanisches Drama (Shakespeare, Marlowe, Jonson)", 4, (1,10)),
    ("Spanisches Goldene-Zeit-Drama & Roman (Lope, Calderón, Cervantes)", 3, (5,10)),
    # ⚑ einfache Kategorie
    ("Mittelalter/Renaissance – Basis (Schlüsselwerke & Figuren)", 2, (1,10)),

    # 4 Aufklärung, Klassik & Romantik (deutschsprachig/Europa)
    ("Aufklärung (Lessing, Voltaire, Swift – Vernunft & Satire)", 3, (3,10)),
    ("Weimarer Klassik (Goethe, Schiller – Drama, Lyrik, Bildungsroman)", 4, (1,10)),
    ("Romantik (Novalis, Tieck, Hoffmann; Byron, Shelley, Keats)", 3, (3,10)),
    ("Historischer Roman & Frührealismus (Scott, Stendhal, Balzac)", 3, (5,10)),
    # ⚑ einfache Kategorie
    ("Aufklärung/Klassik/Romantik – Basis (Zitate, Figuren, Stoffe)", 2, (1,10)),

    # 5 Realismus, Naturalismus & Moderne (19.–frühes 20. Jh.)
    ("Europäischer Realismus (Flaubert, Tolstoi, Dostojewski, Fontane)", 4, (3,10)),
    ("Naturalismus & Décadence (Zola, Ibsen, Strindberg, Huysmans)", 3, (5,10)),
    ("Amerikanischer Kanon 19. Jh. (Poe, Hawthorne, Melville, Twain, Dickinson)", 3, (3,10)),
    ("Frühe Moderne/Avantgarden (Kafka, Joyce, Woolf, Proust)", 4, (5,10)),
    # ⚑ einfache Kategorie
    ("19. Jh. – Basis (Autor–Werk–Epoche zuordnen)", 2, (1,10)),

    # 6 20. Jh. & Weltliteratur (übergreifend)
    ("Exilliteratur & Moderne (Brecht, Thomas Mann, Döblin)", 3, (5,10)),
    ("Lateinamerika: Boom & Magischer Realismus (García Márquez, Borges)", 3, (3,10)),
    ("Afrikanische & postkoloniale Literatur (Achebe, Soyinka, Adichie)", 2, (3,10)),
    ("Asiatische Klassiker & Moderne (Murasaki, Bashō, Kawabata, Murakami)", 2, (3,10)),
    ("Nahost & Persischsprachig (Ferdousi, Rūmī, Hedayat)", 2, (7,10)),
    ("Osteuropa & Russland 20. Jh. (Bulgakow, Solschenizyn, Zwetajewa)", 2, (5,10)),
    ("US/UK 20. Jh. (Faulkner, Hemingway, Steinbeck, Orwell)", 3, (3,10)),
    # ⚑ einfache Kategorie
    ("Weltliteratur – Basis (Nobelpreisträger:innen, ikonische Romane)", 2, (1,10)),

    # 7 Formen & Spezialgebiete
    ("Lyrik – Formen & Epochen (Sonett, Ode, Elegie, freie Rhythmen)", 3, (3,10)),
    ("Drama – Struktur & Typen (Tragödie, Komödie, bürgerliches Trauerspiel)", 3, (3,10)),
    ("Epos/Epik – Erzählverfahren (Rahmen, Montage, Stream of Consciousness)", 3, (5,10)),
    ("Kurzgeschichte & Novelle – Merkmale & Meister:innen", 2, (3,10)),
    ("Kinder-/Jugendliteratur – Klassiker (Ende, Lindgren, Carroll)", 2, (1,10)),
    ("Essay, Tagebuch, Briefroman (Montaigne bis Barthes)", 2, (5,10)),
    ("Reiseliteratur & Utopie/Dystopie (More, Huxley, Orwell, Le Guin)", 2, (3,10)),
    # ⚑ einfache Kategorie
    ("Formenkunde – Basis (Gattung an Merkmalen erkennen)", 2, (1,10)),

    # 8 Figuren, Motive & Stoffe (interkulturell)
    ("Mythische Zyklen (Gilgamesch, Troja, Ragnarök, Ramayana)", 3, (5,10)),
    ("Archetypische Figuren (Trickster, Held, Antiheld, Flaneur)", 2, (5,10)),
    ("Liebes- & Eifersuchtsmotive (Tristan/Isolde, Othello, Madame Bovary)", 2, (3,10)),
    ("Reise- & Bildungsnarrative (Odyssee, Wilhelm Meister)", 2, (3,10)),
    ("Satire & Gesellschaftskritik (Gulliver, Candide, Animal Farm)", 2, (3,10)),
    # ⚑ einfache Kategorie
    ("Motive – Basis (Werk dem Motiv zuordnen)", 2, (1,10)),

    # 9 Übersetzung, Textkritik & Überlieferung
    ("Übertragungen & Übersetzungstheorie (wörtlich vs. frei, Wirkung)", 2, (7,10)),
    ("Editionen, Philologie & Kanonbildung", 3, (7,10)),
    ("Intertextualität & Adaptationen (Theater/Film/Oper)", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Kanon & Edition – Basis (Begriffe, berühmte Übersetzungen)", 2, (1,10)),

    # 10 Vergleichende & Querschnitts-Kategorien
    ("Vergleich: Epochenstile in Prosa/Lyrik/Drama", 2, (5,10)),
    ("Vergleich: nationale Traditionen & Einflüsse (Europa–Welt)", 2, (5,10)),
    ("Preislandschaft & Institutionen (Nobelpreis, Booker, Goncourt) – zeitabhängig", 2, (1,10)),
    ("Biografische Kontexte & Poetiken (Manifest, Vorrede, Essays)", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Vergleich – Basis: Zitate/Anfänge berühmter Werke erkennen", 2, (1,10)),
]
