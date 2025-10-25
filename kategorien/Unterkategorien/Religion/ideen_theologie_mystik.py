# -*- coding: utf-8 -*-
# Unterkategorien/Religion/ideen_theologie_mystik.py
"""
Unterthemen (Subdisciplines) für die Disziplin
„Religiöse Ideen, Theologie & Mystik“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.

Skala:
1 = absolutes Allgemeinwissen, 4 = noch recht leicht, 6 = machbar, ab 8 = komplex
"""

SUBDISCIPLINES = [
    # 1 Grundfragen religiösen Denkens
    ("Begriff Religion: Ursprung, Definition & Funktionen", 4, (4,10)),
    ("Gottesvorstellungen & Theismusformen (Mono-, Poly-, Pantheismus)", 4, (4,10)),
    ("Offenbarung, Vernunft & Glaube – Verhältnis in Theologie & Philosophie", 4, (6,10)),
    ("Religiöse Erfahrung & Transzendenz", 3, (6,10)),
    ("Symbol, Mythos & Ritual als Ausdruck religiösen Denkens", 3, (5,10)),

    # 2 Theologie in den Weltreligionen
    ("Christliche Theologie: Trinität, Schöpfung, Erlösung", 4, (6,10)),
    ("Jüdische Theologie: Bund, Gesetz & Erwählung", 4, (6,10)),
    ("Islamische Theologie (Kalām, Mutaziliten, Aschariten)", 4, (9,10)),
    ("Hinduistische Philosophie (Vedanta, Sankhya, Yoga)", 3, (8,10)),
    ("Buddhistische Philosophie (Leere, Erkenntnis, Mitgefühl)", 3, (8,10)),
    ("Konfuzianische & daoistische Lehren", 2, (7,10)),

    # 3 Religionsphilosophie & Erkenntnistheorie
    ("Philosophie der Religion (Antike bis Moderne)", 4, (6,10)),
    ("Beweise & Argumente für die Existenz Gottes", 4, (6,10)),
    ("Theodizee-Problem & Leidensfrage", 4, (6,10)),
    ("Säkularisierung & Religionskritik (Feuerbach, Marx, Nietzsche)", 4, (5,10)),
    ("Glaube und Wissen (Aquin, Kant, Kierkegaard)", 3, (8,10)),
    ("Existentialismus & Religionsdeutung im 20. Jh.", 3, (7,10)),

    # 4 Mystik (interreligiös)
    ("Mystik: Wesen, Ziel & Ausdrucksformen", 4, (6,10)),
    ("Christliche Mystik (Meister Eckhart, Johannes vom Kreuz)", 4, (8,10)),
    ("Jüdische Mystik: Kabbala & Sephiroth-Lehre", 4, (9,10)),
    ("Islamische Mystik: Sufismus & der Weg zu Gott", 4, (8,10)),
    ("Hinduistische & buddhistische Mystik (Advaita, Zen)", 3, (8,10)),
    ("Mystische Erfahrung & Sprachlosigkeit des Göttlichen", 3, (7,10)),

    # 5 Religiöse Anthropologie & Ethik
    ("Menschenbild in Religion & Theologie", 4, (5,10)),
    ("Freiheit, Sünde & Erlösung – anthropologische Konzepte", 3, (6,10)),
    ("Ethik, Moral & göttliches Gesetz", 4, (5,10)),
    ("Liebe, Mitgefühl & Gerechtigkeit als religiöse Werte", 3, (4,9)),
    ("Heiligkeit, Reinheit & Tabu", 2, (6,9)),
    ("Religiöse Tugendlehren (Glaube, Hoffnung, Liebe, Ahimsa)", 3, (6,10)),

    # 6 Interreligiöse & mystische Vergleichsperspektiven
    ("Einheits- & Erleuchtungserfahrung in verschiedenen Religionen", 4, (7,10)),
    ("Wege der Gotteserkenntnis (via negativa, via positiva)", 3, (9,10)),
    ("Gebet, Kontemplation & Meditation als religiöse Praxis", 4, (4,9)),
    ("Vergleichende Mystikforschung & moderne Psychologie", 3, (7,10)),
    ("Religiöse Symbolik & Allegorie", 2, (5,9)),

    # 7 Moderne Theologie & Religionsdebatten
    ("Liberale & politische Theologie (Bultmann, Moltmann, Küng)", 3, (7,10)),
    ("Befreiungstheologie & soziale Gerechtigkeit", 3, (7,10)),
    ("Feministische & ökologische Theologie", 3, (6,10)),
    ("Interreligiöser Dialog & pluralistische Theologien", 4, (6,10)),
    ("Neue Atheismen & säkulare Spiritualität", 3, (5,10)),

    # 8 Religion & Wissenschaft
    ("Kosmologie & Schöpfung in Religion und Naturwissenschaft", 3, (6,10)),
    ("Evolution, Bewusstsein & religiöse Deutung", 3, (7,10)),
    ("Physik & Mystik (Quantentheologie, Symbolik)", 2, (9,10)),
    ("Neurotheologie & religiöse Erfahrung", 2, (9,10)),
    ("Ethik der Technik (KI, Gentechnik, Biomedizin)", 2, (5,10)),

    # 9 Mystik & Ästhetik
    ("Musik, Kunst & Architektur als Ausdruck religiöser Erfahrung", 3, (4,9)),
    ("Ikonen, Mandalas & Symbolbilder", 3, (6,10)),
    ("Sprache, Poesie & Metapher in der Mystik", 3, (5,10)),
    ("Stille, Meditation & Raumgestaltung", 2, (4,9)),

    # 10 Einfluss & Nachwirkungen
    ("Mystik & Philosophie der Einheit (Plotin, Spinoza)", 3, (8,10)),
    ("Rezeption religiöser Ideen in Literatur & Kunst", 3, (5,10)),
    ("Mystische Traditionen in der Moderne (New Age, Esoterik)", 3, (5,9)),
    ("Psychologische Deutung mystischer Erfahrung (Jung, James)", 3, (6,10)),
]
