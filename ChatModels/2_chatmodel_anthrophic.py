# now in this also the thing is same that the api key of the claude is also paid right now its up to us that we buy or not but for now we skip that part of payment because for now we only learning the things we dont want to pay anywhere right 
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model=ChatAnthropic(model="claude-3-5-sonnet-20241022") # this is the claude model as you knwo right 
result_of_my_question = model.invoke("what is the capital of india")
print(result_of_my_question.content)
# same code just minimal difference similar we do this things with the gemini key and make the chatbot for that also right same process 
# NOW MOVE TO OUR 3 FILE TAHT IS START WITH 3_CHATMODEL I THINK RIGHT IN THIS SAME FOLDER OF CHATMODELS 

