from langchain_huggingface import HuggingFaceEmbeddings
from typing import TypedDict, List

class GraphState(TypedDict):
    question: str
    context: list
    answer: str
    chat_history : List[str]