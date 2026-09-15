import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

def chunk_text(text, chunk_size=200, overlap=50):
    if len(text)<=chunk_size:
        return [text]
    chunks=[]
    start=0
    while start<len(text):
        end= start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

COLLECTION="tea_reviews"
MODEL="sentence-transformers/all-MiniLM-L6-v2"

df = pd.read_csv("data/tea_reviews.csv")
df = df.dropna(subset=["review_text"])


#docs = [
#    "Qdrant has a LangChain integration for chatbots.",
#    "Qdrant has a LlamaIndex integration for agents.",
#]
#metadata = [
#    {"source": "langchain-docs"},
#    {"source": "llamaindex-docs"},
#]
#   ids = [42, 2]