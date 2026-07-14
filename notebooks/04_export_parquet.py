# Databricks notebook source
customers_silver = spark.read.format("delta").load(
    "/Volumes/workspace/default/ecommerce_data/silver/customers"
)

customers_silver.coalesce(1).write \
    .mode("overwrite") \
    .parquet("/Volumes/workspace/default/ecommerce_data/exports/customers")

products_silver = spark.read.format("delta").load(
    "/Volumes/workspace/default/ecommerce_data/silver/products"
)

products_silver.coalesce(1).write \
    .mode("overwrite") \
    .parquet("/Volumes/workspace/default/ecommerce_data/exports/products")

orders_enriched = spark.read.format("delta").load(
    "/Volumes/workspace/default/ecommerce_data/silver/orders_enriched"
)

orders_enriched.coalesce(1).write \
    .mode("overwrite") \
    .parquet("/Volumes/workspace/default/ecommerce_data/exports/orders_enriched")

# COMMAND ----------

display(
    dbutils.fs.ls(
        "/Volumes/workspace/default/ecommerce_data/exports"
    )
)

# COMMAND ----------

display(
    spark.read.parquet(
        "/Volumes/workspace/default/ecommerce_data/exports/orders_enriched"
    )
)