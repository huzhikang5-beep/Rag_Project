"""
文档加载
"""
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_mineru import MinerULoader
from utils import setup_logger

logger = setup_logger(__name__)

class DocumentLoader:
    def __init__(self,file_path):
        self.file_path = file_path

    # 文档加载
    def markdown_loader(self):
        my_loader = UnstructuredMarkdownLoader(file_path = self.file_path)
        docs = my_loader.load()

        return docs
    # Mineru加载器：可以加载pdf、word等
    def mineru_loader(self):
        mu_loader = MinerULoader(source=self.file_path)
        docs = mu_loader.load()
        return docs

    # 定义通用加载器
    def loader(self):
        """
        集成两个加载器的功能，但只需要调用一个
        :return:
        """
        # 提取文件的后缀
        suffix = self.file_path.split('.')[-1]
        if suffix == 'md':
            return self.markdown_loader()
        elif suffix in ["pdf", "docs", "docx"]:
            return self.mineru_loader()
        else:
            raise Exception("不支持该文件格式")