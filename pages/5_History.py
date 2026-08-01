import streamlit as st
from utils.history import get_history, clear_history

st.set_page_config(
    page_title="History",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Activity History")

history = get_history()

if not history:

    st.info("No history found.")

else:

    st.success(f"Total Records : {len(history)}")

    for item in history:

        with st.expander(
            f"{item['type']} | {item['time']}"
        ):

            st.subheader(item["title"])

            st.markdown(item["content"])

st.markdown("---")

if st.button("🗑 Clear History"):

    clear_history()

    st.success("History Cleared")

    st.rerun()
