from langchain_community.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# Local model load karo
#local_model_path = "bigscience/bloom-560m" # becasue this is not a Q/A bot 
local_model_path = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(local_model_path)
model_hf = AutoModelForCausalLM.from_pretrained(local_model_path)


# chathistory  each time when user type the message we append in it 

# Pipeline banao
pipe = pipeline(
    "text-generation",
    model=model_hf,
    tokenizer=tokenizer,
    max_new_tokens=None
)

# LangChain LLM banao
llm = HuggingFacePipeline(pipeline=pipe)

# Simple loop for chatbot
chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input)) #yaha ham chat history ko append ker denge right user input jo bhi dalega 
    if user_input.lower() in ['exit', 'quit', 'bye']:
        break
    
    # Direct invoke - no template needed
    response = llm.invoke(user_input)
    chat_history.append(AIMessage(content=response)) # yaha same way se resuklt ke content ko bhi append ker degne right 
    print(f"Bot: {response}")

    #Now hamne ye to solve ker diay ki chathistory wala scene but the thing is ki jo ye chats history me jaygengii to 
    # isse pata nahi lagega ki bhai maine konsa code diya tha or prompt and user ne kons t us problem ko solve kerne ke liye ham DICTONARY ka use kerte hain right 

    # now yaha pe na dictonarys me chat store kerne ke liye yani ki messages store kerne ke liye yaha pe 
    # hamara messages ka concept ata hai like message 2 type ke hote hain 
    # 1. system message 2.  Human message 3. AI message 
