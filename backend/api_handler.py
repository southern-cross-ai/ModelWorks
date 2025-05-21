from fastapi import FastAPI, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import components.pipeline as pipeline
import components.upload as upload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Upload and store PDF
@app.post("/upload")
async def upload_pdf(file: UploadFile):
    try:
        number_of_text_stored = upload.upload(file)
        return  {"result": f"Stored {number_of_text_stored} paragraphs."}
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        return {"result": f"Server error: {e}"}

@app.post("/ask")
async def ask_question(request: Request):
    try:
        data = await request.json()
        query = data.get("query", "")
        print(f"👉 Received query: {query}")
        
        # 调用 LLM
        answer = pipeline.call(query)
        print(f"✅ LLM returned: {answer}")

        return {"result": answer}

    except Exception as e:
        print(f"❌ Error occurred: {e}")
        return {"result": f"Server error: {e}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)