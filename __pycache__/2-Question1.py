import numpy as np
import pandas as pd

# import streamlit package
import streamlit as st


# Insert a streamlit title 'My First Streamlit App'
st.title("My First Streamlit App")


# Insert a streamlit header 'Details of my first Streamlit App'
st.header("Details of my first Streamlit App")


# Insert streamlit text 'This is my first streamlit app'
st.text("This is my first streamlit app")

# Insert streamlit markdown '<p style="color:blue">A very cool app</p>'
# In the function, set the parameter "unsafe_allow_html" to True
st.markdown('<p style="color:blue">A very cool app</p>', unsafe_allow_html=True)


# Run the app:
# py -m streamlit run 2-Question1.py