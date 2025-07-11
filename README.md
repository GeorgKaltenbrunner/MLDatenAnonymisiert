# MLDatenAnonymisiert
ML mit anonymisierten Daten. Was ist der aktuelle Stand, wie schaut die Performance von Modellen aus?

# Welche Merkmale sind sensibel?
customer_id -> Ja
credit_score -> Nur in Kombination
country -> Nur in Kombination
gender -> Ja
age -> Ja
tenure (Verweildauer bei der Bank) -> Möglich
balance -> Nur in Kombination
products_number -> Nur in Kombination
credit_card -> Sensibel
active_member -> Nur in Kombination
estimated_salary -> Ja

# Methodik
1. Datensätze
 - Keine Anonymisierung
- Sensible Merkmale (Siehe oben) werden in Gruppen / Klassen zusammengefasst, wo möglich
- Sensible Daten werden entfernt

2. Modelle
- Logistische Regression
- Random Forest
- Boosting

3. Feature Engineering (wo möglich)
- Age -> Gruppen (besser für Tree Modelle)
- credit_score -> in ein Band einteilen
- estimated_salary -> in Quartile
- tenure -> hier Aufteilen in junge Kund:innen und alte Kund:innen
