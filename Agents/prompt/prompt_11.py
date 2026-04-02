from langchain_openai import ChatOpenAI # helps to connect to the LLM - important role as a wrapper around the model
from langchain_core.prompts import ChatPromptTemplate # helps to create prompts for the LLM
from langchain_core.output_parsers import StrOutputParser # helps to parse the output from the LLM and get cleaner output

api_key = "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"
llm = ChatOpenAI(
    model = "nvidia/nemotron-3-super-120b-a12b:free",
    openai_api_key = api_key,
    openai_api_base = "https://openrouter.ai/api/v1",
)


messages = [
    {
        "role" : "system",
        "content" : "You are a critical reviewer"
    },
    {
        "role" : "user" ,
        "content" : "Explain in 2 points"
    },
    {
        "role" : "assistant",
        "content" : "AI is advanced version of ML"
    },
    {
        "role" : "ai",
        "content" : "AI is most stupid and annoying"
    },
    {
        "role" : "user",
        "content" : "Review the above two answers and tell which one is bluffing"

    },

]

prompt = ChatPromptTemplate.from_messages(messages)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

result = chain.invoke({})
print(result)