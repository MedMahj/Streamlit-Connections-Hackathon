
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
    ### How it works 

    This demo app presents two different ways to create data connection using `st.experimental_connection` and showcases the functionality of each connection.
    
    #### Data Sources :

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
    ### What's included

    This app has two new connection classes built by extending the built-in `ExperimentalBaseConnection`:

    1. **MongoConnection**:  This class has four methods :
    > * ` _connect` : used to set up connection to MongoDB using database url.
    > * `insert_csv` : used to insert klines data into collection using CSV file.
    > * `find` : used to extract klines data from collecton with specific parameters (symbol, interval, limit).
    > * `count_documents` : used to count number of documents in a collection.

    2. **OpenWeatherConnection** : This class has two methods :
    > * ` _connect` : used to set up connection to OpenWeatherMap using API Key.
    > * `get` : used to extract weather data with specific parameters (city, units).

    You can find the source code here 😉 : [The link to GitHub repository.](https://github.com/MedMahj/Streamlit-Connections-Hackathon)

    """
    