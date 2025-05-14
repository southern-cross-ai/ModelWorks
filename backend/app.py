from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from langchain_ollama import OllamaLLM
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory
from langchain.prompts import PromptTemplate

# 🧠 LLM instance
llm = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://ollama:11434")

# 🧠 Conversation memory that summarizes previous chats
memory = ConversationSummaryMemory(llm=llm, return_messages=True)

# 🧠 Custom prompt to ensure memory context is injected
prompt = PromptTemplate.from_template(
    """The following is a conversation between a helpful AI assistant and a user.
The assistant remembers facts the user tells it across the conversation.

Summary of past conversation:
{history}

User: {input}
AI:"""
)

# 🧠 Conversation chain with memory + custom prompt
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True
)

# 🚀 FastAPI setup
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
        
        # Use conversation chain with memory
        answer = conversation.predict(input=query)
        print(f"✅ LLM returned: {answer}")

        return {"result": answer}

    except Exception as e:
        print(f"❌ Error occurred: {e}")
        return {"result": f"Server error: {e}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)