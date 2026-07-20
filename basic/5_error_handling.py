import random

class LLMUnavailableException(Exception):
    pass

def call_llm(prompt: str, retries: int = 3):
    # raise ValueError("Terjadi kesalahan pada function call_llm")
    for attempt in range(retries):
        try:
            # simulasi api yang 'lambat' / flaky
            flaky_number: float = random.random()
            print(f"flaky_number: {flaky_number}")

            if flaky_number < 0.6:
                raise TimeoutError("API timed out")
            return f"Response to: {prompt}"
        except TimeoutError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == retries - 1:
                raise LLMUnavailableException(f"All {retries} attempts exhausted") from e


try: # 'ruang' untuk mengeksekusi function atau logika program
    result: str = call_llm(prompt="Jelaskan apa itu AI dalam satu kalimat")
    print(f"sukses: {result}")
except Exception as e:
    # 'ruang' untuk mengendalikan kesalahan
    print(f"gagal akses call_llm {e}")
finally:
    # opsional
    # 'ruang' yang akan selalu di eksekusi apapun hasilnya
    print("sesi berakhir")

# Cara debugging
# cd basic
# uv run 5_error_handling.py

