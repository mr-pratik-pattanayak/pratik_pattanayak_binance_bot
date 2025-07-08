import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from binance_client import get_binance_client
from logger_config import setup_logger
import logging

setup_logger()

def place_oco_order(client, symbol, side, quantity, take_profit_price, stop_price):
    try:
        market_price = float(client.futures_symbol_ticker(symbol=symbol)['price'])
        print(f"Current market price: {market_price}")

        if side.upper() == 'SELL':
            if float(take_profit_price) <= market_price or float(stop_price) >= market_price:
                print("Invalid TP/SL prices for SELL. TP must be > market price, SL must be < market price.")
                return
        elif side.upper() == 'BUY':
            if float(take_profit_price) >= market_price or float(stop_price) <= market_price:
                print("Invalid TP/SL prices for BUY. TP must be < market price, SL must be > market price.")
                return
        else:
            print("Invalid side. Use BUY or SELL.")
            return

        # Take-Profit Market Order
        tp_order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='TAKE_PROFIT_MARKET',
            stopPrice=take_profit_price,
            quantity=quantity
        )

        # Stop Market Order
        sl_order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='STOP_MARKET',
            stopPrice=stop_price,
            quantity=quantity
        )

        logging.info(f"OCO simulated orders placed: TP {tp_order}, SL {sl_order}")
        print(f"OCO simulated: Take-Profit @ {take_profit_price}, Stop @ {stop_price}")

    except Exception as e:
        logging.error(f"Error placing OCO simulated orders: {e}")
        print(f"Error placing OCO orders:\n{e}")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python oco_orders.py <SYMBOL> <BUY/SELL> <QUANTITY> <TAKE_PROFIT_PRICE> <STOP_PRICE>")
        sys.exit()

    symbol, side, quantity, tp_price, stop_price = sys.argv[1:]
    client = get_binance_client()
    place_oco_order(client, symbol, side.upper(), float(quantity), tp_price, stop_price)
