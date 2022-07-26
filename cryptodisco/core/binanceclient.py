from binance.client import Client

class BinanceClient:
    """Request Data from binance python wrapper"""


    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = self._get_client(api_key, api_secret)

    def _get_client(self, api_key, api_secret):
        client = Client(api_key, api_secret)
        return client

    def _make_request(self):
        """Call to api here"""
        pass

    
    def get_market_data(self, coin, interval, start_date):
        resp = self.client.get_historical_klines(coin, interval, start_date)
        return resp