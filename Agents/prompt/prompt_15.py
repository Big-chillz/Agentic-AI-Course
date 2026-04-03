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
        "role" : "user",
        "content" : """
        Task : 
        Find all combinations

        Instructions : 
        - step 1 : Count total number or packs
        - step 2 : Count total number of pencils
        - step 3 : Count total number of erasers
        - step 4 : Calculate total units

        Example 1 : 
        Q : 2 pack of pencils, 3 pack of erasers, and each pack has 5 units , total how many units?
        A : 
        step 1 : 
        
            "number of units in a packs" : 5,
            "pack of pencils" : 2,
            "pack of erasers" : 3
            "total units" = (2+3) * 5 = 15

        A store sells 8 packs of seeds and 4 packs of fruits , each pack has 11 units , total how many units do we have?

        RESPOND IN JSON FORMAT ONLY
        """
    }
]

prompt = ChatPromptTemplate.from_messages(messages)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

result = chain.invoke({})
print(result)