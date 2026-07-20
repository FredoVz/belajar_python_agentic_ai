import asyncio

async def query_model(model: str, prompt: str) -> dict:
    # simulasi keterlambatan "latensi"
    start = asyncio.get_event_loop().time()
    delay = {"gemini-flash": 0.4, "gpt": 0.8, "claude-haiku": 0.6}

    delay_model = delay[model]
    await asyncio.sleep(delay_model)

    elapsed = asyncio.get_event_loop().time() - start

    latency_ms = round(elapsed * 1000)

    return {"model": model, "response": prompt, "latency_ms": latency_ms}
    
result = asyncio.run(query_model("claude-haiku", "Jelaskan apa itu AI dalam satu kalimat"))
print(result)

# Cara debugging
# cd basic
# uv run 6_async_await.py