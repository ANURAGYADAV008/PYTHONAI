from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm=ChatOllama(model="gemma4:e2b")
prompt=PromptTemplate(
    template="Genarate Five Intresting Facts On {topic}",
    input_variables=['topic']
)

parser=StrOutputParser()
chain= prompt | llm |parser
##res=chain.invoke({'topic':"Black Hole"})
##print(res)
chain.get_graph().print_ascii();
