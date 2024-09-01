<<<<<<< HEAD
from dotenv import load_dotenv

load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the "genai" library by providing API key
genai.configure(api_key=os.getenv("API_KEY"))

# Function to load Google Gemini 1.5 Flash model and get response
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize our Streamlit app
st.set_page_config(page_title="AI Doctor")

st.header("AI Doctor 👨‍⚕️")
uploaded_file = st.file_uploader("Choose an image..", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about my meal")

input_prompt = """
You are an expert nutritionist. Analyze the food items from the image
and calculate the total calories. Provide the details of every food item with calorie intake
in the following format:
1. Item 1 - number of calories
2. Item 2 - number of calories
----
----
After that, mention whether the meal is healthy or not and also provide the percentage split of
carbohydrates, proteins, fats, sugar, and calories in the meal.
Finally, give suggestions on which items should be removed and which items should be added to the meal
to make it healthy if it's unhealthy.
"""

# If submit button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data)
    st.subheader("The Response is")
    st.write(response)
=======
from dotenv import load_dotenv

load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the "genai" library by providing API key
genai.configure(api_key=os.getenv("API_KEY"))

# Function to load Google Gemini 1.5 Flash model and get response
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize our Streamlit app
st.set_page_config(page_title="AI Doctor")

st.header("AI Doctor 👨‍⚕️")
uploaded_file = st.file_uploader("Choose an image..", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about my meal")

input_prompt = """
You are an expert nutritionist. Analyze the food items from the image
and calculate the total calories. Provide the details of every food item with calorie intake
in the following format:
1. Item 1 - number of calories
2. Item 2 - number of calories
----
----
After that, mention whether the meal is healthy or not and also provide the percentage split of
carbohydrates, proteins, fats, sugar, and calories in the meal.
Finally, give suggestions on which items should be removed and which items should be added to the meal
to make it healthy if it's unhealthy.
"""

# If submit button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data)
    st.subheader("The Response is")
    st.write(response)
>>>>>>> fb018c0179f62e633ecd4b646f4ad4b5de1edc24
