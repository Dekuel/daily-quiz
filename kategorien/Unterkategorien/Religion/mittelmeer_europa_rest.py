# -*- coding: utf-8 -*-
# Unterkategorien/Religion/mittelmeer_europa_rest.py
"""
Unterthemen (Subdisciplines) für die Disziplin
„Weitere antike Mittelmeer- & europäische Mythologien“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte

Hinweis: Dieser Block umfasst bewusst NICHT griechische, römische, ägyptische
oder nordische Mythologien (die sind in „klassisch_nordisch.py“).
"""

SUBDISCIPLINES = [
    # 1 Überblick & Quellen
    ("Antike Mittelmeer- & europäische Mythologien (ohne griech./röm./ägypt./nord.) – Überblick", 4),
    ("Quellenlage: Inschriften, Mythenfragmente, Archäologie", 3),
    ("Rituale, Opfer & Kultorte: allgemeine Muster", 3),
    ("Interpretatio graeca/romana & Synkretismen", 4),

    # 2 Mesopotamien (Sumerer, Akkader, Babylonier, Assyrer)
    ("Mesopotamische Mythologie: Pantheon & Kosmologie", 4),
    ("Sumerische Mythen: An, Enlil, Enki, Inanna", 4),
    ("Akkadisch-babylonische Tradition: Marduk & Enūma eliš", 4),
    ("Gilgamesch-Epos: Held, Freundschaft & Unsterblichkeit", 4),
    ("Assyrische Religion & Königsideologie", 3),
    ("Tempelwirtschaft, Zikkurrat & Priesterschaft", 3),
    ("Unterwelt & Jenseits (Ereškigal, Nergal)", 3),

    # 3 Levante: Kanaanäer, Phönizier, Ugarit, Punisch/Karthago
    ("Kanaanäische & ugaritische Religion: El, Baal, Aschera", 4),
    ("Ugaritische Texte: Baal-Zyklus & Sturmgott-Motive", 3),
    ("Phönizische Kulte & Seehandelsdiaspora", 3),
    ("Punikische/karthagische Religion: Tanit & Baal Hammon", 3),
    ("Kinderopfer-Debatte & Tophet-Funde", 2),

    # 4 Anatolien & Nachbarn: Hethiter, Luwier, Phrygier, Urartäer
    ("Hethitische Religion: Götterversammlung & Staatskult", 4),
    ("Telepinu-Mythos & Fruchtbarkeitszyklen", 3),
    ("Luwische & anatolische Gottheiten (Tarḫunt, Arinna)", 3),
    ("Phrygien: Kybele & Attis-Kult", 4),
    ("Urartu: Festungen, Staatskult & Pantheon", 2),
    ("Anatolische Orakel- & Reinigungsriten", 2),

    # 5 Italischer Raum (vor-/nebenrömisch) & Etrusker
    ("Etruskische Religion: Disziplinen, Auguren & Haruspizes", 4),
    ("Etruskisches Pantheon & Jenseitsdarstellungen", 3),
    ("Frühitalische/italische Kulte (Sabiner, Latinum, Samniten)", 3),
    ("Lokale Heiligtümer & Grenzschutz-Kulte", 2),

    # 6 Ägäis & Balkan (außer griechische Klassik)
    ("Minoische Religion: Ikonographie (Stiersprung, Doppelaxt)", 3),
    ("Mykenische Vorformen: Linear B & Kultspuren", 2),
    ("Thrakische & dakische Kulte (Zalmoxis u. a.)", 3),
    ("Illyrische Gottheiten & Stammesheiligtümer", 2),

    # 7 Westeuropa: Keltischer & iberischer Kulturraum
    ("Keltische Mythologie: Götter, Druiden & Heiligtümer", 4),
    ("Insulare keltische Sagen (Irland, Wales)", 3),
    ("Gallische Kulte & römisch-keltischer Synkretismus", 3),
    ("Iberische & lusitanische Gottheiten (Endovelicus u. a.)", 2),
    ("Megalithische Traditionen & Kultkontinuitäten", 2),

    # 8 Osteuropa & Ostseeraum
    ("Slawische Mythologie: Perun, Veles & Kultlandschaften", 4),
    ("Baltische Religionen: Dievas/Dievs, Perkūnas/Perkons", 3),
    ("Kiewer Rus’ & Christianisierung – religiöse Übergänge", 2),
    ("Heiligtümer, heilige Haine & Prozessionen", 2),

    # 9 Steppenvölker & eurasische Schnittstellen
    ("Skythen & Sarmaten: Tierstil, Grabhügel & Kult", 3),
    ("Nomadische Jenseits- & Ahnenvorstellungen", 2),
    ("Transkulturelle Motive entlang der eurasischen Routen", 2),

    # 10 Querschnitte & Rezeption
    ("Schöpfungs-, Flut- & Heldenmotive im Vergleich", 3),
    ("Heilige Königtümer & Sakralherrschaft", 3),
    ("Schutzgötter, Orakel & Wahrsagepraktiken", 3),
    ("Religiöse Symbolik (Stier, Sonne, Baum, Berg, Meer)", 2),
    ("Antike Rezeption & spätere Umdeutungen (Mittelalter–Neuzeit)", 2),
    ("Archäologischer Befund vs. Schriftüberlieferung: Methodenfragen", 2),
]
