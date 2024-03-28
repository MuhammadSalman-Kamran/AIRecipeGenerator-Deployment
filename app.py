from setup import *
import os
import streamlit as st
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

client = setup_openai()


st.title('AI Recipe Generator')
recipe = st.text_input('Enter your Dish', value= 'Chicken Biryani')
button = st.button('Create Recipe')




output_format = """
                Fun Title of the Recipe and title should be big and bold

                Table Of Contents:

                Links to the different sections of the recipe content.
                Introduction:

                Briefly introduce the dish.
                Ingredients:

                List of ingredients needed for the recipe.
                Cooking Steps:

                Detailed instructions on how to prepare the dish.
                FAQ:

                Answers to frequently asked questions related to the recipe.
                Headings should be bold like html h1 tag and headings font should be greater than 50
                """

prompt =    f"Create a detailed cooking recipe for a dish named {recipe}." \
            f" Include preparation steps and cooking tips." \
            f" Follow the following output format {output_format}"




if button:
    with st.spinner('Generating Recipe ...'):
        generated_text = text_generation(client, prompt, html = True)
        st.write(generated_text)
        with st.spinner('Generating image...'):
            image = generate_image_openai(client, recipe)
            st.image(image, caption=recipe, use_column_width=True)