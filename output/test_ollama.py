from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma4:e2b")
result = llm.invoke("Hello, how are you?")
print(result)