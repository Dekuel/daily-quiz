# -*- coding: utf-8 -*-
# Unterkategorien/KunstLiteratur/kuenstler_bands_hits.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Künstler, Bands & Hits“.
Diese Liste wird von kategorien/kunst_literatur.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================

A. Ziel
-------
Ein strukturierter Überblick über populäre Musikgeschichte, Künstler:innen,
Bands, Songs, Genres und deren kulturelle Bedeutung – von Klassikern bis
zeitgenössischen Strömungen. Ziel ist, Fragen zu Musikgeschichte, Hitkultur
und Popästhetik in unterschiedlichen Schwierigkeitsstufen zu ermöglichen.

B. Skala (1–10) – Bedeutung
---------------------------
1 = populäres Allgemeinwissen (z. B. Beatles, Michael Jackson)  
4–6 = mittleres Wissen (Genres, Ära, Songtitel, typische Instrumentierung)  
9–10 = Expertenwissen (Produzenten, Veröffentlichungsjahre, Kontextanalyse)

C. Struktur
-----------
- Ikonen & Klassiker  
- Bands & Bewegungen  
- Genres & Stilrichtungen  
- Hits & Charts  
- Intermediale & kulturelle Kontexte
"""

# Schwierigkeits-Skala kurz (zur Laufzeit nutzbar):
# 1=Allgemeinwissen … 10=schwerstmöglich.

SUBDISCIPLINES = [
    # 1 Ikonen & Klassiker
    ("Weltweite Pop-Ikonen (Elvis, Beatles, Bowie, Madonna)", 4, (1,10)),
    ("Rock-Legenden & Epochenprägung (Rolling Stones, Queen, Nirvana)", 4, (1,10)),
    ("Soul, Funk & R’n’B (Aretha Franklin, James Brown, Prince)", 3, (3,10)),
    ("Singer-Songwriter & Folk (Dylan, Cohen, Joni Mitchell)", 3, (3,10)),
    ("Jazz- & Blues-Größen (Louis Armstrong, Miles Davis, Billie Holiday)", 3, (3,10)),
    # ⚑ einfache Kategorie
    ("Künstler – Basis (Name, Stilrichtung, berühmtester Song)", 2, (1,9)),

    # 2 Bands & Bewegungen
    ("Britpop & Indie (Oasis, Blur, Arctic Monkeys)", 3, (3,10)),
    ("Punk & Postpunk (Sex Pistols, The Clash, Joy Division)", 3, (3,10)),
    ("Hard Rock & Metal (Led Zeppelin, Metallica, Iron Maiden)", 3, (3,10)),
    ("Reggae & Ska (Bob Marley, Toots, The Specials)", 2, (3,10)),
    ("Hip-Hop & Rap (Tupac, Biggie, Public Enemy, Kendrick Lamar)", 3, (3,10)),
    ("Elektronische Musik & DJ-Kultur (Kraftwerk, Daft Punk, Avicii)", 3, (3,10)),
    ("Boybands & Girlgroups (Spice Girls, BTS, Backstreet Boys)", 2, (1,9)),
    # ⚑ einfache Kategorie
    ("Bands – Basis (Bandname, Herkunft, Jahrzehnt, Genre)", 2, (1,9)),

    # 3 Hits & Klassiker der Musikgeschichte
    ("Welthits der 60er–80er (Yesterday, Imagine, Thriller)", 3, (1,9)),
    ("90er & 2000er Popkultur (Britney Spears, Coldplay, Eminem)", 3, (1,9)),
    ("21. Jahrhundert – globale Charts (Adele, Ed Sheeran, BTS, Billie Eilish)", 2, (1,9)),
    ("Film- & Soundtrack-Klassiker (Titanic, Pulp Fiction, Disney)", 2, (1,9)),
    ("Einflussreiche Alben & Meilensteine (Abbey Road, Thriller, The Dark Side of the Moon)", 3, (3,10)),
    # ⚑ einfache Kategorie
    ("Hits – Basis (Song–Interpret–Dekade zuordnen)", 2, (1,9)),

    # 4 Genres & Stile
    ("Popgeschichte im Überblick (1950–heute)", 4, (3,10)),
    ("Rock, Pop, Jazz, Klassik – stilistische Merkmale", 3, (3,10)),
    ("Hip-Hop, Trap, Drill – Entwicklung & Szene", 3, (5,10)),
    ("Elektronische Musik – House, Techno, EDM", 3, (5,10)),
    ("Alternative, Grunge & Independent-Kultur", 2, (5,10)),
    ("Weltmusik & Crossovers (Afrobeat, Reggaeton, K-Pop)", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Genres – Basis (Stilrichtung & Beispiel zuordnen)", 2, (1,9)),

    # 5 Musiker:innen nach Jahrzehnten
    ("1950er/60er – Rock’n’Roll & Beat", 3, (1,9)),
    ("1970er – Disco, Glam & Progressive Rock", 3, (3,10)),
    ("1980er – Synthpop, New Wave, MTV-Ära", 3, (3,10)),
    ("1990er – Britpop, Alternative, Hip-Hop", 3, (3,10)),
    ("2000er–2010er – Popglobalisierung, Streaming & Internetstars", 2, (3,10)),
    # ⚑ einfache Kategorie
    ("Dekaden – Basis (Stil, Trend, Leitfigur)", 2, (1,9)),

    # 6 Frauen in der Musikgeschichte
    ("Pionierinnen & Stars (Ella Fitzgerald, Janis Joplin, Madonna, Beyoncé)", 3, (3,10)),
    ("Komponistinnen & Produzentinnen im Hintergrund", 2, (5,10)),
    ("Feminismus & Empowerment in Poptexten", 2, (5,10)),
    # ⚑ einfache Kategorie
    ("Musikerinnen – Basis (Name, Epoche, Bedeutung)", 2, (1,9)),

    # 7 Interkulturelle & globale Perspektiven
    ("Lateinamerikanische Musik (Samba, Tango, Reggaeton)", 3, (3,10)),
    ("Afrikanische Rhythmen & Einfluss auf Popmusik", 3, (3,10)),
    ("Asiatische Popkultur (J-Pop, K-Pop, Bollywood)", 2, (3,10)),
    ("Europäische & skandinavische Musikszene", 2, (3,10)),
    # ⚑ einfache Kategorie
    ("Weltmusik – Basis (Stilrichtung, Herkunft, Künstler)", 2, (1,9)),

    # 8 Musikindustrie & Medien
    ("Musiklabels, Charts & Streaming-Plattformen", 2, (5,10)),
    ("Musikvideos & visuelle Inszenierung", 2, (3,10)),
    ("Produzenten & Songwriter (Phil Spector, Quincy Jones, Max Martin)", 3, (5,10)),
    ("Preisverleihungen & Rekorde (Grammy, MTV, Billboard)", 2, (1,9)),
    # ⚑ einfache Kategorie
    ("Industrie – Basis (Label, Preis, Hit)", 2, (1,9)),

    # 9 Text, Botschaft & Wirkung
    ("Protest- & Gesellschaftssongs (Dylan, Marley, Lennon, Rage Against the Machine)", 3, (5,10)),
    ("Liebeslieder & Balladen", 2, (1,9)),
    ("Populäre Themen & Emotionen in Songtexten", 2, (3,10)),
    ("Musik & Politik / Identität", 3, (5,10)),
    # ⚑ einfache Kategorie
    ("Songtexte – Basis (Thema & Song zuordnen)", 2, (1,9)),

    # 10 Vergleich & Querschnitt
    ("Musikepochen vergleichen (Beatles vs. Nirvana vs. Billie Eilish)", 2, (3,10)),
    ("Crossover & Samples (Remix-Kultur, Mashups, Coverversionen)", 2, (5,10)),
    ("Einflüsse zwischen Genres & Generationen", 2, (5,10)),
    ("Musik & Gesellschaft: Trends, Mode, Medien", 2, (3,10)),
    # ⚑ einfache Kategorie
    ("Vergleich – Basis (Song, Künstler, Epoche zuordnen)", 2, (1,9)),
]
