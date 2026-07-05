from app.services.job_matcher import calculate_match_score
from app.services.job_database import SAMPLE_JOBS

def rank_jobs(user_skills):
    ranked = []

    for job in SAMPLE_JOBS:
        result = calculate_match_score(user_skills, job["skills"])

        ranked.append({
            "title": job["title"],
            "company": job["company"],
            "location": job["location"],
            "match_score": result["score"],
            "matched_skills": result["matched_skills"],
            "missing_skills": result["missing_skills"]
        })

    ranked.sort(key=lambda x: x["match_score"], reverse=True)

    return ranked
