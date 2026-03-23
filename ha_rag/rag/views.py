import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .pdf_utils import extract_text_from_pdf
from .chunker import chunk_text
from .embedder import embed_chunks
from .vector_store import build_store, search
from .generator import generate_answer
from .confidence import compute_confidence

UPLOAD_DIR = os.path.join(settings.BASE_DIR, "media/pdfs")


@csrf_exempt
def upload_pdf(request):
    if request.method == "POST":
        file = request.FILES.get("file")

        os.makedirs(UPLOAD_DIR, exist_ok=True)
        path = os.path.join(UPLOAD_DIR, file.name)

        with open(path, "wb+") as f:
            for chunk in file.chunks():
                f.write(chunk)

        # PROCESS
        pages = extract_text_from_pdf(path)
        chunks = chunk_text(pages)
        embeddings = embed_chunks(chunks)

        build_store(embeddings, chunks)

        return JsonResponse({"message": "PDF processed"})


def ask_question(request):
    query = request.GET.get("q")

    query_embedding = embed_chunks([{"text": query}])
    results, distances = search(query_embedding)

    confidence = compute_confidence(distances)
    pages = list(set([r["page"] for r in results]))

    answer = generate_answer(results, query)

    if confidence < 0.3:
        answer = "Not enough information in the document."

    print("QUERY:", query)
    print("RETRIEVED CHUNKS:")
    for r in results:
        print(r["text"][:200])
    print("DISTANCES:", distances)
    print("CONFIDENCE:", confidence)

    return JsonResponse({
        "answer": answer,
        "pages": pages,
        "confidence": confidence
    })