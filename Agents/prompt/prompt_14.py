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
        Example : 
        Q : 2 pack of pencils, 3 pack of erasers, and each pack has 5 units , total how many units?
        A : Respond in json only
            "number_of_units_in_a_packs" : 5,
            "pack_of_pencils" : 2,
            "pack_of_erasers" : 3,
            "total_units" : 25
            

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