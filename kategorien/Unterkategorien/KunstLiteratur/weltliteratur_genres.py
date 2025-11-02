# -*- coding: utf-8 -*-
# Unterkategorien/KunstLiteratur/weltliteratur_genres.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Weltliteratur & Genres“.
Diese Liste wird von kategorien/kunst_literatur.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Ein einheitliches Schema zur Einteilung von Themen im Bereich Weltliteratur und
literarischer Genres. Es verbindet (1) globale Literaturtraditionen mit (2) Gattungswissen
und (3) interkulturellen Perspektiven auf Form, Stil und Funktion.

B. Skala (1–10) – Bedeutung
---------------------------
1 = Allgemeinwissen (z. B. weltbekannte Werke, Figuren)  
5 = mittlere Komplexität (Gattungsmerkmale, Stilrichtungen, interkulturelle Parallelen)  
10 = Expertenwissen (Theorie, Strukturanalyse, komparative Literaturwissenschaft)

C. Struktur
-----------
Dieses Modul bildet die **Querachse zwischen Kanon, Epoche und Form**:
- Teil 1: Überblick über Weltliteraturen
- Teil 2: Genres & Textsorten
- Teil 3: Interkulturelle Formen & Hybridgenres
- Teil 4: Theorie, Vergleich & moderne Entwicklungen
"""

# Schwierigkeits-Skala kurz (zur Laufzeit nutzbar):
# 1=Allgemeinwissen … 10=schwerstmöglich.

SUBDISCIPLINES = [
    # 1 Allgemeines & Grundlagen
    ("Weltliteratur-Begriff (Goethe bis Global Studies)", 4, (5,10)),
    ("Literarische Übersetzung & kulturelle Vermittlung", 3, (5,10)),
    ("Intertextualität & globale Stoffzirkulation", 3, (7,10)),
    # ⚑ einfache Kategorie
    ("Basiswissen Weltliteratur: Länder, Autor:innen, Hauptwerke", 2, (1,10)),

    # 2 Klassische Weltliteraturen (regionale Traditionslinien)
    ("Antike Weltliteratur (Griechisch, Römisch, Indisch, Chinesisch)", 4, (3,10)),
    ("Arabische & Persische Dichtung (Rūmī, Hafis, Kalila wa Dimna)", 3, (5,10)),
    ("Indische & Sanskrit-Literatur (Mahabharata, Ramayana, Kalidasa)", 3, (5,10)),
    ("Chinesische Klassik (Konfuzius, Tang-Lyrik, Der Traum der Roten Kammer)", 3, (5,10)),
    ("Japanische Literatur (Genji, Haiku, Moderne Autoren)", 3, (5,10)),
    ("Afrikanische mündliche Traditionen & frühe Schriftliteratur", 2, (5,10)),
    ("Indigene & mündliche Weltliteraturen (Mythos, Epos, Oral Poetry)", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Weltregionen – Basis (Autor–Werk–Kulturkreis)", 2, (1,10)),

    # 3 Moderne & globale Strömungen
    ("Postkoloniale Literatur (Themen, Stimmen, Sprachpolitik)", 3, (7,10)),
    ("Lateinamerikanischer Boom & Magischer Realismus", 4, (3,10)),
    ("Afrikanische Gegenwartsliteratur (Adichie, Ngũgĩ, Soyinka)", 3, (5,10)),
    ("Asiatische Gegenwartsliteratur (Murakami, Pamuk, Mo Yan)", 3, (5,10)),
    ("Diaspora- & Migrantenliteratur", 2, (5,10)),
    ("Globalisierung & Transkulturalität im Roman", 3, (5,10)),
    # ⚑ einfache Kategorie
    ("Moderne Weltliteratur – Basis (Autoren & Themenfelder)", 2, (1,10)),

    # 4 Genres – Epik & Prosa
    ("Romanformen weltweit (Bildungsroman, Gesellschaftsroman, Entwicklungsroman)", 4, (3,10)),
    ("Kurzgeschichte & Erzählung (Chekhov, Borges, Munro, Lahiri)", 3, (3,10)),
    ("Autobiografie, Memoir, Autofiktion", 2, (5,10)),
    ("Reiseliteratur, Abenteuerroman, Utopie/Dystopie", 2, (3,10)),
    ("Historischer Roman & Zeitroman", 3, (5,10)),
    ("Magischer Realismus & Surrealismus in der Prosa", 3, (5,10)),
    # ⚑ einfache Kategorie
    ("Epik – Basis (Gattung & Werk zuordnen)", 2, (1,10)),

    # 5 Lyrik & Dichtung
    ("Lyrische Formen weltweit (Sonett, Ghazal, Haiku, Slam Poetry)", 3, (3,10)),
    ("Epische Dichtung & Volkslied (Gilgamesch, Homer, Kalevala)", 3, (5,10)),
    ("Moderne Dichtung (Whitman, Eliot, Celan, Neruda)", 3, (5,10)),
    ("Politische & engagierte Lyrik (Resistance, Exil, Feminismus)", 3, (5,10)),
    # ⚑ einfache Kategorie
    ("Lyrik – Basis (Formen & Autoren zuordnen)", 2, (1,10)),

    # 6 Drama & Theater
    ("Antikes Drama (Tragödie, Komödie, Katharsis)", 4, (3,10)),
    ("Europäische Klassiker (Shakespeare, Molière, Goethe, Ibsen)", 4, (1,10)),
    ("Asiatische Theaterformen (No, Kabuki, Kathakali, Peking-Oper)", 3, (5,10)),
    ("Moderne & postdramatische Formen (Brecht, Beckett, Kane)", 3, (5,10)),
    ("Performance & Hybridformen", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Drama – Basis (Autor–Epoche–Form)", 2, (1,10)),

    # 7 Genrevielfalt & Populärkultur
    ("Kriminalliteratur & Thriller (von Poe bis Highsmith)", 2, (3,10)),
    ("Science-Fiction & Fantasy (Verne, Le Guin, Tolkien, Butler)", 3, (3,10)),
    ("Horror & Gothic Novel (Shelley, Stoker, King)", 2, (3,10)),
    ("Romance, Jugend- & Popliteratur", 2, (1,10)),
    ("Comics, Graphic Novels & visuelle Erzählformen", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Populärgenres – Basis (Genremerkmale & Klassiker)", 2, (1,10)),

    # 8 Interkulturelle & vergleichende Perspektiven
    ("Literarische Moderne weltweit (Einflüsse & Zeitverschiebungen)", 3, (5,10)),
    ("Motivvergleiche über Kulturen (Held, Reise, Liebe, Rebellion)", 3, (3,10)),
    ("Gender & Identität in globaler Literatur", 3, (5,10)),
    ("Übersetzung & Weltliteratur-Kanonbildung", 3, (7,10)),
    ("Adaptionen (Film, Theater, Comic, Oper)", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Vergleich – Basis (Motiv/Werk/Kultur zuordnen)", 2, (1,10)),

    # 9 Literaturtheorie & Gattungskritik
    ("Theorien der Weltliteratur (Goethe, Damrosch, Moretti)", 3, (7,10)),
    ("Gattungstheorie: Struktur, Hybridisierung, Metagenres", 3, (7,10)),
    ("Narratologie & Genreanalyse", 3, (7,10)),
    ("Postkoloniale & feministische Genretheorie", 3, (7,10)),
    # ⚑ einfache Kategorie
    ("Theorie – Basis (Begriffe & Strömungen erkennen)", 2, (1,10)),

    # 10 Preislandschaft & Institutionen (zeitabhängig)
    ("Literatur-Nobelpreis & globale Kanonbildung", 2, (1,10)),
    ("Internationale Literaturpreise (Booker, Pulitzer, Prix Goncourt)", 2, (1,10)),
    ("Festival- & Übersetzungsnetzwerke", 2, (3,10)),
    # ⚑ einfache Kategorie
    ("Preise – Basis (Autor:in dem Preis zuordnen)", 2, (1,10)),
]
