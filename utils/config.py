import os
from dotenv import load_dotenv
from ollama import embeddings

# 加载环境变量
load_dotenv()

qwen_model_name = os.getenv("QWEN_MODEL_NAME")
qwen_api_key = os.getenv("QWEN_API_KEY")
qwen_base_url = os.getenv("QWEN_BASE_URL")

embeddings_model_name = os.getenv("EMBEDDINGS_MODEL_NAME")