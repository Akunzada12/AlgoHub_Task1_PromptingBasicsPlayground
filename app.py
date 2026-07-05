import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Prompting Basics Playground")

prompt = st.text_area("Enter your prompt")

if st.button("Generate Response"):
    if prompt:
        response = model.generate_content(prompt)
        st.write(response.text)
    else:
        st.warning("Please enter a prompt")