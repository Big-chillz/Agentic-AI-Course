from langchain_openai import ChatOpenAI # helps to connect to the LLM - important role as a wrapper around the model
from langchain_core.prompts import ChatPromptTemplate # helps to create prompts for the LLM
from langchain_core.output_parsers import StrOutputParser # helps to parse the output from the LLM and get cleaner output

api_key = "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"

llm = ChatOpenAI(
    model = "nvidia/nemotron-3-super-120b-a12b:free",
    openai_api_key = api_key,
    openai_api_base = "https://openrouter.ai/api/v1",
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Act as chef and give me the 5 best dishes from the {city}")
])

output_parser = StrOutputParser()


for i in range(3):
    print(f"attempt {i}")
    chain = prompt | llm | output_parser
    city_by_user = "Edinburg"
    result = chain.invoke({"city" : city_by_user})
    print(result)




"""
 4 important components of prompt : 
1. Task -  what to do
2. Context - what to use
3. Constraints - rules
4. Output Format -  how to respond
"""