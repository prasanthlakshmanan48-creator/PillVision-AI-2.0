import streamlit as st

from utils.gemini import search_medicine
from utils.history import add_history
from utils.pdf import create_pdf

st.set_page_config(
    page_title="Medicine Search",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 AI Medicine Search")

st.write("Search any medicine by its name.")

medicine = st.text_input(
    "Medicine Name",
    placeholder="Example: Paracetamol"
)

if st.button("🔍 Search"):

    if medicine.strip() == "":
        st.warning("Please enter a medicine name.")

    else:

        with st.spinner("Searching..."):

            try:

                result = search_medicine(medicine)

                # Save History
                add_history(
                    "Medicine Search",
                    medicine,
                    result
                )

                st.success("✅ Search Completed")

                st.markdown(result)

                # Create PDF
                pdf = create_pdf(
                    "Medicine Search Report",
                    result,
                    "medicine_report.pdf"
                )

                # Download Button
                with open(pdf, "rb") as file:

                    st.download_button(
                        "📄 Download PDF",
                        data=file,
                        file_name="Medicine_Report.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:

                st.error("❌ Search Failed")

                st.exception(e)
