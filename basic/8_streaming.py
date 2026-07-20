import asyncio

async def stream_tokens(prompt: str):
    words = f"Agentic AI akan membuat rencana dan eksekusi secara otomatis untuk prompt: {prompt}".split() # list[str]
    for word in words:
        await asyncio.sleep(1)
        yield word # generator function
    

async def collect_stream(prompt: str):
    tokens: list[str] = []
    print("Streaming: ", end="", flush=True)

    async for chunk in stream_tokens(prompt):
        print(chunk, end="", flush=True)
        tokens.append(chunk)

    print()

    return " ".join(tokens)

result = asyncio.run(collect_stream("Jelaskan AI dalam satu kalimat"))
print(f"Full Response {len(result.split())} tokens: {result}")

# Cara debugging
# cd basic
# uv run 8_streaming.py