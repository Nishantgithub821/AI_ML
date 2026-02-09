"""
📘 LLMs – Clean Beginner Notes
1️⃣ What is an LLM? (Large Language Model)

LLM ek AI model hota hai jo:

text ko padhta

aur next word / token predict karta hai

🧠 Simple line:

LLM text ko samajhta nahi, balki pattern ke basis par next token predict karta hai.

✅ Examples:

ChatGPT

Gemini

Claude

2️⃣ How LLM works (High-level)

User prompt deta hai

LLM prompt ko tokens me todta hai

Har step pe next token predict karta hai

Final response generate hota hai

3️⃣ Prompt & Response

Prompt → jo hum poochte hain

Response → jo LLM deta hai

Prompt jitna clear, response utna better.

4️⃣ Tokens (Basic Idea)

LLM text ko words / parts of words (tokens) me padhta hai

Prediction token by token hoti hai

5️⃣ Context Window
✅ Correct Definition:

Context window = maximum number of tokens (input + history + output)
jo LLM ek time pe process kar sakta hai.

🧠 Important:

Sirf output limit ❌

Input + history + output ✅

🔑 One-liner:

Context window is what the LLM can see at one time.

6️⃣ What is RAG?
🔹 Full Form:

RAG = Retrieval-Augmented Generation

🔹 Meaning:

RAG ek technique hai jisme LLM ko answer generate karne se pehle
bahar se relevant data laa kar diya jata hai.

🧠 Important:

RAG token generate nahi karta

Token generation sirf LLM karta hai

7️⃣ RAG – 4 Step Flow
1️⃣ Query (Input)

User question poochta hai

2️⃣ Retrieval

System relevant data:

database

files

documents
se nikalta hai

3️⃣ Augmentation

Important content select hota hai

Prompt ke saath LLM ko diya jata hai

4️⃣ Generation

LLM us content ko padhkar

new answer generate karta hai

8️⃣ RAG Real-life Example (Student–Homework)

Query: Teacher question deta hai

Retrieval: Student books / notes dhundta hai

Augmentation: Important points prepare karta hai

Generation: Next day teacher ko answer batata hai

🧠 Mapping:

Student = LLM

Books / notes = external data

Homework = Retrieval + Augmentation

Answer bolna = Generation

9️⃣ Why RAG is Important?

LLM ka knowledge limited / outdated hota hai

Context window limited hoti hai

RAG:

hallucination kam karta hai

fresh & correct info deta hai

🔚 Final Summary (1 line each)

LLM → text predict karta hai

Context Window → LLM ki dekhne ki limit

RAG → pehle data lao, phir answer banao
"""
