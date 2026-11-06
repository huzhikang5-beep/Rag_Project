from pydantic import BaseModel
from typing import Optional,Any

# 创建API接口的响应体
@
class ApiResponse(BaseModel):
    code : int
    msg: str
    data: Optional[Any]