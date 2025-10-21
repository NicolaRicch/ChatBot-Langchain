import streamlit as st
from chatbot_llm import chat
import streamlit.components.v1 as components

st.set_page_config(page_title="Chatbot LLM - Portfolio", page_icon="🤖", layout="centered")

# ---------- STILE PERSONALIZZATO ----------
st.markdown("""
    <style>
    .chat-container {
        background-color: #f4f4f8;
        padding: 1rem;
        border-radius: 10px;
        max-height: 500px;
        overflow-y: auto;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #DCF8C6;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        text-align: right;
    }
    .bot-message {
        background-color: #FFFFFF;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        border: 1px solid #e6e6e6;
    }
    .message {
        font-size: 1rem;
        line-height: 1.4;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Chatbot con Gemma 2B")
st.caption("Creato con LangChain, Streamlit e Ollama")

# ---------- STATO ----------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------- INTERAZIONE ----------
user_input = st.text_input("✍️ Scrivi un messaggio e premi invio", placeholder="Cosa vuoi sapere?", label_visibility="collapsed")

if st.button("Invia", use_container_width=True) and user_input:
    response = chat(user_input)
    st.session_state.history.append(("user", user_input))
    st.session_state.history.append(("bot", response))

# ---------- VISUALIZZAZIONE MESSAGGI ----------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for role, message in st.session_state.history:
    if role == "user":
        st.markdown(f'<div class="user-message message">🧑‍💻 {message}', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message message">🤖 {message}', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
