# -*- coding: utf-8 -*-
# Unterkategorien/Religion/alter_orient.py
"""
Unterthemen (Subdisciplines) für die Disziplin
„Nahöstliche & altorientalische Kulte“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte
"""

SUBDISCIPLINES = [
    # 1 Überblick & Quellen
    ("Altorientalische Religionen: Überblick & historische Entwicklung", 4),
    ("Keilschrifttexte, Mythen & Tempelarchäologie als Quellen", 3),
    ("Kult, Ritual & Königtum im Alten Orient", 4),
    ("Kosmologie, Schöpfung & göttliche Ordnung", 3),
    ("Priester, Propheten & Orakelwesen", 3),

    # 2 Sumerer & Akkader
    ("Sumerische Religion: An, Enlil, Enki & Inanna", 4),
    ("Stadtgötter & lokale Panthea (Uruk, Nippur, Eridu)", 3),
    ("Zikkurrat-Tempel & Kulthandlungen", 3),
    ("Schöpfungsmythen & Fluterzählungen", 3),
    ("Akkadische Überlieferung & Synkretismus", 3),

    # 3 Babylonier & Assyrer
    ("Babylonische Religion: Marduk & Enūma eliš", 4),
    ("Assyrische Königsideologie & Religion", 3),
    ("Magie, Beschwörungen & Exorzismus", 3),
    ("Sternenkult & Astrologie in Mesopotamien", 4),
    ("Totenkult & Jenseitsvorstellungen", 3),

    # 4 Hethiter, Luwier & Anatolien
    ("Hethitische Religion: Götterversammlung & Staatskult", 4),
    ("Stormgott Tarḫunt & Sonnengöttin von Arinna", 3),
    ("Rituale der Reinigung & Versöhnung (Kizzuwatna-Texte)", 3),
    ("Luwische & phrygische Kulte (Kybele, Attis)", 3),
    ("Orakelwesen & Priesterinnen in Anatolien", 2),

    # 5 Syrien & Levante
    ("Kanaanäische Religion: El, Baal, Aschera", 4),
    ("Ugaritische Texte & der Baal-Zyklus", 4),
    ("Phönizische & punische Religion (Baal Hammon, Tanit)", 3),
    ("Kinderopfer & Tempelrituale", 2),
    ("Religiöse Symbolik: Stier, Sonne, Meer, Fruchtbarkeit", 2),

    # 6 Persien & iranische Religionen
    ("Zoroastrismus: Zarathustra & Ahura Mazda", 4),
    ("Dualismus von Gut und Böse (Ahriman)", 4),
    ("Avesta & zoroastrische Ethik", 3),
    ("Feuerkult & Reinheitsvorstellungen", 3),
    ("Manichäismus & spätere iranische Kulte", 2),

    # 7 Tempel, Kult & Gesellschaft
    ("Opferwesen & Tempelwirtschaft", 4),
    ("Rituale des Königtums & göttliche Legitimation", 3),
    ("Priesterschaft, Wahrsager & Beschwörungspraktiken", 3),
    ("Heilige Städte & Kultzentren (Ur, Babylon, Ninive)", 3),
    ("Kultbilder & Idole", 2),

    # 8 Mythen & kosmische Ordnung
    ("Schöpfungs- & Flutmythen (Atramhasis, Gilgamesch)", 4),
    ("Unterwelt & Jenseits (Ereškigal, Nergal)", 3),
    ("Heldenfiguren & göttliche Prüfungen", 2),
    ("Astrale Religion & Götter als Planeten", 3),

    # 9 Übergänge & Nachwirkungen
    ("Einfluss altorientalischer Vorstellungen auf Bibel & Judentum", 4),
    ("Kontinuitäten im Hellenismus & frühen Islam", 3),
    ("Archäologische Entdeckungen & moderne Deutungen", 3),
    ("Mythenrezeption in Literatur & Kulturgeschichte", 2),
]
