# -*- coding: utf-8 -*-
"""
Unterthemen (Subdisciplines) für „Indische & fernöstliche Religionen“.
Alle min/max-Werte wurden automatisch um +1 erhöht (außer 1 und 10 bleiben).

Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte
"""

SUBDISCIPLINES = [
    # 1 Überblick & Ursprünge
    ("Indische & fernöstliche Religionen: Überblick & Entstehung", 4, (1,10)),
    ("Religiöse Vielfalt Asiens & synkretistische Einflüsse", 3, (4,10)),
    ("Veden & Upanishaden: Grundlagen altindischer Religion", 4, (4,10)),
    ("Samsara, Karma & Moksha – zyklisches Weltbild", 4, (3,10)),
    ("Dharma & Kastensystem", 3, (3,10)),

    # 2 Hinduismus
    ("Hinduismus: Ursprung & Entwicklung", 4, (3,10)),
    ("Heilige Schriften: Veden, Bhagavad Gita, Mahabharata", 4, (3,10)),
    ("Trimurti: Brahma, Vishnu, Shiva", 4, (1,10)),
    ("Devi-Kult & weibliche Gottheiten (Durga, Kali, Lakshmi)", 3, (4,10)),
    ("Rituale, Feste & Pilgerorte (z. B. Kumbh Mela, Diwali)", 3, (1,9)),
    ("Bhakti-Bewegung & religiöse Praxis", 3, (3,10)),
    ("Yoga, Meditation & spirituelle Wege", 3, (3,10)),
    ("Hinduismus in der Moderne & Diaspora", 2, (3,10)),

    # 3 Buddhismus
    ("Buddhismus: Leben des Siddhartha Gautama (Buddha)", 4, (1,10)),
    ("Vier Edle Wahrheiten & Achtfacher Pfad", 4, (1,10)),
    ("Theravada, Mahayana & Vajrayana", 4, (4,10)),
    ("Lehre von der Vergänglichkeit (Anicca) & Nicht-Selbst (Anatta)", 3, (4,10)),
    ("Buddhistische Ethik & Mitgefühl (Karuna)", 3, (3,10)),
    ("Klosterwesen & Sangha", 3, (3,10)),
    ("Verbreitung nach Ost- und Südostasien", 3, (1,9)),
    ("Zen, tibetischer & moderner Buddhismus", 3, (4,10)),

    # 4 Jainismus & Sikhismus
    ("Jainismus: Mahavira & Prinzip der Gewaltlosigkeit (Ahimsa)", 4, (4,10)),
    ("Karma-Lehre & asketische Praxis im Jainismus", 3, (5,10)),
    ("Sikhismus: Guru Nanak & die Zehn Gurus", 4, (3,10)),
    ("Heilige Schrift: Guru Granth Sahib", 3, (4,10)),
    ("Khalsa, Symbolik & Rituale der Sikhs", 3, (3,10)),

    # 5 Chinesische & japanische Traditionen
    ("Konfuzianismus: Ethik, Familie & Gesellschaft", 4, (4,10)),
    ("Daoismus (Taoismus): Laozi, Dao De Jing, Wu Wei", 4, (4,10)),
    ("Yin & Yang, Fünf Wandlungsphasen", 3, (3,10)),
    ("Volksreligion & Ahnenkult in China", 3, (3,10)),
    ("Shintoismus: Kami, Schreinwesen & Rituale", 4, (3,10)),
    ("Synkretismus in Japan (Shinto-Buddhismus)", 3, (4,10)),
    ("Zen-Buddhismus & Ästhetik", 3, (4,10)),

    # 6 Religiöse Praxis & Philosophie
    ("Meditation, Kontemplation & Erleuchtung", 4, (3,10)),
    ("Reinkarnation & Befreiung (Moksha, Nirvana)", 4, (3,10)),
    ("Ethik, Mitgefühl & Gewaltlosigkeit", 3, (3,10)),
    ("Pilgerreisen & heilige Orte (Bodhgaya, Varanasi)", 3, (1,10)),
    ("Klosterleben & Askese", 2, (4,10)),
    ("Mantras, Gebetsmühlen & Rituale", 2, (1,9)),

    # 7 Moderne Entwicklungen & globale Rezeption
    ("Reformbewegungen des 19./20. Jh. (Vivekananda, Ambedkar)", 3, (4,10)),
    ("Buddhismus & Westen: Achtsamkeit, Meditation, Zen", 3, (3,10)),
    ("Hinduistische Bewegungen weltweit (ISKCON, Yoga-Kultur)", 3, (3,10)),
    ("Neue Religiosität & interkulturelle Spiritualität", 2, (4,10)),
    ("Religiöse Konflikte & Säkularisierung in Südasien", 3, (4,10)),
]
