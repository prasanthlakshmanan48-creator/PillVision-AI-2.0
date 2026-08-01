import streamlit as st

from utils.history import (
    get_history,
    clear_history
)

st.set_page_config(
    page_title="History",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Activity History")

st.write("View all previous medicine scans, searches, AI chats, and interaction checks.")

st.markdown("---")

history = get_history()

# ===========================
# Empty History
# ===========================

if not history:

    st.info("No activity found.")

# ===========================
# Show History
# ===========================

else:

    col1, col2 = st.columns([2,1])

    with col1:

        search = st.text_input(
            "🔍 Search",
            placeholder="Search medicine, question..."
        )

    with col2:

        filter_type = st.selectbox(
            "📂 Filter",
            [
                "All",
                "Medicine Scan",
                "Medicine Search",
                "Drug Interaction",
                "AI Chat"
            ]
        )

    st.success(f"Total Records : {len(history)}")

    st.markdown("---")

    count = 0

    for item in history:

        # Filter
        if filter_type != "All":

            if item["type"] != filter_type:
                continue

        # Search
        if search:

            text = (
                item["title"] +
                item["content"] +
                item["type"]
            ).lower()

            if search.lower() not in text:
                continue

        count += 1

        with st.expander(
            f"{item['type']} | {item['time']}"
        ):

            st.subheader(item["title"])

            st.markdown(item["content"])

    if count == 0:

        st.warning("No matching records found.")

st.markdown("---")

# ===========================
# Clear History
# ===========================

if st.button(
    "🗑 Clear All History",
    use_container_width=True
):

    clear_history()

    st.success("History Cleared Successfully.")

    st.rerun()
