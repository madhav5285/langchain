from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='gemini-embedding-2',output_dimensionality=32)
#giving document for embedding
documents = [
    "Delhi is in india",
    "Kolkata is also",
    "japan is in up"
]

result = embedding.embed_documents(documents)
print(result)

