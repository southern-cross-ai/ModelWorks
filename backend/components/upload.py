import components.store_text as store
import components.database as database
from langchain.schema import Document

def upload(file):
    paragraphs = store.extract_text_from_pdf(file.file)
    print(paragraphs)
    docs = [Document(page_content=p) for p in paragraphs]
    database.get().add_documents(docs)
    return  len(docs)