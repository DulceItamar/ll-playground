from openai import OpenAI

class LLMClient: 
    def __init__(self):
        self.client = OpenAI()

    def generate(self, conversation: list, schema: dict) -> str:

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
