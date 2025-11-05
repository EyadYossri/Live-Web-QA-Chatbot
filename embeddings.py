from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    embeddings = embed_model.encode(texts, show_progress_bar=False)

    if hasattr(embeddings[0], "tolist"):
        embeddings = [emb.tolist() for emb in embeddings]

    return embeddings
