# Tipe data list
models: list[str] = [
    "gemini-3.5-flash", # index ke 0
    "gemini-3.5-pro", # index ke 1
    "gemini-nano-banana", # index ke 2
    "gemini-veo", # index ke 3
]

# Mengambil item dari list
print(models[3])

# Menghitung panjang ukuran list
print(len(models))

# looping value dari list
for model in models:
    print(model)

#Tipe data dictionary
message: dict = {
    "role": "user", # value dengan tipe data string
    "content": "Jelaskan AI dalam satu kalimat", # value dengan tipe data string
    "tokens_used": 50, # value dengan tipe data integer
}

print(message["role"])

# Cara debugging
# cd basic
# uv run 2_list_dictionary.py