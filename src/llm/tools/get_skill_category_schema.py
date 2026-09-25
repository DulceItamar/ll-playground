from tool_schema_model import ToolSchema, ParametersSchema, PropertySchema

get_skill_category_schema = ToolSchema(
    name="get_skill_category",
    description="Obtiene la categoría de una habilidad.",
    parameters=ParametersSchema(
        properties={
            "skill": PropertySchema(
                type="string",
                description="Habilidad técnica."
            )
        },
        required=["skill"],
        additionalProperties=False
    )
)  