# Tambah package pydantic
# uv add pydantic

from pydantic import BaseModel

class ChatMessage(BaseModel):
    role: str
    content: str
    tokens_used: int

class LLMResponse(BaseModel):
    message: ChatMessage # nested inheritance

# simulasi data mentah "raw" dari LLM Provider
raw = {
    "message": {
        "role": "user",
        "content": "Jelaskan AI dalam satu kalimat",
        "tokens_used": 50,
    }
}

result = LLMResponse.model_validate(raw)
print(result.message.content)

# belum aman apabila di sertakan pada logika program di Python
# belum tentu bisa di proses?
# belum bisa di pastikan tipe data yang tepat

# Cara debugging
# cd basic
# uv run 7_data_modelling.py