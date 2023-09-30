import streamlit as st

st.header("Contact form")

with st.form(key="email_form"):
    user_email = st.text_input("Enter mail address")
    user_message = st.text_area("Enter your message")
    button = st.form_submit_button("Submit")