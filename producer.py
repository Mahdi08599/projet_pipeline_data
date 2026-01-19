import yfinance as yf
from kafka import KafkaProducer
import json
import time

# 1. Configuration du tapis roulant (Kafka)
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# 2. La source de données : On choisit une action (ex: Apple - AAPL)
ticker = "AAPL"

print(f"Démarrage de l'envoi des données pour {ticker}...")

try:
    while True:
        # On récupère les dernières infos
        data = yf.Ticker(ticker).history(period='1d', interval='1m').iloc[-1]
        
        # On prépare le message
        message = {
            "symbol": ticker,
            "price": float(data['Close']),
            "timestamp": str(data.name)
        }
        
        # On envoie dans le topic "stock_prices"
        producer.send('stock_prices', value=message)
        print(f"Envoyé : {message}")
        
        # On attend 60 secondes avant la prochaine mise à jour
        time.sleep(60)
except KeyboardInterrupt:
    print("Arrêt du producer.")