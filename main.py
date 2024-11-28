import google.generativeai as genai
import os
import streamlit as st

os.environ["GEMINI_API_KEY"] = 'AIzaSyB-9yzXgnP6_DKgue2UUQ8pebQQA9ZN_ms'

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

st.title("Healthcare Chatbot")
st.write("Enter your symptoms, and the chatbot will provide information. Type 'bye' to exit.")

user_input = st.text_input("Enter your symptoms:")

if user_input.lower() == "bye":
    st.write("Goodbye!")
else:
    if user_input:
        response = model.generate_content(user_input)
        st.write(response.text)
