from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# ---------------- Step 1: Choose model ----------------
model_name = "bigscience/bloom-560m"  # offline text-generation model

# ---------------- Step 2: Load tokenizer and model ----------------
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",          # auto select CPU/GPU
    torch_dtype=torch.float16   # optional: saves RAM
)

# ---------------- Step 3: Input prompt ----------------
input_text = "What is the capital of India?"
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

# ---------------- Step 4: Generate output ----------------
outputs = model.generate(
    **inputs,
    max_new_tokens=50,    # controls answer length
    do_sample=True,       # randomness in answer
    temperature=0.7       # creativity factor
)

# ---------------- Step 5: Decode & print ----------------
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(answer)
