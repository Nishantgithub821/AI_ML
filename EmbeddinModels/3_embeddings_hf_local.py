from langchain_huggingface import HuggingFaceEndpoint
embeddings = HuggingFaceEndpoint(model_name="sentence-transformers/all-MiniLM-L6-v2")
# niw 
text = "Delhi is the capital of India "
vector = embeddings.embed_query(text)
print(str(vector))