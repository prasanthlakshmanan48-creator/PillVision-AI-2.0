import streamlit as st

from utils.gemini import health_chat
from utils.history import add_history
from utils.pdf import create_pdf

st.set_page_config(
    page_title="AI Health Chat",
    page_icon="💬",
    layout="wide"
)

st.title("💬 PillVision AI Health Assistant")

st.write(
    "Ask medicine and healthcare-related questions."
)

st.markdown("---")

# ======================================
# Session Chat History
# ======================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ======================================
# User Input
# ======================================

question = st.chat_input(
    "Ask your healthcare question..."
)

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                answer = health_chat(question)

                # Save to SQLite history
                add_history(
                    "AI Chat",
                    question,
                    answer
                )

                st.markdown(answer)

                # Store response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

                st.markdown("---")

                # Create PDF
                pdf = create_pdf(
                    "AI Health Chat Report",
                    answer,
                    "ai_chat_report.pdf"
                )

                with open(pdf, "rb") as file:

                    st.download_button(
                        "📄 Download Last Response",
                        data=file,
                        file_name="AI_Health_Chat_Report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            except Exception as e:

                st.error("Unable to generate response.")

                st.exception(e)

# ======================================
# Sidebar
# ======================================

st.sidebar.header("⚙️ Chat Options")

if st.sidebar.button("🗑 Clear Chat"):

    st.session_state.messages = []

    st.rerun()

st.sidebar.markdown("---")

st.sidebar.subheader("💡 Example Questions")

examples = [
    "Can I take Dolo 650 after food?",
    "Is Paracetamol safe during pregnancy?",
    "Can I take Ibuprofen with alcohol?",
    "What are the side effects of Cetirizine?",
    "What should I do if I miss a dose of antibiotics?",
    "Can diabet
