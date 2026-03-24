
# 1. if we have chatgpt , claude any paid subscription and we do text - text only question answering .
from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
model = OpenAI(model="gpt-3.5-turbo-instruct")
result = model.invoke("which is the rarest blod group in human species")
print(result)

# 2. Now if we use ChatOpenAI convo type converstaion if we have api key right
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model="gpt-3.5-turbo-instruct",temperature=0.7,max_completion_tokens=100)
result = model.invoke("which is the rarest blod group in human species")
print(result) # second wale code me ham temp and max tokens ka use ker sakte hain right

#3.Now how we use the huggingface to create the pipeline and get the answer from it huggingface used in opensource right
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()
pipeline_orwesay_model = HuggingFaceEndpoint(
    repo_id="bloom-science-600m/model",
    huggingfacehub_api_token= os.environ["HuggingFaceHub_API_Key"],
    task = "text-generation",
    provider = "auto"
)
result = pipeline_orwesay_model.invoke("which is the rarest blood group of the human species ")
print(result)

#4. How we convert query into vector using openAiEmbeddings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
model = OpenAIEmbeddings(model="text-embeddings-convert/model")
result = embeddings.embed_query("Which is the rarest blood group of the human species ")
print(result)

#5. How we convert a fully document into a vectors and compare with a single query or our question right
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import numpy as np
load_dotenv()
documents =  [
    "This is the first document contains answer of different question",
    "This is the second document contains answer of our question",
    "This is the third document contains answer of different question"
]
model = OpenAIEmbeddings(model = "text-embeddings-convert/model")
vector_of_documents = embeddings.documents(documents)
our_query = "Which is the rarest blood group of the human species"
vector_our_query = embeddings.embed_query(our_query)
array_of_documents = np.array(vector_of_documents)
array_of_our_query =np.array(vector_our_query)
similarity = np.dot(array_of_documents,array_of_our_query)
best_match = np.argmax(similarity)
print(documents[best_match])

#6. How we use transformer to convert the text into vector right
from transformers import AutoModel , Tokenizer
import torch
model_name = "sentence-transformer-all-Mini/llm"
model = AutoModel.from_pretrained(model_name)
tokens = Tokenizer.from_pretrained(model_name)
input_text = "What is the rarest blood group of the human species "
converting_to_vector = tokens(input_text,return_tensor = "pt")
with torch.no_grad():
   embeddings = model(**converting_to_vector).last_hidden_state.mean(dim=1)
print("Embedding vector:", embeddings)
print("Vector shape:", embeddings.shape)

#7.How we use transformers to do text-to-text convo generator
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
model_name = "bigscience/bloom-560m"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float16
)
input_text = "What is the capital of India?"
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs,max_new_tokens=50, temperature=0.7)
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(answer)

#8. How we make the research assistance tool
import warnings
warnings.filterwarnings("ignore",category=UserWarning)

# import libraries all type ki ab ek to propmt chaihiye jo bar bar same template use ho , ek streamlit taki use web pe use ker sake ab ham apni marzi se transformer use kerenge taki khud ke locally me chala ske model and ek last cheej reh gi vo hai langchain_community.llms import huggingFacePipeline kunki pipeline banani jarrori hai right
from langchain_community.llms import huggingFacePipeline
from langchain_core.prompts import PromptTemplate
from transformer import AutoTokenizer , AutoModelForCausalLM ,pipeline
@st.cache_resource # ye sirf speed ke liye hai right
# now we make a function right for making a complete brain of this code or reserch assistant tool
def brain_of_Tool():
  model_id ="bloom/scince-600m-LM-model"
  model_name =AutoModelForCausalLM.from_pretrained(model_id)
  model_tokens = AutoTokenizer.from_pretrained(model_id)
  pipe = pipeline("text-generation",model_name = model_name , model_tokens = model_tokens , max_new_tokens=100)
  return HuggingFacePipeline(pipeline=pipe)
