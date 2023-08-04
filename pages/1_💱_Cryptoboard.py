import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pymongo
import pandas as pd
import plotly.express as px

# My packages
import Style_Functions as sf
from Connections import MongoConnection


def display_klines(df):
    """ 
    This function used to display klines data using plotly charts  
    Input:
          - df(pandas.DataFrame) : contains klines data.
    """

    # Open & Close price
    fig1 = px.line(df, x='Open_date', y=['Open_price', 'Close_price'], color_discrete_sequence=["green","orange",]) 
    fig1.update_layout(title='Open & Close Prices',
                      xaxis_title='Time',
                      yaxis_title='Price',
                    )    
    st.plotly_chart(fig1, use_container_width=True)

    # Low open & High price
    fig2 = px.line(df, x='Open_date', y=['Low_price', 'High_price'], color_discrete_sequence=["red","blue",]) 
    fig2.update_layout(title='Low & High Prices',
                      xaxis_title='Time',
                      yaxis_title='Price',
                    )    
    st.plotly_chart(fig2, use_container_width=True)

    # Number of trades
    fig3 = px.line(df, x='Open_date', y=['Number_trades']) 
    fig3.update_layout(title='Trades Number',
                      xaxis_title='Time',
                      yaxis_title='Number',
                    )    
    st.plotly_chart(fig3, use_container_width=True)

    # Volume
    fig4 = px.line(df, x='Open_date', y=['Volume']) 
    fig4.update_layout(title='Trades Volume',
                      xaxis_title='Time',
                      yaxis_title='Volume',
                    )    
    st.plotly_chart(fig4, use_container_width=True)


if __name__ == "__main__":

    # Set page config
    sf.display_page_config('Cryptoboard','💱')

    # Add page title
    sf.add_page_title('Cryptoboard')

    # Change buttons style
    sf.change_button_style()
  
    # initialize MongoDB connection
    try:
        conn = st.experimental_connection("mongo", type=MongoConnection)
    # return a friendly error if a URI error is thrown 
    except pymongo.errors.ConfigurationError:
        st.error("An Invalid URI host error was received. Is your MongoDB host name correct in your connection string?", icon="🚨")
        st.stop()

    #st.write(conn)
    #st.help(conn)

    
    
    database = "Binance"
    collection = "Klines"

    try:
        nbr = conn.count_documents("Binance", "Klines")
        assert nbr > 0
    except AssertionError:
        st.warning('Your database is empty ! Click on the button below to insert data to your database :', icon="⚠️") 
        col1, col2, col3 = st.columns([3,2,3])
        with col2:
            if st.button('⬇️ Insert Data', use_container_width=True):
                with st.spinner('Loading...'):
                    conn.insert_csv("Binance", "Klines", "./data/klines.csv")
                switch_page('Cryptoboard')
        st.stop()

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
              100
              ]

    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        symbol_option = st.selectbox('Choose Symbol :',SYMBOLS)
    with col2:
        interval_option = st.selectbox('Choose Time Interval :',INTERVALS, index=2)
    with col3:
        limit_option = st.selectbox('Choose Limit :',LIMITS, index=2)

    df = conn.find(database, collection, symbol_option, interval_option, limit_option)
    
    st.subheader(symbol_option + " 🪙")

    display_klines(df)

   


    






   
    

    


    col1, col2, col3 = st.columns([3,2,3])
    with col2:
        if st.button('🏠 Back Home', use_container_width=True):
            switch_page('Home')