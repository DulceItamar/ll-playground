tool_schema = {
    "type": "function",
    "name":  "get_seniority",
    "description": "Obtiene el seniority de acuerdo a los años de experiencia.",
    "parameters": {
        "type": "object", 
        "properties": {
            "years_of_experience": {
                "type": "integer",
                "description": "Años de experiencia laboral.",
            }
        },
        "required": ["years_of_experience"], 
        "additionalProperties": False,
    },
    "strict": True
}