from dotenv import load_dotenv
from openai import OpenAI
from PIL import Image
from io import BytesIO
import os
import requests

def setup_openai():
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    return client

def generate_image_openai(client, prompt, model = "dall-e-2", size = "1024x1024", n= 1):
    response = client.images.generate(
    model=model,
    prompt=prompt,
    size=size,
    n=n,
    )
    image_url = response.data[0].url
    image = requests.get(image_url)
    image = Image.open(BytesIO(image.content))
    return image

def text_generation(client, prompt, text_area_placeholder = None, html = True):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a World best Chef."},
            {"role": "user", "content": prompt}
        ],
        frequency_penalty=0,
        presence_penalty=0,
        max_tokens=3000, 
        top_p=1,
        temperature=0.5,
        )
    return completion.choices[0].message.content
