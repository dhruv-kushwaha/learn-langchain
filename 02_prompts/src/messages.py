from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

model = AzureChatOpenAI(
    azure_deployment=deployment_name,
    api_version=api_version,
    temperature=0.7,
    max_tokens=100,  # type: ignore
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about Langchain"),
]

result = model.invoke(messages)

messages.append(AIMessage(result.content))

print("---- MESSAGES ----")
print(messages)