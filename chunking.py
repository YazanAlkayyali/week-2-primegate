text = """Qdrant is a vector database. It stores embeddings and lets you search
by similarity instead of exact keywords. It supports filtering, payload
metadata, and hybrid search. Qdrant Cloud is a managed hosting option.
It has a free tier with 1 node. Paid tiers add more RAM, disk, and
uptime guarantees. To get started, you create a cluster, get an API
key, then create a collection with a vector size matching your
embedding model."""

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

for i, c in enumerate(chunk_text(text)):
    print(f"--- Chunk {i} ---")
    print(c)
    print()