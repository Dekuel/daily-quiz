# -*- coding: utf-8 -*-
# Unterkategorien/Religion/spiritualitaet_esoterik_nrb.py
"""
Unterthemen (Subdisciplines) für die Disziplin
„Spiritualität, Esoterik & neue religiöse Bewegungen“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte
"""

SUBDISCIPLINES = [
    # 1 Grundlagen & Begriffe
    ("Spiritualität: Begriff, Formen & Abgrenzung zu Religion", 4),
    ("Esoterik & Okkultismus: historische Entwicklung", 4),
    ("Mystik, Magie & symbolisches Denken", 3),
    ("Gnosis & Geheimwissen in der Religionsgeschichte", 3),
    ("Ritual, Initiation & Selbsterkenntnis", 3),

    # 2 Antike & abendländische Esoteriktraditionen
    ("Hermetik & Hermetische Schriften (Corpus Hermeticum)", 4),
    ("Alchemie & Transformation des Geistes", 3),
    ("Astrologie & Sternendeutung in religiösem Kontext", 3),
    ("Kabbala & christliche Esoterik", 3),
    ("Rosenkreuzer & Geheimbünde der Frühen Neuzeit", 3),
    ("Freimaurerei: Symbole, Philosophie & Geschichte", 3),
    ("Theosophie & Anthroposophie (Blavatsky, Steiner)", 4),

    # 3 Volksglaube & Magische Praxis
    ("Volksreligion & Aberglaube in Europa", 3),
    ("Hexenglaube, Inquisition & Volksmagie", 4),
    ("Orakel, Wahrsagung & Tarot", 3),
    ("Amulette, Talismane & Schutzmagie", 2),
    ("Spiritismus & Séancen (19. Jh.)", 3),
    ("Schwarze & weiße Magie – kulturelle Deutungen", 2),

    # 4 Moderne Esoterik & Okkultismus
    ("Okkulte Bewegungen des 19./20. Jahrhunderts", 3),
    ("Aleister Crowley & Thelema", 3),
    ("Esoterische Orden (Golden Dawn, O.T.O.)", 3),
    ("Astrologie, Numerologie & Hermetische Künste", 2),
    ("Satanismus & seine kulturellen Missverständnisse", 2),

    # 5 New Age & moderne Spiritualität
    ("New Age: Ursprung, Ideen & Vertreter", 4),
    ("Bewusstseinswandel & Ganzheitsdenken (1960er–heute)", 3),
    ("Meditation, Energiearbeit & Heilsteine", 3),
    ("Karma, Reinkarnation & spirituelle Selbsthilfe", 3),
    ("Channeling & Engelskult", 2),
    ("Kombination östlicher & westlicher Esoterik", 3),
    ("Pseudowissenschaft & Esoterikmarkt", 2),

    # 6 Neue religiöse Bewegungen (NRB)
    ("Neue religiöse Bewegungen: Definition & Forschung", 4),
    ("Scientology, Hare Krishna, Zeugen Jehovas", 4),
    ("Neue christliche Gruppen & Pfingstbewegungen", 3),
    ("Osho-Bewegung & alternative Lebensgemeinschaften", 3),
    ("Apokalyptische Bewegungen & Endzeitglaube", 3),
    ("Kulte & Sektenbegriff – soziologische Perspektive", 3),
    ("Spirituelle Gurus & Charismatiker (20./21. Jh.)", 3),

    # 7 Schamanismus & Naturspiritualität
    ("Schamanismus: Ursprung, Techniken & Weltbild", 4),
    ("Ekstase, Trommel & Trance als rituelle Mittel", 3),
    ("Naturreligionen & Erdspiritualität", 3),
    ("Neoschamanismus & moderne Anpassungen", 2),
    ("Pflanzenrituale & psychoaktive Substanzen", 2),
    ("Tiere, Elemente & Geister in spirituellen Symbolsystemen", 2),

    # 8 Feminine & ökologische Spiritualität
    ("Göttinnenbewegung & Wicca", 4),
    ("Hexenkult & Neo-Paganismus", 4),
    ("Ökospiritualität & Gaia-Hypothese", 3),
    ("Körper, Sexualität & Sakralität in der Spiritualität", 3),
    ("Feministische Spiritualität & Matriarchatsmythen", 3),

    # 9 Esoterik, Psychologie & Wissenschaft
    ("Psychologische Deutungen spiritueller Erfahrung (Jung, Assagioli)", 3),
    ("Esoterik & Tiefenpsychologie", 3),
    ("Bewusstseinserweiterung & Transpersonale Psychologie", 3),
    ("Wissenschaft, Skepsis & Esoterikkritik", 3),
    ("Placebo, Heilung & Glaube", 2),

    # 10 Gegenwart & Gesellschaft
    ("Esoterik im Internet & soziale Medien", 3),
    ("Kommerzialisierung von Spiritualität (Wellness, Coaching)", 3),
    ("Verschwörungsdenken & religiöser Synkretismus", 3),
    ("Interreligiöse Spiritualität & Weltethos", 3),
    ("Spiritualität ohne Religion – Individualisierung des Glaubens", 4),
]
