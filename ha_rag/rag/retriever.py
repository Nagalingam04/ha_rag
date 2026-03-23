def retrieve(query_embedding, index, chunks, k=3):
    distances, indices = index.search(query_embedding, k)

    results = []
    for idx in indices[0]:
        results.append(chunks[idx])

    return results, distances[0]