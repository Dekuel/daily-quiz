# -*- coding: utf-8 -*-
# Unterkategorien/Religion/klassisch_nordisch.py
"""
Unterthemen (Subdisciplines) für „Klassische & nordische Mythologien“.
Systematik gemäß dem einheitlichen GENERATION_SYSTEM (vgl. monotheismus.py):

- min-Wert = Bekanntheit (Population Familiarity)
- max-Wert = inhaltliche Tiefe / Komplexität
- 1 = Allgemeinwissen, 10 = Expertenniveau
- „Basis…“-Kategorien ermöglichen Level-1-Fragen (Zuordnung, Symbol, Name etc.)
- Maxima sind grundsätzlich bis 10 angesetzt, da diese Bereiche
  in Forschung, Quellenlage und Interpretation nahezu unendlich vertieft werden können.
"""

SUBDISCIPLINES = [
    # 1 Überblick & Charakteristika
    ("Antike und nordische Mythologien: Überblick & kulturelle Bedeutung", 4, (2,10)),
    ("Polytheismus, Kult & Mythenerzählung", 4, (2,10)),
    ("Helden, Götter & Schöpfungserzählungen im Vergleich", 3, (3,10)),
    ("Mythos, Religion & Philosophie – Abgrenzung", 3, (4,10)),
    # ⚑ Basis
    ("Basiswissen Klassische/Nordische Mythologien – Zuordnungen, Hauptgötter, Symbole", 2, (1,7)),

    # 2 Griechische Mythologie
    ("Griechische Mythologie: Ursprung & Quellen (Homer, Hesiod)", 4, (3,10)),
    ("Olympische Götter: Zeus, Hera, Poseidon, Athena, Apollon, Artemis", 4, (1,9)),
    ("Titanen, Chaos & Schöpfungsmythos", 3, (5,10)),
    ("Helden & Sagenzyklen (Herakles, Perseus, Theseus)", 4, (2,10)),
    ("Trojanischer Krieg & Odyssee", 4, (2,10)),
    ("Unterwelt & Jenseitsvorstellungen (Hades, Persephone)", 3, (4,10)),
    ("Orakel, Kulte & Heiligtümer (Delphi, Eleusis, Olympia)", 3, (4,10)),
    ("Mythologische Symbole & Allegorien", 2, (2,9)),
    # ⚑ Basis
    ("Griechische Mythologie – Basisfakten (Götter, Orte, Attribute)", 2, (1,7)),

    # 3 Römische Religion & Mythologie
    ("Römische Religion: Staatskult & Priesterwesen", 3, (6,10)),
    ("Römische Götterwelt: Jupiter, Juno, Mars, Venus, Diana", 4, (2,9)),
    ("Adoption & Anpassung griechischer Mythen", 3, (5,10)),
    ("Kaiser- und Ahnenkult", 3, (7,10)),
    ("Römische Feste & Rituale (Saturnalien, Lupercalien)", 2, (2,9)),
    ("Mysteriensysteme im Römischen Reich (Mithras, Isis, Kybele)", 3, (8,10)),
    # ⚑ Basis
    ("Römische Mythologie – Basis (Götternamen, Feiertage, Orte)", 2, (1,7)),

    # 4 Ägyptische Mythologie
    ("Ägyptische Mythologie: Quellen & kosmische Ordnung (Ma’at)", 4, (5,10)),
    ("Hauptgötter: Ra, Osiris, Isis, Horus, Anubis, Thot", 4, (2,10)),
    ("Schöpfungsmythen von Heliopolis, Hermopolis & Memphis", 3, (6,10)),
    ("Totenkult, Jenseits & das Buch der Toten", 4, (4,10)),
    ("Pharao als göttlicher Herrscher", 3, (6,10)),
    ("Tempel, Priesterschaft & Rituale", 3, (5,10)),
    ("Symbolik: Sonne, Nil, Skarabäus, Ankh", 2, (2,9)),
    # ⚑ Basis
    ("Ägyptische Mythologie – Basis (Symbole, Götter, Unterwelt)", 2, (1,7)),

    # 5 Nordische Mythologie
    ("Nordische Mythologie: Quellen (Edda, Snorri Sturluson)", 4, (5,10)),
    ("Götterwelt: Odin, Thor, Loki, Freyja, Frigg", 4, (2,10)),
    ("Schöpfung & Weltenbaum (Yggdrasil)", 4, (4,10)),
    ("Riesen, Zwerge & mythische Wesen", 3, (4,10)),
    ("Ragnarök & Weltenende", 4, (5,10)),
    ("Helden- & Sagenstoffe (Siegfried, Nibelungenlied)", 3, (4,10)),
    ("Runen, Magie & Kultpraxis", 3, (8,10)),
    ("Nordische Kosmologie & Ethik", 2, (6,10)),
    # ⚑ Basis
    ("Nordische Mythologie – Basis (Götternamen, Symbole, Orte)", 2, (1,7)),

    # 6 Vergleich & Rezeption
    ("Gemeinsamkeiten klassischer und nordischer Mythen", 3, (5,10)),
    ("Mythologische Archetypen (Held, Schöpfung, Unterwelt)", 3, (3,10)),
    ("Einfluss auf Kunst, Literatur & Philosophie (Antike–Moderne)", 3, (4,10)),
    ("Mythologische Motive in moderner Popkultur (Marvel, Tolkien, Wagner)", 3, (2,9)),
    ("Synkretismus & Übergang zu monotheistischen Religionen", 3, (8,10)),
    ("Vergleich & Rezeption – Basis (Zuordnungen, Motive, Figuren)", 2, (1,7)),
]
