import os
from cryptodisco.core.binanceclient import BinanceClient


api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')


if __name__ == '__main__':

    client = BinanceClient(api_key=api_key, api_secret=api_secret)
    data = client.get_market_data(coin="BTCUSDT", interval='4h', start_date="1 day ago UTC")
    print(data)