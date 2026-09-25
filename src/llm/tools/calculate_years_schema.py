from  tool_schema_model import ToolSchema, ParametersSchema, PropertySchema

calculate_years_schema = ToolSchema(
    name="calculate_years_until_senior",
    description="Calcula cúantos años faltan para alcanzar el nivel Senior.",
    parameters=ParametersSchema(
        properties={
            "years_of_experience": PropertySchema(
                type="integer",
                description="Años de experiencia laboral."
            )
        },
        required=["years_of_experience"],
        additionalProperties=False
    )
)