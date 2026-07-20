import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def main():
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"),
        contents="Jelaskan apa itu AI dalam satu kalimat",
    )

    print(response.text)

main()

# Cara debugging
# cd intermediate
# uv run 2_setup_gemini.py