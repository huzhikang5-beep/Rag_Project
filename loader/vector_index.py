from loader.document_index import DocumentIndex
from loader.document_loader import DocumentLoader
from loader.document_splitter import DocumentSplitter
from models.chroma import vectorstore


def create_vector_index(file_path:str, delete_flag:bool = False):
    # 文档加载
    document_loader =DocumentLoader(file_path=file_path)
    docs = document_loader.loader()
    # 文档切割
    document_splitter = DocumentSplitter(docs)
    chunks = document_splitter.split()
    # 文本向量化
    document_index = DocumentIndex(chunks, vectorstore=vectorstore, delete_flag=True)

    document_index.add_documents()