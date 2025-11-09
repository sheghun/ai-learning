from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0)

president_schema = {
    "name": "president_info_schema",
    "description": "Information about the president of a country.",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "The name of the president."
            },
            "country": {
                "type": "string",
                "description": "The country of the president."
            },
            "age": {
                "type": ["integer", "null"],
                "description": "The age of the president."
            }
        },
        "required": ["name", "country"]
    }
}

structured_llm = model.with_structured_output(president_schema)

response = structured_llm.invoke("Who is the president of the United States?")

print(response)