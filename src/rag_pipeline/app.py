# app.py

import streamlit as st
from graph.builder import build_app

st.set_page_config(page_title="NehaGPT - Resume Assistant", layout="wide")

# Title and intro
st.title("NehaGPT - Ask About Neha Jagtap")

with st.expander("⚠️ Disclaimer"):
    st.write("""
    This bot is powered by GPT-4-turbo and designed to answer questions about Neha Jagtap's professional profile. 
    The answers are generated using a Retrieval-Augmented Generation system. Please avoid personal or off-topic questions.
    """)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "graph" not in st.session_state:
    st.session_state.graph = build_app()

# Chat input at the bottom
st.markdown("### Ask something about Neha's resume")
user_input = st.chat_input("Type your question here...")

# Process input
if user_input:
    # Show user's question
    st.session_state.chat_history.append(("user", user_input))

    # Get response from LangGraph app
    result = st.session_state.graph.invoke({"question": user_input})
    answer = result["generation"]

    # Save assistant's reply
    st.session_state.chat_history.append(("bot", answer))

# Display full chat history
for role, message in st.session_state.chat_history:
    if role == "user":
        st.chat_message("user").markdown(message)
    else:
        st.chat_message("assistant").markdown(message)
