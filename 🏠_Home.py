
# Streamlit packages
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
# My packages
import Style_Functions as sf


if __name__ == "__main__":

    # Set page config
    sf.display_page_config()
    
    # Add page title
    sf.add_page_title()

    # Change buttons style
    sf.change_button_style()

    """

    This demo app presents two different ways to create data connection using `st.experimental_connection` and showcases the functionality of each connection :

    - **Database** : [MongoDB Atlas](https://www.mongodb.com/atlas) used to extract Klines data from database and display **Cryptoboard**.
    - **Secured API** : [OpenWeatherMap API](https://openweathermap.org/api) used to extract Weather data and display **Current Weather**.
  
    👇 Click on the buttons to see how it works!

    """
    
    col1, col2, col3 = st.columns([1,4,11])
    with col2:

        if st.button('💱 Cryptoboard', use_container_width=True):
            switch_page('Cryptoboard')
    
        if st.button('⛅ Current Weather', use_container_width=True):
            switch_page('Current Weather')
    

    """

    [The link to GitHub repository.](https://github.com/MedMahj/Streamlit-Connections-Hackathon)

    """
    