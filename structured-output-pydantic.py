from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Optional

model = ChatOpenAI(model="gpt-4o", temperature=0)

class President(BaseModel):
    """Details about the president"""
    name: str = Field(..., description="The name of the president.")
    country: str = Field(..., description="The country of the president.")
    age: Optional[int] = Field(
        None, description="The age of the president. Optional."
    )

structured_llm = model.with_structured_output(President)
response = structured_llm.invoke("Who is the president of the United States?")

print(response)