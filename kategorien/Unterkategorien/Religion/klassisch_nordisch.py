# -*- coding: utf-8 -*-
# Unterkategorien/Religion/klassisch_nordisch.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Klassische & nordische Mythologien“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte
"""

SUBDISCIPLINES = [
    # 1 Überblick & Charakteristika
    ("Antike und nordische Mythologien: Überblick & kulturelle Bedeutung", 4),
    ("Polytheismus, Kult & Mythenerzählung", 4),
    ("Helden, Götter & Schöpfungserzählungen im Vergleich", 3),
    ("Mythos, Religion & Philosophie – Abgrenzung", 3),

    # 2 Griechische Mythologie
    ("Griechische Mythologie: Ursprung & Quellen (Homer, Hesiod)", 4),
    ("Olympische Götter: Zeus, Hera, Poseidon, Athena, Apollon, Artemis", 4),
    ("Titanen, Chaos & Schöpfungsmythos", 3),
    ("Helden & Sagenzyklen (Herakles, Perseus, Theseus)", 4),
    ("Trojanischer Krieg & Odyssee", 4),
    ("Unterwelt & Jenseitsvorstellungen (Hades, Persephone)", 3),
    ("Orakel, Kulte & Heiligtümer (Delphi, Eleusis, Olympia)", 3),
    ("Mythologische Symbole & Allegorien", 2),

    # 3 Römische Religion & Mythologie
    ("Römische Religion: Staatskult & Priesterwesen", 3),
    ("Römische Götterwelt: Jupiter, Juno, Mars, Venus, Diana", 4),
    ("Adoption & Anpassung griechischer Mythen", 3),
    ("Kaiser- und Ahnenkult", 3),
    ("Römische Feste & Rituale (Saturnalien, Lupercalien)", 2),
    ("Mysteriensysteme im Römischen Reich (Mithras, Isis, Kybele)", 3),

    # 4 Ägyptische Mythologie
    ("Ägyptische Mythologie: Quellen & kosmische Ordnung (Ma’at)", 4),
    ("Hauptgötter: Ra, Osiris, Isis, Horus, Anubis, Thot", 4),
    ("Schöpfungsmythen von Heliopolis, Hermopolis & Memphis", 3),
    ("Totenkult, Jenseits & das Buch der Toten", 4),
    ("Pharao als göttlicher Herrscher", 3),
    ("Tempel, Priesterschaft & Rituale", 3),
    ("Symbolik: Sonne, Nil, Skarabäus, Ankh", 2),

    # 5 Nordische Mythologie
    ("Nordische Mythologie: Quellen (Edda, Snorri Sturluson)", 4),
    ("Götterwelt: Odin, Thor, Loki, Freyja, Frigg", 4),
    ("Schöpfung & Weltenbaum (Yggdrasil)", 4),
    ("Riesen, Zwerge & mythische Wesen", 3),
    ("Ragnarök & Weltenende", 4),
    ("Helden- & Sagenstoffe (Siegfried, Nibelungenlied)", 3),
    ("Runen, Magie & Kultpraxis", 3),
    ("Nordische Kosmologie & Ethik", 2),

    # 6 Vergleich & Rezeption
    ("Gemeinsamkeiten klassischer und nordischer Mythen", 3),
    ("Mythologische Archetypen (Held, Schöpfung, Unterwelt)", 3),
    ("Einfluss auf Kunst, Literatur & Philosophie (Antike–Moderne)", 3),
    ("Mythologische Motive in moderner Popkultur (Marvel, Tolkien, Wagner)", 3),
    ("Synkretismus & Übergang zu monotheistischen Religionen", 2),
]
