# -*- coding: utf-8 -*-
# Unterkategorien/KunstLiteratur/epochen_stroemungen.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Epochen & Strömungen“.
Diese Liste wird von kategorien/kunst_literatur.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Ein konsistentes System zur Einteilung von Kunst- und Literaturfragen nach
Epochen, Stilen und Strömungen. Jede Kategorie ist mit einem Schwierigkeits-
intervall (1–10) versehen, das sowohl Bekanntheit als auch inhaltliche Tiefe
abbildet.

B. Skala (1–10) – Bedeutung
---------------------------
1 = Basiswissen (breit bekannt)  
5 = mittlere Komplexität  
10 = Expertenniveau (theoretisch, stilistisch, vergleichend)

C. Zwei Achsen
--------------
1) Bekanntheit in der Allgemeinbevölkerung  
2) Komplexität und notwendige Fachkenntnis  

D. Zielbereich dieser Datei
---------------------------
Dieses Modul behandelt **Epochen, Stile und geistige Bewegungen** in der Kunst-
und Literaturgeschichte. Es dient als verbindende Ebene zwischen 
„Kunstgeschichte & Epochen“ (bildende Kunst) und „Klassische Werke & Autoren“
(Literatur), um übergreifende Fragen zu historischen, stilistischen und
ästhetischen Zusammenhängen zu ermöglichen.
"""

# Schwierigkeits-Skala kurz (zur Laufzeit nutzbar):
# 1=Allgemeinwissen … 10=schwerstmöglich.

SUBDISCIPLINES = [
    # 1 Frühformen & Antike
    ("Antike Klassik & Humanismus-Idee (Griechenland, Rom)", 4, (3,10)),
    ("Mittelalterliche Weltbilder & religiöse Kunst/Literatur", 3, (3,10)),
    ("Renaissance: Wiedergeburt der Antike & Perspektive des Menschen", 4, (1,10)),
    ("Barock: Pathos, Symbolik & Gegenreformation", 4, (3,10)),
    ("Rokoko & Empfindsamkeit – Übergang zum Klassizismus", 3, (5,10)),
    # ⚑ einfache Kategorie
    ("Frühformen – Basis (Renaissance/Barock zuordnen)", 2, (1,10)),

    # 2 Aufklärung bis Klassik
    ("Aufklärung: Vernunft, Fortschritt, Satire", 4, (3,10)),
    ("Weimarer Klassik & Humanismus-Ideal", 4, (1,10)),
    ("Empfindsamkeit & Sturm und Drang", 4, (3,10)),
    # ⚑ einfache Kategorie
    ("Aufklärung/Klassik – Basis (Autoren, Werke, Stilmerkmale)", 2, (1,10)),

    # 3 Romantik & 19. Jahrhundert
    ("Romantik: Gefühl, Natur, Innerlichkeit", 4, (1,10)),
    ("Biedermeier & Vormärz – politische Literatur & Bürgerlichkeit", 3, (5,10)),
    ("Realismus & Naturalismus – Wirklichkeit & Gesellschaft", 3, (3,10)),
    ("Symbolismus & Ästhetizismus – Kunst um der Kunst willen", 3, (5,10)),
    # ⚑ einfache Kategorie
    ("19. Jh. – Basis (Romantik vs. Realismus erkennen)", 2, (1,10)),

    # 4 Moderne & Avantgarde (20. Jh.)
    ("Expressionismus (Kunst & Literatur)", 4, (3,10)),
    ("Futurismus, Dadaismus & Surrealismus", 4, (5,10)),
    ("Neue Sachlichkeit & Verismus", 3, (5,10)),
    ("Existentialismus & Nachkriegsliteratur", 3, (7,10)),
    ("Moderne & Avantgarde-Bewegungen – Überblick", 3, (5,10)),
    # ⚑ einfache Kategorie
    ("Moderne – Basis (Stilrichtungen & Leitfiguren zuordnen)", 2, (1,10)),

    # 5 Zeitgenössische Strömungen
    ("Postmoderne & Dekonstruktion", 3, (7,10)),
    ("Pop Art & Konzeptkunst", 3, (5,10)),
    ("Minimal Art, Fluxus, Performance", 3, (7,10)),
    ("Digitale Kunst & Medienästhetik", 2, (5,10)),
    ("Globalisierung & Diversität in der Gegenwartskunst", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Gegenwart – Basis (Stilbeispiele & Schlüsselbegriffe)", 2, (1,10)),

    # 6 Literatur- & Kunstvergleich nach Epochen
    ("Parallelentwicklungen in Kunst & Literatur (Romantik, Moderne)", 3, (5,10)),
    ("Historischer Kontext: Industrialisierung, Krieg, Gesellschaftswandel", 2, (5,10)),
    ("Interdisziplinäre Einflüsse (Philosophie, Musik, Wissenschaft)", 2, (5,10)),
    ("Epochenübergänge & Hybridformen (z. B. Symbolismus–Jugendstil)", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Vergleich – Basis (Epoche den Merkmalen zuordnen)", 2, (1,10)),

    # 7 Theorien & Stilbegriffe
    ("Stilbegriff & Epocheneinteilung – Problemgeschichte", 3, (7,10)),
    ("Zeitgeist & Kunstverständnis: von Mimesis zu Konzept", 3, (7,10)),
    ("Manifeste & Programme (Avantgarden, Gruppen, Schulen)", 2, (5,10)),
    ("Rezeption & Kanonbildung (nach Epochen)", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Stiltheorie – Basis (Begriffe & Schlagwörter erkennen)", 2, (1,10)),
]
