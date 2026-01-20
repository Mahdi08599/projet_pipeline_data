import yfinance as yf
import time
import sys
import os

# Ajout du chemin src pour l'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from common.kafka_config import get_producer

ticker = "AAPL"
producer = get_producer()

print(f"🚀 Producer démarré pour {ticker}...")

try:
    while True:
        data = yf.Ticker(ticker).history(period='1d', interval='1m').iloc[-1]
        message = {
            "symbol": ticker,
            "price": float(data['Close']),
            "timestamp": str(data.name)
        }
        producer.send('stock_prices', value=message)
        print(f"📡 Donnée envoyée : {message}")
        time.sleep(60)
except KeyboardInterrupt:
    print("Stopping Producer...")