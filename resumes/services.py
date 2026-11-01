import re


SKILLS_DATABASE = [
    "Python",
    "Java",
    "JavaScript",
    "C++",
    "Django",
    "FastAPI",
    "Flask",
    "REST API",
    "PostgreSQL",
    "MySQL",
    "MongoDB",
    "SQLite",
    "Redis",
    "SQL",
    "HTML",
    "CSS",
    "React",
    "Angular",
    "Node.js",
    "Docker",
    "Kubernetes",
    "AWS",
    "EC2",
    "S3",
    "Lambda",
    "Git",
    "GitHub",
    "Linux",
    "Machine Learning",
    "Deep Learning",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "Celery",
    "SQLAlchemy",
]


def extract_skills(resume_text):

    if not resume_text:
        return []

    found_skills = []

    text = resume_text.lower()

    for skill in SKILLS_DATABASE:

        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills