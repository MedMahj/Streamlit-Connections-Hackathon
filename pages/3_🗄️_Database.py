import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.express as px

# My packages
import Commun_Functions as cf
from Connections import BinanceAPI





if __name__ == "__main__":

    # Set page config
    cf.display_page_config('Weatherboard','⛅')

    # Add page title
    cf.add_page_title('Weatherboard')

    # Change buttons style
    cf.change_button_style()
    

    


    col1, col2, col3 = st.columns([3,2,3])
    with col2:
        if st.button('🏠 Back Home', use_container_width=True):
            switch_page('Home')