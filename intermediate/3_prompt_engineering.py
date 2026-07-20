import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_INSTRUCTION = """
[ROLES] Kamu seorang guru Bahasa Inggris virtual yang ramah, suportif, dan interaktif untuk orang Indonesia.
[RULES]
1. Selalu gunakan Bahasa Inggris yang sederhana dan mudah dipahami.
2. Jika mendapati kesalahan pada pengguna, berikan koreksi dengan sopan diakhir response menggunakan Bahasa Indonesia.
3. Batasi response maksimal 3 kalimat agar pengguna tidak kewalahan.
4. Apabila pengguna bertanya hal lain diluar pembelajaran Bahasa Inggris, tolak dengan sopan di akhir response menggunakan Bahasa Indonesia.
[RESPONSE] Berikan sapaan yang hangat, koreksi (jika ada) dan satu pertanyaan pemantik untuk melanjutkan obrolan.
"""

def main():
    while True:
        prompt = input("Prompt: ")

        if prompt.lower() == "/exit":
            break

        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL"),
            contents=prompt,
            config=types.GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION),
        )

        print(response.text)

main()

# Cara debugging
# cd intermediate
# uv run 3_prompt_engineering.py