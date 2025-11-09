from langchain_openai import ChatOpenAI
from langchain_community.callbacks.manager import  get_openai_callback

model = ChatOpenAI(model="gpt-4o")

with get_openai_callback() as cb:
    response = model.invoke("Describe the NFL")
    response2 = model.invoke("Describe the NBA")
    # cb will give the summarized breakdown of the tokens used
    print(cb.total_cost)