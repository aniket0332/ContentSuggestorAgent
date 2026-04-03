from google import genai
from PIL import Image
from app.prompts import PROMPT
from app.utils.parser import extract_json
import requests
import io
import os

# print(os.getenv("GEMINI_API_KEY"))
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def process_image_urls(image_urls):
    images = []

    for url in image_urls:
        response = requests.get(url)
        img = Image.open(io.BytesIO(response.content))
        images.append(img)

    gemini_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[PROMPT] + images
    )

    raw_text = gemini_response.text

    parsed = extract_json(raw_text)

    if not parsed:
        return {
            "status": "error",
            "message": "Failed to parse AI response",
            "raw": raw_text
        }

    return parsed