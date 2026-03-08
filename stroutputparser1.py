from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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
# ab ye cheej dhya me rakhiyo ki parser hamara specially chains ke uper kam kerta hia to ise thoda dhyan me rakhiyo 
parser = StrOutputParser()
# to ab dekh ek pure code ko ek line me cchain ke formate me kaise likhenge right so let see 
chain = template1 | model |parser |template2 |model|parser # ye dekh ek hi line me sara flow right 
result = chain.invoke({"topic":"Black Hole"})
print(result)
