# Databricks notebook source
customers_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/Volumes/workspace/default/ecommerce_data/raw/customers")
)

customers_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/Volumes/workspace/default/ecommerce_data/bronze/customers")

customers_df.display()

# COMMAND ----------

products_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/Volumes/workspace/default/ecommerce_data/raw/products")
)

products_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/Volumes/workspace/default/ecommerce_data/bronze/products")

products_df.display()

# COMMAND ----------

orders_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/Volumes/workspace/default/ecommerce_data/raw/orders")
)

orders_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/Volumes/workspace/default/ecommerce_data/bronze/orders")

orders_df.display()

# COMMAND ----------

payments_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/Volumes/workspace/default/ecommerce_data/raw/payments")
)

payments_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/Volumes/workspace/default/ecommerce_data/bronze/payments")

payments_df.display()

# COMMAND ----------

