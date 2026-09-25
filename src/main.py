from dotenv import load_dotenv
from llm.client import LLMClient
from llm.userRole import UserRole
from llm.conversationComponents import ConversationComponents
from llm.ConversationManager import ConversationManager
from llm.tools.tool_schemas import tool_schemas

load_dotenv()

def main():
    client = LLMClient()
    conversation = [
        {
            ConversationComponents.ROLE.value: UserRole.DEVELOPER.value,
           ConversationComponents.CONTENT.value:"Eres un asistente de revisión de cvs."
        }
    ]

    manager = ConversationManager(client=client, conversation=conversation)
    
    while True: 
        prompt = input("\nYou: ")

        if prompt.lower() == "exit":
            break
        
        if not prompt.strip():
            continue

        response = manager.start_conversation(prompt=prompt, tools=tool_schemas)
  
        print("\nAssistant:")
        print(response.output_text)
     

if __name__== "__main__":
    main()

