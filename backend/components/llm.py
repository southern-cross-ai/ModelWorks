from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://ollama:11434")

def call(query: str):
    return llm.invoke(query)