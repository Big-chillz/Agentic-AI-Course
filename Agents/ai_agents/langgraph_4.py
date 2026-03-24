"""
User Input
   ↓
Planner Node
   ↓
Retrieve Node
   ↓
Executor Node
   ↓
[Condition Check]
   ├── If more steps → back to Retrieve
   └── If done → Final Node
   ↓
Final Answer
   ↓
Memory Storage
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import ArxivLoader
from langchain_community.vectorstores import FAISS
from langchain_chroma import Chroma

from langgraph.graph import StateGraph, END
from typing import TypedDict, List


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
    persist_directory = "./paper_db_2"
) # vector_db = Chroma.from_documents(input_docs,output_vectors,.,...,loc_Space)

retriever = vector_db.as_retriever(search_kwargs={"k": 3})
# Long Term memory
memory_db = Chroma(
    persist_directory = "./memory_db_2",
    embedding_function = embeddings
)

# Graph State
class GraphState(TypedDict):
    question : str
    plan: List[str]
    current_step : int
    step_outputs : List[str]
    answer : str
    context : str
    chat_history : List[str]

def planner(state: GraphState):
    print ("IN planner node")
    question = state["question"]
    prompt = f"""
Break the following task into a clear, ordered list of steps.ChatPromptTemplate

Return ONLY a numbered list. 

Task : 
{question}
"""
    
    response = llm.invoke(prompt).content

    steps = [
        step.strip()
        for step in response.split("\n")
        if step.strip()
    ]

    return {
        "plan" : steps,
        "current_step" : 0,
        "step_output": []
    }


def retrieve(state: GraphState):
    print("IN retrieve node")

    step = state["plan"][state["current_step"]]

    paper_docs = retriever.invoke(step)
    paper_context = "\n".join([d.page_content for d in paper_docs])

    memory_docs = memory_db.similarity_search(step, k=2)
    memory_context = "\n".join([d.memory_content for d in memory_docs])

    combined_context = f"""
-- Paper Context --
{paper_context}

-- memory context --
{memory_context}
"""
    return {"context" : combined_context}


def executor(state : GraphState):
    print("IN executor node\n")
    print(f"--State {state["current_step"]+1}--")
    step = state["plan"][state["current_step"]]
    context = state.get("context","")
    history = state.get("chat_history",[])

    history_text = "\n".join(history)

    prompt = f"""

    You are executing ONE step of a larger plan.
Step : 
{step}

Context : 
{context}

Chat History : 
{history_text}

Give a clear and concise result for THIS step only. 
"""
    response = llm.invoke(prompt)
    result = response.content

    updated_outputs = state["step_outputs"]+[result]

    return {
        "step_outputs" : updated_outputs,
        "current_step" : state["current_steps"]+1
    }

def should_continue(state: GraphState):
    if state["current_step"] < len(state["plan"]):
        return "continue" 
    return "end"

def final_answer(state: GraphState):
    print("- in Final answer node")
    question = state["question"]
    outputs = "\n".join(state["step_outputs"])
    history = state.get("chat_history",[])

    history_text = "\n".join(history)

    prompt = f"""
You are a research assistant. 

User Question : 
{question}

Step-by-Step findings : 
{outputs}

Chat History : 
{history_text}

Combine Everything into a final, well structured answer. 
"""
    response = llm.invoke(prompt)
    answer = response.content

    updated_history = history + [
        f"User: {question}",
        f"Assistant : {answer}"
    ]
    
    memory_db.add_texts([
        f"Q:{question} \n A: {answer}"
    ])

    return {
        "answer" : answer,
        "chat_history" : updated_history
    }


# Build graph

graph = StateGraph(GraphState)

graph.add_node("planner",planner)
graph.add_node("retrieve",retrieve)
graph.add_node("executor",executor)
graph.add_node("final",final_answer)

graph.set_entry_point("planner")

graph.add_edge("planner","retrieve")
graph.add_edge("retrieve","executor")

graph.add_conditional_edges(
    "executor",
    should_continue,
    {
        "continue" : "retrieve",
        "end" : "final"

    }
)

graph.add_edge("final",END)

app = graph.compile()

state = {
    "chat_history" : []
}

while True : 
    user_question = input("\n Ask a question (type 'exit' to quit):")
    if user_question.lower() == "exit" : 
        break

    result = app.invoke({
        "question" : user_question,
        "chat_history" : state["chat_history"]
    })

    print("\nFinal Answer : \n")
    print(result["answer"])

    state["chat_history"] = result["chat_history"]