🚀 Real-Time Stock Data Pipeline : Ingestion & Cloud Analytics
Projet académique - Master 2 Data Science in Business (PST&B)

Ce projet implémente un pipeline de données End-to-End robuste permettant de collecter, stocker et analyser les données boursières d'Apple (AAPL) en temps réel. L'architecture repose sur une hybridation entre une infrastructure locale conteneurisée et un entrepôt de données Cloud professionnel.

 Architecture du Pipeline
L'architecture suit les principes du Modern Data Stack avec une séparation claire des responsabilités :

Ingestion Temps Réel : Utilisation de Kafka (Producer/Consumer) pour streamer les données issues de l'API yfinance.

Data Lake (Couche Bronze) : Stockage des données brutes au format JSON dans MinIO (S3-compatible) pour garantir la persistance des messages.

Orchestration : Utilisation d'Apache Airflow pour automatiser et monitorer le transfert des données vers le Cloud.

Data Warehouse (Couche Silver) : Centralisation et structuration des données dans Snowflake pour l'analyse décisionnelle.

  Technologies Utilisées
Langage : Python (Pandas, yfinance, Boto3, Snowflake-connector).

Streaming : Apache Kafka (Zookeeper, Broker).

Stockage d'objets : MinIO.

Orchestration : Apache Airflow (Docker-based).

Cloud Data Warehouse : Snowflake. 

Infrastructure : Docker & Docker Compose.

  Installation et Utilisation
1. Déploiement de l'infrastructure
Lancer l'ensemble des services via Docker :

Bash
docker-compose up -d

2. Lancement du flux de données
Démarrer le producteur pour capturer les prix boursiers et le consommateur pour les archiver dans MinIO :

Bash
python producer.py
python consumer.py

3. Orchestration Airflow
Activer le DAG transfert_direct_minio_snowflake depuis l'interface web (localhost:8080) pour déclencher l'ingestion vers Snowflake.

  Résultats et Analyse
Le pipeline est capable d'ingérer et de structurer les données automatiquement. Une vérification finale dans Snowflake confirme la présence des données prêtes pour l'analyse SQL :

SQL
SELECT COUNT(*) FROM BOURSE_DB.SILVER.AAPL_DATA;
-- Résultat : Flux opérationnel avec succès.

  👤 Auteur
Mahdi Ben Arfi – Master 2 Data Science in Business @ Paris School of Technology & Business (PST&B).
