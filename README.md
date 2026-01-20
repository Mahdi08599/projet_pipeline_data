# Real-Time Stock Market Data Pipeline

### End-to-End Medallion Architecture & Orchestration

---

## Project Description

This project implements a complete real-time data pipeline for stock market analysis. The goal is to transform raw streaming data into actionable performance indicators using a robust **Medallion Architecture** deployed on **Snowflake**.

---

## Technical Architecture

The entire pipeline is fully containerized using **Docker** and is built around the following components:

* **Ingestion**: Real-time data streams via **Apache Kafka**
* **Object Storage**: Raw data persistence in **MinIO** (S3-compatible)
* **Orchestration**: Workflow management with **Apache Airflow**
* **Data Warehouse**: Distributed storage and computation on **Snowflake**
* **Transformation**: Data modeling and cleansing with **dbt**
* **Visualization**: Analytical dashboards built in **Power BI**

---

##  Technology Stack

| Phase              | Tools                   |
| :----------------- | :---------------------- |
| **Ingestion**      | Kafka, MinIO, Airflow   |
| **Storage**        | Snowflake               |
| **Transformation** | dbt (Data Build Tool)   |
| **Visualization**  | Power BI                |
| **Infrastructure** | Docker & Docker Compose |

---

## Medallion Pipeline (dbt)

Data flows through three quality layers within Snowflake:

### 1️⃣ Bronze Layer (Raw)

* **Table**: `AAPL_DATA` (Schema: `SILVER`)
* **Source**: Raw data ingested directly from MinIO

### 2️⃣ Silver Layer (Cleaned)

* **Models**: `stg_stock_data`, `int_stock_cleansed`
* **Processing**: Data cleaning, type casting, and deduplication

### 3️⃣ Gold Layer (Analytics)

* **Model**: `fct_stock_performance` (Schema: `GOLD`)
* **KPI**: Stock price percentage variation:

  $$
  \text{Price Variation %} =
  \frac{\text{Current Price} - \text{Previous Price}}
  {\text{Previous Price}} \times 100
  $$

---

## Installation & Run

### Prerequisites

* Docker & Docker Compose installed
* Active Snowflake account
  (URL: `lxqrhwo-ov83463.snowflakecomputing.com`)

### Steps

1. **Configuration**: Set Snowflake credentials in the `.env` file
2. **Startup**: Run `docker-compose up -d --build`
3. **Orchestration**: Enable the DAG `transfert_direct_minio_snowflake` in the Airflow UI (`localhost:8080`)
4. **Visualization**: Connect Power BI to the table `GOLD.FCT_STOCK_PERFORMANCE`

---

This project demonstrates an end-to-end, production-oriented real-time data pipeline, combining streaming ingestion, modern data warehousing, and analytics-ready transformations.
