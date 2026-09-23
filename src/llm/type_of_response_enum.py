from enum import Enum

class TypeResponse(Enum):
    BASIC_RESPONSE = "Basic response"
    RESPONSE_WITH_SCHEMA = "response with schema"
    RESPONSE_WITH_TOOLS =  "response with tools"
    