import pandas as pd
import numpy as np
import random
from faker import Faker
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from logs.logger_config import logger

fake = Faker()

# MySQL connection
engine = create_engine(f"mysql+pymysql://root:Buddy!001@localhost/ecommerce_db")

# -------------------
# 1. Generate Customers
# -------------------
num_customers = 200
customers = []

for i in range(1, num_customers + 1):
    customers.append({
        "customer_id": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email() if random.random() > 0.05 else None,  # 5% missing
        "signup_date": fake.date_between(start_date='-2y', end_date='today'),
        "country": fake.country() if random.random() > 0.03 else None  # 3% missing
    })

df_customers = pd.DataFrame(customers)

# Introduce messy names
df_customers.loc[random.sample(range(len(df_customers)), 10), "first_name"] = df_customers["first_name"].str.upper()
df_customers.loc[random.sample(range(len(df_customers)), 10), "last_name"] = df_customers["last_name"] + "  "

# -------------------
# 2. Generate Products
# -------------------
categories = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Sports"]
num_products = 50
products = []

for i in range(1, num_products + 1):
    price = round(random.uniform(5, 500), 2)
    if random.random() < 0.02:  # 2% missing price
        price = None
    products.append({
        "product_id": i,
        "product_name": fake.word().capitalize(),
        "category": random.choice(categories),
        "price": price
    })

df_products = pd.DataFrame(products)

# -------------------
# 3. Generate Orders
# -------------------
num_orders = 1000
orders = []

for i in range(1, num_orders + 1):
    cust_id = random.randint(1, num_customers)
    prod_id = random.randint(1, num_products)
    qty = random.randint(1, 5)
    price = df_products.loc[df_products["product_id"] == prod_id, "price"].values[0]
    total = qty * price if price else None
    if random.random() < 0.01:  # introduce outlier (huge amount)
        total = total * 50 if total else None
    if random.random() < 0.005:  # negative value anomaly
        total = -abs(total) if total else None

    orders.append({
        "order_id": i,
        "customer_id": cust_id,
        "product_id": prod_id,
        "order_date": fake.date_between(start_date='-1y', end_date='today'),
        "quantity": qty,
        "total_amount": total,
        "payment_method": random.choice(["Credit Card", "PayPal", "Bank Transfer", "Cash"]),
        "status": random.choice(["Completed", "Pending", "Cancelled"])
    })

df_orders = pd.DataFrame(orders)

# -------------------
# 4. Load into SQL


df_orders.to_sql("orders", con=engine, if_exists="replace", index=False)
df_customers.to_sql("customers", con=engine, if_exists="replace", index=False)
df_products.to_sql("products", con=engine, if_exists="replace", index=False)

logger.info("data inserted into MySQL")
print("Synthetic data inserted into MySQL.")
