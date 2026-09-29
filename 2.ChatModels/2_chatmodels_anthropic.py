from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()
#chatmodels inherit from base chatmmodel
llm = ChatAnthropic(model='claude-opus-5-5',temperature=0)

result = llm.invoke("what is capital of India")
#content just to see content
print(result.content) 