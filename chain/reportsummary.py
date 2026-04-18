from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm=ChatOllama(model="gemma4:e2b")

report=PromptTemplate(
    template=("Generate The Report On {topic}"),
    input_variables=['topic']
)
summary=PromptTemplate(
    template="Generate The Detailed Summary Of {res}",
    input_variables=['res']
)
parser=StrOutputParser()

chain=report | llm | parser |summary|llm|parser
res=chain.invoke({'topic':"Mystery Of Black Hole"})

print(res)

