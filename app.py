import logging

import streamlit as st

logging.basicConfig()
logger = logging.getLogger('fota')
logger.setLevel(logging.DEBUG)

color = st.color_picker('Pick A Color', '#cccccc')
st.write('The current color is', color)
