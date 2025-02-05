from transformers import pipeline
from langchain.llms import HuggingFacePipeline

hf_pipeline = pipeline("text2text-generation", model="google/flan-t5-large")
llm = HuggingFacePipeline(pipeline=hf_pipeline)

from langchain_community.llms import HuggingFacePipeline #for hugging face models
from langchain.schema import HumanMessage, SystemMessage, AIMessage
Chatllm = HuggingFacePipeline(pipeline=hf_pipeline)

Chatllm([
    SystemMessage(content="You are a comedican AI assistant"),
    HumanMessage(content="Please make some jokes on AI")
])
