import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Apa itu token?
# Token adalah satuan terkecil yang diproses oleh AI
# 1 token = 1 kata, 1/2 kata, 1 karakter bergantung bahasa yang digunakan

# 750 kata = 1000 token Bahasa Inggris

def main():
    prompt = "Jelaskan AI dalam satu kalimat"

    token_count = client.models.count_tokens(
        model=os.getenv("GEMINI_MODEL"), # gemini-3-flash-preview / gemini-3.5-flash
        contents=prompt,
    )

    print(f"Estimasi token: {token_count.total_tokens}")
    print("-" * 50)

    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"), contents=prompt,
    )

    # response.text -> response.usage_metadata
    print(f"Response: {response.text}")
    print(f"Token input: {response.usage_metadata.prompt_token_count}") # Token input sesuai dengan token yang diestimasi penggunaanya
    print(f"Token output: {response.usage_metadata.candidates_token_count}") # Token output merupakan token yang AI gunakan untuk memberikan jawaban
    print(f"Token total: {response.usage_metadata.total_token_count}") # Token total merupakan penjumlahan token input, token output, dan juga sistem instruction atau case historynya
    print(f"Finish reason: {response.candidates[0].finish_reason}") # finish reason yang menandai kenapa AI berhenti memberikan jawaban. Finish reason STOP merupakan finish reason yang normal
    # MAX_TOKENS -> AI berhenti memberikan jawaban karena token maksimum
    # SAFETY -> AI berhenti memberikan jawaban karena prompt atau hasil kemungkinan melanggar aturan keamanan

main()

# Cara debugging
# cd intermediate
# uv run 10_metadata.py