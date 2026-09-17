from dotenv import load_dotenv
from llm.client import LLMClient
from llm.userRole import UserRole
from llm.conversationComponents import ConversationComponents
from llm.ConversationManager import ConversationManager
from llm.Seniority import define_Seniority
import json

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

        if prompt.lower() == "show_conversation":
            print("\nConversación:")
            print(conversation)

        response = manager.start_conversation(prompt=prompt)
        data = json.loads(response)

        seniority = define_Seniority(years=data["years_of_experience"])
        print("\nAssistant:")
        print(seniority)

if __name__== "__main__":
    main()

