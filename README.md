# 📄 RAG PDF Chatbot

## Project Overview

An AI-powered chatbot that allows users to upload any PDF and ask questions about its content in natural language.

The system uses **Retrieval-Augmented Generation (RAG)** — combining a vector database for document search with a large language model for answer generation.

## 🚀 Run the Project

```bash
git clone https://github.com/shawndacosta/RAG_PDF_Chatbot
cd RAG_PDF_Chatbot
pip install -r requirements.txt
```

Create a `.env` file at the root with your Mistral API key:
```
MISTRAL_API_KEY=your_api_key_here
```

Then:
```bash
streamlit run app.py
```

## 🛠️ Tech Stack

- **LLM** — Mistral AI
- **RAG Framework** — LangChain
- **Vector Database** — ChromaDB
- **PDF Parsing** — PyPDF
- **Interface** — Streamlit

## 📑 Table of Contents

1. [I. How it works 🔍](#i-how-it-works-)
2. [II. Architecture 🏗️](#ii-architecture-)
3. [III. Interface 🖥️](#iii-interface-)
4. [IV. Conclusion ✔️](#iv-conclusion-)

# I. How it Works 🔍

The RAG pipeline follows these steps:

1. **PDF Loading** — the PDF is loaded and text is extracted page by page
2. **Chunking** — the text is split into chunks of 1000 characters with 200 character overlap
3. **Embedding** — each chunk is converted into a numerical vector by Mistral
4. **Storage** — vectors are stored in ChromaDB
5. **Question** — the user's question is converted into a vector by Mistral
6. **Retrieval** — ChromaDB finds the 3 most relevant chunks
7. **Generation** — Mistral generates an answer based on the question and the retrieved chunks

# II. Architecture 🏗️

```
PDF uploaded
    ↓
Text extraction (PyPDF)
    ↓
Chunking (LangChain)
    ↓
Embedding (Mistral API)
    ↓
Storage (ChromaDB)
    ↓
User question
    ↓
Question embedding (Mistral API)
    ↓
Similarity search (ChromaDB) → 3 most relevant chunks
    ↓
Answer generation (Mistral API)
    ↓
Display (Streamlit)
```

# III. Interface 🖥️

The Streamlit interface allows users to:

- Upload any PDF file
- Ask questions in any language
- Receive answers grounded in the document content

# IV. Conclusion ✔️

This project demonstrates a complete **RAG pipeline** using state-of-the-art tools. The chatbot can answer questions about any PDF document in any language, making it applicable to a wide range of use cases : legal documents, financial reports, medical records, technical documentation, and more.

## Possible Improvements

- Support for multiple PDFs simultaneously
- Display of source chunks used to generate the answer
- Conversation history (multi-turn chat)
- Docker containerization
- Cloud deployment (AWS, Azure)
