import streamlit as st
import openai

# Set up OpenAI API Key
openai.api_key = st.secrets["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"]  # Store in Streamlit Secrets (Step 3)

st.title("AI Chatbot 🤖 (Powered by GPT-4)")

user_input = st.text_input("You:", "")

if st.button("Send"):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": user_input}]
    )
    st.write(response["choices"][0]["message"]["content"])
