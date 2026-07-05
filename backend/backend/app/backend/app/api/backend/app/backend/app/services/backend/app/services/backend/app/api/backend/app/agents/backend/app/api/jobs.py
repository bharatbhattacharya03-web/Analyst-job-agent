from fastapi import APIRouter
from app.agents.job_agent import search_jobs

router = APIRouter()

@router.get("/jobs")
def get_jobs():
    jobs = search_jobs()

    return {
        "count": len(jobs),
        "jobs": jobs
    }
