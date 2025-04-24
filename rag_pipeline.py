import os
from dotenv import load_dotenv
import fitz  # PyMuPDF
import google.generativeai as genai
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

# Configure Google Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

# Load and split documents
def load_documents(path):
    text = extract_text_from_pdf(path)
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(text)
    docs = [Document(page_content=chunk) for chunk in chunks]
    return docs

# Create vector store
def create_vector_store(docs):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(docs, embeddings)
    return vector_store

# Create Gemini-powered QA chain
def create_qa_chain(vector_store):
    llm = GoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=API_KEY)  # Use LangChain's wrapper for Gemini
    
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )
    return qa

# Complete setup
def setup_rag_pipeline(file_path):
    docs = load_documents(file_path)
    vector_store = create_vector_store(docs)
    qa_chain = create_qa_chain(vector_store)
    return qa_chain