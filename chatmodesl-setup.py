from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4")

response = model.invoke("who is the president of france?")
print(response.content)