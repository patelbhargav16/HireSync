def normalize_skill(skill):
    """
    Normalize skill names for case-insensitive comparison.
    """
    return str(skill).strip().lower()


def calculate_job_match(candidate_skills, required_skills):
    """
    Calculate candidate's skill match percentage for a job.
    """

    candidate_skills_set = {
        normalize_skill(skill)
        for skill in candidate_skills
        if skill
    }

    required_skills_list = [
        skill.strip()
        for skill in required_skills
        if isinstance(skill, str) and skill.strip()
    ]

    matched_skills = []
    missing_skills = []

    for skill in required_skills_list:

        if normalize_skill(skill) in candidate_skills_set:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    total_required = len(required_skills_list)

    if total_required == 0:
        match_percentage = 0
    else:
        match_percentage = round(
            (len(matched_skills) / total_required) * 100
        )

    return {
        "match_percentage": match_percentage,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "total_required_skills": total_required,
    }