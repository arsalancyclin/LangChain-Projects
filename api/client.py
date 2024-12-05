import streamlit as st
import requests
import os

from dotenv import load_dotenv

load_dotenv()

#Langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"


def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke", json={'input':{'topic':input_text}})
    return response.json()['output']

st.title("Langchain Demo with llama3.2 API")
input_text = st.text_input("Write a poem on")

if input_text:
    st.write(get_ollama_response(input_text))