from app.services.ranking import rank_jobs

def get_recommendations(user_skills):
    jobs = rank_jobs(user_skills)

    return {
        "total_jobs": len(jobs),
        "top_matches": jobs[:10]
    }
