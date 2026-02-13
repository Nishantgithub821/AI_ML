# like in this project we buy the api key in future but or now ignore the yellow underline okey because when we buy it thenit generate and give us the api secret key okey 
from langchain_openai import OpenAI # Here we import the openAI so that we use it in our project
from dotenv import load_dotenv # here we import the dotenv in which we store our secret key and the api key to use the openAI api key


load_dotenv() # here we finally load the dotenv so that all set 

llm = OpenAI(model="gpt-3.5-turbo", ) # then here we use model that is our wriiten in there
result = llm.invoke("What is the capital of India?") # here make variable result and then when we invoke any qyestion
# then it hit on our api  key and it give back to us the result (text to text as input as output okey )
# below in terminal it give the answer but for now we dont buy the api  key so it wouldnt give any result 
print(result)