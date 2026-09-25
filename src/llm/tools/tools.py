# Aqui definimos el contrato de la herramienta que el modelo puede usar


def get_seniority(years_of_experience: int) -> str:

    if years_of_experience < 2:
        return "Junior"

    if years_of_experience < 5:
        return "Mid-level"

    return "Senior"


def calculate_years_until_senior(years_of_experience: int) -> int: 
    return max(0,5 - years_of_experience)


def get_skill_category(skill: str) -> str:
    skill_categories = {
        "swift": "Mobile Development",
        "swiftui": "Mobile Development",
        "uikit": "Mobile Development",
        "kotlin": "Mobile Development",
        "java": "Backend Development",
        "spring": "Backend Development",
        "python": "Backend / AI",
        "tensorflow": "AI / Machine Learning",
        "pytorch": "AI / Machine Learning",
        "openai api": "LLM Engineering",
        "rag": "LLM Engineering",
        "docker": "DevOps",
        "kubernetes": "DevOps",
        "figma": "Design"
    }
    
    return skill_categories.get(skill.lower(), "Other")


def calculate_resume_score(years_of_experience: int,
    skills_count: int,
    has_projects: bool) -> int:
    score = 0 
    score += min(years_of_experience * 10, 40)
    score += min(skills_count * 5, 30)
    
    if has_projects: 
        score += 30

    return min(score,100)
    