# to run this page run this script message_place_holder.py 
from langchain_core.prompts import ChatPromptTemplate ,MessagesPlaceholder

#chat  template

chat_template = ChatPromptTemplate([
    ("system","You are a helpful customer support assistant."),
    MessagesPlaceholder(variable_name="chat_history"), 
    ("human","{query}")
])


chat_history = [] # make a list where all past chat in the formate of list is stored 
# load the chat history 

with open("C:/Users/HP/Desktop/Langchain_Model/chat_history.txt") as f:
    chat_history.extend(f.readlines())
    print(chat_history)


# create prompt now 
prompt = chat_template.invoke({"chat_history": chat_history, "query": "Where is my refund"})