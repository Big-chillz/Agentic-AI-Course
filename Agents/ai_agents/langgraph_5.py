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
    persist_directory = "./paper_db_3"
) # vector_db = Chroma.from_documents(input_docs,output_vectors,.,...,loc_Space)

retriever = vector_db.as_retriever(search_kwargs={"k": 3})
# Long Term memory
memory_db = Chroma(
    persist_directory = "./memory_db_3",
    embedding_function = embeddings
)

class GraphState(TypedDict) : 
    question : str
    plan : List[str]
    curent_step = int
    step_output : List[str]
    last_step_output : str
    context : str
    chat_history : List[str]
    retry_count : int
    max_steps : int
    answer : str

def planner(state:GraphState):
    print("In planner")
    if state.get("plan"):
        return {}
    
    prompt = f"""
Break this task into at most 5 clear steps

Return ONLY a numbered list. 

Task : 
{state["question"]}
"""
    response = llm.invoke(prompt).content
    steps = [s.strip() for s in response.split("\n") if s.strip()][:5]

    return {
        "plan" : steps,
        "current_step" : 0,
        "step_outputs" : [],
        "retry_counts": 0,
        "max_steps" : 5
    }

def check_status(state: GraphState):
    if state["current_step"] >= len(state["plan"]) : #if state["current_step"] >= state["max_steps"]
        return "done"
    
    if state["current_step"] >= state["max_steps"]:
        return "done"
    
    return "continue"

def retrieve(state: GraphState):
    print("in retreieve")
    
    if state["current_step"] >= len(state["plan"]):
        return {"context":""}
    
    print(f"\n--- Retrieve (step {state["current_step"]+1})")

    step = state["plan"][state["current_step"]]

    paper_docs = retrieve.invoke(step)
    paper_context = "\n".join([d.page_content for d in paper_docs])

    memory_docs = memory_db.similarity_search(step, k=2)
    memory_context = "\n".join([d.page_content for d in memory_docs])

    return{
        "context" : f"{paper_context}\n{memory_context}"
    }

def executor(state:GraphState):
    print("in execute")
    if state["current_step"] >= len(state["plan"]):
        return {"last_step_output" : "No more Steps"}
    
    print(f"\n - execute step {state["current_step"]+1}")

    step = state["plan"][state["current_step"]]
    context = state.get("context","")

    if not context.strip(): #context.strip() ==  None
        return {"last_Step_outputs" : "NO relevant context found"}
    
    prompt = f"""
Execute this step using the provided context. 

Step : 
{step}

Context : 
{context}

Return a precise and factual result
"""
    response = llm.invoke(prompt)

    return {
        "last_step_output" : response.content
    }        

def judge(state : GraphState) :
    print("In Judge Node")

    if state["current_step"] >= len(state["plan"]):
        return {"decision" : "good"}
    
    step = state["plan"][state["current_step"]]
    output = state.get("last_step_output","")


    prompt = f"""
Evaluate this output based on the step
Step : 
{step}

Output : 
{output}

Responde only: good or bad
"""
    try :
        decision_raw = llm.invoke(prompt).content.lower().strip()
    except : 
        decision_raw = "bad"

    decision = ""

    if  "good" in decision_raw :
        decision = "good"
    else : 
        decision = "bad"

    if state["current_step"] + 1 >= len(state["plan"]) : 
        return{
            "step_outputs" : state["step_outputs"] + [output],
            "current_step" : len(state["plan"]),
            "retry_count" : 0,
            "decision" : "good"
        }
    if decision == "good" :
        return {
            "step_outputs" : state["step_outputs"] + [output],
            "current_stop" : state["current_step"] + 1,
            "retry_count" : 0,
            "decision" : "good"
        }
    return{
        "retry_count" : state["retry_count"]+1,
        "decision" : "bad"
    }

def replan_step(state: GraphState):
    print("in replan step")
    if state["current_step"] >= len(state["plan"]):
        return {}
    
    failed_step = state["plan"][state["current_step"]]

    prompt = f"""
The following step has failed : 
{failed_step}

Rewrite this step better.

Return ONLY ONE improved step.
"""
    new_step = llm.invoke(prompt).content.strip()

    new_plan = state["plan"]
    new_plan[state["current_step"]] = new_step

    return {
        "plan" : new_plan,
        "retry_count" : 0
    }


