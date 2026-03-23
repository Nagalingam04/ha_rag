import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_answer(context_chunks, query):
    context = "\n\n".join([c["text"] for c in context_chunks])

    prompt = f"""
You are a strict academic assistant.

Rules:
1. Answer ONLY using the context
2. Do NOT use outside knowledge
3. If answer not found, say: Not available in document
4. Keep answer concise

Context:
{context}

Question:
{query}
"""

    response = model.generate_content(prompt)

    return response.text