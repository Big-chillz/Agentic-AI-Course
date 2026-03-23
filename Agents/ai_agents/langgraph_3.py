from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import ArxivLoader
from langchain_community.vectorstores import FAISS
from langchain_chroma import Chroma

from langgraph.graph import StateGraph, END
from typing import TypedDict, List

"""

example : diff between similarity and semantic search
vect1 = [0.864, 0.235, -0.741] -> cat
vect2 = [0.874, 0.245, -0.751] -> iphone
vect 3 = [0.654, -0.425, 0.187] -> dog

simialrity_Search(ip = vect1, db = vect2 + vect3) -> vect2 = iphone
semantic_Search(ip = vect1, db = vect2 + vect3) -> vect3 = dog
"""

# llm initiation or setup

api_key = "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"
llm = ChatOpenAI(
    model = "nvidia/nemotron-3-super-120b-a12b:free",
    openai_api_key = api_key,
    openai_api_base = "https://openrouter.ai/api/v1",
)

# paper loader from arxiv
paper_id = "1706.03762"

loader = ArxivLoader(query = paper_id,load_max_docs = 1)

data = loader.load()

# splitting text
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
docs = text_splitter.split_documents(data)

#embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


# vector db : paper knowledge
vector_db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory = "./paper_db"
) # vector_db = Chroma.from_documents(input_docs,output_vectors,.,...,loc_Space)

retriever = vector_db.as_retriever(search_kwargs={"k": 3})
# Long Term memory
memory_db = Chroma(
    persist_directory = "./memory_db",
    embedding_function = embeddings
)

# prompt template
template = """
You are a research agent

Use the following informations

Chat History : 
{chat_history}

Context : 
{context}

Memory : 
{memory}

Question : 
{question}


If the answer is not in context or memory , say you dont know
"""

rag_prompt = ChatPromptTemplate.from_template(template)

# Graphs
class GraphState(TypedDict): #{question : str , context : list ....} -> Graphstate["context"] -> helps us retrieve whatever is ther in context
    question: str
    context: list
    answer: str
    chat_history : List[str]

# Router Function

def router(state: GraphState):
    print("\ninside router \n")
    question = state["question"]

    router_prompt = f"""
Decide whether the question requires document retirval.

Respond only and only with one word : 
- "retrieve" - if question requires information about research paper or external knowledge
- "direct" - if questions can be answered without retrival

Question : {question}
"""
    # if its casual, generic or conversative

    decision = llm.invoke(router_prompt).content.strip().lower()


    if decision == "retrieve" : 
        return "retrieve"
    return "direct"

# retrieve node

def retrieve(state: GraphState):
    print("retrieve node")

    question = state["question"]
    paper_docs = retriever.invoke(question)
    paper_context = "\n\n".join([d.page_content for d in paper_docs])

    memory_docs = memory_db.similarity_search(question, k = 2)
    memory_context = "\n\n".join([d.page_content for d in memory_docs])

    combined_context = f"""
 - paper context -
{paper_context}
- memory context
{memory_context}
"""
    return {"context" : combined_context}


def generate(state: GraphState):
    print("inside generate node")

    question = state["question"]
    context = state.get("context","")
    history = state.get("chat_history",[])

    history_text = "\n".join(history)

    # retrieve memory again but this time for the prompt 
    memory_docs = memory_db.similarity_search(question,k=2)
    memory_text = "\n".join([d.page_content for d in memory_docs])

    prompt = rag_prompt.format(
        context = context,
        question = question,
        chat_history = history_text,
        memory = memory_text
    )

    response = llm.invoke(prompt)
    answer = response.content

    # updating our chat_history
    updated_history = history + [
        f"User : {question}",
        f"Assitant : {answer}"
    ]

    memory_db.add_texts([
        f"Q: {question} \n A: {answer}"
    ])

    return {
        "answer" : answer,
        "chat_history": updated_history
    }

def direct_answer(state : GraphState):
    print("--Direct Answer Node")

    question = state["question"]
    history = state.get("chat_history",[])

    history_text = "\n".join(history)

    prompt = (
        f"""

        Question : 
        {question}

        Chat History :
        {history}
        """
    )

    response = llm.invoke(prompt)
    answer = response.content

    updated_history = history + [
        f"User : {question}",
        f"Assistant : {answer}"
    ]

    # store in memory
    memory_db.add_texts([
        f"Q: {question} \n A : {answer}"
    ])

    return {
        "answer" : answer,
        "chat_history" : updated_history
    }

graph = StateGraph(GraphState)
graph.add_node("retrieve",retrieve)
graph.add_node("generate",generate)
graph.add_node("direct",direct_answer)

graph.add_edge("retrieve","generate")
graph.add_edge("generate",END)
graph.add_edge("direct",END)

graph.set_conditional_entry_point(
    router,
    {
        "retrieve":"retrieve",
        "direct":"direct"
    }
)

app = graph.compile()


state = {
    "chat_history" : []
}

while True : 
    user_question = input("\n Ask a Question or type 'exit' to quit : ")
    if user_question.lower() == "exit":
        break

    result = app.invoke({
        "question" : user_question,
        "chat_history" : state["chat_history"]
    })

    print("\n answer : \n")
    print(result["answer"])

    state["chat_history"] = result["chat_history"]


