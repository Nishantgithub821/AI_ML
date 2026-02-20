from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  # import the static messages which is total 3 right 
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Local model load karo
local_model_path = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(local_model_path)
model_hf = AutoModelForCausalLM.from_pretrained(local_model_path)

pipe = pipeline(
    "text-generation",
    model=model_hf,
    tokenizer=tokenizer,
    max_new_tokens=50,
    max_length=None
)

llm = HuggingFacePipeline(pipeline=pipe)

# Messages
messages = [
    # here we send two messsage one is system and second one is human message and we want that in reuslt it will give back us an ai answer 
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about langchain?"),
]

# ✅ TinyLlama chat format mein convert karo
prompt = f"<|system|>{messages[0].content}</s><|user|>{messages[1].content}</s><|assistant|>"

result = llm.invoke(prompt)

# ✅ Sirf answer nikalo
answer = result.split("<|assistant|>")[-1].strip()

# AI message append karo
messages.append(AIMessage(content=answer)) # here we append the ai message and print the result right

print(messages)

# NOW THE MAIN THING THIS MODEL WHICH WE DOWNLAOD THIS IS NOT GOOD TO DELIVER THE CHAT ANSWERS LIKE WE WANT SO THERE S 
# NO ISSUE IN CODE THIS THING WE ALSO ALTER LATER IN FUTURE IF WE WORK ON REAL CLIENTS PROJECTS THERE THEY ALREADY GIVE US APIS OR MONEY RIGHT 

# NOW , upper we seee how the static messages works but now we also see that how the dynamic messages works 
# now we use this only when we work with list of messages and we create the dymnamic messsages  chatPromptTemplate class in langchain .
