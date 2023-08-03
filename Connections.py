import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
import os
import requests, json
import pandas as pd
from datetime import datetime
import pymongo
#from qdrant_client import QdrantClient


class OpenWeatherConnection(ExperimentalBaseConnection):
    """Basic st.experimental_connection implementation for Opemweather API"""

    def _connect(self, **kwargs) -> None:
        if 'api_key' in kwargs:
            os.environ['API_KEY'] = kwargs.pop('api_key')
        else:
            os.environ['API_KEY'] = self._secrets['api_key']
        return None
    
    def get(self, city :str, units :str, ttl: int = 60, **kwargs) -> json:
        @st.cache_data(ttl=ttl)
        def _get(city :str, units :str, **kwargs) -> json:
            # get API key 
            api_key = os.environ['API_KEY']
            # base_url variable to store url
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            # complete url address
            complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=" + units
            # get method of requests module
            # return response object
            response = requests.get(complete_url)
            # json method of response object
            # convert json format data into
            # python format data
            data = response.json()
            return data
        return _get(city, units, **kwargs)


class QdrantConnection(ExperimentalBaseConnection):
    """Basic st.experimental_connection implementation for Qdrant"""

    def _connect(self, **kwargs) :
        
        if 'cluster' in kwargs:
            clt = kwargs.pop('cluster')
        else:
            clt = self._secrets['cluster']

        if 'api_key' in kwargs:
            key = kwargs.pop('api_key')
        else:
            key = self._secrets['api_key']
    
        return QdrantClient(url=clt, prefer_grpc=True,api_key=key)
    

    def query(self, query: str, ttl: int = 3600, **kwargs) -> pd.DataFrame:
        @st.cache_data(ttl=ttl)
        def _query(query: str, **kwargs) -> pd.DataFrame:
            cursor = self.cursor()
            cursor.execute(query, **kwargs)
            return cursor.df()
        
        return _query(query, **kwargs)

class MongoConnection(ExperimentalBaseConnection[pymongo.MongoClient]):
    """Basic st.experimental_connection implementation for Qdrant"""

    def _connect(self, **kwargs) -> pymongo.MongoClient:
        if 'database' in kwargs:
            db = kwargs.pop('database')
        else:
            db = self._secrets['database']
        return pymongo.MongoClient(database=db, **kwargs)
    

    def query(self, query: str, ttl: int = 3600, **kwargs) -> pd.DataFrame:
        @st.cache_data(ttl=ttl)
        def _query(query: str, **kwargs) -> pd.DataFrame:
            cursor = self.cursor()
            cursor.execute(query, **kwargs)
            return cursor.df()
        
        return _query(query, **kwargs)


class BinanceAPI(ExperimentalBaseConnection):

    def _connect(self) :

        return None


    def get(self,symbol: str, interval: str, limit: int = 1000, ttl: int = 1, **kwargs) -> pd.DataFrame:

        api_url = "https://api.binance.com/api/v3/klines?symbol={}&interval={}&limit={}".format(symbol, interval, limit)

        @st.cache_data(ttl=ttl)
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

            return df
        
        return _get( **kwargs)
    
    def get_all(self,symbols: list, intervals: list, limit: int = 100, ttl: int = 60, **kwargs) -> pd.DataFrame:

        # Binance Kline Column names
        Binance_Columns_name = ["Open_time",
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
        
        # selected column names
        Columns_name = ["Open_date",
                        "Open_price", 
                        "High_price", 
                        "Low_price", 
                        "Close_price", 
                        "Volume",  
                        "Number_trades", 
                        "Symbol", 
                        "Interval"]

        df = pd.DataFrame(columns=Columns_name)

        for interval in intervals:
            for symbol in symbols:

                url = "https://api.binance.com/api/v3/klines?symbol={}&interval={}&limit={}".format(symbol, interval, limit)
                data = requests.get(url).json()

            
                # create DataFrame from data
                df_temp = pd.DataFrame(data, columns=Binance_Columns_name)

                # change columns type
                df_temp = df_temp.astype({'Open_price'   : 'float', 
                                          'High_price'   : 'float', 
                                          'Low_price'    : 'float', 
                                          'Close_price'  : 'float', 
                                          'Volume'       : 'float', 
                                          'Number_trades': 'float' 
                                         })
                # clean 'Open_time' column
                df_temp['Open_time'] = df_temp['Open_time']//1000
                 # create 'Open_date' column
                df_temp['Open_date'] = (df_temp['Open_time']).apply(datetime.fromtimestamp)

                df_temp['Symbol'] = symbol
                df_temp['Interval'] = interval

                # select columns
                df_temp = df_temp[Columns_name]

                df = pd.concat([df, df_temp], axis=0)

        return df

        