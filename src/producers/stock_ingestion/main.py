import yfinance as yf
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from common.kafka_config import get_producer
from common.logger import get_logger

ticker = "AAPL"
producer = get_producer()
logger = get_logger("StockProducer-AAPL")

logger.info("Démarrage du service d'ingestion...")

try:
    while True:
        data = yf.Ticker(ticker).history(period='1d', interval='1m').iloc[-1]
        message = {
            "symbol": ticker,
            "price": float(data['Close']),
            "timestamp": str(data.name)
        }
        producer.send('stock_prices', value=message)
        logger.info(f"Donnée boursière envoyée avec succès : {message['price']} USD")
        time.sleep(60)
except KeyboardInterrupt:
    logger.info("Arrêt du service demandé par l'utilisateur.")