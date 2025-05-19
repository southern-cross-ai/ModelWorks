from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://ollama:11434")

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask_question(request: Request):
    try:
        data = await request.json()
        query = data.get("query", "")
        print(f"👉 Received query: {query}")
        
        # 调用 LLM
        answer = llm.invoke(query)
        print(f"✅ LLM returned: {answer}")

        return {"result": answer}

    except Exception as e:
        print(f"❌ Error occurred: {e}")
        return {"result": f"Server error: {e}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
