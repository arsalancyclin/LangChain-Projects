from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

#ollama llm model

llm=Ollama(model="llama3.2")

prompt=ChatPromptTemplate.from_template("Write me an poem about {topic} for a toddler")

add_routes(
    app,
    prompt|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)