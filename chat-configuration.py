from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", max_tokens=100)

response = model.invoke("Explain quantum physics")

