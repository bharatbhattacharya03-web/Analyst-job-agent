import requests

SEARCH_TERMS = [
    "Data Analyst",
    "Business Analyst",
    "Risk Analyst",
    "BI Analyst",
    "Product Analyst",
    "Analytics Consultant"
]

LOCATIONS = [
    "India",
    "Remote"
]

def search_jobs():
    jobs = []

    for role in SEARCH_TERMS:
        for location in LOCATIONS:
            jobs.append({
                "title": role,
                "company": "Sample Company",
                "location": location,
                "source": "Demo",
                "url": "https://example.com/job",
                "match_score": 0
            })

    return jobs
