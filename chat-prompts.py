from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o")

prompts = [
    ("system", "Reply every prompt in {language}"),
    ("user", "Who is the president of {country}")
]

myPrompt = ChatPromptTemplate.from_messages(prompts)
chatPrompt = myPrompt.invoke({"language": "Spanish", "country": "USA"})
response = model.invoke(chatPrompt)

print(response.content)