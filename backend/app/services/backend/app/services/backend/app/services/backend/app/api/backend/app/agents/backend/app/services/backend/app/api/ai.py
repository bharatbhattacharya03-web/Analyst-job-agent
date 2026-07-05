from fastapi import APIRouter
from app.services.job_search import search_jobs
from app.services.ranking import rank_jobs

router = APIRouter()

@router.get("/ai-search")
def ai_search():
    skills = ["python", "sql", "excel"]

    jobs = search_jobs()

    ranked = rank_jobs(skills)

    return {
        "jobs": jobs,
        "recommendations": ranked
    }
