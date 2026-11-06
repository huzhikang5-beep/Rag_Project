"""
创建chroma 数据库
"""
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from until.config import embeddings_model_name

embeddings = OllamaEmbeddings(
    model=embeddings_model_name
)
vectorstore = Chroma(
    host="localhost",
    port=8081,
    embedding_function=embeddings,
    collection_name="default",
    collection_metadata={"hnsw:space":"cosine"}
)