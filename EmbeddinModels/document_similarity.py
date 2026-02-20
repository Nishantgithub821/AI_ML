# now we make a simpler projects right not actually project we do a question so that our understanding on the vector thing is clear from langchain.embeddings import HuggingFaceEmbeddings
# so the question is simple like We turn all sentences into numbers (vectors) using the embedding model.
#Then we compare the question’s numbers with all sentence numbers and pick the one that is most similar (highest cosine similarity) as the answer.

#  run the scirpt by the help of this comand python EmbeddinModels/document_similarity.py

# Simple document similarity using local embedding model

from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Create embedding model (local)
embedding = HuggingFaceEmbeddings(
    model_name="unsloth/all-MiniLM-L6-v2"
) 

# Documents
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

# Query
query = "Tell me about  Jasprit Bumrah "

# Convert text to vectors
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# Calculate cosine similarity
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Print similarity scores
print(list(enumerate(scores)))

# Print most similar document
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]
print(query)
print(documents[index])
print(f"Similarity Score: {score}")
