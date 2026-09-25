from typing import Callable
from pydantic import  BaseModel

class PropertySchema(BaseModel):
    type: str
    description: str

class ParametersSchema(BaseModel):
    type: str = "object"
    properties: dict[str, PropertySchema]
    required: list[str]
    additionalProperties: bool = False

class ToolSchema(BaseModel):
    type: str = "function"
    name: str
    description: str
    parameters: ParametersSchema
    strict: bool = True

class ToolDefinition(BaseModel):
    function: Callable
    arguments_model: type[BaseModel]