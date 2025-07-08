from binance_client import get_binance_client
from logger_config import setup_logger
import logging
from advanced import oco_orders, twap_order, grid_trading

setup_logger()

def place_market_order(client):
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()
    quantity = float(input("Enter quantity: "))

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



def place_limit_order(client):
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()
    quantity = float(input("Enter quantity: "))
    price = input("Enter limit price: ")
    notional = float(quantity) * float(price)

    if notional < 100:
        print(f"Notional value ({notional} USDT) is less than the minimum 100 USDT.")
        return

    try:
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

def place_oco_order(client):
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()
    quantity = float(input("Enter quantity: "))
    tp_price = input("Enter Take-Profit price: ")
    stop_price = input("Enter Stop price: ")
    market_price = float(client.futures_symbol_ticker(symbol=symbol)['price'])
    print(f"Current market price: {market_price}")
    if side.upper() == 'SELL':
        if float(tp_price) <= market_price or float(stop_price) >= market_price:
            print("Invalid TP/SL prices for SELL. TP must be > market price, SL must be < market price.")
            return
    elif side.upper() == 'BUY':
        if float(tp_price) >= market_price or float(stop_price) <= market_price:
            print("Invalid TP/SL prices for BUY. TP must be < market price, SL must be > market price.")
            return
    else:
        print("Invalid side. Use BUY or SELL.")
        return
    try:
        oco_orders.place_oco_order(client, symbol, side, quantity, tp_price, stop_price)
    except Exception as e:
        logging.error(f"Error placing OCO order: {e}")
        print(f"Error placing OCO order:\n{e}")

def place_twap_order(client):
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()
    total_quantity = float(input("Enter total quantity: "))
    interval_sec = int(input("Enter interval in seconds: "))
    parts = int(input("Enter number of parts: "))

    try:
        twap_order.place_twap_order(client, symbol, side, total_quantity, interval_sec, parts)
    except Exception as e:
        logging.error(f"Error placing TWAP order: {e}")
        print(f"Error placing TWAP order:\n{e}")

def place_grid_orders(client):
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    quantity = float(input("Enter quantity per order: "))
    grid_spacing = float(input("Enter grid spacing in USDT: "))
    grid_levels = int(input("Enter number of grid levels: "))

    try:
        grid_trading.place_grid_orders(client, symbol, quantity, grid_spacing, grid_levels)
    except Exception as e:
        logging.error(f"Error placing grid orders: {e}")
        print(f"Error placing grid orders:\n{e}")

def main():
    client = get_binance_client()

    while True:
        print("\n===== Binance Futures CLI Bot =====")
        print("1. Place Market Order")
        print("2. Place Limit Order")
        print("3. Place OCO Order")
        print("4. Place TWAP Order")
        print("5. Place Grid Orders")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            place_market_order(client)
        elif choice == '2':
            place_limit_order(client)
        elif choice == '3':
            place_oco_order(client)
        elif choice == '4':
            place_twap_order(client)
        elif choice == '5':
            place_grid_orders(client)
        elif choice == '6':
            print("Exiting bot. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()
