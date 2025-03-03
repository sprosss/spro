import openai
import streamlit as st

client = openai.OpenAI(api_key=st.secrets["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"])# Replace with your actual OpenAI API key

# Streamlit UI
st.title("Chat with GPT-4")
st.write("Enter your question below:")

# User input
user_input = st.text_input("Your message:", "")

if st.button("Send"):
    if user_input:
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": user_input}]
        )
        
        # Display response
        st.write("### GPT-4 Response:")
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter a message before sending.")
