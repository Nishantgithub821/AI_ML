import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from langchain_community.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import streamlit as st 

# ✅ CACHING for speed
@st.cache_resource
def load_model():
    model_id = "bigscience/bloom-560m"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=100)
    return HuggingFacePipeline(pipeline=pipe)

llm = load_model()

st.header("Research Assistant Tool")

# User selections
paper_input = st.selectbox(
    "Select Research Paper Name", 
    ["Attention Is All You Need", 
     "BERT: Pre-training of Deep Bidirectional Transformers", 
     "GPT-3: Language Models are Few-Shot Learners", 
     "Diffusion Models Beat GANs on Image Synthesis"]
)

style_input = st.selectbox(
    "Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
) 

length_input = st.selectbox(
    "Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Template definition
template = PromptTemplate(
    template="""
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
    input_variables=['paper_input', 'style_input', 'length_input'],
)

# ✅ Button ke ANDAR sab kuch
if st.button("Summarize"):
    # ✅ ACTUAL user selections use karo
    prompt = template.format(
        paper_input=paper_input,      # ✅ User ka selection
        style_input=style_input,      # ✅ User ka selection
        length_input=length_input     # ✅ User ka selection
    )
    
    with st.spinner("Generating summary..."):
        result = llm.invoke(prompt)          # ✅ Invoke karo
        st.write(result)              # ✅ Direct result display

# Reasons why we use PromptTemplate instead of f-string:
# 1. Input validation - Galat variables detect karta hai
# 2. Reusable - Ek baar define, multiple jagah use
# 3. Langchain ecosystem - Other components ke saath compatible
# 4. Type safety - Variables ka type check hota hai