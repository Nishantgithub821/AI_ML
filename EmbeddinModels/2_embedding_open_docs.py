# how we run multiple embeding vevctors of the more files so
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)
documents=[
    "Delhi is the capital of India?",
    "Kolkata is the capital of West Bengal?",
    "Paris is the capital of France?"
]# we want to do three processing at once 

result = embeddings.embed_documents(documents)
print(str(result)) # now this  will convert into the numbers right 

# the work of this file is only to convert the text into numbers 
