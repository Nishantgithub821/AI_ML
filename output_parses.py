# Now in this file we see how the ooutput parses work because in back file we see how the data send to the database in the form of json or another formate 
# but we dont buy the api key so we use online open sourceand opensource cant give us structure data so to convert this unstructure data to a formate so that we talk iwth out model we use this output parses 
# let start this first what is the output parses 
# DEF = > so kuch nahi langchain me kuch classes likhi gai hai which insure the consistency validation and ease of use in applications so that this functoanlity convert tthe data intos structure formate right
# There ar 4 types of outputParses -> 1. String OP
#2. Json OP
#3. Strucutured OP
#4 Pydantic OP

# let talk about ist output parses that is StrOutputParser 
# so we have one task to do what we do 
# we have a topic send to -> llm -> then model invoke kerke kahenge ki detialed report tyar ker -> then again llm ke pass bejhenge right and kahenge kii 5 line summary de 
# means in code what we do 
# we have two prompts in ist pompt we ask that write a detail report on topic 
# and in second propmmt which text comes our as result from sirst prompt we aks that wrote a 5 line summary on the following text t simple 
# REMINDER - > we use opensource api key right model so let do this code 
from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

# ab ham sabsee pehle libaries ke bad kya kerte hote hain hamara model define kerna now 
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # yeh try karo
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
# now prompt1 me ham prompttemplate ko kahnege ki detailed report bana to now 
template1 = PromptTemplate(
    template = "Write a detailed summary on the {topic}",
    input_variables=["topic"]
)
template2 = PromptTemplate(
    template = "Write a 5 line summary on the  following text /n{text}",
    input_variables=["text"]
)
prompt1 = template1.invoke({"topic":"Black Hole"})
result = model.invoke(prompt1)
prompt2 = template2.invoke({"text":result.content})
result1 = model.invoke(prompt2)

print(result1.content)

# now we write the same code again with the help of the stroutputparses 
