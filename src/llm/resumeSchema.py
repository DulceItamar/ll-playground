
resume_schema= {
    "type": "object",
    "properties": {
        "role": {
            "type": "string"
        }, 
        "years_of_experience": {
            "type": "integer"
        },
        "skills": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "required": [
        "role", 
        "years_of_experience",
        "skills"
    ],
    "additionalProperties": False
}