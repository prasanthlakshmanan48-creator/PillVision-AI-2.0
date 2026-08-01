import streamlit as st
from PIL import Image
from utils.gemini import analyze_medicine_image

st.set_page_config(
    page_title="Scan Medicine",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Scan Medicine")

uploaded_file = st.file_uploader(
    "Upload Medicine Image",
    type=["jpg","jpeg","png"]
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

                st.success("Analysis Completed")

                st.markdown(result)

            except Exception as e:

                st.error("Analysis Failed")

                st.exception(e)
