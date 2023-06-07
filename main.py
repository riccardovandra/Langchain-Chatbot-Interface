import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
# Import Schemas
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

def init():
    load_dotenv()

    st.set_page_config(
        page_title="Your Own ChatGPT 🦾",
        page_icon="🤖"
    )


def main():
    init()

    #Initialize Chat
    chat = ChatOpenAI(temperature=0)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]
    

    st.header("Your own ChatGPT 🤖")

    with st.sidebar:
        user_input = st.text_input("Your Message", key="user_input")
    
    if user_input: #If the user input has been used
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("Thinking"):
            response = chat(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))
    
    messages = st.session_state.get('messages', [])
    for i,msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content,is_user=False, key=str(i) + '_ai') 

# This is just a safety measure
if __name__ == '__main__':
    main()