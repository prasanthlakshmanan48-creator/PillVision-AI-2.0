import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("💊 About PillVision AI")

st.markdown("""
## AI Powered Medicine Recognition System

PillVision AI helps users identify medicines and provides educational information using Google Gemini AI.
""")

st.markdown("---")

st.subheader("✨ Features")

st.success("📷 Scan Medicine")

st.success("🔍 Medicine Search")

st.success("⚠️ Drug Interaction Checker")

st.success("💬 AI Health Chat")

st.success("📚 Activity History")

st.success("🤖 Google Gemini AI")

st.markdown("---")

st.subheader("🛠 Technologies Used")

st.info("""
- Python
- Streamlit
- Google Gemini AI
- Pillow
- ReportLab
- EasyOCR
""")

st.markdown("---")

st.subheader("👨‍💻 Developer")

st.write("**Name:** Prasanth L")

st.write("**Department:** Biomedical Engineering")

st.write("**Project:** PillVision AI")

st.write("**Version:** 1.0")

st.markdown("---")

st.warning("""
This application is for educational purposes only.

Always consult a qualified doctor or pharmacist before taking any medicine.
""")
