# Databricks notebook source
# MAGIC %pip install faker

# COMMAND ----------

# MAGIC %restart_python

# COMMAND ----------

from faker import Faker
import random
import pandas as pd
from datetime import datetime, timedelta

fake = Faker()
random.seed(42)

# COMMAND ----------

customers = []

countries = [
    "France",
    "Germany",
    "Spain",
    "Italy",
    "Netherlands"
]

for i in range(1, 5001):

    customers.append({
        "customer_id": i,
        "customer_name": fake.name(),
        "country": random.choice(countries),
        "signup_date": fake.date_between(
            start_date="-3y",
            end_date="today"
        )
    })

customers_df = pd.DataFrame(customers)

customers_df.head()

# COMMAND ----------

customers_df.to_csv(
    "/Volumes/workspace/default/ecommerce_data/raw/customers/customers.csv",
    index=False
)

customers_df.display()


# COMMAND ----------

products = []

product_catalog = {

    "Electronics": [
        "Wireless Earbuds",
        "Gaming Mouse",
        "Mechanical Keyboard",
        "Smart Watch",
        "Bluetooth Speaker"
    ],

    "Clothing": [
        "Running Shoes",
        "Hoodie",
        "Jeans",
        "T-Shirt",
        "Jacket"
    ],

    "Home & Kitchen": [
        "Coffee Maker",
        "Air Fryer",
        "Vacuum Cleaner",
        "Cookware Set",
        "Desk Lamp"
    ],

    "Sports": [
        "Yoga Mat",
        "Dumbbells",
        "Football",
        "Tennis Racket",
        "Cycling Helmet"
    ],

    "Beauty": [
        "Lipstick Set",
        "Face Wash",
        "Perfume",
        "Hair Dryer",
        "Skin Care Kit"
    ]
}

# COMMAND ----------

products = []

product_id = 1

for category, items in product_catalog.items():

    for item in items:

        for _ in range(4):     # 5 categories × 5 products × 4 copies = 100 products

            products.append({

                "product_id": product_id,
                "product_name": item,
                "category": category,
                "price": round(random.uniform(10, 500), 2)

            })

            product_id += 1


products_df = pd.DataFrame(products)

products_df.display()

# COMMAND ----------

products_df.to_csv(
    "/Volumes/workspace/default/ecommerce_data/raw/products/products.csv",
    index=False
)

# COMMAND ----------

orders = []

for order_id in range(1, 50001):

    orders.append({

        "order_id": order_id,

        "customer_id": random.randint(
            1,
            len(customers_df)
        ),

        "product_id": random.randint(
            1,
            len(products_df)
        ),

        "order_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),

        "quantity": random.randint(1, 5)

    })

orders_df = pd.DataFrame(orders)

orders_df.display()

# COMMAND ----------

orders_df.to_csv(
    "/Volumes/workspace/default/ecommerce_data/raw/orders/orders.csv",
    index=False
)

# COMMAND ----------

payment_methods = [
    "Credit Card",
    "PayPal",
    "Apple Pay",
    "Google Pay"
]

payment_statuses = [
    "Completed",
    "Completed",
    "Completed",
    "Completed",
    "Completed",
    "Failed",
    "Refunded"
]

payments = []

for payment_id in range(1, len(orders_df) + 1):

    payments.append({

        "payment_id": payment_id,

        "order_id": payment_id,

        "payment_method": random.choice(
            payment_methods
        ),

        "payment_status": random.choice(
            payment_statuses
        ),

        "amount": round(
            random.uniform(20, 1000),
            2
        )

    })

payments_df = pd.DataFrame(payments)

payments_df.display()

# COMMAND ----------

payments_df.to_csv(
    "/Volumes/workspace/default/ecommerce_data/raw/payments/payments.csv",
    index=False
)

# COMMAND ----------

