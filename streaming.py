from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o")
streamed_response = model.stream("Tell me about the NBA")

for chunk in streamed_response:
    print(chunk.content, end="|", flush=True)