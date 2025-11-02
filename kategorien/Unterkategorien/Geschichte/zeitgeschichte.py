# -*- coding: utf-8 -*- 
# Unterkategorien/Geschichte/zeitgeschichte.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Zeitgeschichte“.
Diese Liste wird von kategorien/geschichte.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
"""

SUBDISCIPLINES = [
    # 1 Definition, Quellen & Methodik
    ("Zeitgeschichte: Begriff, Abgrenzung & Methodik", 7, (5,10)),
    ("Zeithistorische Quellen & Oral History", 7, (7,10)),
    ("Zeitzeugenarbeit & Erinnerungskultur", 5, (5,10)),
    ("Medien, Öffentlichkeit & Geschichtspolitik", 5, (5,10)),
    ("Historische Sozialforschung & Digital Humanities", 3, (7,10)),
    ("Basis – Zeitgeschichte (Definition, Methoden, Quellenarten)", 3, (1,10)),

    # 2 Zweiter Weltkrieg & seine Folgen
    ("Zweiter Weltkrieg (1939–1945): Gesamtüberblick", 7, (3,10)),
    ("Kriegsverlauf in Europa, Asien & Afrika", 5, (5,10)),
    ("Holocaust & nationalsozialistische Verbrechen", 7, (5,10)),
    ("Kriegsende, Kapitulation & Nachkriegsordnung", 7, (5,10)),
    ("Flucht, Vertreibung & Neuanfang", 5, (5,10)),
    ("Wiederaufbau & Besatzungszonen", 5, (5,10)),
    ("Basis – Zweiter Weltkrieg (Daten, Orte, Akteure)", 3, (1,10)),

    # 3 Deutschland nach 1945
    ("Gründung von BRD & DDR (1949)", 7, (5,10)),
    ("Politische Systeme: Demokratie & Sozialismus", 7, (5,10)),
    ("Wirtschaftswunder & soziale Marktwirtschaft", 7, (3,10)),
    ("Sowjetische Besatzungszone & SED-Herrschaft", 5, (5,10)),
    ("Berlin-Frage & Mauerbau", 7, (3,10)),
    ("Kalter Krieg im geteilten Deutschland", 7, (5,10)),
    ("Opposition & Bürgerrechtsbewegung in der DDR", 5, (5,10)),
    ("Wiedervereinigung 1989/90", 7, (3,10)),
    ("Transformation & Erinnerung an die DDR", 5, (5,10)),
    ("Basis – Nachkriegsdeutschland (Daten, Personen, Ereignisse)", 3, (1,10)),

    # 4 Kalter Krieg & Weltpolitik 1945–1990
    ("Kalter Krieg: globale Struktur & Bipolarität", 7, (5,10)),
    ("Marshallplan & Wiederaufbau Westeuropas", 5, (5,10)),
    ("Koreakrieg, Vietnamkrieg & Stellvertreterkonflikte", 7, (5,10)),
    ("Kuba-Krise & Atomare Abschreckung", 5, (5,10)),
    ("Entspannungspolitik & KSZE-Prozess", 5, (5,10)),
    ("UNO, NATO, Warschauer Pakt", 5, (5,10)),
    ("Ende des Kalten Krieges & Zusammenbruch der UdSSR", 7, (5,10)),
    ("Basis – Kalter Krieg (Blöcke, Begriffe, Konflikte)", 3, (1,10)),

    # 5 Dekolonisation & Dritte Welt
    ("Dekolonisation in Asien & Afrika", 7, (5,10)),
    ("Indien, Algerien, Kongo & Vietnam", 5, (5,10)),
    ("Blockfreie Bewegung & Bandung-Konferenz", 5, (5,10)),
    ("Entwicklungspolitik & Nord-Süd-Konflikt", 5, (5,10)),
    ("Postkoloniale Perspektiven", 3, (7,10)),
    ("Basis – Dekolonisation (Orte, Personen, Daten)", 3, (1,10)),

    # 6 Gesellschaft & Kultur nach 1945
    ("Sozialstaat & Konsumgesellschaft", 7, (3,10)),
    ("68er-Bewegung & neue soziale Bewegungen", 7, (5,10)),
    ("Frauenbewegung & Geschlechterrollenwandel", 5, (5,10)),
    ("Bildungsreformen & Bildungsexpansion", 5, (5,10)),
    ("Jugendkulturen & Populärkultur", 5, (3,10)),
    ("Religion, Säkularisierung & Wertewandel", 5, (5,10)),
    ("Migration & Multikulturalität", 7, (5,10)),
    ("Gesundheitsgeschichte & Biopolitik", 3, (5,10)),
    ("Basis – Gesellschaft/Kultur (Stile, Proteste, Werte)", 3, (1,10)),

    # 7 Internationale Ordnung & Globalisierung (seit 1990)
    ("Globalisierung: Ökonomie, Kommunikation, Mobilität", 7, (5,10)),
    ("Europäische Integration (Maastricht, EU-Erweiterung)", 7, (5,10)),
    ("USA als Hegemon & Globalpolitik nach 1991", 5, (5,10)),
    ("Kriege im Nahen Osten & Terrorismus", 7, (5,10)),
    ("9/11 & ‚Krieg gegen den Terror‘", 7, (5,10)),
    ("China, Russland & neue Großmachtkonflikte", 5, (5,10)),
    ("Internationale Organisationen (UNO, WTO, WHO)", 5, (5,10)),
    ("Flucht, Migration & geopolitische Krisen", 5, (5,10)),
    ("Basis – Globalisierung & Weltordnung (Akteure, Begriffe)", 3, (1,10)),

    # 8 Umwelt, Technik & Wissenschaft
    ("Atomzeitalter & Kernenergie", 5, (5,10)),
    ("Raumfahrt & Wissenschaftswettlauf", 5, (5,10)),
    ("Technologische Revolution (Computer, Internet)", 7, (5,10)),
    ("Umweltbewegung & Klimawandel", 7, (5,10)),
    ("Ernährung, Medizin & Biotechnologie", 5, (5,10)),
    ("Energiekrisen & Nachhaltigkeit", 5, (5,10)),
    ("Basis – Umwelt & Technik (Erfindungen, Bewegungen, Krisen)", 3, (1,10)),

    # 9 Erinnerung, Medien & politische Kultur
    ("Vergangenheitsbewältigung & Erinnerungskultur", 7, (5,10)),
    ("Gedenkstätten, Denkmäler & Musealisierung", 5, (5,10)),
    ("Medienwandel: Fernsehen, Internet, Social Media", 7, (3,10)),
    ("Politische Kommunikation & Fake News", 5, (5,10)),
    ("Geschichtspolitik & kollektives Gedächtnis", 7, (5,10)),
    ("Basis – Erinnerung & Medien (Begriffe, Akteure, Prozesse)", 3, (1,10)),

    # 10 Zeitgeschichte im 21. Jahrhundert
    ("Finanzkrise 2008 & Eurokrise", 7, (5,10)),
    ("Arabischer Frühling & autoritäre Regime", 5, (5,10)),
    ("Klimakrise & Fridays for Future", 5, (5,10)),
    ("COVID-19-Pandemie & Gesellschaft", 7, (5,10)),
    ("Krieg in der Ukraine (ab 2022)", 7, (5,10)),
    ("Künstliche Intelligenz & digitale Transformation", 5, (5,10)),
    ("Polarisierung & Populismus", 5, (5,10)),
    ("Globale Zukunftsfragen & Szenarien", 3, (5,10)),
    ("Basis – Zeitgeschichte aktuell (Krisen, Konflikte, Trends)", 3, (1,10)),
]
