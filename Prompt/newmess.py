from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_ollama import ChatOllama
llm = ChatOllama(
    model="gemma4:e2b",
    num_predict=300,
    num_ctx=4096,
    temperature=0.7
)

ai_msg=AIMessage("I's be happy to help you with that Question")

message=[
    
]