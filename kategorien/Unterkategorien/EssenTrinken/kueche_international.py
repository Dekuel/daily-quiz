# -*- coding: utf-8 -*-
# Unterkategorien/EssenTrinken/kueche_international.py

SUBTOPICS = [
    # ──────────────────────────────────────────────────────────────────────
    # Europa – Süd & West
    # ──────────────────────────────────────────────────────────────────────
    ("Italien: Regionen, Klassiker & DOP/IGP (Nord vs. Süd)", 4, (4, 10)),
    ("Frankreich: Saucen, Regionen & AOP/AOC (Bistros bis Haute Cuisine)", 4, (5, 10)),
    ("Spanien & Portugal: Tapas/Petiscos, Iberico, Bacalhau, DOC", 3, (4, 10)),
    ("Mittelmeer: Olivenöl, Kräuterprofile & Meeresküche (Vergleich)", 2, (1, 10)),
    # Basis
    ("Südeuropa – Basisfakten (typische Gerichte, Zutaten, Käse/Schinken)", 2, (1, 9)),

    # ──────────────────────────────────────────────────────────────────────
    # Europa – Mitteleuropa & DACH / Ost & Nord
    # ──────────────────────────────────────────────────────────────────────
    ("Mitteleuropa & DACH: Brotkultur, Knödel, Wurst & g.g.A./g.U.", 3, (4, 10)),
    ("Balkan & Osteuropa: Eintöpfe, Teigwaren, Käse- & Paprikaküche", 3, (4, 10)),
    ("Nordische Küche: New Nordic, Einlegen, Wild & Fisch", 3, (5, 10)),
    # Basis
    ("Europa – Basisfakten (Regionen erkennen, typische Produkte)", 2, (1, 9)),

    # ──────────────────────────────────────────────────────────────────────
    # Nahost & Levante, Maghreb, Afrika
    # ──────────────────────────────────────────────────────────────────────
    ("Levante & Nahost: Mezze, Tahina/Zaatar, Fladenbrote", 4, (4, 10)),
    ("Maghreb: Couscous, Harissa, Pastilla, Tajine-Traditionen", 3, (5, 10)),
    ("Äthiopien & Horn von Afrika: Injera, Berbere, Niter Kibbeh", 3, (7, 10)),
    ("West-/Zentral-/Südliches Afrika: Jollof, Erdnuss, Maniok, Braise", 3, (5, 10)),
    # Basis
    ("Afrika & Levante – Basisfakten (Gewürze, Brote, Signature-Dishes)", 2, (1, 9)),

    # ──────────────────────────────────────────────────────────────────────
    # Südasien, Zentralasien
    # ──────────────────────────────────────────────────────────────────────
    ("Indien: Regionale Masalas, Tandoor, Tiffin-Kultur (Nord/Süd/Ost/West)", 4, (5, 10)),
    ("Pakistan & Bangladesch: Karahi, Biryani-Profile, Fisch- & Senfsaat", 3, (7, 10)),
    ("Sri Lanka & Malediven: Curryblätter, Kokos, Hoppers/Pol Sambol", 2, (5, 10)),
    ("Zentralasien: Plov/Pilaw, Teigwaren, Nomadenprägungen", 2, (5, 10)),
    # Basis
    ("Südasien – Basisfakten (Grundgewürze, Brotsorten, Garmethoden)", 2, (1, 9)),

    # ──────────────────────────────────────────────────────────────────────
    # Ostasien
    # ──────────────────────────────────────────────────────────────────────
    ("China: Regionalküchen (Sichuan, Kanton, Jiangsu, Shandong) & Techniken", 4, (4, 10)),
    ("Japan: Dashi/Umami, Sushi/Sashimi, Fermentation (Miso/Shoyu)", 4, (5, 10)),
    ("Korea: Hansik-Prinzipien, Kimchi-Ökosystem & Gochujang/Doenjang", 3, (5, 10)),
    # Basis
    ("Ostasien – Basisfakten (Grundtechniken, Grundprodukte, Reis/Soja)", 2, (1, 9)),

    # ──────────────────────────────────────────────────────────────────────
    # Südostasien
    # ──────────────────────────────────────────────────────────────────────
    ("Thailand: Balance süß–sauer–salzig–scharf, Kräuter & Pasten", 4, (4, 10)),
    ("Vietnam: Kräuterfrische, Fischsauce, Pho/Bun/Com – Nord/Süd", 4, (4, 10)),
    ("Indonesien/Malaysia/Singapur: Sambal, Rendang, Nasi Lemak, Peranakan", 3, (5, 10)),
    ("Philippinen: Adobo, Sinigang, Lechon – Einflüsse & Säureprofile", 2, (5, 10)),
    # Basis
    ("Südostasien – Basisfakten (Kräuter, Saucen, Grundgerichte)", 2, (1, 9)),

    # ──────────────────────────────────────────────────────────────────────
    # Amerika – Nord, Mittel, Süd & Karibik
    # ──────────────────────────────────────────────────────────────────────
    ("Mexiko: Mais/Chili/Bohnen, Moles, regionale Vielfalt (Oaxaca/Yucatán)", 4, (4, 10)),
    ("Anden & Peru: Ceviche, Kartoffelvielfalt, Aji & Nikkei-Einflüsse", 3, (5, 10)),
    ("Brasilien: Feijoada, Farofa, Dendê, Regionalvielfalt (Nord/Nordost/Süd)", 3, (5, 10)),
    ("Karibik: Kreolisierung, Callaloo/Jerk, Rumküche", 2, (5, 10)),
    ("Nordamerika: BBQ-Regionen, Diner- & Soul-Food-Traditionen", 2, (4, 10)),
    # Basis
    ("Amerika – Basisfakten (Maiswege, Chili, Bohnen, Signature-Dishes)", 2, (1, 9)),

    # ──────────────────────────────────────────────────────────────────────
    # Ozeanien & Pazifik / Diaspora
    # ──────────────────────────────────────────────────────────────────────
    ("Ozeanien & Pazifik: Hangi, Meeresfrüchte, Wurzeln & Taro", 2, (5, 10)),
    ("Diaspora & Migration: Kreolisierung, Nikkei, Chifa, Indo-Caribbean", 3, (5, 10)),
    # Basis
    ("Pazifik & Diaspora – Basisfakten (Techniken, Zutaten, Hybridgerichte)", 2, (1, 9)),

    # ──────────────────────────────────────────────────────────────────────
    # Querschnitt & Vergleich
    # ──────────────────────────────────────────────────────────────────────
    ("Schutzsiegel international: DOP/AOP/IGP/g.U./g.g.A. – Vergleich & Beispiele", 3, (5, 10)),
    ("Streetfood weltweit: Zubereitungsprinzipien & Authentizität vs. Adaption", 3, (4, 10)),
    ("Vegetarisch/vegan traditionell: Hülsenfrüchte, Tofu/Tempeh, Jackfruit", 2, (4, 10)),
    ("Getreide & Grundnahrungen: Reis, Mais, Weizen, Hirse – regionale Rollen", 2, (1, 10)),
    ("Würz- und Fettprofile im Vergleich (Olivenöl, Ghee, Schmalz, Palmöl, Erdnuss)", 2, (5, 10)),
    # Basis (einfacher Vergleich)
    ("Küche international – Basisvergleiche (Gericht - Land/Region zuordnen)", 2, (1, 10)),
]
