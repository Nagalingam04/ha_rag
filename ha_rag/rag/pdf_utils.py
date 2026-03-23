import fitz

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    pages = []

    for i in range(len(doc)):
        pages.append({
            "page": i + 1,
            "text": doc[i].get_text()
        })

    return pages