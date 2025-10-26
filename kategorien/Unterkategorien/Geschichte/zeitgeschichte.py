# -*- coding: utf-8 -*- 
# Unterkategorien/Geschichte/zeitgeschichte.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Zeitgeschichte“.
Diese Liste wird von kategorien/geschichte.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Einheitliche Skala & Struktur
==========================================================================
- Skala 1–10: 1 = Allgemeinwissen, 10 = Expertenwissen
- min = Bekanntheit (Population Familiarity)
- max = inhaltliche/methodische Tiefe (Conceptual Depth)
- „Basis…“-Kategorien haben immer min = 1 (Zuordnung, Namen, einfache Fakten)
- Nicht-Basis-Themen können i. d. R. bis 10 gehen (Vertiefbarkeit durch Forschung)
"""

SUBDISCIPLINES = [
    # 1 Definition, Quellen & Methodik
    ("Zeitgeschichte: Begriff, Abgrenzung & Methodik", 4, (3,10)),
    ("Zeithistorische Quellen & Oral History", 4, (4,10)),
    ("Zeitzeugenarbeit & Erinnerungskultur", 3, (3,10)),
    ("Medien, Öffentlichkeit & Geschichtspolitik", 3, (3,10)),
    ("Historische Sozialforschung & Digital Humanities", 2, (4,10)),
    ("Basis – Zeitgeschichte (Definition, Methoden, Quellenarten)", 2, (1,7)),

    # 2 Zweiter Weltkrieg & seine Folgen
    ("Zweiter Weltkrieg (1939–1945): Gesamtüberblick", 4, (2,10)),
    ("Kriegsverlauf in Europa, Asien & Afrika", 3, (3,10)),
    ("Holocaust & nationalsozialistische Verbrechen", 4, (3,10)),
    ("Kriegsende, Kapitulation & Nachkriegsordnung", 4, (3,10)),
    ("Flucht, Vertreibung & Neuanfang", 3, (3,10)),
    ("Wiederaufbau & Besatzungszonen", 3, (3,10)),
    ("Basis – Zweiter Weltkrieg (Daten, Orte, Akteure)", 2, (1,7)),

    # 3 Deutschland nach 1945
    ("Gründung von BRD & DDR (1949)", 4, (3,10)),
    ("Politische Systeme: Demokratie & Sozialismus", 4, (3,10)),
    ("Wirtschaftswunder & soziale Marktwirtschaft", 4, (2,10)),
    ("Sowjetische Besatzungszone & SED-Herrschaft", 3, (3,10)),
    ("Berlin-Frage & Mauerbau", 4, (2,10)),
    ("Kalter Krieg im geteilten Deutschland", 4, (3,10)),
    ("Opposition & Bürgerrechtsbewegung in der DDR", 3, (3,10)),
    ("Wiedervereinigung 1989/90", 4, (2,10)),
    ("Transformation & Erinnerung an die DDR", 3, (3,10)),
    ("Basis – Nachkriegsdeutschland (Daten, Personen, Ereignisse)", 2, (1,7)),

    # 4 Kalter Krieg & Weltpolitik 1945–1990
    ("Kalter Krieg: globale Struktur & Bipolarität", 4, (3,10)),
    ("Marshallplan & Wiederaufbau Westeuropas", 3, (3,10)),
    ("Koreakrieg, Vietnamkrieg & Stellvertreterkonflikte", 4, (3,10)),
    ("Kuba-Krise & Atomare Abschreckung", 3, (3,10)),
    ("Entspannungspolitik & KSZE-Prozess", 3, (3,10)),
    ("UNO, NATO, Warschauer Pakt", 3, (3,10)),
    ("Ende des Kalten Krieges & Zusammenbruch der UdSSR", 4, (3,10)),
    ("Basis – Kalter Krieg (Blöcke, Begriffe, Konflikte)", 2, (1,7)),

    # 5 Dekolonisation & Dritte Welt
    ("Dekolonisation in Asien & Afrika", 4, (3,10)),
    ("Indien, Algerien, Kongo & Vietnam", 3, (3,10)),
    ("Blockfreie Bewegung & Bandung-Konferenz", 3, (3,10)),
    ("Entwicklungspolitik & Nord-Süd-Konflikt", 3, (3,10)),
    ("Postkoloniale Perspektiven", 2, (4,10)),
    ("Basis – Dekolonisation (Orte, Personen, Daten)", 2, (1,7)),

    # 6 Gesellschaft & Kultur nach 1945
    ("Sozialstaat & Konsumgesellschaft", 4, (2,10)),
    ("68er-Bewegung & neue soziale Bewegungen", 4, (3,10)),
    ("Frauenbewegung & Geschlechterrollenwandel", 3, (3,10)),
    ("Bildungsreformen & Bildungsexpansion", 3, (3,10)),
    ("Jugendkulturen & Populärkultur", 3, (2,9)),
    ("Religion, Säkularisierung & Wertewandel", 3, (3,10)),
    ("Migration & Multikulturalität", 4, (3,10)),
    ("Gesundheitsgeschichte & Biopolitik", 2, (3,9)),
    ("Basis – Gesellschaft/Kultur (Stile, Proteste, Werte)", 2, (1,7)),

    # 7 Internationale Ordnung & Globalisierung (seit 1990)
    ("Globalisierung: Ökonomie, Kommunikation, Mobilität", 4, (3,10)),
    ("Europäische Integration (Maastricht, EU-Erweiterung)", 4, (3,10)),
    ("USA als Hegemon & Globalpolitik nach 1991", 3, (3,10)),
    ("Kriege im Nahen Osten & Terrorismus", 4, (3,10)),
    ("9/11 & ‚Krieg gegen den Terror‘", 4, (3,10)),
    ("China, Russland & neue Großmachtkonflikte", 3, (3,10)),
    ("Internationale Organisationen (UNO, WTO, WHO)", 3, (3,10)),
    ("Flucht, Migration & geopolitische Krisen", 3, (3,10)),
    ("Basis – Globalisierung & Weltordnung (Akteure, Begriffe)", 2, (1,7)),

    # 8 Umwelt, Technik & Wissenschaft
    ("Atomzeitalter & Kernenergie", 3, (3,10)),
    ("Raumfahrt & Wissenschaftswettlauf", 3, (3,10)),
    ("Technologische Revolution (Computer, Internet)", 4, (3,10)),
    ("Umweltbewegung & Klimawandel", 4, (3,10)),
    ("Ernährung, Medizin & Biotechnologie", 3, (3,10)),
    ("Energiekrisen & Nachhaltigkeit", 3, (3,10)),
    ("Basis – Umwelt & Technik (Erfindungen, Bewegungen, Krisen)", 2, (1,7)),

    # 9 Erinnerung, Medien & politische Kultur
    ("Vergangenheitsbewältigung & Erinnerungskultur", 4, (3,10)),
    ("Gedenkstätten, Denkmäler & Musealisierung", 3, (3,10)),
    ("Medienwandel: Fernsehen, Internet, Social Media", 4, (2,10)),
    ("Politische Kommunikation & Fake News", 3, (3,10)),
    ("Geschichtspolitik & kollektives Gedächtnis", 4, (3,10)),
    ("Basis – Erinnerung & Medien (Begriffe, Akteure, Prozesse)", 2, (1,7)),

    # 10 Zeitgeschichte im 21. Jahrhundert
    ("Finanzkrise 2008 & Eurokrise", 4, (3,10)),
    ("Arabischer Frühling & autoritäre Regime", 3, (3,10)),
    ("Klimakrise & Fridays for Future", 3, (3,10)),
    ("COVID-19-Pandemie & Gesellschaft", 4, (3,10)),
    ("Krieg in der Ukraine (ab 2022)", 4, (3,10)),
    ("Künstliche Intelligenz & digitale Transformation", 3, (3,10)),
    ("Polarisierung & Populismus", 3, (3,10)),
    ("Globale Zukunftsfragen & Szenarien", 2, (3,9)),
    ("Basis – Zeitgeschichte aktuell (Krisen, Konflikte, Trends)", 2, (1,7)),
]
