import os
import asyncio
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

async def generate_content_stream(prompt: str):
    response = client.models.generate_content_stream(
        model=os.getenv("GEMINI_MODEL"), contents=[prompt],
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(include_thoughts=True)
        )
    )

    for chunk in response:
        for part in chunk.candidates[0].content.parts:
            await asyncio.sleep(1)
            if not part.text:
                continue
            elif part.thought:
                yield (True, part.text) # text untuk proses berpikir
            else:
                yield (False, part.text) # hasil akhir

async def collect_stream(prompt: str):
    result = generate_content_stream(prompt)

    async for chunk in result:
        isThinking, text = chunk
        if isThinking:
            print("Berpikir ... ")
            print(text)
        else:
            print(text)

def main():
    prompt = input("Prompt streaming: \n")
    asyncio.run(collect_stream(prompt))

main()

# Cara debugging
# cd intermediate
# uv run 7_streaming.py