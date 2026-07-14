# 🛒 End-to-End E-Commerce Analytics Engineering Pipeline

A modern Analytics Engineering project that demonstrates how raw e-commerce transaction data can be transformed into business-ready analytical datasets using **Databricks, PySpark, Delta Lake, DuckDB, and dbt**.

This project follows a layered architecture inspired by modern data platforms and implements data quality testing, lineage tracking, and modular SQL transformations.

---

# 📌 Architecture

![Architecture](architecture/architecture.png)

---

# 🚀 Tech Stack

| Category | Technology |
|----------|------------|
| Data Processing | PySpark |
| Platform | Databricks Community Edition |
| Data Lake | Delta Lake |
| Storage Format | Parquet |
| Analytical Database | DuckDB |
| Analytics Engineering | dbt |
| Programming Language | Python, SQL |
| Version Control | Git & GitHub |

---

# 🏗️ Project Architecture

```
Synthetic Data
        │
        ▼
Databricks (PySpark)
        │
        ▼
Bronze Layer (Delta)
        │
        ▼
Silver Layer (Delta)
        │
        ▼
Parquet Export
        │
        ▼
DuckDB
        │
        ▼
dbt Staging Layer
        │
        ▼
Fact Layer
        │
        ▼
Business Marts
```

---

# 📂 Project Structure

```
ecommerce-analytics-engineering
│
├── architecture/
├── data_sample/
├── docs/
├── notebooks/
├── screenshots/
├── ecommerce_dbt/
│   ├── models/
│   │   ├── staging/
│   │   ├── intermediate/
│   │   └── marts/
│   ├── macros/
│   ├── tests/
│   └── dbt_project.yml
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Workflow

## Step 1 — Generate Synthetic Data

Generated realistic e-commerce datasets using PySpark, including:

- Customers
- Products
- Orders
- Payments

---

## Step 2 — Bronze Layer

Raw datasets are ingested into Delta Lake without transformation.

Purpose:

- Preserve raw data
- Enable reproducibility
- Maintain immutable source records

---

## Step 3 — Silver Layer

Business transformations include:

- Data cleansing
- Data enrichment
- Revenue calculation
- Table joins
- Business-ready dataset creation

Output:

```
orders_enriched
```

---

## Step 4 — Export to Parquet

The enriched dataset is exported as Parquet files for downstream analytics processing.

---

## Step 5 — Analytics Engineering with dbt

### Staging Layer

```
stg_orders
```

Standardizes and prepares source data for downstream models.

---

### Intermediate Layer

```
fact_orders
```

Central business-ready fact table used by all analytical marts.

---

### Business Marts

The project builds reusable analytical models:

- 📈 Monthly Revenue
- 🌍 Sales by Country
- 👥 Top Customers
- 📦 Product Performance
- 💳 Payment Analysis

---

# ✅ Data Quality Tests

Implemented using **dbt tests**.

Current validations include:

- Unique Order IDs
- Non-null Customer IDs
- Valid Payment Status Values

Example:

```
PASS=4
WARN=0
ERROR=0
```

---

# 📊 dbt Lineage

The project uses dbt documentation to visualize model dependencies.

Example lineage:

```
stg_orders
      │
      ▼
fact_orders
      │
      ├──────────────┬──────────────┬──────────────┬──────────────┐
      ▼              ▼              ▼              ▼              ▼
top_customers
sales_by_country
monthly_revenue
product_performance
payment_analysis
```

---

# 📸 Project Screenshots

## Architecture

![Architecture](architecture/architecture.png)

---

## dbt Lineage


![Screenshots](screenshots/dbt_lineage.png)


## dbt Run


![Screenshots](screenshots/dbt_run.png)


## dbt Tests

![Screenshots](screenshots/dbt_test.png)


## Databricks Workflow

*(Add screenshot here)*

```
screenshots/databricks_workflow.png
```

---

# 💡 Key Learnings

Through this project I learned how modern Analytics Engineering differs from traditional ETL development.

Key concepts explored include:

- Layered data architecture
- Modular SQL transformations using dbt
- Fact-based analytical modeling
- Data quality testing
- Automated lineage documentation
- Building reusable business-ready datasets

---

# 🔮 Future Enhancements

- CI/CD for dbt
- Incremental dbt models
- Automated orchestration
- Cloud deployment (Azure / AWS)
- Dashboarding with Power BI or Apache Superset

---

# 👨‍💻 Author

**Gokul Saravanan**

If you found this project useful or have suggestions for improvement, feel free to connect or open an issue.
