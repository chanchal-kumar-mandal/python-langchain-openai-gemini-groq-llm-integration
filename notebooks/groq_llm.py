import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="qwen/qwen3.8-27b",
    api_key=os.getenv("GROQ_API_KEY")
)

response = llm.invoke("Explain me about Groq LLM in 5 lines.")

print(response.content)