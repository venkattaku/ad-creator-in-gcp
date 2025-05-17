FROM python:3.11-slim

RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Set TESSDATA_PREFIX to the directory containing Tesseract language data
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers", "--forwarded-allow-ips", "*"]
