from tool_schema_model import ToolSchema, ParametersSchema, PropertySchema

calculate_resume_score_schema = ToolSchema(
    name="calculate_resume_score",
    description="Calcula la puntuación de un currículum en base a la experiencia laboral y el nivel de seniority.",
    parameters=ParametersSchema(
        properties={
            "years_of_experience": PropertySchema(
                type="integer",
                description="Años de experiencia laboral."
            ),
            "skills_count": PropertySchema(
                type="integer",
                description="Número de habilidades técnicas."
            ),
            "has_projects": PropertySchema(
                type="boolean",
                description="Indica si el candidato tiene proyectos relevantes."
            )
        },
        required=["years_of_experience", "skills_count", "has_projects"],
        additionalProperties=False
    )
)