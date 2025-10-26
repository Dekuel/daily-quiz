# -*- coding: utf-8 -*-
# Unterkategorien/Religion/ideen_theologie_mystik.py
"""
Unterthemen (Subdisciplines) für die Disziplin
„Religiöse Ideen, Theologie & Mystik“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================
Systematik wie in monotheismus.py:
- min = Bekanntheit (Population Familiarity)   → wie „breit“ Basiswissen vorhanden ist
- max = inhaltliche/methodische Komplexität    → wie tief die Materie geht
- Skala 1–10: 1 = Allgemeinwissen, 10 = Expertenwissen
- „Basis…“-Kategorien haben immer min = 1 (Zuordnungen, einfache Begriffe/Symbole)
- Nicht-Basis-Themen gehen i. d. R. bis 10, da vertiefbar

Hinweis: Einige Bereiche (z. B. Kabbala, Kalām, via negativa) starten bewusst hoch (min ≥ 7),
weil sowohl Bekanntheit gering als auch Einstiegskompetenz hoch ist.
"""

SUBDISCIPLINES = [
    # 1 Grundfragen religiösen Denkens
    ("Begriff Religion: Ursprung, Definition & Funktionen", 4, (2,10)),
    ("Gottesvorstellungen & Theismusformen (Mono-, Poly-, Pan-, Deismus)", 4, (2,10)),
    ("Offenbarung, Vernunft & Glaube – Verhältnis in Theologie & Philosophie", 4, (4,10)),
    ("Religiöse Erfahrung & Transzendenz", 3, (4,10)),
    ("Symbol, Mythos & Ritual als Ausdruck religiösen Denkens", 3, (3,10)),
    # ⚑ Basis
    ("Basiswissen – Religion & Grundbegriffe (Gott, Kult, Ritual, Mythos)", 2, (1,7)),

    # 2 Theologie in den Weltreligionen
    ("Christliche Theologie: Trinität, Schöpfung, Erlösung", 4, (3,10)),
    ("Jüdische Theologie: Bund, Gesetz & Erwählung", 4, (4,10)),
    ("Islamische Theologie (Kalām, Muʿtaziliten, Ašʿariten)", 4, (8,10)),
    ("Hinduistische Philosophie (Vedānta, Sāṃkhya, Yoga)", 3, (6,10)),
    ("Buddhistische Philosophie (Śūnyatā/Leere, Prajñā/Erkenntnis, Karuṇā/ Mitgefühl)", 3, (6,10)),
    ("Konfuzianische & daoistische Lehren", 2, (5,10)),
    # ⚑ Basis
    ("Theologien – Basis (heilige Schriften, Kernbegriffe, zentrale Lehren)", 2, (1,7)),

    # 3 Religionsphilosophie & Erkenntnistheorie
    ("Philosophie der Religion (Antike–Moderne)", 4, (4,10)),
    ("Beweise & Argumente für die Existenz Gottes", 4, (4,10)),
    ("Theodizee-Problem & Leidensfrage", 4, (4,10)),
    ("Säkularisierung & Religionskritik (Feuerbach, Marx, Nietzsche)", 4, (3,10)),
    ("Glaube und Wissen (Aquin, Kant, Kierkegaard)", 3, (6,10)),
    ("Existentialismus & Religionsdeutung im 20. Jh.", 3, (6,10)),
    # ⚑ Basis
    ("Religionsphilosophie – Basis (Begriffe, Hauptpositionen, Denker)", 2, (1,7)),

    # 4 Mystik (interreligiös)
    ("Mystik: Wesen, Ziel & Ausdrucksformen", 4, (4,10)),
    ("Christliche Mystik (Meister Eckhart, Johannes vom Kreuz)", 4, (6,10)),
    ("Jüdische Mystik: Kabbala & Sefirot-Lehre", 4, (8,10)),
    ("Islamische Mystik: Sufismus & der Weg zu Gott", 4, (6,10)),
    ("Hinduistische & buddhistische Mystik (Advaita, Zen)", 3, (6,10)),
    ("Mystische Erfahrung & die Sprachlosigkeit des Göttlichen", 3, (6,10)),
    # ⚑ Basis
    ("Mystik – Basis (Vokabular, Symbole, Praktiken, Hauptgestalten)", 2, (1,7)),

    # 5 Religiöse Anthropologie & Ethik
    ("Menschenbild in Religion & Theologie", 4, (3,10)),
    ("Freiheit, Sünde & Erlösung – anthropologische Konzepte", 3, (4,10)),
    ("Ethik, Moral & göttliches Gesetz", 4, (3,10)),
    ("Liebe, Mitgefühl & Gerechtigkeit als religiöse Werte", 3, (2,9)),
    ("Heiligkeit, Reinheit & Tabu", 2, (4,9)),
    ("Religiöse Tugendlehren (Glaube, Hoffnung, Liebe; Ahimsa u. a.)", 3, (4,10)),
    # ⚑ Basis
    ("Anthropologie/Ethik – Basis (Begriffe, Beispiele, Zuordnungen)", 2, (1,7)),

    # 6 Interreligiöse & mystische Vergleichsperspektiven
    ("Einheits- & Erleuchtungserfahrung in verschiedenen Religionen", 4, (5,10)),
    ("Wege der Gotteserkenntnis (via negativa/apophatisch, via positiva/kataphatisch)", 3, (7,10)),
    ("Gebet, Kontemplation & Meditation als religiöse Praxis", 4, (2,9)),
    ("Vergleichende Mystikforschung & moderne Psychologie", 3, (6,10)),
    ("Religiöse Symbolik & Allegorie", 2, (3,9)),
    # ⚑ Basis
    ("Vergleich – Basis (einfache Zuordnungen von Motiven/Praktiken)", 2, (1,7)),

    # 7 Moderne Theologie & Religionsdebatten
    ("Liberale & politische Theologie (Bultmann, Moltmann, Küng)", 3, (6,10)),
    ("Befreiungstheologie & soziale Gerechtigkeit", 3, (6,10)),
    ("Feministische & ökologische Theologie", 3, (5,10)),
    ("Interreligiöser Dialog & pluralistische Theologien", 4, (4,10)),
    ("Neue Atheismen & säkulare Spiritualität", 3, (4,10)),
    # ⚑ Basis
    ("Moderne Debatten – Basis (Schlagworte, Vertreter, Kernthesen)", 2, (1,7)),

    # 8 Religion & Wissenschaft
    ("Kosmologie & Schöpfung in Religion und Naturwissenschaft", 3, (5,10)),
    ("Evolution, Bewusstsein & religiöse Deutung", 3, (6,10)),
    ("Physik & Mystik (‚Quantentheologie‘, Symbolik) – Diskussionen & Kritik", 2, (8,10)),
    ("Neurotheologie & religiöse Erfahrung", 2, (8,10)),
    ("Ethik der Technik (KI, Gentechnik, Biomedizin)", 2, (4,10)),
    # ⚑ Basis
    ("Religion & Wissenschaft – Basis (Begriffe, Konfliktlinien, Beispiele)", 2, (1,7)),

    # 9 Mystik & Ästhetik
    ("Musik, Kunst & Architektur als Ausdruck religiöser Erfahrung", 3, (3,9)),
    ("Ikonen, Mandalas & Symbolbilder", 3, (4,10)),
    ("Sprache, Poesie & Metapher in der Mystik", 3, (4,10)),
    ("Stille, Meditation & Raumgestaltung", 2, (2,9)),
    # ⚑ Basis
    ("Ästhetik – Basis (einfache Symbol-/Stilzuordnungen)", 2, (1,7)),

    # 10 Einfluss & Nachwirkungen
    ("Mystik & Philosophie der Einheit (Plotin, Spinoza)", 3, (7,10)),
    ("Rezeption religiöser Ideen in Literatur & Kunst", 3, (4,10)),
    ("Mystische Traditionen in der Moderne (New Age, Esoterik)", 3, (4,9)),
    ("Psychologische Deutung mystischer Erfahrung (Jung, James)", 4, (6,10)),
    # ⚑ Basis
    ("Einfluss/Nachwirkung – Basis (Autor–Idee–Epoche zuordnen)", 2, (1,7)),
]
