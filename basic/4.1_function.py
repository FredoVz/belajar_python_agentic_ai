# prompt: str
# model: str
# max_tokens: int

# menghitung biaya penggunaan token dari suatu model
# dictionary -> {}
# input_tokens: int
# output_tokens: int
# estimated_cost: float

def estimate_cost(prompt: str, model: str, max_tokens: int):
    # pass

    # "model": {"input": 0, "output": 0}
    pricing: dict = {"gemini-flash": {"input": 0.0015, "output": 0.0006}}

    rates: dict = pricing[model] # {"input": 0, "output": 0}
    input_tokens: int = len(prompt.split())

    input_cost = (input_tokens / 1000) * rates["input"]
    output_cost = (max_tokens / 1000) * rates["output"]

    estimated_cost = input_cost + output_cost

    return {
        "input_tokens": input_tokens, 
        "output_tokens": max_tokens, 
        "estimated_cost": round(estimated_cost, 5)
    }

# Cara 1
# result: dict = estimate_cost(
#     "Jelaskan tentang AI dalam satu kalimat", "gemini-flash", 512
# )

# Cara 2
result: dict = estimate_cost(
    prompt="Jelaskan tentang AI dalam satu kalimat", 
    model="gemini-flash", 
    max_tokens=512
)

print(result)

# Cara debugging
# cd basic
# uv run 4.1_function.py