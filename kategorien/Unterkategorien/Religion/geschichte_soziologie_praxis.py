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
"""

SUBDISCIPLINES = [
    # 1 Grundlagen & Theorien
    ("Religionsgeschichte: Entwicklung religiöser Systeme", 4),
    ("Religionssoziologie: zentrale Ansätze & Theorien", 4),
    ("Religion als soziales & kulturelles Phänomen", 4),
    ("Ritualtheorie & Symbolanthropologie (Turner, Douglas)", 3),
    ("Institutionalisierung & Autorität in Religionen", 3),

    # 2 Entstehung & Entwicklung religiöser Systeme
    ("Ursprünge von Religion in der Menschheitsgeschichte", 4),
    ("Von Stammeskulten zu Hochreligionen", 3),
    ("Priesterschaft, Prophetentum & religiöse Führung", 4),
    ("Tempel, Kirchen & Moscheen als Institutionen", 3),
    ("Religiöse Architektur & Raumkonzepte", 2),

    # 3 Religion & Gesellschaft
    ("Funktion von Religion in der Gesellschaft", 4),
    ("Religion und Macht: Herrschaftslegitimation & Widerstand", 4),
    ("Religion & Geschlecht: Rollen, Frauenbilder, Patriarchat", 3),
    ("Religiöse Bildung & Sozialisation", 3),
    ("Religiöse Bewegungen & Erweckungen", 3),
    ("Säkularisierung & Entkirchlichung", 4),
    ("Pluralisierung & religiöse Vielfalt", 3),

    # 4 Rituale & Praxis
    ("Religiöse Rituale: Definition & Struktur", 4),
    ("Übergangsriten (Geburt, Initiation, Ehe, Tod)", 4),
    ("Opfer, Gebet & Meditation als Grundformen religiöser Praxis", 3),
    ("Feste & Feiertage im Jahreszyklus", 3),
    ("Pilgerreisen & Wallfahrten", 4),
    ("Kleiderordnungen, Speisegebote & Reinheitsvorschriften", 3),
    ("Heilige Gegenstände & Symbole", 2),

    # 5 Religion & Politik
    ("Trennung von Kirche & Staat", 4),
    ("Theokratie & Religionsrecht", 3),
    ("Mission, Kolonialismus & Kulturkontakte", 3),
    ("Religiöse Konflikte & Kriege (Kreuzzüge, Dschihad, Reformen)", 4),
    ("Religiöse Identität & Nationalismus", 3),
    ("Friedensbewegungen & religiöser Pazifismus", 2),

    # 6 Religion, Wirtschaft & Kultur
    ("Religion & Wirtschaftsethik (Weber, Calvinismus)", 4),
    ("Pilgerwesen & religiöse Ökonomie", 3),
    ("Spendenwesen, Almosen & Zehntsysteme", 3),
    ("Kunst, Musik & Architektur im religiösen Kontext", 3),
    ("Heilige Schrift & Schriftkultur", 2),

    # 7 Religion in der Moderne & Postmoderne
    ("Säkularisierungstheorien & Kritik", 4),
    ("Religionswandel & Individualisierung", 4),
    ("Neue religiöse Bewegungen & Spiritualität", 3),
    ("Fundamentalismus & religiöser Traditionalismus", 4),
    ("Globalisierung & Religion", 3),
    ("Medialisierung von Religion & Popkultur", 3),
    ("Religion & Menschenrechte", 3),

    # 8 Religion & Wissenschaft
    ("Wissenschaftlich-technischer Fortschritt & Glaubenskrisen", 3),
    ("Evolutionstheorie & religiöse Reaktionen", 3),
    ("Bioethik & Religion", 3),
    ("Religiöse Deutung moderner Krisen (Umwelt, KI, Krieg)", 2),

    # 9 Religiöse Minderheiten & Identität
    ("Diaspora-Gemeinschaften & kulturelle Anpassung", 3),
    ("Synkretismus & Hybridreligionen", 3),
    ("Migration & religiöse Identität", 3),
    ("Interreligiöser Dialog & Toleranz", 4),
    ("Verfolgung, Märtyrertum & Religionsfreiheit", 4),

    # 10 Religion & Gegenwartsgesellschaft
    ("Postsäkulare Gesellschaft & neue Religiosität", 4),
    ("Religiöse Symbolik im öffentlichen Raum", 3),
    ("Politische Religionen & Ideologien", 3),
    ("Ethik, Wertewandel & Sinnsuche", 3),
    ("Zukunft der Religion – Prognosen & Szenarien", 2),
]
