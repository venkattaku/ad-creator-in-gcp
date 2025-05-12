# import pytesseract
# from pytesseract import Output
from PIL import Image, ImageDraw
import io


def replace_text(image_bytes: bytes, replacements: list[dict]) -> bytes:
    image = Image.open(io.BytesIO(image_bytes))

    for replacement in replacements:
        if replacement["replacement"]:
            x, y, w, h = replacement["box"]['left'], replacement["box"][
                'top'], replacement["box"]['width'], replacement["box"]['height']
            draw = ImageDraw.Draw(image)
            draw.rectangle((x, y, x + w, y + h), fill="white")
            draw.text((x, y), replacement["replacement"], fill="black")
    output = io.BytesIO()
    image.save(output, format="PNG")
    return output.getvalue()
