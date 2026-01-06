from typing import TypedDict
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

model = AzureChatOpenAI(
    azure_deployment=deployment_name,
    api_version=api_version,
)

class Review(TypedDict):
    summary : str
    sentiment : str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("The phone feels premium in hand and has a bright, smooth display that’s great for daily use. Performance is fast for regular apps and multitasking, though heavy gaming can warm it up slightly. The camera takes sharp photos in good light but struggles a bit at night. Battery life easily lasts a full day with fast charging as a bonus.")

print(result)