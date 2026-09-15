from llm.userRole import UserRole
from llm.conversationComponents import ConversationComponents
from llm.client import LLMClient

class ConversationManager: 
    def __init__(self, client: LLMClient, conversation: list):
        self.client = client
        self.conversation =conversation
 

    def start_conversation(self, prompt: str) -> str:

        self.conversation.append({ 
                ConversationComponents.ROLE.value: UserRole.USER.value,
                ConversationComponents.CONTENT.value: prompt
            })

        response = self.client.generate(conversation=self.conversation)

        self.conversation.append({
            ConversationComponents.ROLE.value: UserRole.ASSISTANT.value,
            ConversationComponents.CONTENT.value: response
        })

        return response
    

        
            
