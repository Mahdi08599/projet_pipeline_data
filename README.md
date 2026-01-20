# 🚀 Production-Grade Data Pipeline: Real-Time Ingestion & Cloud Analytics

This repository features a robust, end-to-end data infrastructure designed for high-availability stock market streaming (AAPL). The system transitions from real-time ingestion to a modular "Clean Architecture," ensuring scalability and professional-grade monitoring.

---

## 🛠️ Tech Stack & Infrastructure

| Layer | Technology | Role |
| :--- | :--- | :--- |
| **Streaming** | Apache Kafka | Real-time message brokerage |
| **Data Lake** | MinIO (S3 API) | Bronze layer for raw JSON persistence |
| **Orchestration** | Apache Airflow | Workflow automation & Cloud sync |
| **Warehouse** | Snowflake | Silver layer for structured analytics |
| **Environment** | Docker | Containerized microservices |

---

## 🏗️ Modular System Architecture

The project follows a **Separation of Concerns (SoC)** principle, isolating technical drivers from business logic.

```text
src/
 ├── common/       # Shared Kafka drivers & Centralized Logger
 ├── producers/    # High-frequency ingestion services
 └── consumers/    # Specialized storage & processing workers
dags/              # Production ETL workflows
docker-compose.yml # Infrastructure as Code (IaC)
screenshots/       # System validation proofs

---

⚡ Key Engineering Features
Modular Ingestion: Decoupled Producers and Consumers allowing independent scaling of services.

Centralized Logging: Standardized monitoring across all Python services for rapid debugging.

Automated Cloud Sync: Airflow DAGs manage the secure bridge between local storage and Snowflake.

Data Integrity: Implements a Bronze-to-Silver transformation flow for analytics readiness.

📊 System Validation
Pipeline Health
Real-time monitoring via the Airflow scheduler ensures 100% task completion for Cloud synchronization.

Warehouse Analytics
Final data landing in the Snowflake Silver layer, verified and indexed for downstream BI tools.

👤 Maintainer
Mahdi Ben Arfi – Business Analyst & Data Scientist
