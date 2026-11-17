
SKILL_KEYWORDS = [
    "Python",
    "Django",
    "Django REST Framework",
    "FastAPI",
    "Flask",
    "PostgreSQL",
    "MySQL",
    "MongoDB",
    "SQL",
    "SQLAlchemy",
    "REST API",
    "Docker",
    "AWS",
    "Git",
    "GitHub",
    "JWT",
    "HTML",
    "CSS",
    "JavaScript",
    "Linux",
    "OOP",
    "Redis",
    "Celery",
    "Kubernetes",
    "Java",
]


def extract_skills(text):
    if not text:
        return []

    text_lower = text.lower()

    found_skills = []

    for skill in SKILL_KEYWORDS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills
