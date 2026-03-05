"""
ChatGPT-like Chatbot — Streamlit app with streaming and memory.

Run with: streamlit run chatbot.py
"""

import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 AI Chatbot")

# Sidebar settings
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("OpenAI API Key", type="password",
                             value=os.environ.get("OPENAI_API_KEY", ""))
    model = st.selectbox("Model", ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o"])
    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful, friendly AI assistant.",
        height=100
    )
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7)
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    if not api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
        st.stop()

    client = OpenAI(api_key=api_key)

    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response with streaming
    with st.chat_message("assistant"):
        messages_for_api = [{"role": "system", "content": system_prompt}] + \
                           st.session_state.messages

        stream = client.chat.completions.create(
            model=model,
            messages=messages_for_api,
            temperature=temperature,
            stream=True
        )

        response = st.write_stream(stream)

    st.session_state.messages.append({"role": "assistant", "content": response})
