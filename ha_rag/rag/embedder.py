import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def embed_chunks(chunks):
    embeddings = []

    for c in chunks:
        res = genai.embed_content(
            model="gemini-embedding-001",
            content=c["text"]
        )
        embeddings.append(res["embedding"])

    return embeddings