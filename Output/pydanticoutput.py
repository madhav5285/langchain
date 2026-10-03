from typing import TypedDict, Annotated, Optional
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel, Field

#Annotated ->to give some,extraa rule
load_dotenv()
model = ChatGroq(model = 'openai/gpt-oss-120b')
class Review(BaseModel):
    summary: list[str] = Field(description="give sort description")
    sentiment: Optional[str]=Field(description="give negative and positive")

structured_model = model.with_structured_output(Review)
result= structured_model.invoke("""This mobile phone has a stylish and modern design.
The display is bright, sharp, and comfortable for watching videos.
The performance is smooth for everyday tasks and multitasking.
Apps open quickly and work without much lag.
The camera takes clear and detailed photos in good lighting.
The battery lasts for a full day with normal usage.
Charging is reasonably fast and convenient.
The sound quality is clear for calls, music, and videos.
The phone offers good features for its price range.
Overall, it is a reliable and value-for-money smartphone for daily use.""")


#new_person : Person = {'name':'nithis','age':35}
print(result.sentiment)