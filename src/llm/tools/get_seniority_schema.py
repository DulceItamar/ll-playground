from tool_schema_model import ParametersSchema, ToolSchema, ParametersSchema, PropertySchema

get_seniority_schema = ToolSchema(
    name="get_seniority",
    description="Obtiene el seniority de acuerdo a los años de experiencia.",
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

