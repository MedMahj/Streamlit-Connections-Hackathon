
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

    This demo app shows three different ways to create data connection using `st.experimental_connection` and showcases the functionality of each connection :

    - **Public API** : [Binance API](https://binance-docs.github.io/apidocs/spot/en/#introduction) used to extract Klines data and create a Cryptoboard.
    - **Secured API** :
    - **Database** :

    👇 Click on the button to see how it works!


    """
    
    col1, col2, col3 = st.columns([1,4,11])
    with col2:

        if st.button('💱 Cryptoboard', use_container_width=True):
            switch_page('Cryptoboard')
    
        if st.button('⛅ Current Weather', use_container_width=True):
            switch_page('Current Weather')

        if st.button('🗄️ Database', use_container_width=True):
            switch_page('Database')
    

    """

    [The link to GitHub repository.](https://github.com/MedMahj/Streamlit-Connections-Hackathon)

    """
    