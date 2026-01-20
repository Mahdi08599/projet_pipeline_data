import boto3
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from common.kafka_config import get_consumer

# Connexion MinIO
s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='admin',
    aws_secret_access_key='password'
)
# Créer le bucket s'il n'existe pas
try:
    s3.head_bucket(Bucket='stock-market-data')
except s3.exceptions.ClientError as e:
    if e.response['Error']['Code'] == '404':
        s3.create_bucket(Bucket='stock-market-data')
        print("Bucket 'stock-market-data' créé.")
    else:
        raise
consumer = get_consumer('stock_prices')

print(" Archiver MinIO prêt...")

for message in consumer:
    data = message.value
    file_name = f"stock_{data['symbol']}_{data['timestamp'].replace(' ', '_')}.json"
    s3.put_object(
        Bucket='stock-market-data',
        Key=file_name,
        Body=json.dumps(data).encode('utf-8')
    )
    print(f" Archivé : {file_name}")