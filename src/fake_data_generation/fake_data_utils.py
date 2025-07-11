from faker import Faker
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Fake Data auf Deutsch verwenden
fake = Faker("de_DE")

def generate_customers(n=100):
    """
    Diese Funktion erzeugt Fake Personen-Daten, die für die Kund:innen verwendet werden
    param n: Deafult auf n = 100 gesetzt. Anzahl der Kund:innen, welche generiert werden sollen
    return: pd.DataFrame mit CustomerID, name, Geburtsdatum, Emailadresse, Datum der Registrierung
    """
    customers = []
    for i in range(n):
        customers.append({
            "customer_id": f"CUST{i:05d}",
            "name": fake.name(),
            "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=85),
            "email": fake.email(),
            "address": fake.address(),
            "registration_date": fake.date_between(start_date='-10y', end_date='today')
        })
    return pd.DataFrame(customers)

def generate_products():
    """
    Diese Funktion erzeugt Produkttypen, die für das Joinen benötit wird
    return: pd.DataFrame mit 4 verschiedenen Produkten
    """
    return pd.DataFrame([
        {"product_id": "PRD001", "product_type": "Girokonto"},
        {"product_id": "PRD002", "product_type": "Kreditkarte"},
        {"product_id": "PRD003", "product_type": "Tagesgeldkonto"},
        {"product_id": "PRD004", "product_type": "Depot"}
    ])

def generate_transactions(customers_df, products_df, n=1000):
    """
    Diese Funktion erzeugt Fake Transaktionen.
    Diese Transaktionen bestehen aus 
        - einer Transaktions-ID
        - Customer-ID (diese wird zufällig aus den Fake Kund:innen gezogen)
        - Proudkt-ID (diese wird zufällig aus den Fake Produkten gezogen)
        - Betrag
        - Währung ist immer auf EUR gesetzt
        - Betreff. Hier wird von fake die Methode sentence verwendet mit einer Länge von 4 Wörtern

    param customer_df: Hier soll der Output aus der Methode generate_customers() eingesetezt werden
    param products_df: Hier soll der Output aus der Methode generate_products() eingesetzt werden
    param n: Ist default auf 1000 gesetzt
    return: Ein pd.DataFrame das Fake-Transaktionen enthält
    """
    transactions = []
    for _ in range(n):
        customer = customers_df.sample(1).iloc[0]
        product = products_df.sample(1).iloc[0]
        amount = round(np.random.normal(loc=100, scale=200), 2)
        amount = max(min(amount, 10000), -10000)  # Begrenzung
        transactions.append({
            "transaction_id": f"TX{random.randint(100000, 999999)}",
            "customer_id": customer["customer_id"],
            "product_id": product["product_id"],
            "transaction_date": fake.date_time_between(start_date='-5y', end_date='now'),
            "amount": amount,
            "currency": "EUR",
            "description": fake.sentence(nb_words=4)
        })
    return pd.DataFrame(transactions)
