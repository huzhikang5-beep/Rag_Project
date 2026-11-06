from fastapi import FastAPI

from api.file_upload_rourter import file_upload_router

app = FastAPI()
app.include_router(file_upload_router, prefix="/api")

