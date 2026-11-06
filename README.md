# RAG Server

基于 **LangChain + Chroma + 通义千问** 的检索增强生成（RAG）服务，负责文档加载、切分、向量化与向量库管理。

## 技术栈

| 组件 | 用途 |
|---|---|
| LangChain | 文档加载 / 切分 / 向量库编排 |
| Chroma | 向量数据库（HTTP 模式，默认 `localhost:8081`） |
| Ollama Embeddings | 本地向量化模型（默认 `nomic-embed-text`） |
| MinerU | PDF / Word 等高精度文档解析 |
| 通义千问 (Qwen) | 大语言模型（DashScope 兼容接口） |

## 处理流程

```
文档 → DocumentLoader（加载）
     → DocumentSplitter（切分，chunk_size=512 / overlap=50）
     → DocumentIndex（向量化写入 Chroma）
```

## 目录结构

```
rag_server/
├── api/
│   └── file_upload.py      # 文件上传接口（开发中）
├── loader/
│   ├── document_loader.py   # 文档加载：Markdown / PDF / Word
│   ├── document_splitter.py # 递归字符切分
│   ├── document_index.py    # 向量写入与清空
│   └── vector_index.py      # 加载→切分→入库 完整链路
├── models/
│   └── chroma.py            # Chroma 连接与 embeddings 实例
├── until/
│   └── config.py            # 环境变量读取
├── .env.example
└── .gitignore
```

## 环境要求

- Python **3.12**
- 已启动的 Chroma 服务：`chroma run --host localhost --port 8081`
- 已启动的 Ollama，并拉取嵌入模型：`ollama pull nomic-embed-text`

## 安装

```bash
conda create -n rag_env python=3.12 -y
conda activate rag_env

pip install -r requirements.txt
```

若暂无 `requirements.txt`，可先手动安装：

```bash
pip install python-dotenv langchain-core langchain-community langchain-text-splitters \
            langchain-chroma langchain-ollama fastapi uvicorn
pip install langchain-mineru ollama
```

## 配置

复制模板并填入真实密钥（`.env` 已被 `.gitignore` 排除，不会提交）：

```bash
cp .env .env
```

| 变量 | 说明 |
|---|---|
| `QWEN_MODEL_NAME` | 通义千问模型名，如 `qwen-plus` |
| `QWEN_API_KEY` | DashScope API Key |
| `QWEN_BASE_URL` | 兼容接口地址 |
| `EMBEDDINGS_MODEL_NAME` | Ollama 嵌入模型名 |

## 使用

```python
from loader.vector_index import create_vector_index

# 建立索引（delete_flag=True 会先清空向量库）
create_vector_index("data/demo.md", delete_flag=True)
```

## 已知问题 / TODO

- [ ] `api/file_upload.py` 尚未完成（`from fastapi import` 语句残缺，当前无法导入）
- [ ] 目录 `until/` 疑为 `utils/` 笔误，建议后续重命名
- [ ] `until/config.py` 中 `from ollama import embeddings` 未被使用，可移除
- [ ] 补充 `requirements.txt` 与 `main.py` 服务入口
- [ ] 增加文档元数据（来源、页码）以支持引用回溯
