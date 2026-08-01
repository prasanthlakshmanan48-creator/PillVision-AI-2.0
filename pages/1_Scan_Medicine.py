import streamlit as st

st.set_page_config(
    page_title="Scan Medicine",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Scan Medicine")

st.write("Upload a medicine image to analyze.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded Medicine",
        use_container_width=True
    )

    if st.button("Analyze Medicine"):

        st.success("✅ Image uploaded successfully!")

        st.info("Gemini AI integration will be added in the next step.")
