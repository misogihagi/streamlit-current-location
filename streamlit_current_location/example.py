import streamlit as st
from __init__ import current_position

result = current_position()
if result:
    st.write(
        f"""your location is 
    latitude: {result['latitude']}
    longitude: {result['longitude']}
    """
    )
