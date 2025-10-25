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
    ("Antike Mittelmeer- & europäische Mythologien (ohne griech./röm./ägypt./nord.) – Überblick", 4, (6,10)),
    ("Quellenlage: Inschriften, Mythenfragmente, Archäologie", 3, (8,10)),
    ("Rituale, Opfer & Kultorte: allgemeine Muster", 3, (7,10)),
    ("Interpretatio graeca/romana & Synkretismen", 4, (8,10)),

    # 2 Mesopotamien (Sumerer, Akkader, Babylonier, Assyrer)
    ("Mesopotamische Mythologie: Pantheon & Kosmologie", 4, (7,10)),
    ("Sumerische Mythen: An, Enlil, Enki, Inanna", 4, (8,10)),
    ("Akkadisch-babylonische Tradition: Marduk & Enūma eliš", 4, (8,10)),
    ("Gilgamesch-Epos: Held, Freundschaft & Unsterblichkeit", 4, (6,10)),
    ("Assyrische Religion & Königsideologie", 3, (7,10)),
    ("Tempelwirtschaft, Zikkurrat & Priesterschaft", 3, (7,10)),
    ("Unterwelt & Jenseits (Ereškigal, Nergal)", 3, (8,10)),

    # 3 Levante: Kanaanäer, Phönizier, Ugarit, Punisch/Karthago
    ("Kanaanäische & ugaritische Religion: El, Baal, Aschera", 4, (8,10)),
    ("Ugaritische Texte: Baal-Zyklus & Sturmgott-Motive", 3, (9,10)),
    ("Phönizische Kulte & Seehandelsdiaspora", 3, (7,10)),
    ("Punikische/karthagische Religion: Tanit & Baal Hammon", 3, (8,10)),
    ("Kinderopfer-Debatte & Tophet-Funde", 2, (9,10)),

    # 4 Anatolien & Nachbarn: Hethiter, Luwier, Phrygier, Urartäer
    ("Hethitische Religion: Götterversammlung & Staatskult", 4, (8,10)),
    ("Telepinu-Mythos & Fruchtbarkeitszyklen", 3, (9,10)),
    ("Luwische & anatolische Gottheiten (Tarḫunt, Arinna)", 3, (9,10)),
    ("Phrygien: Kybele & Attis-Kult", 4, (8,10)),
    ("Urartu: Festungen, Staatskult & Pantheon", 2, (8,10)),
    ("Anatolische Orakel- & Reinigungsriten", 2, (8,10)),

    # 5 Italischer Raum (vor-/nebenrömisch) & Etrusker
    ("Etruskische Religion: Disziplinen, Auguren & Haruspizes", 4, (8,10)),
    ("Etruskisches Pantheon & Jenseitsdarstellungen", 3, (7,10)),
    ("Frühitalische/italische Kulte (Sabiner, Latinum, Samniten)", 3, (8,10)),
    ("Lokale Heiligtümer & Grenzschutz-Kulte", 2, (7,10)),

    # 6 Ägäis & Balkan (außer griechische Klassik)
    ("Minoische Religion: Ikonographie (Stiersprung, Doppelaxt)", 3, (7,10)),
    ("Mykenische Vorformen: Linear B & Kultspuren", 2, (8,10)),
    ("Thrakische & dakische Kulte (Zalmoxis u. a.)", 3, (8,10)),
    ("Illyrische Gottheiten & Stammesheiligtümer", 2, (8,10)),

    # 7 Westeuropa: Keltischer & iberischer Kulturraum
    ("Keltische Mythologie: Götter, Druiden & Heiligtümer", 4, (6,10)),
    ("Insulare keltische Sagen (Irland, Wales)", 3, (7,10)),
    ("Gallische Kulte & römisch-keltischer Synkretismus", 3, (8,10)),
    ("Iberische & lusitanische Gottheiten (Endovelicus u. a.)", 2, (9,10)),
    ("Megalithische Traditionen & Kultkontinuitäten", 2, (6,10)),

    # 8 Osteuropa & Ostseeraum
    ("Slawische Mythologie: Perun, Veles & Kultlandschaften", 4, (6,10)),
    ("Baltische Religionen: Dievas/Dievs, Perkūnas/Perkons", 3, (8,10)),
    ("Kiewer Rus’ & Christianisierung – religiöse Übergänge", 2, (6,10)),
    ("Heiligtümer, heilige Haine & Prozessionen", 2, (6,10)),

    # 9 Steppenvölker & eurasische Schnittstellen
    ("Skythen & Sarmaten: Tierstil, Grabhügel & Kult", 3, (7,10)),
    ("Nomadische Jenseits- & Ahnenvorstellungen", 2, (7,10)),
    ("Transkulturelle Motive entlang der eurasischen Routen", 2, (8,10)),

    # 10 Querschnitte & Rezeption
    ("Schöpfungs-, Flut- & Heldenmotive im Vergleich", 3, (6,10)),
    ("Heilige Königtümer & Sakralherrschaft", 3, (7,10)),
    ("Schutzgötter, Orakel & Wahrsagepraktiken", 3, (6,10)),
    ("Religiöse Symbolik (Stier, Sonne, Baum, Berg, Meer)", 2, (6,9)),
    ("Antike Rezeption & spätere Umdeutungen (Mittelalter–Neuzeit)", 2, (7,10)),
    ("Archäologischer Befund vs. Schriftüberlieferung: Methodenfragen", 2, (8,10)),
]
