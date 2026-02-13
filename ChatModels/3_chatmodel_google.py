from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-1.5-pro-sonnet-20241022")
result = model.invoke("What is the capital of India")
print(result.content)

# same this side also right that sit 
# now we see these these are the paid so now we see the free version or we say ope source right
"""
+-------------------+------------------------------+----------------------------------+
| Feature           | Open-Source Models           | Closed-Source Models             |
+-------------------+------------------------------+----------------------------------+
| Cost              | Free to use (no API costs)   | Paid API usage (e.g., OpenAI     |
|                   |                              | charges per token)               |
+-------------------+------------------------------+----------------------------------+
| Control           | Can modify, fine-tune, and   | Locked to provider’s             |
|                   | deploy anywhere              | infrastructure                   |
+-------------------+------------------------------+----------------------------------+
| Data Privacy      | Runs locally (no data sent   | Sends queries to provider’s      |
|                   | to external servers)         | servers                          |
+-------------------+------------------------------+----------------------------------+
| Customization     | Can fine-tune on specific    | No access to fine-tuning in      |
|                   | datasets                     | most cases                       |
+-------------------+------------------------------+----------------------------------+
| Deployment        | Can be deployed on on-       | Must use vendor’s API            |
|                   | premise servers or cloud     |                                  |
+-------------------+------------------------------+----------------------------------+




+--------------------+-------------+------------+--------------------------------------+
| Model              | Developer   | Parameters | Best Use Case                        |
+--------------------+-------------+------------+--------------------------------------+
| LLaMA-2-7B/13B/70B | Meta AI     | 7B - 70B   | General-purpose text generation      |
+--------------------+-------------+------------+--------------------------------------+
| Mixtral-8x7B       | Mistral AI  | 8x7B (MoE) | Efficient & fast responses           |
+--------------------+-------------+------------+--------------------------------------+
| Mistral-7B         | Mistral AI  | 7B         | Best small-scale model               |
|                    |             |            | (outperforms LLaMA-2-13B)            |
+--------------------+-------------+------------+--------------------------------------+
| Falcon-7B/40B      | TII UAE     | 7B - 40B   | High-speed inference                 |
+--------------------+-------------+------------+--------------------------------------+
| BLOOM-176B         | BigScience  | 176B       | Multilingual text generation         |
+--------------------+-------------+------------+--------------------------------------+
| GPT-J-6B           | EleutherAI  | 6B         | Lightweight and efficient            |
+--------------------+-------------+------------+--------------------------------------+
| GPT-NeoX-20B       | EleutherAI  | 20B        | Large-scale applications             |
+--------------------+-------------+------------+--------------------------------------+
| StableLM           | Stability AI| 3B - 7B    | Compact models for chatbots          |
+--------------------+-------------+------------+--------------------------------------+
"""
# Next Big questino where we found these all types of the free opensources models the answer is -> huggingface.co/models
# Next Big question is what are the ways to open this right ist is using hf inference API and second using running locally 
#NOW THE THING IS WE SEE THE BOTH TECHNIQUES BUT FIRST WE SEE THE INFERENCE API TECHNIQUE BECAUSE THROUGH THIS IT GIVE US API KEY FOR SMALL TESTING PURPIOSE 
# OR MAKING A SMALL LEEVEL PROJECT RIGHT .

# NOW WE ALSO NEXT SEE THE NEDT THAT IS RUNNIGN LOCALLY BY DOWNLAODN IN LOCAL MACHINE BUT I WARN YOU THAT THIS IS THE BIGGEST DISDVANTAGE OF THIS IS 
# IF WE DOWNLAODN IN OUR NORMAL  COMUPUTER OR LEPTOP THEN IT WORK WORK BECAUSE TO RUN THIS WE NEED A HIGH END GPU OR A HIGH END COMPUTER TO RUN THIS MODEL RIGHT AND 
# I ALSO SHOW SOME MORE DISDNVANTAGES  OF THIS ARE 
"""
+----------------------------+---------------------------------------------------------------+
| Disadvantage               | Details                                                       |
+----------------------------+---------------------------------------------------------------+
| High Hardware Requirements | Running large models (e.g., LLaMA-2-70B) requires expensive  |
|                            | GPUs.                                                         |
+----------------------------+---------------------------------------------------------------+
| Setup Complexity           | Requires installation of dependencies like PyTorch, CUDA,    |
|                            | transformers.                                                |
+----------------------------+---------------------------------------------------------------+
| Lack of RLHF               | Most open-source models don’t have fine-tuning with human    |
|                            | feedback, making them weaker in instruction-following.       |
+----------------------------+---------------------------------------------------------------+
| Limited Multimodal         | Open models don’t support images, audio, or video like       |
| Abilities                  | GPT-4V.                                                       |
+----------------------------+---------------------------------------------------------------+
"""