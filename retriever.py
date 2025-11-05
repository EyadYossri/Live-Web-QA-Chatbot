import os
from dotenv import load_dotenv
from embeddings import embed_texts
import pinecone

load_dotenv()

INDEX_NAME = os.getenv("INDEX_NAME", "webqa")
pc = pinecone.Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

if INDEX_NAME not in pc.list_indexes().names():
    from pinecone import ServerlessSpec
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-west-2")
    )

index = pc.Index(INDEX_NAME)

def add_to_vectorstore(texts, metas):
    embeddings = embed_texts(texts)  

    vectors = [
        {
            "id": str(i),
            "values": emb,  
            "metadata": {"source": metas[i], "text": texts[i]}
        }
        for i, emb in enumerate(embeddings)
    ]


    index.upsert(vectors=vectors)


def search_similar(query, top_k=5):
    query_vec = embed_texts([query])[0]  
    if hasattr(query_vec, "tolist"):  
        query_vec = query_vec.tolist()    
    
    results = index.query(vector=query_vec, top_k=top_k, include_metadata=True)

    chunks = []
    if results and results.matches:
        for match in results.matches:
            text = match.metadata.get("text", "")
            if text:
                chunks.append(text)
    return chunks






