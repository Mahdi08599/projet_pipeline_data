from kafka import KafkaProducer, KafkaConsumer
import json

# Configuration partagée
BOOTSTRAP_SERVERS = ['localhost:9092']

def get_producer():
    """Crée et retourne un Producer Kafka configuré."""
    return KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )

def get_consumer(topic_name):
    """Crée et retourne un Consumer Kafka pour un topic spécifique."""
    return KafkaConsumer(
        topic_name,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )