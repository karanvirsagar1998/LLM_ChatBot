from transformers import pipeline
from langchain.llms import HuggingFacePipeline
hf_pipeline = pipeline("text2text-generation", model="google/flan-t5-large")
from langchain.schema import HumanMessage, SystemMessage


import streamlit as st

# function to load model and get response
def get_response(content:str):
    SystemMessage.content="You are a intelling AI chat bot and please answer this question:-"
    HumanMessage.content = content
    llm = HuggingFacePipeline(pipeline=hf_pipeline)
    question = "/n".join([SystemMessage.content,HumanMessage.content])
    response = llm(question)
    return response

# front-end #streamlit
st.set_page_config(page_title="Q&A - Chat Bot")
st.header("Langchain Application")

input = st.text_input("Input: ", key="input")
response = get_response(input)

submit = st.button("ASK")

if submit:
    st.subheader("The response is: ")
    st.write(response)


print(get_response("Write an poem on Moon in 50 words"))