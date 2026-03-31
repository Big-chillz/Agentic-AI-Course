from langchain_openai import ChatOpenAI # helps to connect to the LLM - important role as a wrapper around the model
from langchain_core.prompts import ChatPromptTemplate # helps to create prompts for the LLM
from langchain_core.output_parsers import StrOutputParser # helps to parse the output from the LLM and get cleaner output

api_key = "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"

llm = ChatOpenAI(
    model = "nvidia/nemotron-3-super-120b-a12b:free",
    openai_api_key = api_key,
    openai_api_base = "https://openrouter.ai/api/v1",
)

CITY = "Edinburgh"
template = f"""
I need 5 most famous dishes from {CITY}
rules : 
- Should ne only vegan
- Should be healthy
- Should be local

Provide the result in the following format : 
Dish Name :
- why it is famous
- some history
- ingredients in it
"""
prompt = ChatPromptTemplate.from_template(template)

output_parser = StrOutputParser()


for i in range(2):
    print(f"attempt {i}")
    chain = prompt | llm | output_parser
    city_by_user = CITY
    result = chain.invoke({"city" : city_by_user})
    print(result)




"""
 4 important components of prompt : 
1. Task -  what to do
2. Context - what to use
3. Constraints - rules
4. Output Format -  how to respond
"""

# Extractor-> Analysis -> Final_Output