# Tambah package python-dotenv
# uv add python-dotenv
# uv add google-genai

import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

print(gemini_api_key)

# Cara debugging
# cd intermediate
# uv run 1_environment.py