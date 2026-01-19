from kafka import KafkaConsumer
import json
import boto3
from io import BytesIO

# 1. Connexion au coffre-fort MinIO (S3)
s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id= 'YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY'
)

# Créer le bucket si nécessaire
try:
    s3.create_bucket(Bucket='stock-market-data')
    print("Bucket 'stock-market-data' créé.")
except Exception as e:
    print(f"Bucket existe déjà ou erreur : {e}")

# 2. Connexion au tapis roulant Kafka
consumer = KafkaConsumer(
    'stock_prices',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Le Consumer est prêt et attend des données...")

try:
    for message in consumer:
        data = message.value
        # On crée un nom de fichier unique avec le timestamp
        file_name = f"stock_{data['symbol']}_{data['timestamp'].replace(' ', '_')}.json"
        
        # On transforme la donnée en format fichier pour MinIO
        json_data = json.dumps(data).encode('utf-8')
        
        # On envoie le fichier dans le bucket "stock-market-data"
        s3.put_object(
            Bucket='stock-market-data',
            Key=file_name,
            Body=json_data
        )
        
        print(f"Fichier sauvegardé dans MinIO : {file_name}")
except KeyboardInterrupt:
    print("Arrêt du consumer.")