import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from chonkie import QdrantHandshake, SemanticChunker

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

COLLECTION = "entre_ch1"
MODEL = "sentence-transformers/all-MiniLM-L6-v2"

with open("data/entre_ch1.txt", "r", encoding="utf-8") as f:
    full_text = f.read()

handshake = QdrantHandshake(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
    collection_name=COLLECTION,
    embedding_model=MODEL,
)

chunker = SemanticChunker()
chunks = chunker.chunk(full_text)

handshake.write(chunks)

print(f"Chunked and stored {len(chunks)} chunks into '{COLLECTION}'.")

info = client.get_collection(COLLECTION)
print(f"Collection now has {info.points_count} points.")