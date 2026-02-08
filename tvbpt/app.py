import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="Broadband Chatbot", page_icon="🌐")

st.title("🌐 Broadband Assistant")
st.write("Ask me anything about broadband plans, WiFi speed, routers, etc.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input
user_input = st.chat_input("Ask your broadband question...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    prompt = f"""
    You are a broadband expert assistant.
    Only answer questions related to internet, wifi, broadband plans,
    speed, routers, and data usage.

    User Question: {user_input}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    answer = response.text

    st.chat_message("assistant").write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

import os
port = int(os.environ.get("PORT", 8501))
