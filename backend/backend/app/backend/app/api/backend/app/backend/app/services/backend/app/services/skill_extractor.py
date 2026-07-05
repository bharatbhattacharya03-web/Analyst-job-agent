import re

COMMON_SKILLS = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "r",
    "statistics",
    "machine learning",
    "data analysis",
    "business analysis",
    "risk management",
    "communication",
    "problem solving",
    "pandas",
    "numpy",
    "mysql",
    "postgresql",
    "mongodb",
    "aws",
    "azure",
    "google cloud",
    "git",
    "github",
    "etl",
    "dashboard",
    "data visualization"
]

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in COMMON_SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found.append(skill)

    return sorted(list(set(found)))
