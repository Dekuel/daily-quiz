# -*- coding: utf-8 -*-
# Unterkategorien/Religion/monotheismus.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Monotheistische Religionen“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte
"""

SUBDISCIPLINES = [
    # 1 Allgemeines & Grundlagen
    ("Monotheismus: Begriff, Ursprung, Abgrenzung", 4),
    ("Abrahamitische Religionen: gemeinsame Wurzeln", 4),
    ("Offenbarung, Prophetie & Heilige Schriften", 4),
    ("Ethik & Gottesbild im Monotheismus", 3),
    ("Schöpfung, Erlösung, Eschatologie", 3),

    # 2 Judentum
    ("Judentum: Ursprung & Geschichte Israels", 4),
    ("Tanach (Tora, Neviim, Ketuvim)", 4),
    ("Tempel, Priesterschaft & Opferkult", 3),
    ("Rabbinisches Judentum & Talmud", 3),
    ("Diaspora & jüdische Identität", 3),
    ("Jüdische Feste & Bräuche (Pessach, Jom Kippur, Schabbat)", 3),
    ("Zionismus & Staat Israel", 2),

    # 3 Christentum
    ("Christentum: Entstehung & frühe Kirche", 4),
    ("Neues Testament & Evangelien", 4),
    ("Jesus von Nazareth & Apostelgeschichte", 4),
    ("Konzile & Dogmenbildung (Nicäa, Chalcedon)", 3),
    ("Katholizismus, Orthodoxie & Protestantismus", 4),
    ("Reformation & Gegenreformation", 3),
    ("Christliche Liturgie, Sakramente & Heilige", 3),
    ("Mission, Kolonialismus & Weltkirche", 2),

    # 4 Islam
    ("Islam: Ursprung & Prophet Mohammed", 4),
    ("Koran & Hadith", 4),
    ("Fünf Säulen des Islam", 4),
    ("Scharia & islamische Rechtsschulen", 3),
    ("Sunniten & Schiiten", 4),
    ("Kalifate & islamische Geschichte", 3),
    ("Sufismus (islamische Mystik)", 3),
    ("Islam in der Moderne & interreligiöser Dialog", 3),

    # 5 Bahaitum & andere monotheistische Strömungen
    ("Bahaitum: Ursprung & Lehre", 3),
    ("Zoroastrismus (Ahura Mazda & Dualismus)", 3),
    ("Manichäismus & spätantike monotheistische Bewegungen", 2),

    # 6 Vergleichende Themen
    ("Gemeinsamkeiten & Unterschiede der abrahamitischen Religionen", 4),
    ("Monotheismus & Gewalt / Toleranz", 3),
    ("Frauenbilder im Monotheismus", 2),
    ("Monotheismus und Moderne (Säkularisierung, Pluralismus)", 3),
    ("Heilige Orte: Jerusalem, Mekka, Rom", 3),
]
