import streamlit as st

def display_page_config(title='Connections Hackathon', icon="🔌"):
    '''
    This function used to set page config
    '''
    st.set_page_config(
        page_title = title,
        page_icon = icon,
        menu_items = {
            'Get Help': 'https://www.linkedin.com/in/bousetta-mahjoub-mohamed/',
            'Report a bug': "mailto:mohamed.bousettamahjoub@hardis-group.com",
            'About': "## Made by Mohame BOUSETTA MAHJOUB (*Hardis Group*) 😊"
        }
    )


def add_page_title(title='Connections Hackathon'):
    '''
    This function used to addd page title
    '''
    st.markdown(f""" <h1 style='
                text-align:center; 
                border-radius:25px; 
                background-color:#f3feff; 
                color:#0493ab; 
                margin-bottom: 25px;'>
                {title}</h1>""",
                unsafe_allow_html=True)


def change_button_style():
    '''
    This function used to change buttons style
    '''
    html = """
        <style>
            .stButton button {
                background-color: #0493ab;
                color: white ;
                text-align: center;
                border-radius: 25px;
            }
        </style>
    """
    st.markdown(html, unsafe_allow_html=True)
