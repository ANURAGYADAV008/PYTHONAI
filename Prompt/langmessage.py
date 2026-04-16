from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_ollama import ChatOllama
llm = ChatOllama(
    model="phi3:latest",
    num_predict=300,
    num_ctx=4096,
    temperature=0.7
)

chat_template=ChatPromptTemplate([
    
    ('system','You are Helpful {domain} expert'),
    ('human','Expalin in simple Term what is {topic}'),
    
])

prompt=chat_template.invoke({'domain':'cricket','topic':'Dusra'})
print(prompt)