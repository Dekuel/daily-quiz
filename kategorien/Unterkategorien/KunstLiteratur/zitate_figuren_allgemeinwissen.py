# -*- coding: utf-8 -*-
# Unterkategorien/KunstLiteratur/zitate_figuren_allgemeinwissen.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Zitate, Figuren & Allgemeinwissen Literatur“.
Diese Liste wird von kategorien/kunst_literatur.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Dieses Modul bündelt leicht zugängliches, aber kulturprägendes Literaturwissen:
berühmte Zitate, Figuren, erste Sätze, Werkzuordnungen, ikonische Autor:innen.
Es bildet die niedrigste Einstiegsebene in die Kategorie „Literaturwissen“ und
dient zugleich als Schnittstelle zwischen Trivia, Bildungskanon und Analyse.

B. Skala (1–10) – Bedeutung
---------------------------
1 = absolutes Allgemeinwissen (z. B. „Sein oder Nichtsein“)  
4–6 = mittleres Bildungswissen (Werke, Figuren, Zitate zuordnen)  
9–10 = komplexe Quellenkenntnis, Fehlzitate, Meta-Interpretationen

C. Fokus
--------
- Zuordnungen (Zitat → Werk/Autor, Figur → Werk)  
- Wiedererkennen klassischer Textstellen  
- Überblick über kulturell ikonische Aussagen, Archetypen & Symbole  
- Sprachlich/stilistisch berühmte Wendungen, geflügelte Worte
"""

# Schwierigkeits-Skala kurz (zur Laufzeit nutzbar):
# 1=Allgemeinwissen … 10=schwerstmöglich.

SUBDISCIPLINES = [
    # 1 Klassiker – Allgemein bekannte Zitate
    ("Berühmte Zitate der Weltliteratur (Shakespeare, Goethe, Cervantes)", 4, (1,10)),
    ("Philosophische & existenzielle Zitate (Nietzsche, Camus, Dostojewski)", 3, (5,10)),
    ("Geflügelte Worte aus Romanen & Dramen", 3, (5,10)),
    ("Missverständene oder falsch zugeschriebene Zitate", 2, (7,10)),
    # ⚑ einfache Kategorie
    ("Basiswissen Zitate – Klassiker & Redewendungen zuordnen", 2, (1,9)),

    # 2 Figuren & Charaktere
    ("Ikonische Romanfiguren (Don Quijote, Faust, Hamlet, Anna Karenina)", 4, (1,10)),
    ("Held:innen, Antiheld:innen & Erzählerfiguren", 3, (5,10)),
    ("Nebenfiguren & Symbolträger:innen (Mephisto, Sancho, Friday, Ophelia)", 3, (5,10)),
    ("Tierfiguren & Allegorien (Fabeln, Orwell, Aesop)", 2, (1,10)),
    ("Archetypen & Typen (Narr, Genie, Außenseiter, Tragödin)", 2, (3,10)),
    # ⚑ einfache Kategorie
    ("Figuren – Basis: Figur dem Werk/Autor zuordnen", 2, (1,9)),

    # 3 Werkeinstiege & Schlusssätze
    ("Berühmte erste Sätze der Literaturgeschichte", 3, (5,10)),
    ("Schlusssätze & ihre Symbolik", 2, (5,10)),
    ("Anfänge und Enden vergleichen (Rahmenbau, Kreisform, Pointe)", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Anfänge – Basis (Zitat dem Werk zuordnen)", 2, (1,9)),

    # 4 Stil & Sprache
    ("Sprichwörtliche Redewendungen aus Literatur (Bibel, Klassik, Volksgut)", 3, (1,10)),
    ("Metaphern & geflügelte Worte (Faust, Hamlet, Ilias, 1984)", 3, (5,10)),
    ("Ironie, Parodie & Sprachspiel (Cervantes, Swift, Wilde)", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Sprachbilder – Basis (Bedeutung & Quelle erkennen)", 2, (1,9)),

    # 5 Länder & Kulturen
    ("Berühmte Zitate aus nicht-europäischen Literaturen (Asien, Afrika, Lateinamerika)", 3, (5,10)),
    ("Bibelzitate & religiöse Literatur in der Alltagssprache", 3, (5,10)),
    ("Weltweite Sprichwörter & literarische Ursprünge", 2, (3,10)),
    # ⚑ einfache Kategorie
    ("Weltzitate – Basis (Zitat dem Kulturkreis zuordnen)", 2, (1,9)),

    # 6 Intermediale Adaptionen
    ("Berühmte Figuren in Film & Theater-Adaptionen", 3, (5,10)),
    ("Zitate in Popkultur & Musik (Allusionen, Hommagen)", 2, (3,10)),
    ("Ikonische Monologe & Szenen", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Adaptionen – Basis (Werk–Medium–Zitat erkennen)", 2, (1,9)),

    # 7 Themen & Motive hinter Zitaten
    ("Leben, Tod, Liebe – zentrale Motive der Weltliteratur", 3, (1,10)),
    ("Freiheit, Macht & Identität in Zitaten", 3, (5,10)),
    ("Zynismus, Humor & Satire in Sprache & Figurenrede", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Motive – Basis (Thema & Zitat verbinden)", 2, (1,9)),

    # 8 Metazitate & Selbstreflexion
    ("Zitate über das Schreiben & Lesen selbst", 3, (5,10)),
    ("Autorenkommentare & Paratexte (Vorreden, Briefe, Essays)", 2, (5,10)),
    ("Ironische Selbstzitate & Selbstparodien", 2, (7,10)),
    # ⚑ einfache Kategorie
    ("Metazitate – Basis (Selbstreferenzen erkennen)", 2, (1,9)),

    # 9 Vergleichende & spielerische Formen
    ("Zitate-Rätsel: ähnlich lautende Passagen aus verschiedenen Werken", 2, (7,10)),
    ("Figuren-Cluster: Wer gehört zu wem? (z. B. Familien, Gegenspieler, Liebespaare)", 2, (3,10)),
    ("Crossover & Anachronismen (Parodien, Mashups, Popkultur)", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Vergleich – Basis (Werkfamilien & Paare zuordnen)", 2, (1,9)),

    # 10 Allgemeinwissen & Trivia
    ("Literarische Preise, Spitznamen & Anekdoten", 2, (1,10)),
    ("Autoren in Zitaten (Selbst- und Fremdzitate)", 2, (3,10)),
    ("Bekannte Fehlzuschreibungen & Irrtümer", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Trivia – Basis (Zitat oder Figur dem Autor zuordnen)", 2, (1,9)),
]
