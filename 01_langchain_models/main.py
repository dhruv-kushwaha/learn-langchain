from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # Use a chat-capable model
    task="text-generation"
) # type: ignore

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of France?")

print(response.content)