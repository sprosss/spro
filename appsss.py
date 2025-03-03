import subprocess
import sys

# Install required packages if missing
missing_packages = ["openai", "streamlit"]
for package in missing_packages:
    try:
        __import__(package)
    except ModuleNotFoundError:
        subprocess.run([sys.executable, "-m", "pip", "install", package])

import openai
import streamlit as st

st.title("AI Chatbot 🤖 (GPT-4)")

openai.api_key = "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"

user_input = st.text_input("You:", "")

if st.button("Send"):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": user_input}]
    )
    st.write(response["choices"][0]["message"]["content"])
