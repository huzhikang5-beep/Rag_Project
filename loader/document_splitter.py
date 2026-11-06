"""
文档分割
"""
from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter


class DocumentSplitter:
    def __init__(self, docs: List[Document]):
        self.docs = docs

    # seperator：分隔符，类型是列表，按照列表中元素的顺序进行分割
    # chunk_size：文本块的最大长度,一般按token计算
    # chunk_overlap：滑动窗口：相邻文本块之间重叠的字符/token数
    # length_function：文本长度计算函数，计算的是字符数（一般来说一个英文字符=四个token）,
    # 作用：防止完整句子被切割成两段，保证相邻句子之间有重叠，从而保证能获取到连贯的上下文信息
    # 在切割时，先按照seperator切割，如果切割后的文本块大于chunk_size,再按照chunk_size切割

    # 按标题切割的切隔器： MarkdownHeaderTextSplitter
    # headers_splitter_on = [
    #     ("#","H1"),
    #     ("##","H2"),
    #     ("##","H3"),
    # ]
    # MarkdownHeaderTextSplitter(
    #     headers_to_split_on=headers_splitter_on,
    # )
    def split(self):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size= 512,
            chunk_overlap = 50,
            separators=["\n\n", "\n","。","？"]
        )

        chunks = splitter.split_documents(self.docs)
        return chunks

