from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_ollama import ChatOllama
llm = ChatOllama(
    model="gemma4:e2b",
)

chat_template=ChatPromptTemplate([
    
    ('system','You are Helpful {domain} expert'),
    ('human','Expalin in simple Term what is {topic}'),
    
])

prompt=chat_template.invoke({'domain':'cricket','topic':'DRS'})
print(prompt)
res=llm.invoke(prompt)
print(res.content)