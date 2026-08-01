import streamlit as st
from datetime import datetime

# Add new history record
def add_history(history_type, title, content):

    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.insert(0, {
        "type": history_type,
        "title": title,
        "content": content,
        "time": datetime.now().strftime("%d-%m-%Y %H:%M")
    })


# Get all history
def get_history():

    if "history" not in st.session_state:
        st.session_state.history = []

    return st.session_state.history


# Clear history
def clear_history():

    st.session_state.history = []


# Total records
def history_count():

    if "history" not in st.session_state:
        return 0

    return len(st.session_state.history)
