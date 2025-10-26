# -*- coding: utf-8 -*-
# Unterkategorien/Religion/alter_orient.py
"""
Unterthemen (Subdisciplines) für die Disziplin
„Nahöstliche & altorientalische Kulte“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Einheitliche Skala & Struktur
==========================================================================
System wie in monotheismus.py:

- min = Bekanntheit (Population Familiarity)
- max = inhaltliche/methodische Tiefe
- 1 = Allgemeinwissen … 10 = Expertenwissen
- „Basis…“-Kategorien: min = 1 (Zuordnungen, einfache Begriffe)
- Nicht-Basis-Themen i. d. R. bis 10 (theoretisch vertiefbar)
"""

SUBDISCIPLINES = [
    # 1 Überblick & Quellen
    ("Altorientalische Religionen: Überblick & historische Entwicklung", 4, (3,10)),
    ("Keilschrifttexte, Mythen & Tempelarchäologie als Quellen", 3, (5,10)),
    ("Kult, Ritual & Königtum im Alten Orient", 4, (4,10)),
    ("Kosmologie, Schöpfung & göttliche Ordnung", 3, (5,10)),
    ("Priester, Propheten & Orakelwesen", 3, (5,10)),
    # ⚑ Basis
    ("Basiswissen – Altorient (Begriffe, Orte, Gottheiten, Quellenarten)", 2, (1,7)),

    # 2 Sumerer & Akkader
    ("Sumerische Religion: An, Enlil, Enki & Inanna", 4, (4,10)),
    ("Stadtgötter & lokale Panthea (Uruk, Nippur, Eridu)", 3, (5,10)),
    ("Zikkurrat-Tempel & Kulthandlungen", 3, (5,10)),
    ("Schöpfungsmythen & Fluterzählungen (Atramhasis)", 3, (4,10)),
    ("Akkadische Überlieferung & Synkretismus", 3, (6,10)),
    # ⚑ Basis
    ("Sumer/Akkad – Basis (Götternamen, Städte, Symbole)", 2, (1,7)),

    # 3 Babylonier & Assyrer
    ("Babylonische Religion: Marduk & Enūma eliš", 4, (5,10)),
    ("Assyrische Königsideologie & Religion", 3, (6,10)),
    ("Magie, Beschwörungen & Exorzismus", 3, (6,10)),
    ("Sternenkult & Astrologie in Mesopotamien", 4, (4,10)),
    ("Totenkult & Jenseitsvorstellungen", 3, (5,10)),
    # ⚑ Basis
    ("Babylon/Assyrien – Basis (Symbole, Orte, Gottheiten)", 2, (1,7)),

    # 4 Hethiter, Luwier & Anatolien
    ("Hethitische Religion: Götterversammlung & Staatskult", 4, (7,10)),
    ("Stormgott Tarḫunt & Sonnengöttin von Arinna", 3, (8,10)),
    ("Rituale der Reinigung & Versöhnung (Kizzuwatna-Texte)", 3, (8,10)),
    ("Luwische & phrygische Kulte (Kybele, Attis)", 3, (6,10)),
    ("Orakelwesen & Priesterinnen in Anatolien", 2, (6,10)),
    # ⚑ Basis
    ("Anatolien – Basis (Hauptgötter, Orte, Begriffe)", 2, (1,7)),

    # 5 Syrien & Levante
    ("Kanaanäische Religion: El, Baal, Aschera", 4, (6,10)),
    ("Ugaritische Texte & der Baal-Zyklus", 4, (7,10)),
    ("Phönizische & punische Religion (Baal Hammon, Tanit)", 3, (7,10)),
    ("Kinderopfer & Tempelrituale", 2, (8,10)),
    ("Religiöse Symbolik: Stier, Sonne, Meer, Fruchtbarkeit", 2, (5,9)),
    # ⚑ Basis
    ("Levante – Basis (Götter, Orte, Funde, Symbole)", 2, (1,7)),

    # 6 Persien & iranische Religionen
    ("Zoroastrismus: Zarathustra & Ahura Mazda", 4, (4,10)),
    ("Dualismus von Gut und Böse (Ahriman)", 4, (5,10)),
    ("Avesta & zoroastrische Ethik", 3, (5,10)),
    ("Feuerkult & Reinheitsvorstellungen", 3, (5,10)),
    ("Manichäismus & spätere iranische Kulte", 3, (7,10)),
    # ⚑ Basis
    ("Iranische Religionen – Basis (Zarathustra, Symbole, Ethik)", 2, (1,7)),

    # 7 Tempel, Kult & Gesellschaft
    ("Opferwesen & Tempelwirtschaft", 4, (4,10)),
    ("Rituale des Königtums & göttliche Legitimation", 3, (5,10)),
    ("Priesterschaft, Wahrsager & Beschwörungspraktiken", 3, (5,10)),
    ("Heilige Städte & Kultzentren (Ur, Babylon, Ninive)", 3, (3,9)),
    ("Kultbilder & Idole", 2, (3,9)),
    # ⚑ Basis
    ("Kult & Gesellschaft – Basis (Rituale, Ämter, Orte)", 2, (1,7)),

    # 8 Mythen & kosmische Ordnung
    ("Schöpfungs- & Flutmythen (Atramhasis, Gilgamesch)", 4, (3,10)),
    ("Unterwelt & Jenseits (Ereškigal, Nergal)", 3, (5,10)),
    ("Heldenfiguren & göttliche Prüfungen", 2, (4,9)),
    ("Astrale Religion & Götter als Planeten", 3, (6,10)),
    # ⚑ Basis
    ("Mythen – Basis (Helden, Schöpfung, Götternamen)", 2, (1,7)),

    # 9 Übergänge & Nachwirkungen
    ("Einfluss altorientalischer Vorstellungen auf Bibel & Judentum", 4, (4,10)),
    ("Kontinuitäten im Hellenismus & frühen Islam", 3, (6,10)),
    ("Archäologische Entdeckungen & moderne Deutungen", 3, (4,10)),
    ("Mythenrezeption in Literatur & Kulturgeschichte", 2, (3,9)),
    # ⚑ Basis
    ("Nachwirkungen – Basis (Einflüsse, Begriffe, Epochen)", 2, (1,7)),
]
