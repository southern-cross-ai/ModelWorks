import pdfplumber

def extract_text_from_pdf(pdf_path):
    paragraphs = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                page_paragraphs = page_text.split("\n\n")
                paragraphs += [p.strip() for p in page_paragraphs if p.strip()]
    return paragraphs