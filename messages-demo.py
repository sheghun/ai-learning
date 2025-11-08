from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatOpenAI(model="gpt-4o")

systemInstruction = SystemMessage(content="Reply every prompt in French")
userMessage = HumanMessage(content="Who is the president of the United States?")

response = model.invoke([systemInstruction, userMessage])

print(response.content)
