So we are now in our I think 4h video of the langchan and that would be on langchan components 
So there are majorly 6 components in there 
1.Models 2. prompts 3. chains 4 memory 5 indexes 6 models 

We start with our ist topic that is our Models so let started  ( and this is the most important 
type )

So the model is basically describe as I tell you a story so like when the topic of models is come then the famous word that is our chatbot comes in picture so  everyone in back then era wants to create a chatbot now there is two major problem faced by them so ist one is NLU and second one is context aware text generation that means like if we say hi to chatgpt so that means it understand first that is our NLU and then back reply with relevant content hello that is our context aware text generation now after sometime numerous works are happen on it and llms comes in picture which solve these both two problems but after solving this problem the major one problem that came in picture that is our storage or placement means to run it the llms we somewhere place like in database but the storage of it is more than 100gb and if we put this in our cloud or somewhere else that will be very very costly and difficutl then Api comes in pictures like some developers put the llms on their servers and make the apis to access form anywhere now that problmee solved again one major problem comes that is there are numerous chatbots in market so every kind of bot have their own api and that means own boiler plate code of if we want that yes now we use gemini api rather than chatgpt we want to replace it fully that is very difficult than the langchain comes in picture that says that we makae this type of interface so that when we want to replace it so that we don't want to change the whole  code just minimal changes give us good results so this is the working of the model .

So according tp this working we understand that langchain models re the core interfaces through which you interact with Ai models 

So in langchains there are tow types of models so the first one is language model and second one is embedding model 
now in language model how it works one text to text means take input as text and convert or output gives as text but 
int embedding model I give in input as text but it gives output as vector right like ex is semantic search and this thing we also discuss in the previous video topic of the semantic search and embedding model right 

2) Prompt 
So next is our prompt so basically in our  chatbots what the question we ask to the bots that is called the prompt right so we create our own prompts with the help of the langchians how 

1) Dynamic and Reusable prompts :
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template('Summarize {topic} in {emotion} tone')

print(prompt.format(topic='Cricket', length='fun'))

2. Role Based prompts : 
# Define the ChatPromptTemplate using from_template
chat_prompt = ChatPromptTemplate.from_template([
    ("system", "Hi you are a experienced {profession}"),
    ("user", "Tell me about {topic}"),
])

# Format the prompt with the variable
formatted_messages = chat_prompt.format_messages(profession="Doctor", topic="Viral Fever")

3. Few Shot prompting : 
 # Define the ChatPromptTemplate using from_template
chat_prompt = ChatPromptTemplate.from_template([
    ("system", "Hi you are a experienced {profession}"),
    ("user", "Tell me about {topic}"),
])

# Format the prompt with the variable
formatted_messages = chat_prompt.format_messages(
    profession="Doctor", 
    topic="Viral Fever"
)



3. CHAINS : with this name our langchain name is select  right . so  forthis we create the pipelines  and this is the most important topic of the langchain right 
now 1 -> how the sequential chain works so i give /paste here the flowchart
Chains  -->  Pipelines  -->  LLM
  ↑                            |
  |                        Pipeline
  |                            |
input             Hindi        ↓
Eng text  ------> Summar  --> Pipeline
(1000)            (100)        ↓
  |                            |
  ↓                            ↓
[ input ] ------> [  LLM  ] ------> [ Transt ] ------> [  LLM  ] ------> [ Summary ]
    ↑               manully           sequential                            |
    |                  |                  ↑                                 |
    -------------------|------------------|                                 ↓
                    Chains Call                                          result



  # Now the parallel chain flowchart okey 
  Chains  -->  Pipelines  -->  LLM
  ↑                            |
  |                        Pipeline
  |                            |
input             Hindi        ↓
Eng text  ------> Summar  --> Pipeline
(1000)            (100)        ↓
  |                            |
  ↓                            ↓
[ input ] ------> [  LLM  ] ------> [ Transt ] ------> [  LLM  ] ------> [ Summary ]
    ↑               manully           sequential                            |
    |                  |                  ↑                                 |
    -------------------|------------------|                                 ↓
                    Chains Call                                          result


  # Now conditional chain flowchart okey 
  Parallel
 chain

           .-----> [ LLM1 ] -----.  [ ist parralel work]---------  |
          .                       .                                |
[ input ]                          -----> [ report ] -----> [ combine ] -----> [ output ]
          .                       .                                |
           .-----> [ LLM2 ] -----. [second parallel work]]---------|

4. Index 
Now this topic is the previous notes all copy of the langchain part 2 in which i describe the pdf loader i think a project flowchart and no need to rewrite it because we already explain that thing 
in that file but one thing that we remember that is a 
Our indexes combine of 4 things specially only 4  -> 1.Doc Loader 
2.Text Splitter 
3.Vector Store
4.Reterivers 

5. Memory 
So our next topic that is Memory now the thing is let think  you are doing chat with a bot who dont remember previous chats like if i take example then you ask who is the prime minister of india and it 
give you answer but after that next thign you ask is or type is how old is he now it says i dont have acess of the prive or personal data and information until or unless it has been shared with me 
Now talking to this type of chatbot is very frustrating right so TO SOLVE THIS PROBLEM WE USE THE MEMORY COMPONENT RIGHT 
SO THIS IS VERY ADVANCE TOPIC BUT STILL WE HAVE ATLEAST A IDEA WHAT IS THIS OKEY 
# Now how many types of the memory now tthere is many types exists inn markets but frequently used are only 4 which we see that is 
1) Conversation Buffer Memory -> we chat it takes all the memory stored then wehn we hit the another api then we also send the previous stored memory the problem is this is only if the previous chat or memory 
is big then we pay more and that will be complex and costly 
2) conversationBufferWindowMemory we chat and we say tha tonly storesthe last N interactions to avoid this type of problem which we discuss in first right 
3) Summarizer Based Memory : in this we told it to generate a summary type and stored it so that when we hit another call api then wee send to this then this would be effiecent method to saerch right 
4) Custom Memory : this is for the advances use caseses you can store the specialize state like if i take ex the users preference or key facts about tem in a custom memory clas .

6. Agents 
# Now this is the last component of the langhcain right : 
So this is the interesting component in which we talk with the chatbos and ai agents 
Now in this what is the main difference of the Agents and chatbots Now 
if we take an example so we want to book a flight between delhi to banglore now if we do this work to chatbot it wont do it because the chatbots only give us inormatoin not the own working cappablitiy 
But in another side the ai agents do this right book a ticket of the flight ya this sounds very diffficult but we only just find the logic for now right 

Next thing is lets take a real life example how we performe this 
Let suppose we make a ai agent in whichi we give it only TWO TOOLS THAT IS CALCULATOR AND WEATHER API RIGHT 
Now a user give pormpt to it that multiply the weather of delhi by 3 now it have two things 
REASONING CAPABILITY 
TOOLS ONLY THESE TWO THINGS IT HAVE WHICH MAKE IT DIFFERENT FROM CHATBOT 
now what it do it breaks the pormpt into two first is to the temperature of delhi so it found out the tool which did this work and we alraedy gave this tool to it so it goes to the weather api and aks it to give it the result 
so let say it gaves te result 25 now 
next breakdown opeartion is our to perform mulitplication now it goes to calcualtor and same process then it also give the reuslt that will be the 25*3  75 that will be the answer . simple 


