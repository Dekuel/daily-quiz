# -*- coding: utf-8 -*-
# Unterkategorien/Religion/ideen_theologie_mystik.py
"""
Unterthemen (Subdisciplines) für die Disziplin
„Religiöse Ideen, Theologie & Mystik“.
Diese Liste wird von kategorien/glaube_religion.py importiert und dient als Datenquelle
für die Subthema-Auswahl im Prompt.
Gewichte (Heuristik):
- 4 = Kernkonzepte / sehr fragentauglich
- 3 = wichtige Vertiefungen
- 2 = Standard-Unterthemen
- 1 = Kontext oder Zusatzaspekte
"""

SUBDISCIPLINES = [
    # 1 Grundfragen religiösen Denkens
    ("Begriff Religion: Ursprung, Definition & Funktionen", 4),
    ("Gottesvorstellungen & Theismusformen (Mono-, Poly-, Pantheismus)", 4),
    ("Offenbarung, Vernunft & Glaube – Verhältnis in Theologie & Philosophie", 4),
    ("Religiöse Erfahrung & Transzendenz", 3),
    ("Symbol, Mythos & Ritual als Ausdruck religiösen Denkens", 3),

    # 2 Theologie in den Weltreligionen
    ("Christliche Theologie: Trinität, Schöpfung, Erlösung", 4),
    ("Jüdische Theologie: Bund, Gesetz & Erwählung", 4),
    ("Islamische Theologie (Kalām, Mutaziliten, Aschariten)", 4),
    ("Hinduistische Philosophie (Vedanta, Sankhya, Yoga)", 3),
    ("Buddhistische Philosophie (Leere, Erkenntnis, Mitgefühl)", 3),
    ("Konfuzianische & daoistische Lehren", 2),

    # 3 Religionsphilosophie & Erkenntnistheorie
    ("Philosophie der Religion (Antike bis Moderne)", 4),
    ("Beweise & Argumente für die Existenz Gottes", 4),
    ("Theodizee-Problem & Leidensfrage", 4),
    ("Säkularisierung & Religionskritik (Feuerbach, Marx, Nietzsche)", 4),
    ("Glaube und Wissen (Aquin, Kant, Kierkegaard)", 3),
    ("Existentialismus & Religionsdeutung im 20. Jh.", 3),

    # 4 Mystik (interreligiös)
    ("Mystik: Wesen, Ziel & Ausdrucksformen", 4),
    ("Christliche Mystik (Meister Eckhart, Johannes vom Kreuz)", 4),
    ("Jüdische Mystik: Kabbala & Sephiroth-Lehre", 4),
    ("Islamische Mystik: Sufismus & der Weg zu Gott", 4),
    ("Hinduistische & buddhistische Mystik (Advaita, Zen)", 3),
    ("Mystische Erfahrung & Sprachlosigkeit des Göttlichen", 3),

    # 5 Religiöse Anthropologie & Ethik
    ("Menschenbild in Religion & Theologie", 4),
    ("Freiheit, Sünde & Erlösung – anthropologische Konzepte", 3),
    ("Ethik, Moral & göttliches Gesetz", 4),
    ("Liebe, Mitgefühl & Gerechtigkeit als religiöse Werte", 3),
    ("Heiligkeit, Reinheit & Tabu", 2),
    ("Religiöse Tugendlehren (Glaube, Hoffnung, Liebe, Ahimsa)", 3),

    # 6 Interreligiöse & mystische Vergleichsperspektiven
    ("Einheits- & Erleuchtungserfahrung in verschiedenen Religionen", 4),
    ("Wege der Gotteserkenntnis (via negativa, via positiva)", 3),
    ("Gebet, Kontemplation & Meditation als religiöse Praxis", 4),
    ("Vergleichende Mystikforschung & moderne Psychologie", 3),
    ("Religiöse Symbolik & Allegorie", 2),

    # 7 Moderne Theologie & Religionsdebatten
    ("Liberale & politische Theologie (Bultmann, Moltmann, Küng)", 3),
    ("Befreiungstheologie & soziale Gerechtigkeit", 3),
    ("Feministische & ökologische Theologie", 3),
    ("Interreligiöser Dialog & pluralistische Theologien", 4),
    ("Neue Atheismen & säkulare Spiritualität", 3),

    # 8 Religion & Wissenschaft
    ("Kosmologie & Schöpfung in Religion und Naturwissenschaft", 3),
    ("Evolution, Bewusstsein & religiöse Deutung", 3),
    ("Physik & Mystik (Quantentheologie, Symbolik)", 2),
    ("Neurotheologie & religiöse Erfahrung", 2),
    ("Ethik der Technik (KI, Gentechnik, Biomedizin)", 2),

    # 9 Mystik & Ästhetik
    ("Musik, Kunst & Architektur als Ausdruck religiöser Erfahrung", 3),
    ("Ikonen, Mandalas & Symbolbilder", 3),
    ("Sprache, Poesie & Metapher in der Mystik", 3),
    ("Stille, Meditation & Raumgestaltung", 2),

    # 10 Einfluss & Nachwirkungen
    ("Mystik & Philosophie der Einheit (Plotin, Spinoza)", 3),
    ("Rezeption religiöser Ideen in Literatur & Kunst", 3),
    ("Mystische Traditionen in der Moderne (New Age, Esoterik)", 3),
    ("Psychologische Deutung mystischer Erfahrung (Jung, James)", 3),
]
