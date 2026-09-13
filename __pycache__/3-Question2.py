# Building a simple streamlit app that:
# 1. Prints 'Goodbye' by default
# 2. Prints 'Hello' if the user clicks on the button 'Say Hello'

import numpy as np
import pandas as pd

# import streamlit package
import streamlit as st

# Insert a streamlit title 'My Greeting Streamlit App'
st.title("My Greeting Streamlit App")

# Insert streamlit button 'Say Hello' and assign it to a variable 'btn'

# If btn is clicked
if st.button("Say Hello"):
    # Display 'Hello' on the app using st.text
        st.text("Hello")

# Else
# else st.text("Goodbye")
    # Display 'Goodbye' on the app using st.text


# Run the app:
# py -m streamlit run 3-Question2.py
