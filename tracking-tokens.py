from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o")

response = model.invoke("Who is the president of the United States?")

# print(response.usage_metadata)
print(response.response_metadata["token_usage"])