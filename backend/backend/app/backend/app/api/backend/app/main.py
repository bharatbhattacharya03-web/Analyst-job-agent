from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.config import MODEL

app = FastAPI(
    title="Analyst Job Agent",
    version="1.0.0"
)

app.include_router(upload_router)

@app.get("/")
def home():
    return {
        "message": "🚀 Analyst Job Agent Running",
        "model": MODEL
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
