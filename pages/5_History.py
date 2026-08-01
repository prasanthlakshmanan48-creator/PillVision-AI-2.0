import streamlit as st
from datetime import datetime


def add_history(history_type, title, content):

    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.insert(0, {
        "type": history_type,
        "title": title,
        "content": content,
        "time": datetime.now().strftime("%d-%m-%Y %H:%M")
    })


def get_history():

    if "history" not in st.session_state:
        st.session_state.history = []

    return st.session_state.history


def clear_history():

    st.session_state.history = []


def history_count():

    return len(get_history())
