import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate,load_prompt

llm = ChatOllama(model="phi3:latest")

st.title("Local Chatbot")

paper_input=st.selectbox("Select Reserch Paper",["Select..","Transformer Attention all You Need","BERT : Pre-Traning of Deep Bidirectional Tranformers "])

style_input=st.selectbox("Select Explanation Style ",["Bigineer-Friendly","Technical Code Oriented","Mathmatical"])

length_input=st.selectbox("Select explanation Length",["Short 1-2 Paragraph "," Medium 3-4 Paragraph"])

template=load_prompt('template.json')

# prompt=template.invoke({
#     'paper_input':paper_input,
#     'style_input':style_input,
#     'length_input':length_input
    
# })

# if st.button("summarize"):
#     result=llm.invoke(prompt)
#     print(result.content)
#     st.write(result.content)

if st.button("summarize"):
    chain=template | llm
    result=chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
        
    })
    st.write(result.content)
    

