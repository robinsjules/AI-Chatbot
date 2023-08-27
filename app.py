import os
import constants 

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = constants.APIKEY

st.title('SMU Libraries GPT')
prompt = st.text_input('Prompt away!')

llm = OpenAI(temperature=0.4)

if prompt:
    response = llm(prompt)
    st.write(response)