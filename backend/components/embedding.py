from langchain_ollama import OllamaEmbeddings

def get():
    return OllamaEmbeddings(
        model="nomic-embed-text",
        base_url="http://ollama:11434"
    )