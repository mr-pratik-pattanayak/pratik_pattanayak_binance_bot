import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from binance_client import get_binance_client
from logger_config import setup_logger
import logging

setup_logger()

def place_grid_orders(client, symbol, quantity, grid_spacing, grid_levels):
    try:
        current_price = float(client.futures_symbol_ticker(symbol=symbol)['price'])
        print(f"Current market price: {current_price}")

        for i in range(1, grid_levels + 1):
            # Buy limit order below market
            buy_price = current_price - (i * grid_spacing)
            client.futures_create_order(
                symbol=symbol,
                side='BUY',
                type='LIMIT',
                quantity=quantity,
                price=round(buy_price, 2),
                timeInForce='GTC'
            )
            print(f"Buy limit placed at {buy_price}")

            # Sell limit order above market
            sell_price = current_price + (i * grid_spacing)
            client.futures_create_order(
                symbol=symbol,
                side='SELL',
                type='LIMIT',
                quantity=quantity,
                price=round(sell_price, 2),
                timeInForce='GTC'
            )
            print(f"Sell limit placed at {sell_price}")

        print("All grid orders placed.")

    except Exception as e:
        logging.error(f"Error placing grid orders: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python grid_trading.py <SYMBOL> <QUANTITY> <GRID_SPACING> <GRID_LEVELS>")
        sys.exit()

    symbol, quantity, grid_spacing, grid_levels = sys.argv[1:]
    client = get_binance_client()
    place_grid_orders(client, symbol, float(quantity), float(grid_spacing), int(grid_levels))
