# This is our open source method to generate the result 
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# The key is already in the environment
# Just pass it directly from os.environ
llm = HuggingFaceEndpoint(
    repo_id="bigscience/bloom-560m",
    task="text-generation",
    huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_KEY"],  # already loaded
    provider="auto"
)

result = llm.invoke("What is the capital of India?")
print(result)

