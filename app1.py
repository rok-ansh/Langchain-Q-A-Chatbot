# Conversational Q & A Chatbot
import os
from langchain.llms import OpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import streamlit as st
from langchain.chat_models import ChatOpenAI



# Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, lets Chat !")

# This code will take the Key from env file but we dont need this while deploying 
from dotenv import load_dotenv 
load_dotenv()

chat = ChatOpenAI(temperature=0.5)

if 'flowmessage' not in st.session_state:
    st.session_state['flowmessage'] = [
        SystemMessage(content="You are a comedian AI system")
    ]

# funtion to load OpenAI model and get response 
def get_chat_resonse(question):
    st.session_state['flowmessage'].append(HumanMessage(content=question)) #asking question chatbot
    answer = chat(st.session_state['flowmessage']) # gettig resposne from chatbot 
    st.session_state['flowmessage'].append(AIMessage(content=answer.content)) #storing the ans to use it latter in the conversation
    # so the same thing thing the store ans we will return answer.content 
    return answer.content

input = st.text_input("Input : ", key = "input")
response = get_chat_resonse(input)

submit  = st.button("Ask me a question")

# if button is clicked 
if submit:
    st.subheader("The response is :")
    st.write(response)