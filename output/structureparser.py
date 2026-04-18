from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

class FactItem(BaseModel):
    title: str
    type: str

class Facts(BaseModel):
    fact_1: FactItem
    fact_2: FactItem
    fact_3: FactItem

llm = ChatOllama(model="gemma4:e2b")

parser = PydanticOutputParser(pydantic_object=Facts)

template = PromptTemplate(
    template="Give 3 facts about {topic}.\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = template | llm | parser

final_res = chain.invoke({"topic": "Black Hole"})
print(final_res)

