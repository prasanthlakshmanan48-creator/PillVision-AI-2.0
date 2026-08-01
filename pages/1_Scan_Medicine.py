import streamlit as st
from PIL import Image
import json

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

                # Save history
                add_history(
                    "Medicine Scan",
                    "Medicine Image",
                    result
                )

                st.success("✅ Analysis Completed")

                # Try to display JSON nicely
                try:

                    data = json.loads(result)

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric("💊 Medicine", data.get("medicine_name", "Unknown"))
                        st.metric("🧪 Active Ingredient", data.get("active_ingredient", "Unknown"))
                        st.metric("🏭 Manufacturer", data.get("manufacturer", "Unknown"))
                        st.metric("💉 Strength", data.get("strength", "Unknown"))

                    with col2:
                        st.metric("🩺 Uses", data.get("uses", "Unknown"))
                        st.metric("💊 Dosage", data.get("dosage", "Unknown"))
                        st.metric("⚠️ Side Effects", data.get("side_effects", "Unknown"))
                        st.metric("🤰 Pregnancy", data.get("pregnancy", "Unknown"))

                    st.subheader("🔄 Drug Interactions")
                    st.write(data.get("drug_interactions", "Unknown"))

                    st.subheader("📦 Storage")
                    st.write(data.get("storage", "Unknown"))

                    st.subheader("📝 Summary")
                    st.write(data.get("summary", "Unknown"))

                except Exception:
                    # If Gemini returns Markdown instead of JSON
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
