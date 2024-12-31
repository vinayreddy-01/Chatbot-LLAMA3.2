from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Loading .env variables
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit Layout Enhancements
st.set_page_config(page_title="Q&A ChatBot with LLAMA 3.2", page_icon="🦙", layout="centered")

# Custom styling for the page (darker light theme)
st.markdown("""
    <style>
        /* Basic Reset and Font Settings */
        body {
            background-color: #f0f0f5;  /* Light gray background */
            font-family: 'Arial', sans-serif;
            color: #222;  /* Darker text */
        }
        
        .header {
            color: #3b5998;  /* Slightly deeper blue */
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            padding-bottom: 10px;
        }
        
        .subheader {
            color: #404040;  /* Darker gray */
            font-size: 22px;
            text-align: center;
            padding-bottom: 30px;
        }
        
        .input-box {
            font-size: 16px;
            width: 80%;
            padding: 14px;  /* Slightly bigger padding for a better feel */
            border-radius: 8px;
            border: 2px solid #3b5998;
            margin-bottom: 20px;
            background-color: #ffffff;  /* Keeping the input box light */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .input-box:focus {
            outline-color: #3b5998;
            border-color: #3355a0;  /* Darker border when focused */
        }

        .chatbot-response {
            background-color: #f4f7fb;  /* Light but darker background for response area */
            padding: 15px;
            border-radius: 8px;
            font-size: 18px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            max-width: 900px;
            margin: auto;
            border-left: 6px solid #3b5998;  /* Slightly bolder border */
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            color: #7d7d7d;  /* Dark gray text for footer */
            font-size: 14px;
        }

        .spinner {
            color: #3b5998;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Adding title and subheading
st.markdown('<div class="header">Q&A ChatBot with LLAMA 3.2 🦙</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Ask anything and get insightful responses from LLAMA</div>', unsafe_allow_html=True)

# User input
input_text = st.text_input("Search the topic you want to ask about:", "", key="question", placeholder="Type your question here...", help="Enter your query for a quick answer")

# Setting up the Ollama LLM Model and Streamlit backend components
llm = Ollama(model="llama3.2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Interaction logic
if input_text:
    with st.spinner("LLAMA is thinking... Please wait..."):
        response = chain.invoke({"question": input_text})
    
    st.markdown(f'<div class="chatbot-response">{response}</div>', unsafe_allow_html=True)

# Footer for Credits or Contact Info
st.markdown('<div class="footer">Powered by LLAMA 3.2 Model | Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)
