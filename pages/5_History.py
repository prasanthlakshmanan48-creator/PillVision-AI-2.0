import streamlit as st
from utils.history import get_history, clear_history

st.set_page_config(
    page_title="History",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Activity History")

history = get_history()

if len(history) == 0:
    st.info("No history available yet.")

else:

    st.success(f"Total Records: {len(history)}")

    search = st.text_input(
        "🔍 Search History",
        placeholder="Search by medicine or chat..."
    )

    st.markdown("---")

    for item in history:

        if search:
            if (
                search.lower() not in item["title"].lower()
                and search.lower() not in item["type"].lower()
            ):
                continue

        with st.expander(
            f"{item['type']} | {item['time']}"
        ):

            st.subheader(item["title"])

            st.markdown(item["content"])

st.markdown("---")

if st.button("🗑 Clear History", use_container_width=True):

    clear_history()

    st.success("History Cleared")

    st.rerun()
