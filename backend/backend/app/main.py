from fastapi import FastAPI
from app.config import MODEL

app = FastAPI(
    title="Analyst Job Agent",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "🚀 Analyst Job Agent is Running",
        "model": MODEL
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/jobs")
def jobs():
    return {
        "jobs": [],
        "message": "Job search agent coming next."
    }
