from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ["HF_HOME"] = "./hf_models"  # Set the HF cache directory
# This automatically downloads and loads the model locally
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # Use a chat-capable model
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.7,
        "max_new_tokens": 50,
    }
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of Uttar Pradesh?")

print(response.content)