import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from datetime import datetime

# My packages
import Style_Functions as sf
from Connections import OpenWeatherConnection


def display_weather(data, units):
    '''
    This function used to display weather data
    Input:
         - data(json): contains response of openweather API
    '''
    # Check the value of "cod" key is equal to
    # "200", means city is found otherwise,
    # city is not found
    if str(data["cod"]) == "200":

        # store the value corresponding to the city "name"
        city = data["name"]

        # store the value corresponding to the city location (Lon & lat)
        lon = data["coord"]["lon"]
        lat = data["coord"]["lat"]
        
        # store and transform weather time
        time = datetime.fromtimestamp(data["dt"])
 
        # store the value corresponding to the "temp"
        current_temperature = data["main"]["temp"]
 
        # store the value corresponding to the "pressure" 
        current_pressure = data["main"]["pressure"]
 
        # store the value corresponding to the "humidity"
        current_humidity = data["main"]["humidity"]
 
        # store the value corresponding to the "weather description" 
        weather_description = data["weather"][0]["description"]
        
        # temperature unit
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
    sf.display_page_config('Current Weather','⛅')

    # Add page title
    sf.add_page_title('Current Weather')

    # Change buttons style
    sf.change_button_style()

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
    
    # display weather
    display_weather(data, units)

    # back home page
    col1, col2, col3 = st.columns([3,2,3])
    with col2:
        if st.button('🏠 Back Home', use_container_width=True):
            switch_page('Home')

        