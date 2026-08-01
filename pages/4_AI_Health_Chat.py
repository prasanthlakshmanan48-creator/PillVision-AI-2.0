import streamlit as st

from utils.gemini import health_chat
from utils.history import add_history
from utils.pdf import create_pdf

st.set_page_config(
    page_title="AI Health Chat",
    page_icon="💬",
    layout="wide"
)

st.title("💬 AI Health Chat")

st.write("Ask medicine or healthcare-related questions.")

# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
question = st.chat_input("Type your question here...")

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

    # AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                answer = health_chat(question)

                # Save to History
                add_history(
                    "AI Chat",
                    question,
                    answer
                )

                st.markdown(answer)

                # Store assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

                # Create PDF
                pdf = create_pdf(
                    "AI Chat Report",
                    answer,
                    "chat_report.pdf"
                )

                # Download PDF
                with open(pdf, "rb") as file:

                    st.download_button(
                        "📄 Download Chat PDF",
                        data=file,
                        file_name="AI_Chat_Report.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:

                st.error("Unable to get response.")

                st.exception(e)

# Sidebar
st.sidebar.header("Options")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.sidebar.markdown("---")

st.sidebar.info("""
### Example Questions

• Can I take Dolo 650 after food?

• Is Paracetamol safe during pregnancy?

• Can I take Ibuprofen with alcohol?

• What are the side effects of Cetirizine?
""")
