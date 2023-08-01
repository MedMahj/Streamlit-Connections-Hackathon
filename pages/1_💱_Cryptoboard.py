import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.express as px

# My packages
import Commun_Functions as cf
from Connections import BinanceAPI





if __name__ == "__main__":

    # Set page config
    cf.display_page_config('Cryptoboard','💱')

    # Add page title
    cf.add_page_title('Cryptoboard')

    # Change buttons style
    cf.change_button_style()
    
    
    SYMBOLS = ['BTCBUSD',
           'BNBBUSD',
           'ETHBUSD',
           'DOGEBUSD',
           'HOOKBUSD']
    INTERVALS = ['1m', 
                 '5m',
                '15m',
                '1h', 
                '1d']
    LIMITS = [10,
              50,
              100,
              500,
              1000]

    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        symbol_option = st.selectbox('Choose Symbol :',SYMBOLS)
    with col2:
        interval_option = st.selectbox('Choose Time Interval :',INTERVALS)
    with col3:
        limit_option = st.selectbox('Choose Limit :',LIMITS, index=2)
    
    #conn = st.experimental_connection(name='binance', type=BinanceAPI)
    conn = BinanceAPI('binance')

    df = conn.get(symbol=symbol_option, interval=interval_option, limit=limit_option)
    st.dataframe(df)

    st.subheader(symbol_option)

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


    col1, col2, col3 = st.columns([3,2,3])
    with col2:
        if st.button('🏠 Back Home', use_container_width=True):
            switch_page('Home')

        