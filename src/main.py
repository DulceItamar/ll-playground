from dotenv import load_dotenv
from llm.client import LLMClient

load_dotenv()

def main():
    client = LLMClient()
    prompt = input("You: ")
    response = client.generate(prompt)

    print("\nAssistent:")
    print(response)

if __name__== "__main__":
    main()