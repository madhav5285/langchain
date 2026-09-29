from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="ukisai/Swift-1.5-Qwen3.8-27B-GSQ-RCO-GGUF",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

result=model.invoke("What is ccapital of INDIA")
print(result.content)