
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from knowledge_base import KNOWLEDGE_BASE


# Load a pretrained sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Extract knowledge content
documents = [
    item["title"] + ". " + item["content"]
    for item in KNOWLEDGE_BASE
]


# Convert knowledge documents into embeddings
document_embeddings = model.encode(
    documents,
    convert_to_numpy=True,
    normalize_embeddings=True
)

# Create a FAISS similarity index
dimension = document_embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

index.add(
    document_embeddings.astype("float32")
)



def semantic_search(question, top_k=1, min_score=0.35):

    # Convert the user's question into an embedding
    question_embedding = model.encode(
        [question],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    # Search for similar knowledge records
    scores, indices = index.search(
        question_embedding.astype("float32"),
        min(top_k, len(KNOWLEDGE_BASE))
    )

    results = []

    for score, idx in zip(scores[0], indices[0]):

        # Ignore invalid or low-scoring matches
        if idx == -1 or score < min_score:
            continue

        results.append({
            "title": KNOWLEDGE_BASE[idx]["title"],
            "category": KNOWLEDGE_BASE[idx]["category"],
            "content": KNOWLEDGE_BASE[idx]["content"],
            "score": float(score),
            "sources": KNOWLEDGE_BASE[idx]["sources"]
        })

    return results
