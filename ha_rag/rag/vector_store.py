import faiss
import numpy as np
import pickle
import os

INDEX_PATH = "faiss.index"
CHUNKS_PATH = "chunks.pkl"

index = None
stored_chunks = []


def build_store(embeddings, chunks):
    global index, stored_chunks

    embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    stored_chunks = chunks

    # 🔥 SAVE TO DISK
    faiss.write_index(index, INDEX_PATH)

    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(stored_chunks, f)


def load_store():
    global index, stored_chunks

    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)

    if os.path.exists(CHUNKS_PATH):
        with open(CHUNKS_PATH, "rb") as f:
            stored_chunks = pickle.load(f)


def search(query_embedding, k=3):
    global index, stored_chunks

    if index is None:
        raise ValueError("No document indexed.")

    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []
    valid_distances = []

    for dist, idx in zip(distances[0], indices[0]):
        if idx == -1:
            continue
        if dist > 1e5:   # filter garbage values
            continue

        results.append(stored_chunks[idx])
        valid_distances.append(dist)

    return results, valid_distances