import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

conversation_history: list[types.Content] = []

def save_message(role: str, message_text: str):
    conversation_history.append(
        types.Content(role=role, parts=[types.Part(text=message_text)])
    )

def load_history() -> list[types.Content]:
    return conversation_history

def main():
    while True:
        prompt = input("Kamu: ")

        if prompt.lower() == "/exit":
            break

        save_message(role="user", message_text=prompt)

        history = load_history()

        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL"), contents=history,
        )

        save_message(role="model", message_text=response.text)

        print(f"AI: {response.text}")

main()

# Cara debugging
# cd intermediate
# uv run 9_multiturn_chat.py