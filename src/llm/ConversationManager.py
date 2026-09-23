from llm.userRole import UserRole
from llm.conversationComponents import ConversationComponents
from llm.client import LLMClient
from llm.resumeSchema import resume_schema
from llm.tools import get_seniority
import json



class ConversationManager: 
    def __init__(self, client: LLMClient, conversation: list):
        self.client = client
        self.conversation =conversation
 

    def start_conversation(
        self,
        prompt: str,
        tools: list
    ):

        self.conversation.append({
            ConversationComponents.ROLE.value: UserRole.USER.value,
            ConversationComponents.CONTENT.value: prompt
        })

        response = self.client.generate_with_tools(
            conversation=self.conversation,
            tools=tools
        )

        for item in response.output:

            if item.type == "function_call":

                arguments = json.loads(item.arguments)

                years = arguments["years_of_experience"]

                result = get_seniority(
                    years_of_experience=years
                )

                tool_output = {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": result
                }

                next_input = [
                    *self.conversation,
                    *response.output,
                    tool_output
                ]

                final_response = self.client.generate_with_tools(
                    conversation=next_input,
                    tools=tools
                )

                return final_response

        return response
