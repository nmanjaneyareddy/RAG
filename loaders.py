# loaders.py

from langchain_community.document_loaders import PyPDFLoader, BSHTMLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_documents():
    docs = []

    # Load PDF
    if os.path.exists("data/igidr_library_details.pdf"):
        pdf_loader = PyPDFLoader("data/examigidr_library_detailsple.pdf")
        docs += pdf_loader.load()
    else:
        print("⚠️ PDF file not found at data/igidr_library_details.pdf")

    # Load HTML using built-in parser
    if os.path.exists("data/li.html"):
        html_loader = BSHTMLLoader("data/li.html", bs_kwargs={"features": "html.parser"})
        docs += html_loader.load()
    else:
        print("⚠️ HTML file not found at data/li.html")

    if not docs:
        raise ValueError("No valid documents found in the data/ directory.")
    
    return docs

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(docs)
