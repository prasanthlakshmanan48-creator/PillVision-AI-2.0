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

st.write("Search detailed information about any medicine.")

st.markdown("---")

medicine = st.text_input(
    "💊 Enter Medicine Name",
    placeholder="Example: Dolo 650"
)

search = st.button(
    "🔍 Search Medicine",
    use_container_width=True
)

if search:

    if medicine.strip() == "":
        st.warning("Please enter a medicine name.")

    else:

        with st.spinner("Searching medicine database..."):

            try:

                result = search_medicine(medicine)

                add_history(
                    "Medicine Search",
                    medicine,
                    result
                )

                st.success("Medicine Found")

                st.markdown(result)

                st.markdown("---")

                pdf = create_pdf(
                    "Medicine Search Report",
                    result,
                    "medicine_search_report.pdf"
                )

                with open(pdf, "rb") as file:

                    st.download_button(
                        "📄 Download Report",
                        data=file,
                        file_name="Medicine_Search_Report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            except Exception as e:

                st.error("Unable to search medicine.")

                st.exception(e)

st.markdown("---")

st.subheader("💡 Popular Medicines")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Dolo 650"):
        st.session_state["quick_search"] = "Dolo 650"

with col2:
    if st.button("Paracetamol"):
        st.session_state["quick_search"] = "Paracetamol"

with col3:
    if st.button("Azithromycin"):
        st.session_state["quick_search"] = "Azithromycin"

if "quick_search" in st.session_state:

    with st.spinner("Loading medicine..."):

        try:

            result = search_medicine(
                st.session_state["quick_search"]
            )

            st.success(
                f"Result for {st.session_state['quick_search']}"
            )

            st.markdown(result)

        except Exception as e:

            st.error("Search failed.")

            st.exception(e)
