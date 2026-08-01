import streamlit as st
from PIL import Image
import json

from utils.gemini import analyze_medicine_image
from utils.history import add_history
from utils.pdf import create_pdf
from utils.ocr import extract_text

st.set_page_config(
    page_title="Scan Medicine",
    page_icon="💊",
    layout="wide"
)

st.title("💊 AI Medicine Scanner")
st.write("Upload a medicine strip, box, or bottle image for AI analysis.")

st.markdown("---")

# ===============================
# Upload Options
# ===============================

tab1, tab2 = st.tabs(["📂 Upload Image", "📷 Camera"])

with tab1:
    uploaded_file = st.file_uploader(
        "Upload Medicine Image",
        type=["jpg", "jpeg", "png"]
    )

with tab2:
    uploaded_file = st.camera_input(
        "Take Medicine Photo"
    )

if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1,1])

    with col1:
        st.image(
            image,
            caption="Uploaded Medicine",
            use_container_width=True
        )

    with col2:

        st.subheader("🔍 OCR Preview")

        with st.spinner("Reading text..."):

            ocr = extract_text(image)

            st.code(ocr)

            # Estimated confidence
            if ocr == "No readable text detected.":
                confidence = 30
            elif len(ocr) < 20:
                confidence = 60
            else:
                confidence = 90

            st.progress(confidence / 100)

            st.success(
                f"Recognition Confidence: {confidence}%"
            )

    st.markdown("---")

    if st.button(
        "🤖 Analyze Medicine",
        use_container_width=True
    ):

        with st.spinner("Gemini AI is analyzing..."):

            try:

                result = analyze_medicine_image(image)

                add_history(
                    "Medicine Scan",
                    "Medicine Image",
                    result
                )

                st.success("Analysis Completed")

                # ----------------------
                # JSON Parsing
                # ----------------------

                try:

                    clean = result.replace(
                        "```json",
                        ""
                    ).replace(
                        "```",
                        ""
                    ).strip()

                    data = json.loads(clean)

                    st.markdown("## 💊 Medicine Details")

                    c1, c2 = st.columns(2)

                    with c1:

                        st.info(
                            f"💊 Medicine\n\n{data.get('medicine_name','Unknown')}"
                        )

                        st.info(
                            f"🧪 Active Ingredient\n\n{data.get('active_ingredient','Unknown')}"
                        )

                        st.info(
                            f"🏭 Manufacturer\n\n{data.get('manufacturer','Unknown')}"
                        )

                        st.info(
                            f"💉 Strength\n\n{data.get('strength','Unknown')}"
                        )

                    with c2:

                        st.info(
                            f"🩺 Uses\n\n{data.get('uses','Unknown')}"
                        )

                        st.info(
                            f"💊 Dosage\n\n{data.get('dosage','Unknown')}"
                        )

                        st.info(
                            f"⚠️ Side Effects\n\n{data.get('side_effects','Unknown')}"
                        )

                        st.info(
                            f"🤰 Pregnancy\n\n{data.get('pregnancy','Unknown')}"
                        )

                    st.subheader("🔄 Drug Interactions")
                    st.write(
                        data.get("drug_interactions","Unknown")
                    )

                    st.subheader("🍺 Alcohol Interaction")
                    st.write(
                        data.get("alcohol_interaction","Unknown")
                    )

                    st.subheader("📦 Storage")
                    st.write(
                        data.get("storage","Unknown")
                    )

                    st.subheader("📝 Summary")
                    st.write(
                        data.get("summary","Unknown")
                    )

                except Exception:

                    st.markdown(result)

                # ----------------------
                # PDF
                # ----------------------

                pdf = create_pdf(
                    "Medicine Scan Report",
                    result,
                    "medicine_scan_report.pdf"
                )

                with open(pdf, "rb") as
