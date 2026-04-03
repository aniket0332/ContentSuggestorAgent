from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from agent import process_image_urls
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
);

class ImageRequest(BaseModel):
    image_urls: List[str]

@app.post("/generate-post")
async def generate_post(request: ImageRequest):

    if len(request.image_urls) != 5:
        return {"error": "Please provide exactly 5 image URLs"}

    result = process_image_urls(request.image_urls)

    return result
