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

response = model.invoke("Explain the theory of relativity in simple terms.")

print(response.content)