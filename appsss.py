import streamlit as st

st.title("Simple Chatbot 🤖")

user_input = st.text_input("You:", "")

if st.button("Send"):
    response = f"You said: {user_input}. I'm still learning!"
    st.write(response)
