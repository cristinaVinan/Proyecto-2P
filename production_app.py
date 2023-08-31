# Import Python libraries

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
from collections import namedtuple

# Icon
icon =Image.open("Resources/Logo Petro.png")

# App configuration
st.set_page_config(page_title='PetroGraphix', page_icon=icon)

# App's title
st.title('PetroGraphix')

st.write('----')

# App's description
st.markdown("""This app helps you visualise production curves by year, IPR curves, 
perform calculations, among other things.
""")

# Add aditional info
expander =
