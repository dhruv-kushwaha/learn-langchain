from langchain_openai import AzureChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

model = AzureChatOpenAI(
    azure_deployment=deployment_name,
    api_version=api_version,
    temperature=0.7,
    max_tokens=1000,  # type: ignore
)

chat_history = [
    SystemMessage(content="You are a helpful AI assistant."),
]

while True:
    user_input =input("You: ")
    chat_history.append(HumanMessage(content=user_input)) # type: ignore
    if(user_input.lower() in ['exit', 'quit']):
        print("Exiting the chatbot. Goodbye!")
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content)) # type: ignore
    print("AI: ", result.content)

print(chat_history)