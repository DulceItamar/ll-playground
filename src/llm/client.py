from openai import OpenAI

class LLMClient: 
    def __init__(self):
        self.client = OpenAI()
        
    
    def generate_basic_response(self, conversation: list) -> str:

        response = self.client.responses.create(
            model="gpt-5.6-luna",
            input= conversation, 
        )

        return response.output_text

    def generate_with_schema(self, conversation: list, schema: dict) -> str:

        response = self.client.responses.create(
            model="gpt-5.6-luna",
            input= conversation, 
            text= {
                "format": {
                "type": "json_schema",
                "name": "resume_analysis",
                "schema": schema,
                "strict": True
                }
            }
        )

        return response.output_text
    
    # Ahora necesitamos inspeccionar qué decidió hacer el modelo
    def generate_with_tools(self, conversation: list, tools: list):
        response = self.client.responses.create(
            model = "gpt-5.6-luna",
            input=conversation,
            tools=tools
        )
        return response
    
    #
    def generate_tool_result(
        self, 
        tool_output: dict
    ): 
        response = self.client.responses.create(
            model="gpt-5.6-luna",
            input=list(tool_output)
        )
        return response