import pytesseract
from pytesseract import Output
from PIL import Image
import io


def extract_text(image_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(image_bytes))
    data = pytesseract.image_to_data(image, output_type=Output.DICT)
    ocr_texts = []
    for i in range(len(data['text'])):
        if data['text'][i].strip():
            ocr_texts.append({
                'text': data['text'][i],
                'box': {"left": data['left'][i], "top": data['top'][i],
                        "width": data['width'][i], "height": data['height'][i]},
            })
    return ocr_texts
