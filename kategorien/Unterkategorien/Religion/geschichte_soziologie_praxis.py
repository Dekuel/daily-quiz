# -*- coding: utf-8 -*-
# Unterkategorien/Religion/geschichte_soziologie_praxis.py
"""
Unterthemen (Subdisciplines) für die Disziplin
„Religionsgeschichte, Soziologie & Praxis (Rituale, Institutionen, Säkularisierung)“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Einheitliche Skalierung & Struktur
==========================================================================
System wie in monotheismus.py:

- Skala 1–10: 1 = Allgemeinwissen, 10 = Expertenwissen.
- min = Bekanntheit (Population Familiarity)
- max = Komplexität (Conceptual Depth)
- Alle Nicht-Basis-Themen reichen i. d. R. bis 10.
- „Basis…“-Kategorien: min = 1 → ermöglichen Zuordnungs-/Grundfragen.
- Fachspezifische Theorieansätze oder seltene Diskurse beginnen bei 6–9.
"""

SUBDISCIPLINES = [
    # 1 Grundlagen & Theorien
    ("Religionsgeschichte: Entwicklung religiöser Systeme", 4, (4,10)),
    ("Religionssoziologie: zentrale Ansätze & Theorien", 4, (6,10)),
    ("Religion als soziales & kulturelles Phänomen", 4, (4,10)),
    ("Ritualtheorie & Symbolanthropologie (Turner, Douglas)", 3, (7,10)),
    ("Institutionalisierung & Autorität in Religionen", 3, (5,10)),
    # ⚑ Basis
    ("Basis – Grundbegriffe (Religion, Ritual, Institution, Gesellschaft)", 2, (1,7)),

    # 2 Entstehung & Entwicklung religiöser Systeme
    ("Ursprünge von Religion in der Menschheitsgeschichte", 4, (5,10)),
    ("Von Stammeskulten zu Hochreligionen", 3, (4,10)),
    ("Priesterschaft, Prophetentum & religiöse Führung", 4, (4,10)),
    ("Tempel, Kirchen & Moscheen als Institutionen", 3, (3,9)),
    ("Religiöse Architektur & Raumkonzepte", 2, (3,9)),
    # ⚑ Basis
    ("Basis – Entstehung & Formen (Frühreligionen, Bauten, Ämter)", 2, (1,7)),

    # 3 Religion & Gesellschaft
    ("Funktion von Religion in der Gesellschaft", 4, (4,10)),
    ("Religion und Macht: Herrschaftslegitimation & Widerstand", 4, (5,10)),
    ("Religion & Geschlecht: Rollen, Frauenbilder, Patriarchat", 3, (4,10)),
    ("Religiöse Bildung & Sozialisation", 3, (3,9)),
    ("Religiöse Bewegungen & Erweckungen", 3, (4,10)),
    ("Säkularisierung & Entkirchlichung", 4, (5,10)),
    ("Pluralisierung & religiöse Vielfalt", 3, (4,10)),
    # ⚑ Basis
    ("Basis – Religion & Gesellschaft (Funktionen, Gruppen, Rollen)", 2, (1,7)),

    # 4 Rituale & Praxis
    ("Religiöse Rituale: Definition & Struktur", 4, (3,10)),
    ("Übergangsriten (Geburt, Initiation, Ehe, Tod)", 4, (2,9)),
    ("Opfer, Gebet & Meditation als Grundformen religiöser Praxis", 3, (2,9)),
    ("Feste & Feiertage im Jahreszyklus", 3, (1,8)),
    ("Pilgerreisen & Wallfahrten", 4, (3,9)),
    ("Kleiderordnungen, Speisegebote & Reinheitsvorschriften", 3, (3,9)),
    ("Heilige Gegenstände & Symbole", 2, (2,8)),
    # ⚑ Basis
    ("Basis – Rituale & Praxis (Symbole, Orte, Feste, Handlungen)", 2, (1,7)),

    # 5 Religion & Politik
    ("Trennung von Kirche & Staat", 4, (3,9)),
    ("Theokratie & Religionsrecht", 3, (6,10)),
    ("Mission, Kolonialismus & Kulturkontakte", 3, (5,10)),
    ("Religiöse Konflikte & Kriege (Kreuzzüge, Dschihad, Reformen)", 4, (6,10)),
    ("Religiöse Identität & Nationalismus", 3, (4,10)),
    ("Friedensbewegungen & religiöser Pazifismus", 2, (3,9)),
    # ⚑ Basis
    ("Basis – Religion & Politik (Staat, Kirche, Konflikte, Begriffe)", 2, (1,7)),

    # 6 Religion, Wirtschaft & Kultur
    ("Religion & Wirtschaftsethik (Weber, Calvinismus)", 4, (6,10)),
    ("Pilgerwesen & religiöse Ökonomie", 3, (4,10)),
    ("Spendenwesen, Almosen & Zehntsysteme", 3, (3,9)),
    ("Kunst, Musik & Architektur im religiösen Kontext", 3, (3,9)),
    ("Heilige Schrift & Schriftkultur", 2, (3,9)),
    # ⚑ Basis
    ("Basis – Religion & Kultur (Musik, Kunst, Spenden, Werte)", 2, (1,7)),

    # 7 Religion in der Moderne & Postmoderne
    ("Säkularisierungstheorien & Kritik", 4, (7,10)),
    ("Religionswandel & Individualisierung", 4, (5,10)),
    ("Neue religiöse Bewegungen & Spiritualität", 3, (4,10)),
    ("Fundamentalismus & religiöser Traditionalismus", 4, (6,10)),
    ("Globalisierung & Religion", 3, (4,10)),
    ("Medialisierung von Religion & Popkultur", 3, (3,9)),
    ("Religion & Menschenrechte", 3, (4,10)),
    # ⚑ Basis
    ("Basis – Moderne & Gegenwart (Begriffe, Trends, Beispiele)", 2, (1,7)),

    # 8 Religion & Wissenschaft
    ("Wissenschaftlich-technischer Fortschritt & Glaubenskrisen", 3, (4,10)),
    ("Evolutionstheorie & religiöse Reaktionen", 3, (3,9)),
    ("Bioethik & Religion", 3, (4,10)),
    ("Religiöse Deutung moderner Krisen (Umwelt, KI, Krieg)", 2, (4,10)),
    # ⚑ Basis
    ("Basis – Religion & Wissenschaft (Beispiele, Konfliktlinien)", 2, (1,7)),

    # 9 Religiöse Minderheiten & Identität
    ("Diaspora-Gemeinschaften & kulturelle Anpassung", 3, (4,10)),
    ("Synkretismus & Hybridreligionen", 3, (6,10)),
    ("Migration & religiöse Identität", 3, (4,10)),
    ("Interreligiöser Dialog & Toleranz", 4, (4,10)),
    ("Verfolgung, Märtyrertum & Religionsfreiheit", 4, (5,10)),
    # ⚑ Basis
    ("Basis – Minderheiten & Identität (Begriffe, Beispiele, Regionen)", 2, (1,7)),

    # 10 Religion & Gegenwartsgesellschaft
    ("Postsäkulare Gesellschaft & neue Religiosität", 4, (5,10)),
    ("Religiöse Symbolik im öffentlichen Raum", 3, (3,9)),
    ("Politische Religionen & Ideologien", 3, (6,10)),
    ("Ethik, Wertewandel & Sinnsuche", 3, (3,9)),
    ("Zukunft der Religion – Prognosen & Szenarien", 2, (4,10)),
    # ⚑ Basis
    ("Basis – Gegenwart (Trends, Symbole, Begriffe)", 2, (1,7)),
]
