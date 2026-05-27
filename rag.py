import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings, ChatMistralAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def load_and_index_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pdf = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(pdf)

    embeddings = MistralAIEmbeddings(
        api_key=MISTRAL_API_KEY,
        model="mistral-embed"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    return vectorstore

def get_answer(vectorstore, question):
    llm = ChatMistralAI(
        api_key=MISTRAL_API_KEY,
        model="mistral-large-latest"
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )

    result = qa_chain.invoke({"query": question})
    return result["result"]