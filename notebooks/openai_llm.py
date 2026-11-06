import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-5-nano",
    api_key=os.getenv("OPENAI_API_KEY")
)

response = llm.invoke("Explain me about OpenAI LLM in 3 lines.")

print(response.content)