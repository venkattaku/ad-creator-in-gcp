from PIL import Image, ImageDraw
import io
from diffusers import StableDiffusionInpaintPipeline
import torch

# Load the Stable Diffusion inpainting pipeline
pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "runwayml/stable-diffusion-inpainting",
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16",
)
# pipe = pipe.to("cuda")  # Use GPU for faster processing
pipe = pipe.to("cpu")  # Fall back to CPU if GPU is not available

def replace_text(image_bytes: bytes, replacements: list[dict]) -> bytes:
    # Load the image
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # Create a mask for the regions to be replaced
    mask = Image.new("L", image.size, 0)  # Black mask (0 = no inpainting)
    draw = ImageDraw.Draw(mask)

    # Draw white rectangles (255 = inpainting) for each replacement region
    for replacement in replacements:
        if replacement["replacement"]:
            x, y, w, h = (
                replacement["box"]["left"],
                replacement["box"]["top"],
                replacement["box"]["width"],
                replacement["box"]["height"],
            )
            draw.rectangle((x, y, x + w, y + h), fill=255)

    # Generate the prompt for Stable Diffusion
    prompt = ". ".join(
        [
            f"Replace text at location ({r['box']['left']}, {r['box']['top']}, {r['box']['width']}, {r['box']['height']}) with '{r['replacement']}'"
            for r in replacements if r["replacement"]
        ]
    )

    # Use the Stable Diffusion pipeline to inpaint the image
    result = pipe(
        prompt=prompt,
        image=image,
        mask_image=mask,
        num_inference_steps=50,
    )

    # Get the inpainted image
    inpainted_image = result.images[0]

    # Save the inpainted image to bytes
    output = io.BytesIO()
    inpainted_image.save(output, format="PNG")
    return output.getvalue()
