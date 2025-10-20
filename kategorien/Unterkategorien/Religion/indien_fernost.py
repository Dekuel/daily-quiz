# -*- coding: utf-8 -*-
# Unterkategorien/Religion/indien_fernost.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Indische & fernöstliche Religionen“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte
"""

SUBDISCIPLINES = [
    # 1 Überblick & Ursprünge
    ("Indische & fernöstliche Religionen: Überblick & Entstehung", 4),
    ("Religiöse Vielfalt Asiens & synkretistische Einflüsse", 3),
    ("Veden & Upanishaden: Grundlagen altindischer Religion", 4),
    ("Samsara, Karma & Moksha – zyklisches Weltbild", 4),
    ("Dharma & Kastensystem", 3),

    # 2 Hinduismus
    ("Hinduismus: Ursprung & Entwicklung", 4),
    ("Heilige Schriften: Veden, Bhagavad Gita, Mahabharata", 4),
    ("Trimurti: Brahma, Vishnu, Shiva", 4),
    ("Devi-Kult & weibliche Gottheiten (Durga, Kali, Lakshmi)", 3),
    ("Rituale, Feste & Pilgerorte (z. B. Kumbh Mela, Diwali)", 3),
    ("Bhakti-Bewegung & religiöse Praxis", 3),
    ("Yoga, Meditation & spirituelle Wege", 3),
    ("Hinduismus in der Moderne & Diaspora", 2),

    # 3 Buddhismus
    ("Buddhismus: Leben des Siddhartha Gautama (Buddha)", 4),
    ("Vier Edle Wahrheiten & Achtfacher Pfad", 4),
    ("Theravada, Mahayana & Vajrayana", 4),
    ("Lehre von der Vergänglichkeit (Anicca) & Nicht-Selbst (Anatta)", 3),
    ("Buddhistische Ethik & Mitgefühl (Karuna)", 3),
    ("Klosterwesen & Sangha", 3),
    ("Verbreitung nach Ost- und Südostasien", 3),
    ("Zen, tibetischer & moderner Buddhismus", 3),

    # 4 Jainismus & Sikhismus
    ("Jainismus: Mahavira & Prinzip der Gewaltlosigkeit (Ahimsa)", 4),
    ("Karma-Lehre & asketische Praxis im Jainismus", 3),
    ("Sikhismus: Guru Nanak & die Zehn Gurus", 4),
    ("Heilige Schrift: Guru Granth Sahib", 3),
    ("Khalsa, Symbolik & Rituale der Sikhs", 3),

    # 5 Chinesische & japanische Traditionen
    ("Konfuzianismus: Ethik, Familie & Gesellschaft", 4),
    ("Daoismus (Taoismus): Laozi, Dao De Jing, Wu Wei", 4),
    ("Yin & Yang, Fünf Wandlungsphasen", 3),
    ("Volksreligion & Ahnenkult in China", 3),
    ("Shintoismus: Kami, Schreinwesen & Rituale", 4),
    ("Synkretismus in Japan (Shinto-Buddhismus)", 3),
    ("Zen-Buddhismus & Ästhetik", 3),

    # 6 Religiöse Praxis & Philosophie
    ("Meditation, Kontemplation & Erleuchtung", 4),
    ("Reinkarnation & Befreiung (Moksha, Nirvana)", 4),
    ("Ethik, Mitgefühl & Gewaltlosigkeit", 3),
    ("Pilgerreisen & heilige Orte (Bodhgaya, Varanasi)", 3),
    ("Klosterleben & Askese", 2),
    ("Mantras, Gebetsmühlen & Rituale", 2),

    # 7 Moderne Entwicklungen & globale Rezeption
    ("Reformbewegungen des 19./20. Jh. (Vivekananda, Ambedkar)", 3),
    ("Buddhismus & Westen: Achtsamkeit, Meditation, Zen", 3),
    ("Hinduistische Bewegungen weltweit (ISKCON, Yoga-Kultur)", 3),
    ("Neue Religiosität & interkulturelle Spiritualität", 2),
    ("Religiöse Konflikte & Säkularisierung in Südasien", 3),
]
