import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
import os
import requests, json
import pandas as pd
from datetime import datetime
import pymongo


class MongoConnection(ExperimentalBaseConnection[pymongo.MongoClient]):
    """Basic st.experimental_connection implementation for MongoDB"""

    def _connect(self, **kwargs) -> pymongo.MongoClient:
        if 'database' in kwargs:
            db = kwargs.pop('database')
        else:
            db = self._secrets['database']
        return pymongo.MongoClient(db, **kwargs)
    
    def cursor(self, database: str, collection: str , **kwargs) :
        db = self._connect()[database]
        coll = db[collection]
        return coll.find()


    def insert_csv(self, database: str, collection: str, csv_file: str, **kwargs) -> None:
        db = self._connect()[database]
        coll = db[collection]
        data = pd.read_csv(csv_file).to_dict('record')
        coll.insert_many(data)
    
    def find(self, database: str, collection: str, symbol: str, interval: str, limit: int = 100, ttl: int = 3600, **kwargs) -> pd.DataFrame:
        @st.cache_data(ttl=ttl)
        def _find(database :str, collection :str, symbol: str, interval: str, limit: int = 100, **kwargs) -> pd.DataFrame:
            db = self._connect()[database]
            coll = db[collection]
            data = coll.find({"Symbol" : symbol, "Interval" : interval}, {"_id":0}).sort("Open_date", -1).limit(limit)
            df = pd.DataFrame(data)
            return df 
        return  _find(database, collection, symbol, interval, limit, **kwargs)
    
    def count_documents(self, database: str, collection: str, **kwargs) -> int:
        db = self._connect()[database]
        coll = db[collection]
        nbr = coll.count_documents({})
        return nbr


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




        