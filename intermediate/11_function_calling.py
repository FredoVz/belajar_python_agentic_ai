import os
import random

from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Dog string = Memberi tahu Gemini apa yang dilakukan oleh fungsi tersebut

# Membuat tugas atau latihan
# skill_type: reading, listening, writing, dan speaking
def generate_exercise(skill_type: str) -> str:
    """Menghasilkan soal dan latihan bahasa inggris. skill_type berupa: reading, listening, writing, dan speaking"""
    print(f"masuk generate_exercise: {skill_type}")
    exercise = {
        "reading": (
            "Baca paragraf berikut lalu jawab pertanyaannya:\n\n"
            '"Every morning, Sarah wakes up at 6 AM. She drinks a glass of water, '
            'does light stretching, and prepares breakfast before going to work."\n\n'
            "Pertanyaan: What does Sarah do first after waking up?"
        ),
        "listening": (
            "Latihan listening:\n\n"
            "Minta seseorang membacakan kalimat ini, lalu tulis apa yang kamu dengar:\n"
            '"The weather today is sunny with a light breeze. It is a perfect day for a walk in the park."'
        ),
        "writing": (
            "Latihan writing:\n\n"
            "Tulis 3 kalimat dalam Bahasa Inggris tentang rutinitas pagi kamu. "
            "Gunakan Simple Present Tense."
        ),
        "speaking": (
            "Latihan speaking:\n\n"
            "Ceritakan tentang hobi kamu dalam Bahasa Inggris selama 1 menit. "
            'Mulai dengan: "My favorite hobby is..."'
        ),
    }

    return exercise.get(
        skill_type, "Perkenalkan dirimu dengan Bahasa Inggris dalam 3 kalimat"
    ) # skill_type = reading

# Memeriksa tulisan (grammar)
def check_grammar(text: str):
    """Memeriksa grammar dan penulisan dari teks bahasa inggris yang dikirim pengguna"""
    print(f"masuk check_grammar: {text}")
    prompt = (
        f"Periksa grammar tulisan bahasa inggris berikut secara singkat."
        f"Berikan koreksi dan penjelasan dalam Bahasa Indonesia: {text}"
    )
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"), contents=prompt,
    )

    return response.text

# Memberikan tips belajar
def get_learning_tips():
    """Memberikan 1 tips berguna untuk belajar bahasa inggris"""
    print(f"masuk get_learning_tips")
    tips = [
        "Latihan berbicara 10 menit sehari lebih efektif daripada belajar 2 jam seminggu sekali.",
        "Tonton film atau series berbahasa Inggris dengan subtitle bahasa Inggris, bukan Indonesia.",
        "Catat 5 kata baru setiap hari dan coba gunakan masing-masing dalam satu kalimat.",
        "Jangan takut salah - kesalahan adalah bagian dari proses belajar yang paling berharga.",
        "Coba berpikir dalam Bahasa Inggris saat melakukan aktivitas sehari-hari"
    ]

    return random.choice(tips)

def main():

    print("English Tutor - Function Calling Demo")
    print("Coba ketik:")
    print(" - 'Buatkan soal reading' -> generate_exercise dipanggil")
    print(" - 'periksa: I goes to school' -> check_grammar dipanggil")
    print(" - 'kasih tips belajar' -> get_learning_tip dipanggil")
    print(" - atau ngobrol bebas")
    prompt = input("Prompt Kamu: ")

    # System Instruction = Memberi tahu Gemini kapan harus memanggil fungsi tersebut

    SYSTEM_INSTRUCTION = """
        [ROLE] Kamu seorang guru Bahasa inggris virtual yang ramah untuk orang Indonesia
        [RULES]
        - Panggil fungsi `generate_exercise` jika pengguna meminta soal atau latihan
        - Panggil fungsi `check_grammar` jika pengguna mengirim kalimat bahasa Inggris yang ingin diperiksa
        - Panggil fungsi `get_learning_tip` jika pengguna meminta tips atau saran belajar
        - Jika pengguna hanya mengobrol, jawab langsung tanpa memanggil fungsi apapun
        [RESPONSE] Berikan respons yang hangat, singkat, dan suportif
    """

    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"), 
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            tools=[generate_exercise, check_grammar, get_learning_tips],
        ),
        contents=prompt,
    )

    print(response.text)

main()

# Cara debugging
# cd intermediate
# uv run 11_function_calling.py