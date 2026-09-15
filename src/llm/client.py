from openai import OpenAI

class LLMClient: 
    def __init__(self):
        self.client = OpenAI()

    def generate(self, conversation: list) -> str:

        response = self.client.responses.create(
            model="gpt-5.6-luna",
            input= conversation
        )

        return response.output_text
