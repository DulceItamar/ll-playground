from llm.userRole import UserRole
from llm.conversationComponents import ConversationComponents
from llm.client import LLMClient
from llm.tools.tool_registry import tool_registry
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
        
        max_iterations = 10
        iteration = 0
        
        while iteration < max_iterations: 
            function_call = None
            for item in response.output:

                if item.type == "function_call":
                    function_call = item
                    break
                
                if function_call is None:
                    return response
                
                iteration += 1
                
                # ----------------------
                # Tool Validation 
                # ----------------------
                
                tool = tool_registry[function_call.name]
                
                if tool is None:
                    raise ValueError(f"Tool '{function_call.name}' not found in the tool registry.")
                
                tool_function = tool.function
                arguments_model = tool.arguments_model
                
                arguments = arguments_model.model_validate_json(function_call.arguments)
                
                # ----------------------
                # Tool execution
                # ----------------------
                
                result = tool_function(**arguments.model_dump())
                
                tool_output = {
                    "type": "function_call_output",
                    "call_id": function_call.call_id,
                    "output": result
                }

                next_input = [
                    *self.conversation,
                    *response.output,
                    tool_output
                ]

                response = self.client.generate_with_tools(
                    conversation=next_input,
                    tools=tools
                )

        raise RuntimeError(
            f"Agent Loop excedió el máximo de "
            f"{max_iterations} iteraciones."
)

