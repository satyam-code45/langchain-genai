from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
import os

load_dotenv()

model = ChatOpenAI(model='gpt-4')

st.header('Player Comparison with Rohit Sharma')

player_input = st.selectbox("Select Player Name",["Virat Kohli", "Ms Dhoni", "Abhishek Sharma", "Sachin Tendulkar"])

format_input = st.selectbox("Select Format to Compare", ["ODI+TEST+T20", "ODI", "TEST", "T20", "ODI+T20", "ODI+TEST", "TEST+T20"])

compare_input = st.selectbox("What to compare ", ["Batting","Bowling","Captiancy", "Batting+Captaincy"])

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, "template.json")

template = load_prompt(TEMPLATE_PATH)

if st.button('Compare'):
    chain = template | model
    result  = chain.invoke({
        'player_input': player_input,
        'format_input': format_input,
        'compare_input': compare_input
    })
    st.text(result.content)