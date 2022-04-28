import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
st.title('IEEE IoT')
from PIL import Image
image = Image.open('sunrise.jpg')
st.image(image, caption='Sunrise by the mountains')
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
  with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
