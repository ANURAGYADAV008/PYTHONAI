from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma4:e2b")

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful Customer support agent"),
    MessagesPlaceholder(variable_name="chathistory"),
    ("human", "{query}")
])

chat_history = []

with open("chat_history.txt") as f:
    lines = f.readlines()

for line in lines:
    chat_history.append(HumanMessage(content=line.strip()))

prompt = chat_template.invoke({
    "chathistory": chat_history,
    "query": "where is my refund"
})

res = llm.invoke(prompt)

print(res.content)