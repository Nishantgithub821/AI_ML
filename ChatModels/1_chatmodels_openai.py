from langchain_openai import chatOpenAI # NOW here we import the chatopenAI not ai 

from dotenv import load_dotenv
load_dotenv()
# now tilll this we know we dont do anything complext just use the chatopenai right and dotenv file now 

model = chatOpenAI(model="gpt-4",temperature=1.5,max_completion_tokens=10)
resultofquestion = model.invoke("What is the capital of the India ")
print(resultofquestion.content) # here we print the result 

# now here is some things to understand through which we improve the result that is our temperature like how we use this parameter 
# we use parameter to see the acuarate answers or  we say more predictable answers now there is also a table on this that which range of the 
# temperature works on which type of technology like on maths or on englihs text or on genreal question like mcqs etc now we use it then 
# we change this line from this  model = chatOpenAI(model="gpt-4) to this model = chatOpenAI(model="gpt-4",temperature=1.5)
# and for check the reuslts we use the new promopt that is write a 5 line poen on cricket 
# like this resultofquestion = model.invoke("Write a 5 line poem on cricket") invoke means bulana or is quesitno ko us api pe hit kerna right 

# now in reuslt if you buy the open ai key then you see when use import the chatopen ai insstead of openai then when you print the result so much 
# content with diff diff parameters shows and thats why we print print(resultpfquestion.content) because in that content there is parameter named content 
# which give us the exact output of the question 

# next parameter is max_completion_tokens = 10 throught this that means we want that the answer should be in 1000 words or 1000 tokens 
# because in paid api we need to pay to generate the tokens /words thats why we use this parameter for betterment and cost saving right 

# now we seee that how the openai bot api key works but in future we also work on claude api so now we make a new file and same process but the things that is different is
# now we work on claude api key and we import the claude api key and then we use the same process to generate the result of the question .