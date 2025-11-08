from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o")

prompts = [
    "Who is the president of the United States?",
    "What is the capital of United States?",
    "What is the most popular sport in the United States?"
]

batch_responses = model.batch(prompts)

for response in batch_responses:
    print(response.content)