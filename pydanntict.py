# now we see the benefit of the pydantic library 
# ab pydantic me kya hai ki like agar ham typedict use kerte hain abd string me integer pass kerdete hai to error nahi ata 
# vo seedha agge pass kerdeta hai but agar ham pydantic me string ki jagah integer pass kerte hai to error dega right so this is 
# used for extra check or for safety reasons 

from pydantic import BaseModel 
from pydantic import EmailStr
from pydantic import Field
 # like typedict ham use kerte the typedict me ise basemodel use kerenge right 
from typing import Optional

class Student(BaseModel):
    name:str
    age:Optional[int] = None
    email :str
    cgpa :float = Field(gt=0 , lt=10,default=6,description="yaha kuch bhi add ker sakte hain right ")
new_person = {"name":"Anonymous","age":44, "email": "anonymous@gmail.com","cgpa":6.8}
student = Student(**new_person)
student_dict = dict(student)
print(student_dict["age"])
student_json =student.model_dump_json()

# is code ka outut aissa ayega name='Anonymous' age=44 email='anonymous@gmail.com'  


#how we set the defauult values right 
#name :str = "Nitish"
#optional fill
#age:Optional[int] = None
# type coercing ka matlab hota hai like hamne age=32 string formae mee bhejh di but hame printto integera me chaihye to error nahi ayega 
# ye behind the scene apne app type coercing ker dega 

# Next hai builtin validations like emailstr
# next hai apna field functions like default values , constrinas descripiotns regexexpressions 
# and last hai humara pydantic object convert into json/dict 
# let see one by one start from field functions constraints 

# yes we discuss all about pydantic 

# let copy the structed output code of typedict and then we use how the pydantic is aplicable in here right 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel,Field

load_dotenv()

model = ChatOpenAI()

# schema
class Review(BaseModel): # yaha pe typedict ki place pe BaseModel aa jayega 
     # ab ham ise recreate kerenge let see how okey 





    key_themes:list[str] = Field(discription="Write down all the key themes discussed in the review in a list")
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

print(result['name'])