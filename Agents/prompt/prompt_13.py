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
        - step 1 : List possible counts of pencils and erasers
        - step 2 : Calculate or sum the total units available of both
        - step 3 : Provide all possible permutaions

        Question : 
        A store sells 5 packs of Eraser and 7 packs of pencil , each pack has 5 units , total how many units do we have?

        What combinations are possible?
        """
    }
]

prompt = ChatPromptTemplate.from_messages(messages)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

result = chain.invoke({})
print(result)