import streamlit as st
from rag_pipeline import setup_rag_pipeline
import tempfile

st.set_page_config(page_title="LLM Q&A with RAG", layout="wide")

st.title("🤖 Ask Me Anything (RAG + LLM)")

# File upload
uploaded_file = st.file_uploader("Upload your PDF document", type=["pdf"])

if uploaded_file:
    # Save the uploaded PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
        tmp_pdf.write(uploaded_file.read())
        tmp_pdf_path = tmp_pdf.name

    # Initialize the RAG pipeline with the uploaded PDF
    st.write("Processing your document...")
    qa_chain = setup_rag_pipeline(tmp_pdf_path)
    st.success("Document ready for Q&A!")

    # Question input
    question = st.text_input("Enter your question:")

    # Get answer
    if question:
        with st.spinner("Thinking..."):
            response = qa_chain.run(question)
        st.markdown("### 🧠 Answer:")
        st.write(response)
