# -*- coding: utf-8 -*-
# Unterkategorien/KunstLiteratur/musikwissen_theorie_allgemein.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Musikwissen & Theorie (Allgemein)“.
Diese Liste wird von kategorien/kunst_literatur.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Dieses Modul bietet eine strukturierte Übersicht über Grundlagen- und Theoriewissen
zur Musik: von elementarem Hörverständnis bis zu harmonischen, formalen und
ästhetischen Konzepten. Es verbindet populäres Musikwissen mit grundlegenden
Begriffen der Musiktheorie, Akustik und Wahrnehmung.

B. Skala (1–10) – Bedeutung
---------------------------
1 = Basiswissen (Noten, Töne, bekannte Begriffe)  
4–6 = mittlere Komplexität (Tonarten, Intervalle, Formenlehre)  
9–10 = Expertenwissen (Harmonielehre, Satztechnik, Theoriediskurse)

C. Struktur
-----------
1) Allgemeine Musiklehre & Notation  
2) Rhythmik, Melodik, Harmonik  
3) Formenlehre & Komposition  
4) Instrumentenkunde & Klang  
5) Akustik, Wahrnehmung & Ästhetik  
6) Musiktheorie, Philosophie & Analyse
"""

# Schwierigkeits-Skala kurz (zur Laufzeit nutzbar):
# 1=Allgemeinwissen … 10=schwerstmöglich.

SUBDISCIPLINES = [
    # 1 Allgemeine Grundlagen
    ("Musik als Kunstform: Definition, Wirkung, Funktionen", 4, (3,10)),
    ("Grundbegriffe: Ton, Klang, Geräusch, Dynamik, Tempo", 4, (1,9)),
    ("Notenschrift & Notation (Schlüssel, Notenwerte, Pausen)", 3, (1,9)),
    ("Tonleiter, Tonarten & Intervalle", 3, (3,10)),
    ("Rhythmus, Takt & Metrum", 3, (3,9)),
    # ⚑ einfache Kategorie
    ("Basiswissen Musik: Noten, Begriffe, Instrumente erkennen", 2, (1,9)),

    # 2 Melodik & Harmonik
    ("Melodie & Motiv – Aufbau, Wiederholung, Variation", 4, (3,10)),
    ("Akkorde & Harmonielehre – Dur/Moll, Dreiklänge, Kadenz", 4, (5,10)),
    ("Tonarten & Modulation (Wechsel der Tonalität)", 3, (5,10)),
    ("Konsonanz, Dissonanz & Spannung", 3, (5,10)),
    ("Melodiebildung in verschiedenen Stilen (Volkslied, Jazz, Pop)", 2, (3,9)),
    # ⚑ einfache Kategorie
    ("Harmonie – Basis (Akkord, Tonart, Klangwirkung)", 2, (1,9)),

    # 3 Rhythmus & Form
    ("Taktarten & rhythmische Muster", 3, (3,9)),
    ("Formenlehre (Periode, Satz, Rondo, Fuge, Sonate)", 3, (5,10)),
    ("Motivische Arbeit & Entwicklung", 3, (5,10)),
    ("Rhythmische Besonderheiten (Synkope, Polyrhythmik)", 3, (5,10)),
    ("Improvisation & Variation in Musikstilen", 2, (3,9)),
    # ⚑ einfache Kategorie
    ("Rhythmus – Basis (Taktarten, einfache Notenwerte)", 2, (1,9)),

    # 4 Instrumentenkunde & Klang
    ("Instrumentenfamilien & Bauweise (Streicher, Bläser, Schlagzeug)", 4, (3,10)),
    ("Stimmen & Gesang – Stimmlagen, Technik, Ausdruck", 3, (3,9)),
    ("Orchesteraufbau & Besetzungen", 3, (3,10)),
    ("Akustische Grundlagen (Frequenz, Schwingung, Resonanz)", 3, (5,10)),
    ("Elektronische Klangerzeugung & Synthese", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Instrumente – Basis (Familie, Klang, Funktion)", 2, (1,9)),

    # 5 Musikästhetik & Wahrnehmung
    ("Musik & Emotion – psychologische Grundlagen", 3, (3,9)),
    ("Musikalische Wahrnehmung & Höranalyse", 3, (5,10)),
    ("Musikästhetik (Affektenlehre, Ausdruck, Schönheit, Form)", 3, (5,10)),
    ("Musik & Philosophie (Schopenhauer, Adorno, Cage)", 3, (7,10)),
    ("Kulturelle & soziale Funktion von Musik", 2, (3,9)),
    # ⚑ einfache Kategorie
    ("Ästhetik – Basis (Musik & Wirkung zuordnen)", 2, (1,9)),

    # 6 Komposition & Analyse
    ("Satztechnik (zweistimmig, vierstimmig, Kontrapunkt)", 4, (7,10)),
    ("Analyse klassischer Formen (Sonate, Fuge, Variation)", 3, (7,10)),
    ("Moderne Kompositionsverfahren (Zwölfton, Serialismus, Aleatorik)", 3, (8,10)),
    ("Populäre Songstruktur (Vers, Refrain, Bridge, Hook)", 2, (3,9)),
    ("Improvisation & Struktur im Jazz", 3, (5,10)),
    # ⚑ einfache Kategorie
    ("Form & Aufbau – Basis (Teile eines Musikstücks erkennen)", 2, (1,9)),

    # 7 Akustik & Technik
    ("Schall, Frequenz & Klangfarbe", 3, (5,10)),
    ("Akustische Räume & Hall", 2, (5,10)),
    ("Tonaufzeichnung & Studioarbeit (analog/digital)", 2, (5,10)),
    ("Mikrofonie & Verstärkung – Grundlagen", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Technik – Basis (Ton, Klang, Aufnahme)", 2, (1,9)),

    # 8 Interdisziplinäre Themen
    ("Musik & Mathematik (Proportion, Rhythmus, Struktur)", 3, (7,10)),
    ("Musik & Sprache (Melodie, Intonation, Semantik)", 3, (5,10)),
    ("Musik & Farbe – synästhetische Konzepte", 2, (5,10)),
    ("Musik in Religion, Ritual & Kultur", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Interdisziplinär – Basis (Musik in anderen Kontexten)", 2, (1,9)),

    # 9 Musiktheoriegeschichte
    ("Antike & Mittelalterliche Musiktheorie (Boethius, Guidonische Hand)", 3, (7,10)),
    ("Barock & Klassik (Rameau, Mattheson, Koch)", 3, (7,10)),
    ("Romantik & Moderne (Schenker, Hindemith, Schönberg)", 3, (8,10)),
    ("Zeitgenössische Theorie (Spektralmusik, Systemtheorie, KI)", 2, (8,10)),
    # ⚑ einfache Kategorie
    ("Theoriegeschichte – Basis (Epoche & Theoretiker zuordnen)", 2, (1,9)),

    # 10 Vergleichende & anwendungsorientierte Themen
    ("Vergleich: Tonalität, Modalität, Atonalität", 3, (5,10)),
    ("Formenvergleich Klassik vs. Pop", 2, (5,10)),
    ("Musikalische Analyse verschiedener Kulturen", 2, (5,10)),
    ("Anwendung: Notenlesen, Intervalle hören, Akkorde erkennen", 2, (1,9)),
    # ⚑ einfache Kategorie
    ("Praxis – Basis (Ton, Akkord, Rhythmus erkennen)", 2, (1,9)),
]
