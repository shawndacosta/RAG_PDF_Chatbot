import streamlit as st
import tempfile
import os
from rag import load_and_index_pdf, get_answer

st.set_page_config(page_title="PDF Chatbot", page_icon="📄", layout="centered")

st.title("📄 PDF Chatbot")
st.markdown("Upload a PDF and ask questions about its content.")

st.divider()

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with st.spinner("Reading and indexing PDF..."):
        vectorstore = load_and_index_pdf(tmp_path)
        os.unlink(tmp_path)

    st.success("PDF indexed successfully ✅")
    st.divider()

    question = st.text_input("Ask a question about the PDF")

    if question:
        with st.spinner("Generating answer..."):
            answer = get_answer(vectorstore, question)
        st.markdown("### Answer")
        st.write(answer)