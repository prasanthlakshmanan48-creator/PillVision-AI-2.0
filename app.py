import streamlit as st

from utils.dashboard import (
    total_records,
    total_scans,
    total_searches,
    total_interactions,
    total_chats
)

st.set_page_config(
    page_title="PillVision AI",
    page_icon="💊",
    layout="wide"
)

st.title("💊 PillVision AI")
st.subheader("AI Powered Medicine Recognition & Healthcare Assistant")

st.markdown("---")

# ============================
# Dashboard
# ============================

st.header("📊 Dashboard")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("📂 Total Activities", total_records())

with col2:
    st.metric("💊 Medicine Scans", total_scans())

with col3:
    st.metric("🔍 Searches", total_searches())

with col4:
    st.metric("⚠️ Interactions", total_interactions())

with col5:
    st.metric("💬 AI Chats", total_chats())

st.markdown("---")

# ============================
# Features
# ============================

st.header("✨ Features")

left, right = st.columns(2)

with left:

    st.success("📷 Scan Medicine")

    st.success("🔍 Medicine Search")

    st.success("⚠️ Drug Interaction Checker")

with right:

    st.success("💬 AI Health Chat")

    st.success("📚 History")

    st.success("📄 PDF Reports")

st.markdown("---")

st.info("👈 Use the sidebar to access all features.")

st.markdown("---")

# ============================
# Project Info
# ============================

st.header("ℹ️ Project Information")

a, b, c = st.columns(3)

with a:
    st.metric("Version", "2.0")

with b:
    st.metric("AI Model", "Gemini")

with c:
    st.metric("Status", "🟢 Online")

st.markdown("---")

st.warning(
    """
### ⚠️ Disclaimer

This application is intended for **educational purposes only**.

Always consult a qualified doctor or pharmacist before taking any medicine.
"""
)
