from fastapi import APIRouter
from app.services.ranking import rank_jobs

router = APIRouter()

@router.get("/recommend")
def recommend():
    sample_user_skills = [
        "python",
        "sql",
        "excel"
    ]

    jobs = rank_jobs(sample_user_skills)

    return {
        "recommended_jobs": jobs
    }
