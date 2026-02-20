import warnings
warnings.filterwarnings('ignore')
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from dotenv import load_dotenv
from typing import TypedDict , Annotated
# Path to your locally downloaded model
model_path = "C:/path/to/your/downloaded/model/bloom-560m"  # Yahan apna path dalo

# OR if it's in default HuggingFace cache, just use model name
model_id = "bigscience/bloom-560m"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id)  # Ya model_path
model = AutoModelForCausalLM.from_pretrained(model_id)  # Ya model_path

# Create pipeline
pipe = pipeline(
    "text-generation", 
    model=model, 
    tokenizer=tokenizer, 
    max_new_tokens=30
)

# Wrap in LangChain
llm = HuggingFacePipeline(pipeline=pipe)

# yaha neche huum do ways se define ker sakte se  ek to bina annotated ke ek uske sath 
# agar ham annotated use ekrte hain to isse help milti hai topic ko specific ache se janne ke liye 
# code : 
class Review(TypedDict):
    summary:Annotated[str,"A Breif Summary of the review "]
    sentiment:Annotated[str,"Return Sentiment of the review either negative , positive or neutral Summary "]
    

structured_model = llm.with_structured_output(Review)

# here we write the review about the phone 
result = structured_model.invoke("This phone is amazing! The camera quality is outstanding and captures stunning photos even in low light.  life easily lasts all day with heavy usage. e display is crisp and smooth, making it perfect for gaming and watching videos.")
# Use it
print(type(result))

# To is code vaise error ayega because ye funciton with_structured_output kuch hi models me use hota hai  
# joo ki paid hai to hum unke bina hi seekhenge right 