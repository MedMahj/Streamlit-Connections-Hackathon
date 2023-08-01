import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import numpy as np
import plotly.express as px
import requests

# My packages
import Commun_Functions as cf
from Connections import OpenWeatherConnection


def display_weather(data):
    '''
    '''
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if data["cod"] != "404":
 
        # store the value of "main"
        # key in variable y
        main = data["main"]
 
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = main["temp"]
 
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = main["pressure"]
 
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = main["humidity"]
 
        # store the value of "weather"
        # key in variable z
        weather = data["weather"]
 
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = weather[0]["description"]

        lon = data["coord"]["lon"]
        lat = data["coord"]["lat"]
 
        # displau following values
        col1, col2, col3 = st.columns([1,1,1])
        col1.metric(label="Temperature 🌡️", value=str(current_temperature) +" °K")
        col2.metric(label="Atmospheric Pressure 💨", value=str(current_pressure) +" hPa")
        col3.metric(label="Humidity 💦", value=str(current_humidity) +" %")

        # display city map
        df = pd.DataFrame([[lat , lon]], columns=['LAT', 'LON'])
        st.map(df, zoom=6)

 
    else:
        st.write("")
        st.error('City Not Found', icon="🚨")
        



def find_weather(api_key):
    '''
    '''
    # import required modules
    import requests, json
 
    # Enter your API key here
    api_key = api_key
 
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
    # Give city name
    city_name = st.text_input('Enter City Name', 'Paris')
 
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
 
    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()
 
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
 
        # store the value of "main"
        # key in variable y
        y = x["main"]
 
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
 
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
 
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
 
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
 
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
 
        # print following values
        st.write(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
              "\n humidity (in percentage) = " +
                        str(current_humidity) +
              "\n description = " +
                        str(weather_description))
 
    else:
        st.write(" City Not Found ")
        st.write(x["cod"])





if __name__ == "__main__":

    # Set page config
    cf.display_page_config('Weatherboard','⛅')

    # Add page title
    cf.add_page_title('Weatherboard')

    # Change buttons style
    cf.change_button_style()

    # initialize OpenWeather connection
    conn = st.experimental_connection("openweather", type=OpenWeatherConnection)

    # Enter city name
    city = st.text_input('Enter City Name', 'Paris')
    data = conn.get(city)
    
    #data

    # display weather
    display_weather(data)

    
    
    #API_key=""
    #find_weather(API_key)

    #url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid{API_key}"
    #data = requests.get(url).json()
    #data

    #url = "https://api.binance.com/api/v3/klines?symbol=BTCBUSD&interval=1d&limit=10"
    #data = requests.get(url).json()
    #data


    col1, col2, col3 = st.columns([3,2,3])
    with col2:
        if st.button('🏠 Back Home', use_container_width=True):
            switch_page('Home')

        