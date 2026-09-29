from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='gemini-embedding-2')

documents = [
    "The software engineer spent hours debugging the database connection error.",

    "Freshly baked sourdough bread fills the kitchen with a warm, comforting aroma.",

    "Consistent daily aerobic exercise significantly strengthens the cardiovascular system.",

    "The central bank announced a sharp increase in interest rates to curb inflation.",
    "Golden retriever puppies love running across the grass chasing tennis balls."
]

query="What help by aerobic exercise"
doc_embed=embedding.embed_documents(documents)
query_embed= embedding.embed_query(query)

scores=cosine_similarity([query_embed],doc_embed)[0]
#enumerate->to connect id with each score
index, score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(documents[index])