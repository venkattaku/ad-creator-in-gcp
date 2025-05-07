from fastapi import FastAPI, File, UploadFile
from app.ocr import extract_text

app = FastAPI()

@app.post("/extract-text/")
async def extract_text_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    text = extract_text(image_bytes)
    return {"extracted_text": text}
