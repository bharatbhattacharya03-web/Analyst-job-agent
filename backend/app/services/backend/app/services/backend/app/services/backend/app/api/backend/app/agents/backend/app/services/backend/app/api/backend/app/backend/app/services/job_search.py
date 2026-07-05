import requests

API_URL = "https://arbeitnow.com/api/job-board-api"

def search_jobs():
    response = requests.get(API_URL, timeout=10)

    if response.status_code != 200:
        return []

    data = response.json().get("data", [])

    jobs = []

    keywords = [
        "data analyst",
        "business analyst",
        "risk analyst",
        "bi analyst",
        "analytics"
    ]

    for job in data:
        title = job.get("title", "").lower()

        if any(k in title for k in keywords):
            jobs.append({
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("location"),
                "url": job.get("url"),
                "skills": []
            })

    return jobs
