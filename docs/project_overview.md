# Project Overview

## Introduction

This project demonstrates a modern Analytics Engineering workflow using Databricks, PySpark, Delta Lake, DuckDB, and dbt.

The objective is to transform raw e-commerce transactional data into business-ready analytical datasets by following a layered architecture commonly used in modern data platforms.

Unlike traditional ETL projects, this implementation emphasizes modular transformations, reusable SQL models, data quality testing, and documented lineage.

---

# Objectives

The project aims to:

- Build an end-to-end analytics engineering pipeline.
- Implement Bronze and Silver data layers using Delta Lake.
- Create reusable analytical models with dbt.
- Apply data quality validation through dbt tests.
- Produce business-ready datasets for reporting and analysis.

---

# Dataset

Synthetic e-commerce datasets were generated using PySpark.

The pipeline includes the following entities:

- Customers
- Products
- Orders
- Payments

These datasets simulate a realistic transactional environment for analytics.

---

# Pipeline Overview

```
Synthetic Data
        │
        ▼
Databricks (PySpark)
        │
        ▼
Bronze Layer
        │
        ▼
Silver Layer
        │
        ▼
Parquet Export
        │
        ▼
DuckDB
        │
        ▼
dbt Staging
        │
        ▼
Fact Layer
        │
        ▼
Business Marts
```

---

# dbt Layers

## Staging

The staging layer standardizes the source dataset and prepares it for downstream transformations.

Model:

- stg_orders

---

## Intermediate

The intermediate layer creates a centralized business-ready fact table.

Model:

- fact_orders

---

## Business Marts

Business marts are designed to answer common analytical questions.

Models include:

- top_customers
- sales_by_country
- monthly_revenue
- product_performance
- payment_analysis

---

# Data Quality

The project uses dbt generic tests to validate data integrity.

Implemented checks include:

- Unique Order IDs
- Non-null Customer IDs
- Accepted Payment Status values

These tests help ensure the analytical models are built on reliable data.

---

# Key Features

- End-to-end Analytics Engineering workflow
- Delta Lake architecture
- Modular dbt transformations
- Fact-based analytical modeling
- Data quality testing
- Automated lineage documentation
- GitHub-ready project structure

---

# Future Enhancements

Potential improvements include:

- Incremental dbt models
- Automated orchestration
- CI/CD integration
- Cloud deployment
- Business Intelligence dashboard integration

---

# Conclusion

This project demonstrates how modern Analytics Engineering extends beyond traditional ETL by introducing modular transformations, reusable business logic, data validation, and documentation.

The resulting pipeline provides a scalable foundation for building reliable analytical datasets suitable for downstream reporting and business intelligence.
