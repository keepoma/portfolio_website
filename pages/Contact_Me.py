import streamlit as st
from send_email import send_email

st.header("Contact form")

with st.form(key="email_form"):
    user_email = st.text_input("Enter mail address")
    user_message = st.text_area("Enter your message")
    message = f"""\
Subject: A user has sent you a message

From: {user_email}
{user_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.markdown("Message sent!")