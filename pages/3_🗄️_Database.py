import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.express as px
import pymongo

# My packages
import Style_Functions as sf
from Connections import MongoConnection



def insert_csv(client, database :str, collection :str, csv_file : str, **kwargs) -> None:

    db = client[database]
    coll = db[collection]
    data = pd.read_csv(csv_file).to_dict('record')
    coll.insert_many(data)






if __name__ == "__main__":

    # Set page config
    sf.display_page_config('Weatherboard','⛅')

    # Add page title
    sf.add_page_title('Weatherboard')

    # Change buttons style
    sf.change_button_style()
  
    # initialize OpenWeather connection
    try:
        conn = st.experimental_connection("mongo", type=MongoConnection)
    # return a friendly error if a URI error is thrown 
    except pymongo.errors.ConfigurationError:
        st.error("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?", icon="🚨")
        st.stop()

    client = pymongo.MongoClient(st.secrets.mongo.database)

    #st.write(client.list_database_names())

    db = client.Binance
    #st.write( db.list_collection_names())
   
    klines = db["Klines"]
    #result = klines.find()

    data = klines.find({"Symbol" : "BTCBUSD", "Interval" : "1m"}, {"_id":0})
    
    df = pd.DataFrame(data)
    df


    






   
    

    


    col1, col2, col3 = st.columns([3,2,3])
    with col2:
        if st.button('🏠 Back Home', use_container_width=True):
            switch_page('Home')