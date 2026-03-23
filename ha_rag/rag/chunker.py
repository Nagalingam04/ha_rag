def chunk_text(pages, size=400, overlap=50):
    chunks = []

    for page in pages:
        words = page["text"].split()
        start = 0

        while start < len(words):
            end = start + size

            chunks.append({
                "text": " ".join(words[start:end]),
                "page": page["page"]
            })

            start += size - overlap

    return chunks