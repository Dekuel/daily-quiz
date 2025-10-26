# -*- coding: utf-8 -*-
# Unterkategorien/Religion/afrika_indigen.py
"""
Unterthemen (Subdisciplines) für die Disziplin
„Afrikanische & indigene Religionen“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Einheitliche Skala & Struktur
==========================================================================
Systematik wie in monotheismus.py:
- min = Bekanntheit (Population Familiarity)
- max = inhaltliche Tiefe / methodische Komplexität
- 1 = Allgemeinwissen, 10 = Expertenwissen
- „Basis…“-Kategorien erlauben Level-1-Fragen (Zuordnung, Symbole, einfache Namen)
- Alle Nicht-Basis-Kategorien können bis 10 reichen.
"""

SUBDISCIPLINES = [
    # 1 Überblick & Grundlagen
    ("Afrikanische & indigene Religionen: Überblick & Merkmale", 4, (3,10)),
    ("Oralität, Ahnenverehrung & Ritualpraxis", 4, (3,10)),
    ("Gemeinschaftsorientierte Religiosität & Weltbild", 3, (4,10)),
    ("Animismus, Magie & spirituelle Vermittlerfiguren", 3, (4,10)),
    ("Naturgeister, Totemismus & Schöpfungsmythen", 3, (3,10)),
    # ⚑ Basis
    ("Basiswissen – Afrika & indigene Religionen (Begriffe, Orte, Symbole)", 2, (1,7)),

    # 2 Afrika südlich der Sahara
    ("Westafrika: Yoruba-Religion & Orisha-Pantheon", 4, (4,10)),
    ("Ifa-Orakel & Ritualsystem der Yoruba", 3, (7,10)),
    ("Akan-Religion (Nyame, Asase Yaa)", 3, (6,10)),
    ("Igbo & Dualismus von Ala und Chukwu", 3, (6,10)),
    ("Zulu- & Bantu-Religionen (Ahnenkult, Heilerwesen)", 3, (4,10)),
    ("San- & Khoisan-Spiritualität", 2, (5,10)),
    ("Religiöse Musik, Tanz & Trommelrituale", 2, (2,9)),
    # ⚑ Basis
    ("Subsahara – Basis (Götter, Masken, Trommeln, Regionen)", 2, (1,7)),

    # 3 Nord- & Ostafrika
    ("Nubische & äthiopische Religionstraditionen (vorchristlich)", 3, (6,10)),
    ("Kuschitische & nilotische Glaubenssysteme", 3, (7,10)),
    ("Synkretismus in Äthiopien (jüdisch-christlich-indigen)", 3, (7,10)),
    ("Berberische Kulte & Oasenreligionen", 2, (6,10)),
    # ⚑ Basis
    ("Nord-/Ostafrika – Basis (Orte, Symbole, Gottheiten)", 2, (1,7)),

    # 4 Afrikanische Diaspora & synkretistische Religionen
    ("Afroamerikanische Religionen: Voodoo, Santería, Candomblé", 4, (4,10)),
    ("Vermischung afrikanischer & christlicher Elemente", 4, (4,10)),
    ("Ahnengeister & Besessenheitskult", 3, (5,10)),
    ("Haitianischer Voodoo: Loa-Pantheon", 3, (5,10)),
    ("Brasilianischer Candomblé & Umbanda", 3, (5,10)),
    ("Kubanische Santería & Orishas", 3, (5,10)),
    ("Karibische Religionsformen & koloniale Einflüsse", 2, (4,10)),
    # ⚑ Basis
    ("Diaspora – Basis (Regionen, Hauptgötter, Rituale)", 2, (1,7)),

    # 5 Indigene Religionen Amerikas
    ("Nordamerikanische Ureinwohner: Geisterwelt & Schöpfungsmythen", 4, (3,10)),
    ("Peyote-Kult & Native American Church", 3, (7,10)),
    ("Südamerika: Andine Religionen (Inka, Pachamama, Inti)", 4, (4,10)),
    ("Amazonasgebiet: Schamanismus & Pflanzenrituale (Ayahuasca)", 3, (6,10)),
    ("Maya- & Azteken-Religion: Götter, Opfer & Kosmos", 4, (4,10)),
    ("Mexica & Sonnenkult (Huitzilopochtli, Quetzalcoatl)", 3, (5,10)),
    ("Olmeken & präkolumbische Grundlagen", 2, (5,10)),
    # ⚑ Basis
    ("Amerikas – Basis (Völker, Symbole, Rituale, Orte)", 2, (1,7)),

    # 6 Indigene Religionen Ozeaniens & Australiens
    ("Aborigines: Traumzeit (Dreamtime) & Schöpfungserzählungen", 4, (6,10)),
    ("Ahnenlandschaften & Songlines", 3, (7,10)),
    ("Melanesische & polynesische Religionen (Mana, Tabu, Ahnen)", 4, (5,10)),
    ("Totems, Masken & Initiationsrituale im Pazifikraum", 3, (4,10)),
    ("Südseegötter & koloniale Begegnungen", 2, (4,10)),
    # ⚑ Basis
    ("Ozeanien/Australien – Basis (Begriffe, Rituale, Symbole)", 2, (1,7)),

    # 7 Vergleichende Aspekte
    ("Ahnenverehrung & Schöpfungsmythen im Vergleich", 3, (4,10)),
    ("Rolle des Schamanen & spiritueller Spezialisten", 4, (5,10)),
    ("Ekstase, Tanz & Körperpraktiken", 3, (3,9)),
    ("Synkretismus & Kolonialisierungseinflüsse", 4, (6,10)),
    ("Mündliche Überlieferung & Mythenerzählung", 3, (3,9)),
    ("Symbolik: Tiermotive, Masken, Naturzeichen", 2, (2,9)),
    # ⚑ Basis
    ("Vergleich – Basis (Symbole, Praktiken, Regionen)", 2, (1,7)),

    # 8 Moderne Entwicklungen
    ("Afrikanische unabhängige Kirchen & Prophetentum", 3, (4,10)),
    ("Neotraditionalistische Bewegungen & Kulturen der Diaspora", 3, (5,10)),
    ("Kulturelle Wiederbelebung indigener Religionen", 3, (4,10)),
    ("Tourismus, Globalisierung & spirituelle Aneignung", 2, (4,10)),
    # ⚑ Basis
    ("Moderne Entwicklungen – Basis (Beispiele, Bewegungen, Begriffe)", 2, (1,7)),
]
