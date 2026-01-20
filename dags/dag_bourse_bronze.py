from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from datetime import datetime
import json

def transferer_minio_a_snowflake():
    # 1. Se connecter à MinIO et Snowflake
    s3_hook = S3Hook(aws_conn_id='minio_conn')
    snowflake_hook = SnowflakeHook(snowflake_conn_id='snowflake_conn')
    
    # 2. Récupérer la liste des fichiers dans le bucket Bronze
    bucket = 'stock-market-data'
    keys = s3_hook.list_keys(bucket_name=bucket)
    
    if not keys:
        print("Aucun fichier à transférer.")
        return

    for key in keys:
        # 3. Lire le fichier JSON depuis MinIO
        file_content = s3_hook.read_key(key, bucket_name=bucket)
        data = json.loads(file_content)
        
        # 4. Insérer les données dans Snowflake
        sql = f"""
        INSERT INTO BOURSE_DB.SILVER.AAPL_DATA (ticker, price, timestamp)
        VALUES ('{data['symbol']}', {data['price']}, '{data['timestamp']}')
        """
        snowflake_hook.run(sql)
        print(f"Fichier {key} transféré avec succès !")

with DAG(
    dag_id='transfert_direct_minio_snowflake',
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    load_to_snowflake = PythonOperator(
        task_id='pousser_vers_snowflake',
        python_callable=transferer_minio_a_snowflake
    )

    dbt_run_transformations = BashOperator(
    task_id='dbt_run_transformations',
    bash_command='cd /opt/airflow/dbt && /home/airflow/.local/bin/dbt run --profiles-dir .',
    dag=dag,
)

    load_to_snowflake >> dbt_run_transformations