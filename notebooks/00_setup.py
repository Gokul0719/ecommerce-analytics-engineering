# Databricks notebook source
catalog = "workspace"
schema = "default"
volume = "ecommerce_data"

spark.sql(
    f"CREATE VOLUME IF NOT EXISTS {catalog}.{schema}.{volume}"
)

# COMMAND ----------

base_path = f"/Volumes/{catalog}/{schema}/{volume}"

# Raw layer
dbutils.fs.mkdirs(f"{base_path}/raw/customers")
dbutils.fs.mkdirs(f"{base_path}/raw/products")
dbutils.fs.mkdirs(f"{base_path}/raw/orders")
dbutils.fs.mkdirs(f"{base_path}/raw/payments")

# Bronze layer
dbutils.fs.mkdirs(f"{base_path}/bronze/customers")
dbutils.fs.mkdirs(f"{base_path}/bronze/products")
dbutils.fs.mkdirs(f"{base_path}/bronze/orders")
dbutils.fs.mkdirs(f"{base_path}/bronze/payments")

# Silver layer
dbutils.fs.mkdirs(f"{base_path}/silver/customers")
dbutils.fs.mkdirs(f"{base_path}/silver/products")
dbutils.fs.mkdirs(f"{base_path}/silver/orders")
dbutils.fs.mkdirs(f"{base_path}/silver/payments")

# Export layer for dbt
dbutils.fs.mkdirs(f"{base_path}/exports")

print("✅ Folder structure created")