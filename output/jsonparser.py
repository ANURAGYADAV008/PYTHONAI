from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
llm=ChatOllama(model="gemma4:e2b")
parser=JsonOutputParser()

template=PromptTemplate(
    template="generate Any Random SuperHero name ,Place ,age, \n {format_instruction} ",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
prompt=template.format()
result=llm.invoke(prompt)
final_output=parser.parse(result.content)
print(final_output)