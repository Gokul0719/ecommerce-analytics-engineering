# Databricks notebook source
customers_silver = (
    spark.read.format("delta")
    .load("/Volumes/workspace/default/ecommerce_data/bronze/customers")
)

customers_silver = customers_silver.withColumn(
    "signup_date",
    customers_silver.signup_date.cast("date")
)

customers_silver.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/Volumes/workspace/default/ecommerce_data/silver/customers")

customers_silver.display()

# COMMAND ----------

from pyspark.sql.functions import round

products_silver = (
    spark.read.format("delta")
    .load("/Volumes/workspace/default/ecommerce_data/bronze/products")
)

products_silver = products_silver.withColumn(
    "price",
    round("price", 2)
)

products_silver.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/Volumes/workspace/default/ecommerce_data/silver/products")

products_silver.display()

# COMMAND ----------

from pyspark.sql.functions import col, round

orders_df = (
    spark.read.format("delta")
    .load("/Volumes/workspace/default/ecommerce_data/bronze/orders")
)

payments_df = (
    spark.read.format("delta")
    .load("/Volumes/workspace/default/ecommerce_data/bronze/payments")
)

products_df = (
    spark.read.format("delta")
    .load("/Volumes/workspace/default/ecommerce_data/silver/products")
)

customers_df = (
    spark.read.format("delta")
    .load("/Volumes/workspace/default/ecommerce_data/silver/customers")
)

# COMMAND ----------

orders_enriched = (
    orders_df
    .join(customers_df, "customer_id", "left")
    .join(products_df, "product_id", "left")
    .join(payments_df, "order_id", "left")
)

# COMMAND ----------

orders_enriched = orders_enriched.withColumn(
    "revenue",
    round(col("price") * col("quantity"), 2)
)

# COMMAND ----------

orders_enriched = orders_enriched.select(
    "order_id",
    "order_date",
    "customer_id",
    "customer_name",
    "country",
    "product_id",
    "product_name",
    "category",
    "quantity",
    "price",
    "revenue",
    "payment_method",
    "payment_status"
)

# COMMAND ----------

orders_enriched.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/Volumes/workspace/default/ecommerce_data/silver/orders_enriched")

# COMMAND ----------

orders_enriched.display()

# COMMAND ----------

orders_enriched.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/Volumes/workspace/default/ecommerce_data/silver/orders_enriched")

# COMMAND ----------

