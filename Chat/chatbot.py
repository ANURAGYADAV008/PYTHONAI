from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
llm=ChatOllama(model="gemma4:e2b")

chat_history=[
    SystemMessage(content="You Are helpful Ai Assistant And You ")
]
while True:
    user_input=input('Anurag :')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    else:
        result=llm.invoke(chat_history)
        chat_history.append(AIMessage(content=result.content))
        print(f'gemma4:{result.content}')


        
print(chat_history)