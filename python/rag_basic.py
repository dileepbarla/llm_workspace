import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import chroma
from langchain_openai import OpenAIEmbeddings
import chromadb
new_client = chromadb.EphemeralClient()