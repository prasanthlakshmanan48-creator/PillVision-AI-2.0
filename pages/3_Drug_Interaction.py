import streamlit as st

from utils.gemini import drug_interaction
from utils.history import add_history

st.set_page_config(
    page_title="Drug Interaction Checker",
    page_icon="⚠️",
    layout="wide"
)

st.title("⚠️ Drug Interaction Checker")

st.write("Check whether two medicines are safe to take together.")

col1, col2 = st.columns(2)

with col1:
    medicine1 = st.text_input(
        "💊 Medicine 1",
        placeholder="Example: Paracetamol"
    )

with col2:
    medicine2 = st.text_input(
        "💊 Medicine 2",
        placeholder="Example: Ibuprofen"
    )

if st.button("🔍 Check Interaction", use_container_width=True):

    if medicine1.strip() == "" or medicine2.strip() == "":
        st.warning("Please enter both medicine names.")

    else:

        with st.spinner("Analyzing interaction..."):

            try:

                result = drug_interaction(
                    medicine1,
                    medicine2
                )

                # Save to History
                add_history(
                    "Drug Interaction",
                    f"{medicine1} + {medicine2}",
                    result
                )

                st.success("✅ Analysis Completed")

                st.markdown(result)

            except Exception as e:

                st.error("❌ Unable to analyze interaction.")

                st.exception(e)
