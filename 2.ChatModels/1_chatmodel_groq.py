from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
#chatmodels inherit from base chatmmodel
llm = ChatGroq(model='openai/gpt-oss-120b',temperature=0)

result = llm.invoke("what is capital of India")
#content just to see content
print(result.content) 