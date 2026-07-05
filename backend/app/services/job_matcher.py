def calculate_match_score(user_skills, job_skills):
    user = set(skill.lower() for skill in user_skills)
    job = set(skill.lower() for skill in job_skills)

    if not job:
        return 0

    matched = user.intersection(job)
    score = int((len(matched) / len(job)) * 100)

    return {
        "score": score,
        "matched_skills": list(matched),
        "missing_skills": list(job - user)
    }