# ham ek variable me is pure brain ko store ker lenge to
Brain = brain_of_Tool()
# now header
st.header("Research Assistant Tool")
# user selection right jo web page pe user ko select kerne ke options dene hai right
#paper ka input kya hai
paper_input = st.selectbox(
    "Select Research Paper Name",
    # [ ] isme jo bhi dalenge uska matlab hai ki options web page pe kon kon se ayenge right
    ["Attention Is All You Need",
     "BERT: Pre-training of Deep Bidirectional Transformers",
     "GPT-3: Language Models are Few-Shot Learners",
     "Diffusion Models Beat GANs on Image Synthesis"]
)
style_input  = st.selectbox(
    "Select the Explanation Style of the paper ",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# ab ham template define kernege right jisme user ko output mil sake
template = PromptTemplate(
    template = """
    Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

2. Analogies:
   - Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
    input_variables = ["paper_input","style_input","length_input"]

)
#ab ham button  banayenge agr uspe click kerenge to kya hoga right
if st.button("summarize"):
  prompt = template.format(
      paper_input=paper_input,      # ✅ User ka selection
        style_input=style_input,      # ✅ User ka selection
        length_input=length_input
  )
  if st.spinner("Generating summary..."):
        result = Brain.invoke(prompt)          # ✅ Invoke karo
        st.write(result.content)

# 9.Now we see messages and its three types :
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage  # sabse pehle hamne messages ko import kiya
from langchain_huggingface import HuggingFacePipeline # ham locally huggingface ko use kerna chahta hai to pipeline banai padegi agar chatopenai ya claude hota to direct use ker sakte the right
from transformers import AutoTokenizer , AutoModelForCausalLM , pipeline # next hamne transformer se autotokenizer and automodelforcausallmand pipeline import ker li

model ="Tiny/lama-llm/model-v1.0" # library ke bad sabse pehla kam model ko define kerne hota hai
tokens = AutoTokenizer.from_pretrained(model) # hamne tokens nikale
actual_model = AutoModelForCausalLM.from_pretrained(model) # hamne model nikala
pipe = pipeline(
    "text-generation",
    model = actual_model,
    tokenizer = tokens,
    max_new_tokens = 50,
    max_length = None
)
wraper = HuggingFacePipeline(pipeline = pipe) # wrapper define kiya kunki direct pipeline ni bana kerti ban bhi jaye per chalti nahi hai wraper to atleast chaiye hi chaiye
#messages ka kam aya theek hai
messages  = [
    SystemMessage(content ="You are very helpful assitant "),
    HumanMessage(content="Tell me about messages in the langchain ")
]
# ab jo model hai tiny lama uska answer dene ka ek formate hai sabhi models ka apna apna alag ek hota hai right to just google it and we get that right
prompt = f"<|system|>{messages[0].content}</s><|user|>{messages[1].content}</s><|assistant|>"
result = wraper.invoke(prompt)

answer = result.split("<|assistant|>")[-1].strip() # ye isiliye kiya kunki formate to theek hai hota hai har model but jabb answer dega to usme extra cheje bhi ayengi to us time pe hame sirf result chaihuye theekhai
print(answer)

#10.Now we create simple chatbot using this three types so that we have a strong knowledge in this topic right so let see
from langchain_core.messages import SystemMessage , AIMessage , HumanMessage
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoTokenizer , AutoModelForCausalLM , pipeline

model = "tiny/lama-llm/model-v1.0"
tokens = AutoTokenizer.from_pretrained(model)
actual_model1 = AutoModelForCausalLM.from_pretrained(model)
pipe = pipeline("text-generation",
                model = actual_model1,
                tokenizer = tokens,
                max_new_tokens=50,
                max_length = None)
wrapper_again = HuggingFacePipeline(pipeline=pipe)
chat_history = [
    SystemMessage(content="You are a very helpful assistant ")
]
while True:
  user_input = input("You")
  chat_history.append(HumanMessage(content=user_input))
  if user_input.lower() in ["exit","break","stop","bye"]
     break
  response = wraper.invoke(user_input)
  chat_history.append(AIMessage(content=response))
  print(f"chatbot: {response}")

# now we practice all three types with prompt template  But first try specifically prompt template code right
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage , AIMessage , SystemMessage
template = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant "),
    ("huamn","{question}")
])
chat_history = []
user_question_pucha = "tell me about what is python"
chat_history.append(HumanMessage(content=user_question_pucha))
message = template.format_messages(question=user_input)

# ab ai ka response bhi to jodna hai prompt use kerna hai
prompt = f"You are helpful. User: {user_input}\nAssistant:"
ai_response = wrapper_again.invoke(prompt)
chat_history.append(AIMessage(content=ai_response))
for msg in chat_history:
  print(msg.content)

# now we practice the nex tthings that are typedict and pydantic and its strcutre output files right so let se first
#1. Typedict Demo that how the syntax is written of it
from typing import TypedDict
class Person(TypedDict):
  name : str
  age:int
  weight: float
  height: float
new_person: Person = {"name":"Nishant","age":"21","weight":"80.7","height":"6.2"}
print(new_person)
# now we practice its struture_output_typedict file right
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Optional , Annotated,Literal

load_dotenv()
model = ChatOpenAI()

class Review(TypedDict):
  key_themes:Annotated[list[str],"Write Down the all key themes discuss in the review in a list "]
  summary:Annotated[list[str],"Write down a brief summary about this review "]
  sentiment:Annotated[Literal["pos","neg"], "Return sentiment of the review either positive  negative or neautral "]
  pros: Annotated[Optional[list[str]],"Write down all the pros inside a list "]
  cons: Annotated[Optional[list[str]],"Write down all the cons inside a list "]
  name: Annotated[Optional[list[str]],"write the name of the reviewwer"]

  strucutred_model = model.with_strcutured_output(Review)
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

print(result)

# now we see the pydnatic right  ye wala code uper wala code pydantic me kaiise likha jaye vo hai right and second wala
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

load_dotenv()
model = ChatOpenAI()

# 🔹 Pydantic Model
class Review(BaseModel):
    key_themes: List[str] = Field(description="All key themes")
    summary: str = Field(description="Short summary")
    sentiment: Literal["pos", "neg"] = Field(description="Sentiment")
    pros: Optional[List[str]] = Field(default=None)
    cons: Optional[List[str]] = Field(default=None)
    name: Optional[str] = Field(default=None)

# 🔹 Structured output
structured_model = model.with_structured_output(Review)

# 🔹 Invoke
result = structured_model.invoke("your review text here")

# 🔹 Print
print(result)
#second code : agar hamare pass apna raw data hai and use hi use kerenge and ai se nahi use kerna data to ham ye basemodel wala use kerenge

from pydantic import BaseModel ,EmailStr,Field
from typing import Optional
class Student(BaseModel):
  name:str = "Nishant"
  age:Optional[int]=None
  email:EmailStr
  cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')

  new_student = {"age":"32","email":"abcd@gmail.com"}
  student = Student(**new_student) # dict data ko unpack kerke student object banana
  student_dict = dict(student) # convert object to dictonray
  print(student_dict["age"])
  student_json = student.model_dump_json() # fianlly convert into json file

  # agar hame open sourece use kerna hai then
  from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# schema
class Review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")


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

print(result)

# and man lo ki ham chahte hai ki ek review me se hame ek schema ek fixed formate me output chahiye to uske liye ham json shema stcture ka use kerte hain kaise chalo dekhte hain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

# schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}


structured_model = model.with_structured_output(json_schema)

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

print(result)

# now we practice the stringoutputparser but use pehle ek or code dekhgen jo chathuggingface and endpoint ka usecase hai jisse ham multiple templates use kerna seekhenge

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndPoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndPoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)
wraper = ChatHuggingFace(llm = llm)
template1 = PromptTemplate(
    template = "Write a detailed report on this {topic}",
    input_variables = ["topic"]
)
template2 = PromptTemplate(
    template = "Write a 5 line summary on the follwing text /n {text}",
    input_variables = ["text"]
)
pr1 = template1.invoke({"topic":"black hole"})
result = wraper.invoke(pr1)
pr2 = template.invoke({"text":result.content})
result1 = model.invoke(pr2)
print(result1.content)

#Ab dekhte hain String Output parser ka scene okey
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatOpenAI()

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser # ab isme chain user ki gayi hai to vo next me dekhenge bus isme vaise dikha diya and ye easy ker deti hai process ko right

result = chain.invoke({'topic':'black hole'})

print(result)

#now we do the json output parser practice right which convert the dataa into json formate automatically
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndPoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
# model right
model = HuggingFaceEndPoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)
wraper = chatHuhingFace(model=model)
parser = JsonOutputParser()
template = PromptTemplate(
    template = "give me 5 facts about {topic} \n {format_instructino}",
    input_variables =["topic"]
    partial_variables={"format_instruction":parser.get_format_instruction()}
)
chain=template|model|parser
result = chain.invoke({"topic":"black hole"})
print(result)


# now strucutre_output ka sytaax practice kerte hain
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)

# now pydantic parser dekhte hain right

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

final_result = chain.invoke({'place':'sri lankan'})

print(final_result)

# now we see the chains simple chains , parallel and sequential chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
prompt = PromptTemplate(
    template ="Write about a 5 interesting facts about this {topic}",
    input_variables= ["input"]
)
model=ChatOpenAI()
parser = StrOutputParser()
# chain kaise banegi  prompt jayega model ke pass and model jo result dega parser ke pass jayega use ye string me badal dega neat and clean without any wwhitespaces
chain = prompt|model|parser
result = chain.invoke({"topic":"cricket"})
print(result)

# now we practice the
