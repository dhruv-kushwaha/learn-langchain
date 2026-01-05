from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import  load_prompt

load_dotenv()

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

model = AzureChatOpenAI(
    azure_deployment=deployment_name,
    api_version=api_version,
    temperature=0.7,
    max_tokens=1000,  # type: ignore
)

st.header("Research Tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

#PromptTemplate allows you to generate the prompt from the template and save it in a json file enhancing the reusability of the file.

template = load_prompt("template.json")

prompt = template.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
})


if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)