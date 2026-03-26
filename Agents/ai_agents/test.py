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
    ("user", "Evaluate the following: '2+2' is {res}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser
city_by_user = input("Enter a city name: ")

try : 
    result_refined = chain.invoke({"res": city_by_user}).lower().strip()
    print(result_refined)
except : 
    result_refined = "bad"

if "good" or "correct" or "right" in result_refined :
    decision = "good"
else :
    decision = "bad"

print(decision)