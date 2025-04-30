# 🌐 ModelWorks: PDF Semantic Search & LLM QA System
<h2 style="font-size: 24px;">🧠 Overview</h2>  

 

<p style="font-size: 16px;">  

  

This branch of ModelWorks delivers an end-to-end system for semantic document search and intelligent question answering. Users can upload a PDF file, extract its semantic content into a vector database (Chroma), and query it using natural language via a large language model hosted on Ollama.

All components run in isolated containers orchestrated with Docker Compose for easy deployment and reproducibility.

  

</p>  

<hr>
   

  

<h2 style="font-size: 24px;">🚀 Features</h2>  

  

<p style="font-size: 16px;">  

  

📄 PDF Upload — Extracts and splits text from uploaded PDF documents.

🔎 Semantic Embedding — Stores document chunks in ChromaDB using Sentence Transformers.

🤖 AI QA via Ollama — Answers user queries using DeepSeek-R1:1.5B hosted in a container.

🧩 Integrated Interface — Intuitive Gradio UI for document processing and QA.

  

</p>  


<br> 

<h3 style="font-size: 24px;">🧱 Tech Stack</h3>  

| Layer       | Technology               |
|-------------|---------------------------|
| Backend     | Python, LangChain         |
| Vector DB   | Chroma                    |
| LLM         | Ollama                    |
| UI          | Gradio                    |
| Container   | Docker + Compose          |

<br>



## 🐳 Quick Start

### 1. Clone & Build

```bash
git clone https://github.com/yourusername/ModelWorks.git
cd ModelWorks
docker compose up --build
```



### 2. Access UI

Visit [http://localhost:7860](http://localhost:7860) to use the interface.

<br>


<br>

## 📌 Usage Workflow

1. **Upload PDF** → Split paragraphs and store in Chroma.
2. **Ask a Question** → The system retrieves relevant text.
3. **LLM Answer** → Generate a contextual response.

<br>

## 🛠 Development Tips

- To rebuild the image after code changes:

```bash
docker compose build
```

- To stop all services:

```bash
docker compose down
```

- For troubleshooting Ollama:

```bash
docker exec -it <ollama-container-name> bash
```

<br>



---

## 📄 License & Contribution

Refer to [CONTRIBUTING.md](./CONTRIBUTING.md) to get started with contributions.

