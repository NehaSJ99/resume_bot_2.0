# config/settings.py

import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from prompts.route_prompt import question_router
from prompts.retrieval_grader_prompt import retrieval_grader
from prompts.hallucination_grader_prompt import hallucination_grader
from prompts.answer_grader_prompt import answer_grader
from prompts.question_rewrite_prompt import question_rewriter
from prompts.rag_prompt import rag_chain

from tools.web_search import web_search_tool
from utils.loader import build_vectorstore_from_pdf

# Load environment variables
load_dotenv()

# === Shared LLM & Embeddings ===
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embeddings = OpenAIEmbeddings()

pdf_path = os.path.join("data", "Resume.pdf")
retriever = build_vectorstore_from_pdf(pdf_path).as_retriever()
