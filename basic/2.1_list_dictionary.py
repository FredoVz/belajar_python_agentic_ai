# Variable conversation bertipe data list dan mempunyai value bertipe data dictionary untuk setiap item valuenya
conversations: list[dict] = []

conversations.append(
    {
        "role": "system",
        "content": "Kamu adalah seorang pengajar programming Python professional",
    }
)

conversations.append({"role": "user", "content": "Jelaskan tentang list pada Python"})

conversations.append(
    {
        "role": "assistant", 
        "content": "List adalah tipe data yang menampung sekumpulan value yang bertipe data sejenis"
    }
)

conversations.append(
    {"role": "user", "content": "Berikan saya contoh kode tentang list"}
)

for conversation in conversations:
    print(conversation)

user_messages = [
    message["content"] for message in conversations if message["role"] == "user"
]

print(user_messages)

# Cara debugging
# cd basic
# uv run 2.1_list_dictionary.py