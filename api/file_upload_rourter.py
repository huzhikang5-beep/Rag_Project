'''
文件上传，创建向量数据库索引
'''

import os

from fastapi import APIRouter,UploadFile,File
from openai import APIResponse

from loader.vector_index import create_vector_index

file_upload_router = APIRouter(prefix="/admin")

@file_upload_router.post("/upload")
async def upload_file(file:UploadFile = File(...)):
    try:
        file_name = file.filename
        # 创建保存上传文件的目录
        dir_path = "tmp_upload"
        # makedirs: 创建目录
        # 参数：exist_ok:若果目录不存在则创建，如果存在则跳过
        os.makedirs(dir_path,exist_ok=True)

        # 读取file中的内容
        content = await file.read()

        # 把读取的内容保存到临时目录下的文件中
        file_path = os.path.join(dir_path,file_name)

        with open(file_path,'wb') as f:
            f.write(content)

        create_vector_index(file_path=file_path)
    except Exception as e:
        raise Exception("上传文件，创建向量索引失败：", e)
