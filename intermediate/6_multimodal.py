import os
from google import genai
from dotenv import load_dotenv

from pathlib import Path

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def image_generation():
    prompt = input("Prompt image generation: \n")

    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL_IMAGE"), contents=[prompt], # Paid API
    )

    file_name = "generated.jpeg"
    directory = "multimodal"

    file_path = Path(directory)
    file_path.mkdir(exist_ok=True)

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image.save(f"{directory}/{file_name}")

    print("Image successfully generated!")

def main():
    image_generation()

main()

# Cara debugging
# cd intermediate
# uv run 6_multimodal.py