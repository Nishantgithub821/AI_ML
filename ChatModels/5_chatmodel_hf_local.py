#I dont  run this code because if i run this and i t works so it donwalod in background the api in my local machine and i dont want to donwalod any in my local machine 
# Thsi is our downlaod method of apny open source in our machine right 
"""
from langchain_huggingface import ChathuggingFace, HuggingFaceEndpoint, HuggingFacePipeline

import os 
os.environ["HF_HOME"] = "D:/huggingface_cache"  # 
llm = HuggingFacePipeline.from_model_id(
    model_id="google/flan-t5-xxl",
    task="text-generation",
    pipeline_kwargs=dict(
      temperature=0.7, 
        max_new_tokens=100
        )
    
)
model = ChathuggingFace(llm=llm) 
result=model("What is the capital of France?")
print(result.content)
# now one main things here that is let supppose you downlaod this one on your local macine but before that you want than i want to keep this in my d folder d drice because my 
# c drive is full so then we import os right and after os code is mentioned upper in code do that to use it okey 

# we dont run this because this is locally machine workable model and for that we need the good gpu and ram formate right 
"""
# Now our next step that we understand is come that is embedding part so go on embedding folder and there are 2 fiels which i build so check it 
# open first one you understand what is going on right 
from transformers import AutoTokenizer, AutoModel
import torch

# --------- Step 1: Choose model ----------
model_name = "unsloth/all-MiniLM-L6-v2"

# --------- Step 2: Load tokenizer & model ----------
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# --------- Step 3: Input text ----------
input_text = "What is the capital of India?"
inputs = tokenizer(input_text, return_tensors="pt")

# --------- Step 4: Generate embeddings ----------
with torch.no_grad():
    embeddings = model(**inputs).last_hidden_state.mean(dim=1)

# --------- Step 5: Print result ----------
print("Embedding vector:", embeddings)
print("Vector shape:", embeddings.shape)
