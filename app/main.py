import os
from fastapi import FastAPI, UploadFile, File

app = FastAPI(title="企业级RAG知识库API", version="0.1.0")#?

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"message": "RAG知识库服务已启动"}

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "rag-knowledge-base"}

@app.get("/info")
def info_get():
    return {"name": "RAG知识库", "version": "0.1.0", "status": "running"}

@app.post("/api/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": file.size,
        "message": f"文件{file.filename}上传成功！"
    }