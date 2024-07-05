import os
import pathlib
import textwrap
import streamlit as st
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv


## take environment variables from .env.
load_dotenv() 

## Configure the gemini api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# initializ the model
model = genai.GenerativeModel("gemini-pro-vision")

# function to load GeminiPro model and its responses
def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

## Iitialize the streamlit app
st.set_page_config(page_title="Gemini Q&A with Image")
st.header("Gemini Q&A Application")
input = st.text_input("Ask the question: ",key="input")
uploaded_file = st.file_uploader("Choose an image..", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me more insights about the image")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The answer is")
    st.write(response)