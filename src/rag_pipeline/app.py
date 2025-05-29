# app.py

import streamlit as st
from graph.builder import build_app

st.set_page_config(page_title="NehaGPT - Resume Assistant", layout="centered")
# Inject custom CSS to restrict width
st.markdown("""
    <style>
        .main .block-container {
            max-width: 400px;
            padding-left: 10rem;
            padding-right: 10rem;
        }
    </style>
    """, unsafe_allow_html=True)

# Add Back button
if st.button("Back to Portfolio"):
    st.markdown("""
        <meta http-equiv="refresh" content="0; url='https://nehasjportfolio.vercel.app/'" />
    """, unsafe_allow_html=True)

# Title and intro
st.image("banner.png", width=1000)
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
