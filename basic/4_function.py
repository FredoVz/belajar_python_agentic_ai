def print_message_hello():
    print("Halo ini function `my_function`")

def penambahan(a: int, b: int):
    result: int = a + b
    return result

# argument -> parameter
# proses -> logika, algoritma -> 1 tanggung jawab
# return value -> tipe data

result_penambahan: int = penambahan(5, 10)
print(result_penambahan)
print_message_hello()

# Cara debugging
# cd basic
# uv run 4_function.py