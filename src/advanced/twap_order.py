import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from binance_client import get_binance_client
from logger_config import setup_logger
import logging

setup_logger()

def place_twap_order(client, symbol, side, total_quantity, interval_sec, parts):
    try:
        qty_per_order = total_quantity / parts
        print(f"Placing {parts} orders of {qty_per_order} {symbol} every {interval_sec} seconds.")

        for i in range(parts):
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=qty_per_order
            )
            logging.info(f"TWAP Order {i+1}/{parts} executed: {order}")
            print(f"Order {i+1} placed successfully.")

            if i < parts - 1:
                time.sleep(interval_sec)

        print("All TWAP orders completed.")

    except Exception as e:
        logging.error(f"Error placing TWAP orders: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python twap_order.py <SYMBOL> <BUY/SELL> <TOTAL_QUANTITY> <INTERVAL_SECONDS> <PARTS>")
        sys.exit()

    symbol, side, total_qty, interval_sec, parts = sys.argv[1:]
    client = get_binance_client()
    place_twap_order(client, symbol, side.upper(), float(total_qty), int(interval_sec), int(parts))
