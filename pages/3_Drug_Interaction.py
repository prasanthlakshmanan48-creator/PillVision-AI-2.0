import streamlit as st

from utils.gemini import drug_interaction
from utils.history import add_history
from utils.pdf import create_pdf

st.set_page_config(
    page_title="Drug Interaction Checker",
    page_icon="⚠️",
    layout="wide"
)

st.title("⚠️ Drug Interaction Checker")

st.write("Check whether two medicines are safe to take together.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    medicine1 = st.text_input(
        "💊 Medicine 1",
        placeholder="Example: Dolo 650"
    )

with col2:
    medicine2 = st.text_input(
        "💊 Medicine 2",
        placeholder="Example: Ibuprofen"
    )

if st.button(
    "🔍 Check Interaction",
    use_container_width=True
):

    if medicine1.strip() == "" or medicine2.strip() == "":
        st.warning("Please enter both medicine names.")

    else:

        with st.spinner("Analyzing drug interaction..."):

            try:

                result = drug_interaction(
                    medicine1,
                    medicine2
                )

                # Save History
                add_history(
                    "Drug Interaction",
                    f"{medicine1} + {medicine2}",
                    result
                )

                st.success("✅ Analysis Completed")

                st.markdown(result)

                st.markdown("---")

                # PDF Report
                pdf = create_pdf(
                    "Drug Interaction Report",
                    result,
                    "drug_interaction_report.pdf"
                )

                with open(pdf, "rb") as file:

                    st.download_button(
                        "📄 Download Interaction Report",
                        data=file,
                        file_name="Drug_Interaction_Report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            except Exception as e:

                st.error("❌ Unable to analyze interaction.")

                st.exception(e)

st.markdown("---")

st.subheader("💡 Quick Examples")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("Dolo 650 + Ibuprofen"):
        st.session_state["example1"] = (
            "Dolo 650",
            "Ibuprofen"
        )

with c2:
    if st.button("Paracetamol + Cetirizine"):
        st.session_state["example2"] = (
            "Paracetamol",
            "Cetirizine"
        )

with c3:
    if st.button("Metformin + Insulin"):
        st.session_state["example3"] = (
            "Metformin",
            "Insulin"
        )

example = None

if "example1" in st.session_state:
    example = st.session_state.pop("example1")

elif "example2" in st.session_state:
    example = st.session_state.pop("example2")

elif "example3" in st.session_state:
    example = st.session_state.pop("example3")

if example:

    with st.spinner("Checking example..."):

        try:

            result = drug_interaction(
                example[0],
                example[1]
            )

            st.success(
                f"Example
