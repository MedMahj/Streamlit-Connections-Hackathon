import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit.connections import ExperimentalBaseConnection
import os
import requests, json
import pandas as pd
from datetime import datetime


# My packages
import Style_Functions as sf


class BinanceAPI(ExperimentalBaseConnection):
    """Basic st.experimental_connection implementation for Binance API"""

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


if __name__ == "__main__":

    # Set page config
    sf.display_page_config('ETL Klines','💱')

    # Add page title
    sf.add_page_title('ETL Klines')

    # Change buttons style
    sf.change_button_style()
    

    SYMBOLS = ['BTCBUSD',
           'BNBBUSD',
           'ETHBUSD',
           'DOGEBUSD',
           'HOOKBUSD']
    INTERVALS = ['1m', 
                '1h', 
                '1d']
    LIMITS = [10,
              50,
              100]

    
    #conn = st.experimental_connection(name='binance', type=BinanceAPI)
    conn = BinanceAPI('binance')
    col1, col2, col3 = st.columns([3,2,3])
    
    if col2.button('Download Data', use_container_width=True):
        df = conn.get_all(SYMBOLS, INTERVALS, limit = 100)
        st.dataframe(df)

        df.to_csv('./data/klines.csv', index = False)
    


    col1, col2, col3 = st.columns([3,2,3])
    with col2:
        if st.button('🏠 Back Home', use_container_width=True):
            switch_page('Home')
