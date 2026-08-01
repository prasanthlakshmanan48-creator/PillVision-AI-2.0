import streamlit as st
from PIL import Image

from utils.gemini import analyze_medicine_image
from utils.history import add_history
from utils.pdf import create_pdf

st.set_page_config(
    page_title="Scan Medicine",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Scan Medicine")

uploaded_file = st.file_uploader(
    "Upload Medicine Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Medicine",
        use_container_width=True
    )

    if st.button("🔍 Analyze Medicine"):

        with st.spinner("Analyzing..."):

            try:

                result = analyze_medicine_image(image)

                # Save History
                add_history(
                    "Medicine Scan",
                    "Medicine Image",
                    result
                )

                st.success("✅ Analysis Completed")

                st.markdown(result)

                # Create PDF
                pdf = create_pdf(
                    "Medicine Scan Report",
                    result,
                    "medicine_scan.pdf"
                )

                # Download Button
                with open(pdf, "rb") as file:

                    st.download_button(
                        "📄 Download Scan Report",
                        data=file,
                        file_name="Medicine_Scan_Report.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:

                st.error("❌ Analysis Failed")

                st.exception(e)
