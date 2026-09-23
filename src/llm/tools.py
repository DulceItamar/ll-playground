# Aqui definimos el contrato de la herramienta que el modelo puede usar


def get_seniority(years_of_experience: int) -> str:

    if years_of_experience < 2:
        return "Junior"

    if years_of_experience < 5:
        return "Mid-level"

    return "Senior"