from binance.client import Client
import config
import time

def get_binance_client():
    client = Client(config.API_KEY, config.API_SECRET, requests_params={"timeout": 20})

    # Set base URL for Futures Testnet manually
    client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

    # Sync time to avoid timestamp errors
    server_time = client.get_server_time()['serverTime']
    local_time = int(time.time() * 1000)
    offset = server_time - local_time
    client.timestamp_offset = offset

    return client
