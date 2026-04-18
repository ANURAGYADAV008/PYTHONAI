from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
llm=ChatOllama(model="gemma4:e2b")

template1=PromptTemplate(
    template="Write a Detailed Report On {topic} ",
    input_variables=['topic']
)

template2=PromptTemplate(
    template="write The Five Lines Summary On the Following {text}",
    input_variables=['text']
)

prompt1=template1.invoke({'topic':'black Hole'})
result=llm.invoke(prompt1)
prompt2=template2.invoke({'text':result.content})
print(llm.invoke(prompt2))