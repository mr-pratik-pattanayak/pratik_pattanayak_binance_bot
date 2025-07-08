import sys
from binance_client import get_binance_client
from logger_config import setup_logger
import logging

setup_logger()

def place_limit_order(client, symbol, side, quantity, price):
    try:
        notional = float(quantity) * float(price)
        if notional < 100:
            print(f"Notional value ({notional} USDT) is less than minimum 100 USDT.")
            return

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            quantity=quantity,
            price=price,
            timeInForce='GTC'
        )
        logging.info(f"Limit Order executed successfully: {order}")
        print(f"Limit Order placed successfully:\n{order}")
    except Exception as e:
        logging.error(f"Error placing limit order: {e}")
        print(f"Error placing limit order:\n{e}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python limit_orders.py <SYMBOL> <BUY/SELL> <QUANTITY> <PRICE>")
        sys.exit()

    symbol, side, quantity, price = sys.argv[1:]
    client = get_binance_client()
    place_limit_order(client, symbol, side.upper(), float(quantity), price)
