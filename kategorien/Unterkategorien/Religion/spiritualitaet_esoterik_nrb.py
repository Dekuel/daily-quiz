# -*- coding: utf-8 -*-
# Unterkategorien/Religion/spiritualitaet_esoterik_nrb.py
"""
Unterthemen (Subdisciplines) für die Disziplin
„Spiritualität, Esoterik & neue religiöse Bewegungen (NRB)“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================
Dieses Modul folgt demselben System wie in monotheismus.py beschrieben.

1–10 = Schwierigkeitsstufen:
1 = Allgemeinwissen / 10 = Expertenwissen.
Zwei Achsen bestimmen das Intervall:
Bekanntheit (min) und Komplexität (max).

Alle Nicht-Basis-Themen reichen grundsätzlich bis 10, 
da die Domäne theoretisch immer vertiefbar ist.
"""

SUBDISCIPLINES = [
    # 1 Grundlagen & Begriffe
    ("Spiritualität: Begriff, Formen & Abgrenzung zu Religion", 4, (2,10)),
    ("Esoterik & Okkultismus: historische Entwicklung & Leitmotive", 4, (3,10)),
    ("Mystik, Magie & symbolisches Denken", 3, (4,10)),
    ("Gnosis & Geheimwissen in der Religionsgeschichte", 3, (5,10)),
    ("Ritual, Initiation & Selbsterkenntnis", 3, (4,10)),
    # ⚑ Basis
    ("Basiswissen Spiritualität/Esoterik – Zuordnungen & Begriffe (Symbole, Praktiken, Orte)", 2, (1,7)),
    ("Verbreitung & Soziodemografie (zeitabhängig; Stand/Quelle angeben)", 2, (1,8)),

    # 2 Antike & abendländische Esoteriktraditionen
    ("Hermetik & Hermetische Schriften (Corpus Hermeticum)", 4, (5,10)),
    ("Alchemie: Stoff- & Geistestransformation, Allegorien", 3, (5,10)),
    ("Astrologie & Sternendeutung im religiösen Kontext", 3, (3,10)),
    ("Kabbala & christliche Esoterik", 3, (6,10)),
    ("Rosenkreuzer & Geheimbünde der Frühen Neuzeit", 3, (5,10)),
    ("Freimaurerei: Symbole, Philosophie & Geschichte", 3, (3,10)),
    ("Theosophie & Anthroposophie (Blavatsky, Steiner)", 4, (4,10)),
    # ⚑ Basis
    ("Abendländische Esoterik – Basisfakten (Begriffe, Symbole, Akteure)", 2, (1,7)),

    # 3 Volksglaube & Magische Praxis
    ("Volksreligion & Aberglaube in Europa", 3, (3,10)),
    ("Hexenglaube, Inquisition & Volksmagie", 4, (3,10)),
    ("Orakel, Wahrsagung & Tarot", 3, (2,9)),
    ("Amulette, Talismane & Schutzmagie", 2, (1,8)),
    ("Spiritismus & Séancen (19. Jh.)", 3, (4,10)),
    ("Schwarze & weiße Magie – kulturelle Deutungen", 2, (3,9)),
    # ⚑ Basis
    ("Volksglaube & Magie – Basis (Zuordnungen, Begriffe, Objekte)", 2, (1,7)),

    # 4 Moderne Esoterik & Okkultismus (19./20. Jh.)
    ("Okkulte Bewegungen des 19./20. Jahrhunderts (Überblick)", 3, (4,10)),
    ("Aleister Crowley & Thelema", 3, (6,10)),
    ("Esoterische Orden (Hermetic Order of the Golden Dawn, O.T.O.)", 3, (5,10)),
    ("Astrologie, Numerologie & Hermetische Künste (moderne Rezeption)", 2, (3,9)),
    ("Satanismus: Strömungen, Selbstbeschreibungen & populäre Missverständnisse", 2, (4,9)),
    # ⚑ Basis
    ("Moderne Okkultismen – Basisfakten (Gruppen, Texte, Symbole)", 2, (1,7)),

    # 5 New Age & moderne Spiritualität (seit 1960er)
    ("New Age: Ursprung, Ideen & Vertreter", 4, (3,10)),
    ("Bewusstseinswandel & Ganzheitsdenken (1960er–heute)", 3, (4,10)),
    ("Meditation, Energiearbeit & Heilsteine (Praxisfelder)", 3, (2,9)),
    ("Karma, Reinkarnation & spirituelle Selbsthilfe", 3, (3,9)),
    ("Channeling, Engelskult & ‚Aufgestiegene Meister‘", 2, (3,9)),
    ("Synkretismus: Kombination östlicher & westlicher Elemente", 3, (4,10)),
    ("Pseudowissenschaft, Evidenzfragen & Esoterikmarkt", 2, (4,9)),
    # ⚑ Basis
    ("New Age & moderne Spiritualität – Basis (Begriffe, Praktiken, Ikonen)", 2, (1,7)),

    # 6 Neue religiöse Bewegungen (NRB)
    ("NRB: Definitionen, Forschungsansätze & Typologien", 4, (4,10)),
    ("Gruppenporträts (Scientology, Hare Krishna, Zeugen Jehovas u. a.)", 4, (3,10)),
    ("Neue christliche Gruppen & Pfingstbewegungen (20./21. Jh.)", 3, (3,10)),
    ("Osho-Bewegung & alternative Lebensgemeinschaften", 3, (4,10)),
    ("Apokalyptische Bewegungen & Endzeitglaube", 3, (4,10)),
    ("Kulte? Sekten? – soziologische, rechtliche & begriffliche Perspektiven", 3, (6,10)),
    ("Spirituelle Gurus & Charismatiker (Autorität, Leitung, Dynamiken)", 3, (4,10)),
    # ⚑ Basis
    ("NRB – Basisfakten (Selbstbezeichnungen, Gründungsdaten, Schlüsselpraktiken)", 2, (1,7)),

    # 7 Schamanismus & Naturspiritualität
    ("Schamanismus: Ursprung, Techniken (Trance, Reise) & Weltbild", 4, (3,10)),
    ("Ekstase, Trommel & Trance als rituelle Mittel", 3, (3,10)),
    ("Naturreligionen & Erdspiritualität (Animismus, Ahnenkult)", 3, (3,10)),
    ("Neoschamanismus & moderne Adaptionen", 2, (3,9)),
    ("Pflanzenrituale & psychoaktive Substanzen (Kontexte & Deutungen)", 2, (4,10)),
    ("Tiere, Elemente & Geister in spirituellen Symbolsystemen", 2, (2,9)),
    # ⚑ Basis
    ("Schamanismus/Naturspiritualität – Basis (Begriffe, Instrumente, Rollen)", 2, (1,7)),

    # 8 Feminine & ökologische Spiritualität
    ("Göttinnenbewegung & Wicca (Geschichte, Theologie, Praxis)", 4, (3,10)),
    ("Hexenkult & Neo-Paganismus (Moderne Rekonstruktionen)", 4, (3,10)),
    ("Ökospiritualität & Gaia-Hypothese", 3, (4,10)),
    ("Körper, Sexualität & Sakralität in spirituellen Konzepten", 3, (4,10)),
    ("Feministische Spiritualität & Matriarchatsmythen", 3, (5,10)),
    # ⚑ Basis
    ("Feminine/ökologische Spiritualität – Basis (Symbole, Rituale, Jahreskreis)", 2, (1,7)),

    # 9 Esoterik, Psychologie & Wissenschaft
    ("Psychologische Deutungen spiritueller Erfahrung (z. B. C. G. Jung, Assagioli)", 4, (6,10)),
    ("Esoterik & Tiefen-/Transpersonale Psychologie", 4, (9,10)),
    ("Bewusstseinserweiterung: Modelle, Methoden, Debatten", 3, (7,10)),
    ("Wissenschaft, Skepsis & Esoterikkritik (Methoden, Evidenz, Biases)", 3, (5,10)),
    ("Placebo, Heilung & Glaube (Wirkfaktoren, Rituale, Setting)", 2, (4,10)),
    # ⚑ Basis
    ("Psychologie & Esoterik – Basisbegriffe (Archetypen, Selbst, Transpersonal)", 2, (1,8)),

    # 10 Gegenwart & Gesellschaft
    ("Esoterik im Internet & sozialen Medien (Memetik, Influencing)", 3, (4,10)),
    ("Kommerzialisierung von Spiritualität (Wellness, Coaching, Retreats)", 3, (4,10)),
    ("Verschwörungsdenken, Esoterik & moderner Synkretismus", 3, (5,10)),
    ("Interreligiöse Spiritualität & Weltethos-Ansätze", 3, (4,10)),
    ("Spiritualität ohne Religion – Individualisierung & ‚Believing without Belonging‘", 4, (3,10)),
    # ⚑ Basis
    ("Gegenwart – Basis (Begriffe, Trends, Formate)", 2, (1,7)),
]
