from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)
result = embeddings.embed_query("What is the capital of France?")
print(str(result))
#  it gie us the result in the form of vector like we give that 32 dimesions so it give us in 32 vectors rightt 