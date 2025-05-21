import components.embedding as embedding
from langchain_chroma import Chroma

def get():
    return Chroma(persist_directory="./chroma_db1", embedding_function=embedding.get())