from fastapi import FastAPI, UploadFile, File

from src.services.AudioService import AudioService
from src.services.AssistantService import AssistantService
from src.services.OpenAiService import OpenAiService

app = FastAPI()


@app.get("/text/{prompt}")
async def text(prompt):
    return OpenAiService.text_from_prompt(prompt)


@app.get("/image/{prompt}")
async def image(prompt):
    return OpenAiService.image_from_prompt(prompt)


@app.post("/audio/")
async def audio(file: UploadFile = File(...)):
    return AudioService.text_from_audio(file)


@app.post("/assistant/")
async def assistant(file: UploadFile = File(...)):
    return AssistantService.response_from_audio(file)
