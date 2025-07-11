import fake_data_utils;

# Generierung
customers_df = fake_data_utils.generate_customers(1000)
products_df = fake_data_utils.generate_products()
transactions_df = fake_data_utils.generate_transactions(customers_df, products_df, 1000)


# customers_df.to_csv("data/raw/customers.csv", index=False)
# products_df.to_csv("data/raw/products.csv", index=False)
transactions_df.to_csv("data/raw/transactions.csv", index=False)