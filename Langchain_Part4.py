WHAT IS MODEL-> THIS IS IN DEPTH PART FOR THE ONLY MODEL COMPONENT IN LANCHAIN
"""
The model component in langchain is a cruicial part of the framework desgined to faciliate intereactions with variaous language models and embedding models 
Iska matlab kya hai ki model component hame facility provide kerwata hai different type of models se itneract kerne me like there are two of them one is language modes and another one is embedding models right 
As e also discussed wah is language model and embedding modelBut i also again expalin -> 
language model like LLms and chatbot in which text to text is there if we give input it returns the output as text foramte like chatgpt 
But in embeddding model it did the symentic search ok and we all know if you check out my previous documentation on it you know what is sementic search .
symentic search -> Rag based system build help of embedding models . ( output as numbers not text) 

"""
# Now in this video we see the practial of it right we done so much theortical now we do practical of it so let start 
# now hows the flowchhart of it right so 
"""
First we do language models in which thereaer two tye of source we do 
Closed source 
Open source 
in closed source----> open Ai , claude gemini on these we work 
in open source  -----> hugging face 
WHEN THESE ARE COMPLETED THEN WE MOVE ON OUR EMBEDDING MODELS IN WHICH 
closed source -> open ai embedding model 
open source -> hugging face embedding model and then we create small chatbot okey 

"""

# Language Models :
"""
Now the thing  is we know what are the language models and we know in which there is two type of models 
llms and chatbots now the era of llms is now slowly slowly finished because now the langchain technology is coming 
And these are replaced by chatbots now what the chatbots do instead of doing the text to text generation like llms they generate the text as well and they also do our work help of embedding searching .

+-------------------+----------------------------------------------+--------------------------------------------------+
| Feature           | LLMs (Base Models)                           | Chat Models (Instruction-Tuned)                  |
+-------------------+----------------------------------------------+--------------------------------------------------+
| Purpose           | Free-form text generation                    | Optimized for multi-turn conversations           |
+-------------------+----------------------------------------------+--------------------------------------------------+
| Training Data     | General text corpora (books, articles)       | Fine-tuned on chat datasets (dialogues,          |
|                   |                                              | user-assistant conversations)                    |
+-------------------+----------------------------------------------+--------------------------------------------------+
| Memory & Context  | No built-in memory                           | Supports structured conversation history         |
+-------------------+----------------------------------------------+--------------------------------------------------+
| Role Awareness    | No understanding of "user" and "assistant"   | Understands "system", "user", and "assistant"    |
|                   | roles                                        | roles                                            |
+-------------------+----------------------------------------------+--------------------------------------------------+
| Example Models    | GPT-3, Llama-2-7B, Mistral-7B, OPT-1.3B      | GPT-4, GPT-3.5-turbo, Llama-2-Chat,              |
|                   |                                              | Mistral-Instruct, Claude                         |
+-------------------+----------------------------------------------+--------------------------------------------------+
| Use Cases         | Text generation, summarization, translation, | Conversational AI, chatbots, virtual assistants, |
|                   | creative writing, code generation            | customer support, AI tutors                      |
+-------------------+----------------------------------------------+--------------------------------------------------+

"""
# Setup 
"""
Create a new folder in desktop 
then open in a vs code 
then create a new venv with this comand run on vs code terminal python -m venv venv 
