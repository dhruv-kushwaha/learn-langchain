from langchain_huggingface import ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
model_name = os.getenv("HUGGINGFACE_MODEL")

print(api_token)
print(model_name)