import streamlit as st

from utils.gemini import search_medicine
from utils.history import add_history

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

                # Save to History
                add_history(
                    "Medicine Search",
                    medicine,
                    result
                )

                st.success("✅ Search Completed")

                st.markdown(result)

            except Exception as e:

                st.error("❌ Search Failed")

                st.exception(e)
