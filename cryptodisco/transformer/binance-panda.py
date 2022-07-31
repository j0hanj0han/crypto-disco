from os import lseek




Class BinanceTransformer:

    def __init__(self, binancejson):
        self.binancejson = binancejson

    def transform(self):
        """
        transform json to pandas object
        """