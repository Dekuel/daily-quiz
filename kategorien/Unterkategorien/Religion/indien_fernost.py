# -*- coding: utf-8 -*-
# Unterkategorien/Religion/indien_fernost.py
"""
Unterthemen (Subdisciplines) für „Indische & fernöstliche Religionen“.
Diese Datei folgt dem GENERATION_SYSTEM wie in monotheismus.py:
- min = Bekanntheit (Population Familiarity)
- max = inhaltliche / methodische Tiefe
- 1 = Allgemeinwissen, 10 = Expertenniveau
- Maxima grundsätzlich bis 10
- „Basis…“-Kategorien ermöglichen Level-1-Fragen (Zuordnung, Symbole, einfache Fakten)
"""

SUBDISCIPLINES = [
    # 1 Überblick & Ursprünge
    ("Indische & fernöstliche Religionen: Überblick & Entstehung", 4, (2,10)),
    ("Religiöse Vielfalt Asiens & synkretistische Einflüsse", 3, (5,10)),
    ("Veden & Upanishaden: Grundlagen altindischer Religion", 4, (6,10)),
    ("Samsara, Karma & Moksha – zyklisches Weltbild", 4, (4,10)),
    ("Dharma & soziale Ordnung (Kastensystem, Pflichten)", 3, (5,10)),
    # ⚑ Basis
    ("Basiswissen Asien – Zuordnungen (Religion–Land, Symbole, zentrale Begriffe)", 2, (1,7)),

    # 2 Hinduismus
    ("Hinduismus: Ursprung & Entwicklung", 4, (5,10)),
    ("Heilige Schriften: Veden, Bhagavad Gita, Mahabharata", 4, (4,10)),
    ("Trimurti: Brahma, Vishnu, Shiva", 4, (2,9)),
    ("Devi-Kult & weibliche Gottheiten (Durga, Kali, Lakshmi)", 3, (5,10)),
    ("Rituale, Feste & Pilgerorte (z. B. Kumbh Mela, Diwali)", 3, (2,9)),
    ("Bhakti-Bewegung & religiöse Praxis", 3, (5,10)),
    ("Yoga, Meditation & spirituelle Wege", 3, (2,9)),
    ("Hinduismus in der Moderne & Diaspora", 2, (5,10)),
    # ⚑ Basis
    ("Hinduismus – Basisfakten (Götter, Symbole, Schriften, Feste)", 2, (1,7)),

    # 3 Buddhismus
    ("Buddhismus: Leben des Siddhartha Gautama (Buddha)", 4, (2,9)),
    ("Vier Edle Wahrheiten & Achtfacher Pfad", 4, (2,9)),
    ("Theravada, Mahayana & Vajrayana", 4, (5,10)),
    ("Lehre von der Vergänglichkeit (Anicca) & Nicht-Selbst (Anatta)", 3, (6,10)),
    ("Buddhistische Ethik & Mitgefühl (Karuna)", 3, (5,10)),
    ("Klosterwesen & Sangha", 3, (4,10)),
    ("Verbreitung nach Ost- und Südostasien", 3, (2,9)),
    ("Zen, tibetischer & moderner Buddhismus", 3, (5,10)),
    # ⚑ Basis
    ("Buddhismus – Basis (Begriffe, Symbole, Schulen, Länder)", 2, (1,7)),

    # 4 Jainismus & Sikhismus
    ("Jainismus: Mahavira & Prinzip der Gewaltlosigkeit (Ahimsa)", 4, (7,10)),
    ("Karma-Lehre & asketische Praxis im Jainismus", 3, (8,10)),
    ("Sikhismus: Guru Nanak & die Zehn Gurus", 4, (6,10)),
    ("Heilige Schrift: Guru Granth Sahib", 3, (6,10)),
    ("Khalsa, Symbolik & Rituale der Sikhs", 3, (5,10)),
    # ⚑ Basis
    ("Jainismus & Sikhismus – Basis (Gründer, Symbole, Grundideen)", 2, (1,7)),

    # 5 Chinesische & japanische Traditionen
    ("Konfuzianismus: Ethik, Familie & Gesellschaft", 4, (5,10)),
    ("Daoismus (Taoismus): Laozi, Dao De Jing, Wu Wei", 4, (6,10)),
    ("Yin & Yang, Fünf Wandlungsphasen", 3, (5,10)),
    ("Volksreligion & Ahnenkult in China", 3, (4,10)),
    ("Shintoismus: Kami, Schreinwesen & Rituale", 4, (4,10)),
    ("Synkretismus in Japan (Shinto–Buddhismus)", 3, (5,10)),
    ("Zen-Buddhismus & Ästhetik (Zen-Garten, Teezeremonie)", 3, (5,10)),
    # ⚑ Basis
    ("China/Japan – Basisfakten (Begriffe, Gottheiten, Praktiken)", 2, (1,7)),

    # 6 Religiöse Praxis & Philosophie
    ("Meditation, Kontemplation & Erleuchtung", 4, (3,10)),
    ("Reinkarnation & Befreiung (Moksha, Nirvana)", 4, (4,10)),
    ("Ethik, Mitgefühl & Gewaltlosigkeit", 3, (3,10)),
    ("Pilgerreisen & heilige Orte (Bodhgaya, Varanasi)", 3, (2,9)),
    ("Klosterleben & Askese", 2, (5,10)),
    ("Mantras, Gebetsmühlen & Rituale", 2, (2,9)),
    # ⚑ Basis
    ("Praxis & Philosophie – Basis (Symbole, Begriffe, Orte)", 2, (1,7)),

    # 7 Moderne Entwicklungen & globale Rezeption
    ("Reformbewegungen des 19./20. Jh. (Vivekananda, Ambedkar)", 3, (6,10)),
    ("Buddhismus & Westen: Achtsamkeit, Meditation, Zen", 3, (4,10)),
    ("Hinduistische Bewegungen weltweit (ISKCON, Yoga-Kultur)", 3, (3,10)),
    ("Neue Religiosität & interkulturelle Spiritualität", 2, (4,10)),
    ("Religiöse Konflikte & Säkularisierung in Südasien", 3, (6,10)),
    # ⚑ Basis
    ("Moderne & globale Rezeption – Basis (Personen, Bewegungen, Trends)", 2, (1,7)),
]
