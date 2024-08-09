from PIL import Image
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import google.generativeai as genai
import streamlit as st

import os
Google_API_key = os.getenv("Google_API_key")
genai.configure(api_key=Google_API_key)


def extract_image(prompt, image):
    google_model = genai.GenerativeModel("gemini-1.5-flash")
    response = google_model.generate_content([prompt, image])
    result = response.text
    return result
def ask_gemini_model(input_text):
    gemini_ai_model = genai.GenerativeModel("gemini-pro")
    response  = gemini_ai_model.generate_content(input_text)
    return response
st.set_page_config(page_title="PrescriptiLens",
                   page_icon="🏥"
                )
st.title("🏥 PRESCRIPTILENS")

uploader = st.file_uploader(label="Upload Your Prescription", type=["jpg", "jpeg", "png"])
question = st.text_input(label="Ask Your Question")
if st.button("Result"):

    image = Image.open(uploader)
    response = extract_image(prompt="WHAT IS WRITTEN IN THE IMAGE",image=image)
    prescription = [response , question, "You are a Medical Professional Just Give Response To Medical Related Quesries Else say I don't Know"," Try To Give as much Detail response as you can and never give wrong response " ]
    output = " ".join(prescription)
    result = ask_gemini_model(output)
    st.markdown(result.parts[0].text)



