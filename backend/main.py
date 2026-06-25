from fastapi import FastAPI
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/chat/{item_id}")
def read_chat(item_id: str):
    return {"item_id": item_id}


@app.post("/chat/{chat_data}")
def create_chat(chat_data: str):

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=chat_data
    )

    return {"response": response.text}