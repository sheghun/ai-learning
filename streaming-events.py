from langchain_openai import ChatOpenAI
import asyncio

model = ChatOpenAI(model="gpt-4o")

async def stream_response_events():
    event_limit = 0
    prompt = "Describe the NBA"

    async for event in model.astream_events(prompt, version="v2"):
        event_limit += 1
        if event_limit >= 5:
            print("...Event Streaming done...")
            break

        print(event)

asyncio.run(stream_response_events())