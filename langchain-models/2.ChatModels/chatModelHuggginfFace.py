import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()  # loads HUGGINGFACEHUB_API_TOKEN from .env into environment
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not token:
    raise SystemExit("Set HUGGINGFACEHUB_API_TOKEN in your .env (or env) before running.")

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=token,
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India")
print(result)
