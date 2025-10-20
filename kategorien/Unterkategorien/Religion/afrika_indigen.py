# -*- coding: utf-8 -*-
# Unterkategorien/Religion/afrika_indigen.py
"""
Unterthemen (Subdisciplines) für die Disziplin
„Afrikanische & indigene Religionen“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte
"""

SUBDISCIPLINES = [
    # 1 Überblick & Grundlagen
    ("Afrikanische & indigene Religionen: Überblick & Merkmale", 4),
    ("Oralität, Ahnenverehrung & Ritualpraxis", 4),
    ("Gemeinschaftsorientierte Religiosität & Weltbild", 3),
    ("Animismus, Magie & spirituelle Vermittlerfiguren", 3),
    ("Naturgeister, Totemismus & Schöpfungsmythen", 3),

    # 2 Afrika südlich der Sahara
    ("Westafrika: Yoruba-Religion & Orisha-Pantheon", 4),
    ("Ifa-Orakel & Ritualsystem der Yoruba", 3),
    ("Akan-Religion (Nyame, Asase Yaa)", 3),
    ("Igbo & Dualismus von Ala und Chukwu", 2),
    ("Zulu- & Bantu-Religionen (Ahnenkult, Heilerwesen)", 3),
    ("San- & Khoisan-Spiritualität", 2),
    ("Religiöse Musik, Tanz & Trommelrituale", 2),

    # 3 Nord- & Ostafrika
    ("Nubische & äthiopische Religionstraditionen (vorchristlich)", 3),
    ("Kuschitische und nilotische Glaubenssysteme", 2),
    ("Synkretismus in Äthiopien (jüdisch-christlich-indigen)", 2),
    ("Berberische Kulte & Oasenreligionen", 2),

    # 4 Afrikanische Diaspora & synkretistische Religionen
    ("Afroamerikanische Religionen: Voodoo, Santería, Candomblé", 4),
    ("Vermischung afrikanischer & christlicher Elemente", 4),
    ("Ahnengeister & Besessenheitskult", 3),
    ("Haitianischer Voodoo: Loa-Pantheon", 3),
    ("Brasilianischer Candomblé & Umbanda", 3),
    ("Kubanische Santería & Orishas", 3),
    ("Karibische Religionsformen & koloniale Einflüsse", 2),

    # 5 Indigene Religionen Amerikas
    ("Nordamerikanische Ureinwohner: Geisterwelt & Schöpfungsmythen", 4),
    ("Peyote-Kult & Native American Church", 3),
    ("Südamerika: Andine Religionen (Inka, Pachamama, Inti)", 4),
    ("Amazonasgebiet: Schamanismus & Pflanzenrituale (Ayahuasca)", 3),
    ("Maya- & Azteken-Religion: Götter, Opfer & Kosmos", 4),
    ("Mexica & Sonnenkult (Huitzilopochtli, Quetzalcoatl)", 3),
    ("Olmeken & präkolumbische Grundlagen", 2),

    # 6 Indigene Religionen Ozeaniens & Australiens
    ("Aborigines: Traumzeit (Dreamtime) & Schöpfungserzählungen", 4),
    ("Ahnenlandschaften & Songlines", 3),
    ("Melanesische & polynesische Religionen (Mana, Tabu, Ahnen)", 4),
    ("Totems, Masken & Initiationsrituale im Pazifikraum", 3),
    ("Südseegötter & koloniale Begegnungen", 2),

    # 7 Vergleichende Aspekte
    ("Ahnenverehrung & Schöpfungsmythen im Vergleich", 3),
    ("Rolle des Schamanen & spiritueller Spezialisten", 4),
    ("Ekstase, Tanz & Körperpraktiken", 3),
    ("Synkretismus & Kolonialisierungseinflüsse", 4),
    ("Mündliche Überlieferung & Mythenerzählung", 3),
    ("Symbolik: Tiermotive, Masken, Naturzeichen", 2),

    # 8 Moderne Entwicklungen
    ("Afrikanische unabhängige Kirchen & Prophetentum", 3),
    ("Neotraditionalistische Bewegungen & Kulturen der Diaspora", 3),
    ("Kulturelle Wiederbelebung indigener Religionen", 3),
    ("Tourismus, Globalisierung & spirituelle Aneignung", 2),
]
