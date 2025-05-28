# utils/loaders.py

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def load_pdf_as_documents(file_path: str, chunk_size: int = 1000, chunk_overlap: int = 100):
    """
    Load a PDF and split it into document chunks.
    """
    loader = PyPDFLoader(file_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(pages)

def build_vectorstore_from_pdf(file_path: str):
    """
    Load, split, and embed PDF content into a FAISS vectorstore.
    """
    chunks = load_pdf_as_documents(file_path)
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(chunks, embeddings)
