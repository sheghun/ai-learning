from langchain_openai import ChatOpenAI
from langchain_core.globals import set_llm_cache
from langchain_community.cache import SQLiteCache

set_llm_cache(SQLiteCache(database_path="sqlite.db"))


model = ChatOpenAI(model="gpt-4o")

prompt = "Who is the president of Spain"

response1 = model.invoke(prompt)
print(response1.content)
response2 = model.invoke(prompt)
print(response2.content)