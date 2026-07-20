model_name: str = "gemini-3.5-flash" # value dengan tipe data string
max_tokens: int = 1_500 # tipe data number -> integer dengan value = 1500
temperature: float = 0.5 # tipe data number -> float (bisa menerima angka desimal)
streaming: bool = True # tipe data boolean dengan value True atau False

print(model_name)
print(max_tokens)
print(temperature)
print(streaming)

# Cara debugging
# cd basic
# uv run 1_variable_types.py