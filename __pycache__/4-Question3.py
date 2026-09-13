# Create a form that allows users to enter their personal details and submit it.
# Import streamlit package
import streamlit as st

# Insert title 'My Personal Details Form'
st.title("My Personal Details Form")
# Insert subheader 'Please enter your personal details'
st.subheader("Please enter your personal details")

# Insert a text input field for 'Name' and assign it to a variable 'name'
name = st.text_input("Name")
# Insert a number input field for 'Age' and assign it to a variable 'age'
age = st.number_input("Age")
# Insert a text area field for 'Address' and assign it to variable 'address'
adress = st.text_area("address")
# Insert a selectbox for 'Gender' with options 'Male' and 'Female' and assign it to 'gender'
gender = st.selectbox("gender", ["Male", "Female"])

# Insert a camera input field for 'Photo' and assign it to variable 'photo'
photo = st.camera_input("Photo")

# Insert a checkbox for 'I agree to the terms and conditions' and assign it to variable 'agree'
agree = st.checkbox("I agree to the terms and conditions")
# Insert a button for 'Submit' and assign it to variable 'submit'
submit = st.button("Submit")

# If submit is clicked
if submit:
    st.write("Thank you for submitting your details")
    # Display 'Thank you for submitting your details' on the app using st.write


# Run the app:
# py -m streamlit run 4-Question3.py