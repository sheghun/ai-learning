from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o")
prompt1 = PromptTemplate(template="What is the capital of France?")

# Recommended
prompt2 = PromptTemplate.from_template("Who is the president of {country}")

# dictionary for invoke
print(prompt2.invoke({"country": "India"}))
# Positional arguments for format
print(prompt2.format(country="India"))

response = model.invoke(prompt2.invoke({"country": "India"}))
print(response.content)
