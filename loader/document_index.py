"""
向量化，创建向量数据库
"""
from typing import List

from langchain_core.documents import Document

class DocumentIndex:
    def __init__(self,chunks:list[Document],vectorstore, delete_flag: bool = False):
        self.chunks = chunks
        self.vectorstore = vectorstore
        self.delete_flag = delete_flag

    # 删除向量数据库中的数据
    def delete_vector(self):
        '''
        在向量数据库中，
        '''
        ids = self.vectorstore.get()['ids']
        if len(ids)>0:
            self.vectorstore.delete(ids)
    # 添加数据到向量数据库
    def add_documents(self):
        if self.delete_flag:
            self.delete_vector()

        self.vectorstore.add_documents(self.chunks)