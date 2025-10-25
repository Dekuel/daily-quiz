# -*- coding: utf-8 -*-
# Unterkategorien/Religion/geschichte_soziologie_praxis.py
"""
Unterthemen (Subdisciplines) für die Disziplin
„Religionsgeschichte, Soziologie & Praxis (Rituale, Institutionen, Säkularisierung)“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte

Schwierigkeits-Skala (1–10) – präzisiert:
1 = absolutes Grundwissen (≈95 %), 4 = einfach,
5 = einfach–mittel (≈70–80 %), 6 = mittel (≈60 %),
7 = mittel–schwer (≈30–50 %), 8 = schwer (deutliches Vorwissen),
9 = Expertenwissen, 10 = schwerstmöglich.
"""

SUBDISCIPLINES = [
    # 1 Grundlagen & Theorien
    ("Religionsgeschichte: Entwicklung religiöser Systeme", 4, (6,10)),
    ("Religionssoziologie: zentrale Ansätze & Theorien", 4, (7,10)),
    ("Religion als soziales & kulturelles Phänomen", 4, (6,10)),
    ("Ritualtheorie & Symbolanthropologie (Turner, Douglas)", 3, (8,10)),
    ("Institutionalisierung & Autorität in Religionen", 3, (7,10)),

    # 2 Entstehung & Entwicklung religiöser Systeme
    ("Ursprünge von Religion in der Menschheitsgeschichte", 4, (7,10)),
    ("Von Stammeskulten zu Hochreligionen", 3, (6,10)),
    ("Priesterschaft, Prophetentum & religiöse Führung", 4, (6,10)),
    ("Tempel, Kirchen & Moscheen als Institutionen", 3, (5,9)),
    ("Religiöse Architektur & Raumkonzepte", 2, (5,9)),

    # 3 Religion & Gesellschaft
    ("Funktion von Religion in der Gesellschaft", 4, (6,10)),
    ("Religion und Macht: Herrschaftslegitimation & Widerstand", 4, (7,10)),
    ("Religion & Geschlecht: Rollen, Frauenbilder, Patriarchat", 3, (6,10)),
    ("Religiöse Bildung & Sozialisation", 3, (5,9)),
    ("Religiöse Bewegungen & Erweckungen", 3, (6,10)),
    ("Säkularisierung & Entkirchlichung", 4, (7,10)),
    ("Pluralisierung & religiöse Vielfalt", 3, (6,10)),

    # 4 Rituale & Praxis
    ("Religiöse Rituale: Definition & Struktur", 4, (6,10)),
    ("Übergangsriten (Geburt, Initiation, Ehe, Tod)", 4, (5,9)),
    ("Opfer, Gebet & Meditation als Grundformen religiöser Praxis", 3, (5,9)),
    ("Feste & Feiertage im Jahreszyklus", 3, (4,8)),
    ("Pilgerreisen & Wallfahrten", 4, (5,9)),
    ("Kleiderordnungen, Speisegebote & Reinheitsvorschriften", 3, (5,9)),
    ("Heilige Gegenstände & Symbole", 2, (4,8)),

    # 5 Religion & Politik
    ("Trennung von Kirche & Staat", 4, (5,9)),
    ("Theokratie & Religionsrecht", 3, (7,10)),
    ("Mission, Kolonialismus & Kulturkontakte", 3, (6,10)),
    ("Religiöse Konflikte & Kriege (Kreuzzüge, Dschihad, Reformen)", 4, (7,10)),
    ("Religiöse Identität & Nationalismus", 3, (6,10)),
    ("Friedensbewegungen & religiöser Pazifismus", 2, (5,9)),

    # 6 Religion, Wirtschaft & Kultur
    ("Religion & Wirtschaftsethik (Weber, Calvinismus)", 4, (8,10)),
    ("Pilgerwesen & religiöse Ökonomie", 3, (6,10)),
    ("Spendenwesen, Almosen & Zehntsysteme", 3, (5,9)),
    ("Kunst, Musik & Architektur im religiösen Kontext", 3, (5,9)),
    ("Heilige Schrift & Schriftkultur", 2, (5,9)),

    # 7 Religion in der Moderne & Postmoderne
    ("Säkularisierungstheorien & Kritik", 4, (8,10)),
    ("Religionswandel & Individualisierung", 4, (7,10)),
    ("Neue religiöse Bewegungen & Spiritualität", 3, (6,10)),
    ("Fundamentalismus & religiöser Traditionalismus", 4, (7,10)),
    ("Globalisierung & Religion", 3, (6,10)),
    ("Medialisierung von Religion & Popkultur", 3, (5,9)),
    ("Religion & Menschenrechte", 3, (6,10)),

    # 8 Religion & Wissenschaft
    ("Wissenschaftlich-technischer Fortschritt & Glaubenskrisen", 3, (6,10)),
    ("Evolutionstheorie & religiöse Reaktionen", 3, (5,9)),
    ("Bioethik & Religion", 3, (6,10)),
    ("Religiöse Deutung moderner Krisen (Umwelt, KI, Krieg)", 2, (5,9)),

    # 9 Religiöse Minderheiten & Identität
    ("Diaspora-Gemeinschaften & kulturelle Anpassung", 3, (6,10)),
    ("Synkretismus & Hybridreligionen", 3, (7,10)),
    ("Migration & religiöse Identität", 3, (6,10)),
    ("Interreligiöser Dialog & Toleranz", 4, (6,10)),
    ("Verfolgung, Märtyrertum & Religionsfreiheit", 4, (7,10)),

    # 10 Religion & Gegenwartsgesellschaft
    ("Postsäkulare Gesellschaft & neue Religiosität", 4, (7,10)),
    ("Religiöse Symbolik im öffentlichen Raum", 3, (5,9)),
    ("Politische Religionen & Ideologien", 3, (7,10)),
    ("Ethik, Wertewandel & Sinnsuche", 3, (5,9)),
    ("Zukunft der Religion – Prognosen & Szenarien", 2, (6,10)),
]
