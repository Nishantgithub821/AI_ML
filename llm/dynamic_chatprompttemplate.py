from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    #SystemMessage(content="You are a helpful {domain} expert."),
    #HumanMessage(content="Explain in simple terms, what is {topic}?") # 
    # now her we create message template now below we fill the placeholders okey
    
    # Now the way of declaring the system messages and human messages is not right because it print asetease 
    #in result but we we want to the fill the placeholders right so we pass the tuples 

    ("system","You are a helpful {domain} expert."),
    ("human","Explain in simple terms, what is {topic}?")
])
prompt = chat_template.invoke({"domain": "software development", "topic": "machine learning"})
print(prompt)

#python llm\dynamic_chatprompttemplate.py to run the script this will run okey 

# now the output will come with placehodlers fills okey

#Message place Holder is a special placeholder inside a chatptompttemplate to dynamicaly insert chathistory of a list of messages at runtime 
  