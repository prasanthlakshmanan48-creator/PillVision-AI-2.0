import streamlit as st
from utils.history import get_history, clear_history

st.set_page_config(
    page_title="History",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Activity History")

st.write("History page loaded successfully.")

history = get_history()

st.write("History object:", history)

if len(history) == 0:
    st.info("No history available yet.")

else:
    st.success(f"Total Records: {len(history)}")

    for item in history:
        st.write(item)

if st.button("🗑 Clear History"):
    clear_history()
    st.rerun()
