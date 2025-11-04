from sentence_transformers import SentenceTransformer

# Load model once
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    """
    Embed a list of texts using SentenceTransformers.
    Returns a list of embeddings (each embedding is a list of floats).
    """
    embeddings = embed_model.encode(texts, show_progress_bar=False)

    # Check if embeddings are ndarray, convert to list if needed
    if hasattr(embeddings[0], "tolist"):
        embeddings = [emb.tolist() for emb in embeddings]

    return embeddings
