import components.retrieve as retrieve
import components.llm as llm
import components.history as history
import components.store_text as store
from langchain.schema import Document
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

k = 3
embedding_model = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://ollama:11434"
)
vector_db = Chroma(persist_directory="./chroma_db1", embedding_function=embedding_model)

# primary function
def call(query: str, messages: list = []):
    history_aware_query = history.contextualize(query, messages)

    context = retrieve.retrieve(history_aware_query, k, embedding_model, vector_db)

    if context != []:
        contextualized_query = format(history_aware_query, context)
        llm_response = llm.call(contextualized_query)
    else: 
        llm_response = llm.call(history_aware_query)

    return llm_response

def format(query: str, context: str):
    # to be implimented
    context = "\n".join(context)
    query = f"Refer to the following information:\n\n{context}\n\nQuestion: {query}"
    return query

def upload(file):
    paragraphs = store.extract_text_from_pdf(file.file)
    print(paragraphs)
    docs = [Document(page_content=p) for p in paragraphs]
    vector_db.add_documents(docs)
    return  len(docs)