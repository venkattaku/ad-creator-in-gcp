from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_proxiedheadersmiddleware import ProxiedHeadersMiddleware

from app.ocr import extract_text

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
    text = extract_text(image_bytes)
    return {"extracted_text": text}
