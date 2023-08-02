import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from datetime import datetime



# My packages
import Commun_Functions as cf
from Connections import OpenWeatherConnection


def display_weather(data, units):
    '''
    '''
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if str(data["cod"]) == "200":
 
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

        city = data["name"]
        time = datetime.fromtimestamp(data["dt"])
        st.write(time )

        unit_str = " °C" if units == "metric" else " °F"
 
        # display following values
        col1, col2, col3 = st.columns([2,3,1])
        col1.metric(label="City 🌎", value=city)
        col2.metric(label="Weather ⛅", value=weather_description)
        col3.metric(label="Time(UTC) 🕗", value=str(time)[-8:-3])
        

        col1, col2, col3 = st.columns([2,3,1])
        col1.metric(label="Temperature 🌡️", value=str(current_temperature) + unit_str)
        col2.metric(label="Atmospheric Pressure 💨", value=str(current_pressure) +" hPa")
        col3.metric(label="Humidity 💦", value=str(current_humidity) +" %")
        

        # display city map
        df = pd.DataFrame([[lat , lon]], columns=['LAT', 'LON'])
        st.map(df, zoom=6)

 
    elif str(data["cod"]) == "404":
        st.write("")
        st.error('City Not Found ! Try valid name (ex. : Paris, Tokyo, New York...).', icon="🚨")
    
    else:
        st.write("")
        st.error(data["message"], icon="🚨")

        

if __name__ == "__main__":

    # Set page config
    cf.display_page_config('Weatherboard','⛅')

    # Add page title
    cf.add_page_title('Weatherboard')

    # Change buttons style
    cf.change_button_style()

    # initialize OpenWeather connection
    conn = st.experimental_connection("openweather", type=OpenWeatherConnection)

    # Enter city name et choose units
    col1, col2 = st.columns([3,1])
    with col1:
        city = st.text_input('Enter City Name', 'Paris')
    with col2:
        units_options = ['metric', 'imperial']
        units = st.selectbox('Choose Units :', units_options)

    # Extract data from API
    data = conn.get(city, units)
    
    #data

    # display weather
    display_weather(data, units)

    
    
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

        