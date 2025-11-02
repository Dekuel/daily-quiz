# -*- coding: utf-8 -*-
# Unterkategorien/KunstLiteratur/moderne_zeitgenoessische_kunst.py
"""
Unterthemen (Subdisciplines) für die Disziplin „Moderne & Zeitgenössische Kunst“.
Diese Liste wird von kategorien/kunst_literatur.py importiert und dient als
Datenquelle für die Subthema-Auswahl im Prompt.

==========================================================================
GENERATION_SYSTEM – Wie Kategorien & Schwierigkeitsbereiche erzeugt werden
==========================================================================
Kurzfassung: Ein konsistentes Schema definiert Subkategorien mit Gewichten
(4 = Kernfelder, 3 = Vertiefungen, 2 = Standard/Umfeld) und realistischen
Schwierigkeitsintervallen (1–10) entlang der Achsen Bekanntheit & Komplexität.
Mindestens eine „Basis“-Kategorie pro Bereich erlaubt Level-1-Fragen.
"""

# Schwierigkeits-Skala kurz (zur Laufzeit nutzbar):
# 1=Allgemeinwissen … 10=schwerstmöglich.

SUBDISCIPLINES = [
    # 1) Überblick & Grundbegriffe der Moderne/Gegenwart
    ("Moderne vs. Zeitgenössische Kunst: Periodisierung, Institutionen, Märkte", 3, (5,10)),
    ("Avantgarde, Neo-Avantgarde & Postmoderne: Linien und Brüche", 3, (7,10)),
    ("Materialturn & Prozesskunst: Ephemeres, Site-Specific, Kontext", 3, (7,10)),
    # ⚑ Basis
    ("Moderne/Gegenwart – Basis (Ikonen & Schlagworte schnell zuordnen: Pop Art, Minimal, Performance)", 2, (1,10)),

    # 2) Fotografie (analog/digital)
    ("Fotografie 1900–1945: Piktorialismus, Neue Sachlichkeit, Surrealismus", 3, (5,10)),
    ("Dokumentarische & künstlerische Fotografie nach 1945", 3, (7,10)),
    ("Porträt, Street, Konzeptfotografie: Becher-Schule & Düsseldorfer Fotografie", 3, (7,10)),
    ("Zeitgenössische Fotografie: Cindy Sherman, Andreas Gursky, Thomas Struth", 4, (5,10)),
    # ⚑ Basis
    ("Fotografie – Basis (Genres, Dunkelkammer/ISO/RAW, ikonische Serien erkennen)", 2, (1,10)),

    # 3) Installation, Environment & Skulptur nach 1960
    ("Installationskunst: Raum, Immersion, Partizipation (Kaprow bis Höller)", 4, (7,10)),
    ("Land Art & Environmental Art: Smithson, Heizer, De Maria", 3, (8,10)),
    ("Licht- und Klanginstallation: Turrell, Eliasson, Cardiff", 3, (7,10)),
    ("Soziale Plastik & partizipative Praktiken (Beuys, Tiravanija)", 3, (8,10)),
    # ⚑ Basis
    ("Installation – Basis (Begriffe: Site-specific, Ready-made, White Cube)", 2, (1,10)),

    # 4) Performance & Body Art
    ("Performance-Kunst: Happenings, Fluxus, Kaprow, Ono", 3, (7,10)),
    ("Body Art & Risikoästhetik: Marina Abramović, Chris Burden, ORLAN", 4, (8,10)),
    ("Queere & feministische Performance: VALIE EXPORT, Guerrilla Girls", 3, (7,10)),
    # ⚑ Basis
    ("Performance – Basis (Aktion vs. Dokumentation; Live-Moment, Publikum)", 2, (1,10)),

    # 5) Konzeptkunst, Minimal & Post-Konzept
    ("Konzeptkunst: Sprache, System, Idee (Kosuth, Weiner, Huebler)", 4, (8,10)),
    ("Minimal Art: Reduktion & Serialität (Judd, Andre, LeWitt)", 4, (7,10)),
    ("Institutionelle Kritik & Appropriation (Buren, Haacke, Levine)", 3, (8,10)),
    ("Relationale Ästhetik & Post-Konzept (Bourriaud, Tiravanija)", 3, (8,10)),
    # ⚑ Basis
    ("Konzept/Minimal – Basis (Objekt vs. Idee, Gitter/Modul/Serie)", 2, (1,10)),

    # 6) Pop, Neo-Expressionismus & Malerei seit 1960
    ("Pop Art: Warhol, Lichtenstein, Hamilton – Reproduktion & Massenkultur", 4, (3,10)),
    ("Neo-Expressionismus & Neue Wilde: Baselitz, Kiefer, Schnabel", 3, (7,10)),
    ("Abstrakter Expressionismus → Post-Painterly → Farbfeld: Übergänge", 3, (7,10)),
    ("Zeitgenössische Malerei global (Nigeria, China, Leipzig-Schule, u. a.)", 3, (7,10)),
    # ⚑ Basis
    ("Malerei – Basis (Pop-Ikonen, Dripping, Farbfeld schnell erkennen)", 2, (1,10)),

    # 7) Street Art, Graffiti & Public Art
    ("Graffiti-Kulturen: Tags, Throw-ups, Pieces – Geschichte & Ethik", 3, (5,10)),
    ("Street Art: Banksy, Shepard Fairey, JR – Politiken & Öffentlichkeit", 4, (3,10)),
    ("Murals, Intervention & Community Art: Siqueiros bis heutige Projekte", 3, (5,10)),
    # ⚑ Basis
    ("Street Art – Basis (Stencil, Paste-up, Legal vs. Illegal, ikonische Motive)", 2, (1,10)),

    # 8) Video-, Medien- & Digitale Kunst
    ("Videokunst: von Nam June Paik bis Hito Steyerl", 4, (7,10)),
    ("Net-Art & Plattformästhetiken: frühes Web bis Social Media", 3, (8,10)),
    ("AR/VR/XR-Kunst & Immersion: Interface, Präsenz, Sensorik", 3, (8,10)),
    ("KI-/Algorithmische Kunst & Generative Verfahren", 3, (8,10)),
    # ⚑ Basis
    ("Medienkunst – Basis (Loop, Projection Mapping, Interface/Interaktion)", 2, (1,10)),

    # 9) Globale Gegenwart & Geopolitiken
    ("China & Ostasien: Ai Weiwei, Cao Fei, Yoshitomo Nara, teamLab", 3, (5,10)),
    ("Süd-/Südostasien: Nalini Malani, Rirkrit Tiravanija, FX Harsono", 2, (7,10)),
    ("Afrika & Diaspora: El Anatsui, Yinka Shonibare, Zanele Muholi", 3, (5,10)),
    ("Lateinamerika: Tarsila, Lygia Clark/Pape, Doris Salcedo", 3, (7,10)),
    ("Nahost & Nordafrika: Mona Hatoum, Shirin Neshat, Larissa Sansour", 2, (7,10)),
    # ⚑ Basis
    ("Global Contemporary – Basis (Biennalen, Documenta, Marktzentren)", 2, (1,10)),

    # 10) Diskurse, Politik & Ökologie
    ("Feministische & queere Kunsttheorien (Überblick, Positionen, Werke)", 3, (7,10)),
    ("Postkoloniale & dekoloniale Perspektiven (Theorie & Praxis)", 3, (8,10)),
    ("Ökologie & Anthropozän in der Kunst: Nachhaltigkeit, Materialkritik", 3, (7,10)),
    ("Protest, Aktivismus & Kunstfreiheit (Zensur, Exil, Public Sphere)", 3, (7,10)),
    # ⚑ Basis
    ("Diskurse – Basis (Begriffe: Gaze, Othering, Care, Commons)", 2, (1,10)),

    # 11) Institutionen, Markt & Kuratieren
    ("Museen, Off-Spaces & Biennalen: Formate, Displays, Publikum", 2, (5,10)),
    ("Kunstmarkt: Galerie-System, Auktionshäuser, Editionen, NFTs", 2, (7,10)),
    ("Kuratieren & Ausstellungsdesign: Narrativ, Szenografie, Vermittlung", 2, (7,10)),
    ("Provenienz, Restitution & Kulturpolitik (Gegenwart)", 2, (8,10)),
    # ⚑ Basis
    ("Institutionen – Basis (White Cube, Blockbuster-Schau, Edition vs. Unikat)", 2, (1,10)),

    # 12) Künstler:innen-Fokus (Auswahl, ikonische Positionen)
    ("Marcel Duchamp bis heute: Ready-made-Genealogie", 3, (7,10)),
    ("Joseph Beuys & Erweiterter Kunstbegriff", 3, (7,10)),
    ("Marina Abramović & Performance-Kanon", 3, (7,10)),
    ("Andy Warhol & Pop-Strategien", 3, (3,10)),
    ("Damien Hirst & YBAs: Spektakel, Markt, Kritik", 2, (7,10)),
    ("Banksy & Politiken der Anonymität", 3, (3,10)),
    ("Olafur Eliasson & Wahrnehmung/Ökologie", 2, (5,10)),
    ("Ai Weiwei & Aktivismus/Materialkultur", 3, (5,10)),
    ("Kara Walker, Theaster Gates, Njideka Akunyili Crosby – Erinnerung & Community", 2, (7,10)),
    # ⚑ Basis
    ("Künstler:innen – Basis (Signaturwerke & Erkennungsmerkmale zuordnen)", 2, (1,10)),

    # 13) Methoden, Analyse & Vergleich
    ("Werk-, Stil- & Diskursanalyse zeitgenössischer Arbeiten", 3, (8,10)),
    ("Vergleich: Installation vs. Skulptur; Performance vs. Theater", 2, (7,10)),
    ("Ethik & Dokumentation in Performance/partizipativer Kunst", 2, (8,10)),
    ("Publikumserfahrung & Atmosphären (Relationale Settings)", 2, (7,10)),
    # ⚑ Basis
    ("Analyse – Basis (Werkfragen: Medium? Ort? Dauer? Interaktion?)", 2, (1,10)),
]
