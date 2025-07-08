import sys
from binance_client import get_binance_client
from logger_config import setup_logger
import logging

setup_logger()

def place_market_order(client, symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        logging.info(f"Market Order executed successfully: {order}")
        print(f"Market Order placed successfully:\n{order}")
    except Exception as e:
        logging.error(f"Error placing market order: {e}")
        print(f"Error placing market order:\n{e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python market_orders.py <SYMBOL> <BUY/SELL> <QUANTITY>")
        sys.exit()

    symbol, side, quantity = sys.argv[1:]
    client = get_binance_client()
    place_market_order(client, symbol, side.upper(), float(quantity))
