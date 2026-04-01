from langchain_openai import ChatOpenAI # helps to connect to the LLM - important role as a wrapper around the model
from langchain_core.prompts import ChatPromptTemplate # helps to create prompts for the LLM
from langchain_core.output_parsers import StrOutputParser # helps to parse the output from the LLM and get cleaner output

api_key = "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"

llm = ChatOpenAI(
    model = "nvidia/nemotron-3-super-120b-a12b:free",
    openai_api_key = api_key,
    openai_api_base = "https://openrouter.ai/api/v1",
    temperature = 1.5,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Comedian."),
    ("user", "Act as Comedian and give me the 5 best jokes for the {city}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser
city_by_user = "Delhi"
result = chain.invoke({"city": city_by_user})
print(result)

with open("temp_1.5_prompt_4.txt","a",encoding = "utf-8") as f:
    f.write(result)
