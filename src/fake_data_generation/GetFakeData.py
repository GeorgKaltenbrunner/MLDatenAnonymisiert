import fake_data_utils;

# Generierung von 50.000 Fake Kund:innen und 500.000 Fake Transkationen
customers_df = fake_data_utils.generate_customers(50_000)
products_df = fake_data_utils.generate_products()
transactions_df = fake_data_utils.generate_transactions(customers_df, products_df, 500_000)


customers_df.to_csv("data/raw/customers.csv", index=False)
products_df.to_csv("data/raw/products.csv", index=False)
transactions_df.to_csv("data/raw/transactions.csv", index=False)