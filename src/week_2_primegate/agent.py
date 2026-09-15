import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langfuse import Langfuse
from langfuse.langchain import CallbackHandler
from .ai_config import API_KEY
from .retrieval import search_chapter

Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST"),
)
langfuse_handler = CallbackHandler()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=API_KEY,
    temperature=0.0,
    max_retries=2,
)

qa_system_prompt = (
    "You are an assistant that answers questions using ONLY the context provided below. "
    "Do not use any outside knowledge, even if you know the answer. "
    "If the context does not contain the answer, respond with exactly: "
    "I dont know based on the provided document. "
    "Do not guess, and do not answer from general knowledge under any circumstances."
    "\n\n"
    "Context:\n{context}"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", qa_system_prompt),
    MessagesPlaceholder("history"),
    ("human", "{input}"),
])

chain = prompt | model

history = []

def chat(user_input: str) -> str:
    context_chunks = search_chapter(user_input)
    context = "\n\n".join(context_chunks)

    response = chain.invoke(
        {"history": history, "input": user_input, "context": context},
        config={"callbacks": [langfuse_handler]},
    )
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response.content))
    return str(response.content)
