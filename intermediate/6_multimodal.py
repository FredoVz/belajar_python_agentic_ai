import os
import time
from google import genai
from google.genai import types
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

def image_understanding():
    with open("multimodal/sample-image.jpg", "rb") as f:
        image_bytes = f.read()

    prompt = input("Prompt image understanding: \n")

    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"), 
        contents=[
            prompt, 
            types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")
        ], # Paid API
    )

    print(response.text)

def video_generation():
    prompt = input("Prompt video generation: \n")

    operation = client.models.generate_videos(
        model=os.getenv("GEMINI_MODEL_VIDEO"), prompt=prompt, # Paid API
    )

    while not operation.done:
        print("Menunggu proses video generation selesai ... ")
        time.sleep(10)
        operation = client.operations.get(operation)

    generated_video = operation.response.generated_videos[0]
    client.files.download(file=generated_video)

    generated_video.video.save("multimodal/generated-video.mp4")
    print("Video berhasil di simpan ke multimodal/generated-video.mp4")

def video_understanding():
    prompt = input("Prompt video understanding: \n")
    file_video_path = "multimodal/sample-video.mp4"

    file_video = client.files.upload(file=file_video_path)

    while file_video.state.name == "PROCESSING":
        print("Video sedang diproses")
        time.sleep(5)
        file_video = client.files.get(name=file_video.name)

    if file_video.state.name == "FAILED":
        raise ValueError("Gagal upload video")
    
    print("Video berhasil di upload.")

    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"), 
        contents=[
            file_video, 
            prompt
        ],
    )

    print(response.text)

def main():
    # image_generation()
    # image_understanding()
    # video_generation()
    video_understanding()

main()

# Cara debugging
# cd intermediate
# uv run 6_multimodal.py