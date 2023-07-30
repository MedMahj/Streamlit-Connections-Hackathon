import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
import requests
import pandas as pd
from datetime import datetime


class BinanceAPI(ExperimentalBaseConnection):

    def _connect(self) :

        return None


    def get(self,symbol: str, interval: str, limit: int = 1000, ttl: int = 3600, **kwargs) -> pd.DataFrame:

        api_url = "https://api.binance.com/api/v3/klines?symbol={}&interval={}&limit={}".format(symbol, interval, limit)

        #@cache_data(ttl=ttl)
        def _get(url :str =api_url, **kwargs) -> pd.DataFrame:

            data = requests.get(url).json()

            # Binance Kline Column names
            Column_name = ["Open_time",
                           "Open_price", 
                           "High_price", 
                           "Low_price", 
                           "Close_price", 
                           "Volume", 
                           "Close_time", 
                           "Quote_asset_volume", 
                           "Number_trades", 
                           "Taker_buy_base_asset_volume", 
                           "Taker_buy_quote_asset_volume", 
                           "Ignore"]
            # create DataFrame from data
            df = pd.DataFrame(data, columns=Column_name)

            # change columns type
            df = df.astype({'Open_price'   : 'float', 
                            'High_price'   : 'float', 
                            'Low_price'    : 'float', 
                            'Close_price'  : 'float', 
                            'Volume'       : 'float', 
                            'Number_trades': 'float' 
                          })
            # clean 'Open_time' column
            df['Open_time'] = df['Open_time']//1000
            # create 'Open_date' column
            df['Open_date'] = (df['Open_time']).apply(datetime.fromtimestamp)

            return data
        
        return _get( **kwargs)

        