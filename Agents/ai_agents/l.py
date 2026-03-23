

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import ArxivLoader
from langchain_community.vectorstores import FAISS
from langchain_chroma import Chroma




from langgraph.graph import StateGraph, END
from typing import TypedDict, List








# =========================
# 1. LLM Setup
# =========================




api_key = "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"




llm = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1",
)








# =========================
# 2. Load Paper from Arxiv
# =========================




paper_id = "1706.03762"




loader = ArxivLoader(query=paper_id, load_max_docs=1)
data = loader.load()








# =========================
# 3. Split Text
# =========================




text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)




docs = text_splitter.split_documents(data)








# =========================
# 4. Embeddings
# =========================




embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)








# =========================
# 5. Vector DB (Paper Knowledge)
# =========================




vector_db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="./paper_db"
)




retriever = vector_db.as_retriever(search_kwargs={"k": 3})








# =========================
# 6. Memory DB (Long-Term Memory)
# =========================




memory_db = Chroma(
    persist_directory="./memory_db",
    embedding_function=embeddings
)








# =========================
# 7. Prompt Template
# =========================




template = """
You are a research assistant.




Use the following information carefully.




If the answer is not in the context, say you don't know.




Chat History:
{chat_history}




Memory:
{memory}




Context:
{context}




Question:
{question}
"""




rag_prompt = ChatPromptTemplate.from_template(template)








# =========================
# 8. Graph State
# =========================




class GraphState(TypedDict):
    question: str
    context: str
    answer: str
    chat_history: List[str]








# =========================
# 9. Router Function
# =========================




def router(state: GraphState):




    print("\n--- Router Node ---")




    question = state["question"]




    router_prompt = f"""
Decide whether the question needs document retrieval.


Respond with ONLY one word:
- "retrieve" → if question is about the research paper or needs external knowledge
- "direct" → if it's casual, general, or conversational


Question: {question}
"""




    decision = llm.invoke(router_prompt).content.strip().lower()




    if decision == "retrieve":
        return "retrieve"




    return "direct"








# =========================
# 10. Retrieve Node
# =========================




def retrieve(state: GraphState):




    print("\n--- Retrieve Node ---")




    question = state["question"]




    # Paper retrieval
    paper_docs = retriever.invoke(question)
    paper_context = "\n\n".join([d.page_content for d in paper_docs])




    # Memory retrieval
    memory_docs = memory_db.similarity_search(question, k=2)
    memory_context = "\n\n".join([d.page_content for d in memory_docs])




    combined_context = f"""
=== Paper Context ===
{paper_context}




=== Memory Context ===
{memory_context}
"""




    return {"context": combined_context}








# =========================
# 11. Generate Node
# =========================




def generate(state: GraphState):




    print("\n--- Generate Node ---")




    question = state["question"]
    context = state.get("context", "")
    history = state.get("chat_history", [])




    history_text = "\n".join(history)




    # Retrieve memory again (for prompt)
    memory_docs = memory_db.similarity_search(question, k=2)
    memory_text = "\n".join([d.page_content for d in memory_docs])




    prompt = rag_prompt.format(
        context=context,
        question=question,
        chat_history=history_text,
        memory=memory_text
    )




    response = llm.invoke(prompt)




    answer = response.content




    # Update chat history
    updated_history = history + [
        f"User: {question}",
        f"Assistant: {answer}"
    ]




    # Store in memory DB
    memory_db.add_texts([
        f"Q: {question}\nA: {answer}"
    ])
   




    return {
        "answer": answer,
        "chat_history": updated_history
    }








# =========================
# 12. Direct Answer Node
# =========================




def direct_answer(state: GraphState):




    print("\n--- Direct Answer Node ---")




    question = state["question"]
    history = state.get("chat_history", [])




    history_text = "\n".join(history)




    response = llm.invoke(f"""
Chat History:
{history_text}




Question:
{question}
""")




    answer = response.content




    updated_history = history + [
        f"User: {question}",
        f"Assistant: {answer}"
    ]




    # Store memory
    memory_db.add_texts([
        f"Q: {question}\nA: {answer}"
    ])
   




    return {
        "answer": answer,
        "chat_history": updated_history
    }








# =========================
# 13. Build Graph
# =========================




graph = StateGraph(GraphState)




graph.add_node("retrieve", retrieve)
graph.add_node("generate", generate)
graph.add_node("direct", direct_answer)




graph.set_conditional_entry_point(
    router,
    {
        "retrieve": "retrieve",
        "direct": "direct"
    }
)




graph.add_edge("retrieve", "generate")
graph.add_edge("generate", END)
graph.add_edge("direct", END)




app = graph.compile()








# =========================
# 14. Run System
# =========================




state = {
    "chat_history": []
}




while True:




    user_question = input("\nAsk a question (type 'exit' to quit): ")




    if user_question.lower() == "exit":
        break




    result = app.invoke({
        "question": user_question,
        "chat_history": state["chat_history"]
    })




    print("\nFinal Answer:\n")
    print(result["answer"])




    state["chat_history"] = result["chat_history"]





