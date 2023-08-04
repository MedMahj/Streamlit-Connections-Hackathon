import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.express as px
import pymongo

# My packages
import Style_Functions as sf
from Connections import MongoConnection


if __name__ == "__main__":

    # Set page config
    sf.display_page_config('Cryptoboard','💱')

    # Add page title
    sf.add_page_title('Cryptoboard')

    # Change buttons style
    sf.change_button_style()
  
    # initialize Atlas MongoDB connection
    try:
        conn = st.experimental_connection("mongo", type=MongoConnection)
    # return a friendly error if a URI error is thrown 
    except pymongo.errors.ConfigurationError:
        st.error("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?", icon="🚨")
        st.stop()

   


    






   
    

    


    col1, col2, col3 = st.columns([3,2,3])
    with col2:
        if st.button('🏠 Back Home', use_container_width=True):
            switch_page('Home')