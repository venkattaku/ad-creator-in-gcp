from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_proxiedheadersmiddleware import ProxiedHeadersMiddleware
import json
import base64

from app.ocr import extract_text
from app.replace_text import replace_text

app = FastAPI()

app.add_middleware(ProxiedHeadersMiddleware)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/extract-text/")
async def extract_text_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    ocr_texts = extract_text(image_bytes)
    return {"extracted_text": ocr_texts}


@app.post("/replace-image-text/")
async def replace_image_text(file: UploadFile = File(...), replacements: str = Form(...)):
    image_bytes = await file.read()
    replacements = json.loads(replacements)
    
    # Process the image and apply replacements
    processed_image_bytes = replace_text(image_bytes, replacements)

    # Encode the processed image as Base64
    encoded_image = base64.b64encode(processed_image_bytes).decode("utf-8")

    # Return the Base64-encoded image
    return {"image_after_replacements": f"data:image/png;base64,{encoded_image}"}
