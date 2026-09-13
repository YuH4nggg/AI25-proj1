# Create an app with 2 pages: Home and About me
# Import streamlit package
import streamlit as st
# Insert title 'My App with 2 Pages'
st.title("My App with 2 Pages")

# Insert a sidebar with 2 options: Home and About me
# Insert a sidebar title 'Sidebar'
st.sidebar.title("Sidebar")

# Insert a sidebar selectbox 'Select page' with options 'Home' and 'About me' and assign it to variable 'page'
page = st.sidebar.selectbox("Select page", ("Home", "About Me"))

# If page is 'Home'
if page =="Home":
    # Insert a header 'Home'
    st.header("Home")
    # Insert text 'This is my home page' using st.write
    st.write("This is my home page")
# Else
else:
    # Insert a header 'About me'
    st.header("About Me")
    # Insert text 'This is my about me page' using st.write
    st.write("This is my about me page")

# Run the app:
# py -m streamlit run 5-Question4.py