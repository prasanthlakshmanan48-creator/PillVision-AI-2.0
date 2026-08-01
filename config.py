import streamlit as st
from google import genai

MODEL_NAME = "gemini-flash-latest"

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)
