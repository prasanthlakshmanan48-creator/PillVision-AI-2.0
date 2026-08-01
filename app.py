import streamlit as st

st.set_page_config(
    page_title="PillVision AI",
    page_icon="💊",
    layout="wide"
)

st.title("💊 PillVision AI")
st.subheader("AI Powered Medicine Recognition & Healthcare Assistant")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💊 Medicine Scan", "AI")

with col2:
    st.metric("🔍 Search", "Available")

with col3:
    st.metric("⚠️ Interaction", "Checker")

with col4:
    st.metric("🤖 AI Chat", "Online")

st.markdown("---")

st.header("✨ Features")

c1, c2 = st.columns(2)

with c1:
    st.success("📷 Scan Medicine")
    st.success("🔍 Search Medicine")
    st.success("⚠️ Drug Interaction Checker")

with c2:
    st.success("💬 AI Health Chat")
    st.success("📚 Activity History")
    st.success("📄 Download PDF Report")

st.markdown("---")

st.info("👈 Select a feature from the sidebar.")

st.markdown("---")

st.subheader("📊 Project Statistics")

a, b, c = st.columns(3)

with a:
    st.metric("Version", "2.0")

with b:
    st.metric("AI Model", "Gemini")

with c:
    st.metric("Status", "🟢 Online")

st.markdown("---")

st.warning("""
⚠️ Educational Use Only

This application is not a substitute for professional medical advice.

Always consult a qualified doctor or pharmacist before taking medicines.
""")
