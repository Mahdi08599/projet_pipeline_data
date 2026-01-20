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
last_price = None

logger.info("Démarrage du service d'ingestion...")

try:
    while True:
        data = yf.Ticker(ticker).history(period='1d', interval='1m').iloc[-1]
        current_price = float(data['Close'])
        
        if current_price != last_price:
            message = {
                "symbol": ticker,
                "price": current_price,
                "timestamp": str(data.name)
            }
            producer.send('stock_prices', value=message)
            logger.info(f"Donnée boursière envoyée avec succès : {message['price']} USD")
            last_price = current_price
        else:
            logger.info(f"Prix inchangé ({current_price} USD), pas d'envoi.")
        
        time.sleep(60)
except KeyboardInterrupt:
    logger.info("Arrêt du service demandé par l'utilisateur.")