import gradio as gr
import pdfplumber
from langchain_ollama import OllamaLLM
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes

########################################################
#########################UI#############################
########################################################

# Setting up (dummy) Modelworks Theme
# This has a format that is very similar to CSS (but not quite).
# Documentation is better (and probably better explained) on the Gradio Github
class Modelworks(Base):
    def __init__(
        self,
        *,
        # This will be the colour that 'draws attention to the theme" (e.g. the speech bubble)
        primary_hue: colors.Color | str = colors.violet,

        # This will be the colour of "secondary elements"
        secondary_hue: colors.Color | str = colors.indigo,

        # neutral_hue determines a majority of the theme, so for this it is a custom colour.  
        # Otherwise, for a simpler colour just copy the other hues above
    ):
        super().__init__(
            
            # Defining the needed hue variables

            primary_hue=primary_hue, # textbubble
            secondary_hue=secondary_hue,
            neutral_hue = gr.themes.Color(
                c50="#FFFFFF", # colour of chatwindow (light)*
                c100="#FFFFFF", # textbox inside (dark)
                c200="#AB96BD", # text/icon colour of chatwindow (dark)
                c300="#AB96BD", # hover for light mode
                c400="#B88CE8", # lighter text (for light textbox and settings page)
                c500="#B88CE8", # text/icon inside chatwindow (light)
                c600="#655BA6", # button colour (dark)
                c700="#211D26", # inside textbox/textbubble, border (dark)*
                c800="#211D26", # outside textbox (dark), text colour (light)*
                c900="#211D26", # colour of chatwindow*
                c950="#332F40"), # error colour and dark mode settings window
        )
        super().set(
            # This is just editing other parts of the theme
            # "_dark" = in dark mode
            body_background_fill="white",
            body_background_fill_dark="#1B102E",
            block_border_width="3px",
            block_shadow="*shadow_drop_lg",
            button_primary_shadow="*shadow_drop_lg",
            button_large_padding="32px",
        )

main_theme = Modelworks()

########################################################
#####################FUNCTIONALITY######################
########################################################

# Load the DeepSeek R1 1.5B model in Ollama
llm = OllamaLLM(model="gemma3:1b")

# Select a Embedding Model (provided by LangChain)
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize ChromaDB (Persistent Storage)
vector_db = Chroma(persist_directory="./chroma_db1", embedding_function=embedding_model)
# Documents
# documents = [
#     Document(page_content="DeepSeek is a powerful AI language model."),
#     Document(page_content="DeepSeek is a model."),
#     Document(page_content="AI language model: DeepSeek"),
#     Document(page_content="LangChain helps you connect the LLM to the database."),
#     Document(page_content="ChromaDB is an efficient vector database."),
#     Document(page_content="KNN is a similarity search method used to find nearest neighbor vectors."),
# ]

def extract_text_from_pdf(pdf_path):
    """Parse PDF and extract text """
    paragraphs = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                
                page_paragraphs = page_text.split("\n\n")
                paragraphs += [p.strip() for p in page_paragraphs if p.strip()]

    return paragraphs

def store_pdf_embeddings(pdf_file):
    pdf_path = pdf_file.name
    paragraphs = extract_text_from_pdf(pdf_path)

    documents = [Document(page_content=p) for p in paragraphs]
    vector_db.add_documents(documents)

    return f"📄 PDF processing complete. {len(documents)} chunks stored in ChromaDB."

# Query ChromaDB for the k most similar document fragments
def search_similar_chunks(query, k=3):
    query_embedding = embedding_model.embed_query(query)
    docs = vector_db.similarity_search_by_vector(query_embedding, k=k)
    return [doc.page_content for doc in docs]


# Function to interact with the model
def chat_with_model(prompt):
    response = llm.invoke(prompt)  # Invoke the model with user input
    return response

def generate_answer(query):
    """Let the LLM generate an answer based on retrieved documents"""
    similar_chunks = search_similar_chunks(query, k=3)
    context = "\n".join(similar_chunks)

    prompt = f"Refer to the following information to answer the question:\n\n{context}\n\nQuestion: {query}"
    response = llm.invoke(prompt)

    return f"**🔍 Relevant Document Snippets:**\n{context}\n\n**🤖 LLM Answer:**\n{response}"

# Create a Gradio interface
with gr.Blocks(theme=main_theme) as demo:

    gr.Markdown("<div style='display: flex; margin: auto; text-align: center;'> <img style='display: block;' src='https://avatars.githubusercontent.com/u/159676205' alt='Southern Cross AI Logo' height='50' width='50'> <h2 style='display: block;'>⠀⠀⠀PDF Semantic Search + Gemma3 (1B) Question Answering System </h2> </div>"),
    gr.Markdown("### 🔹 Upload a PDF and Perform Semantic Search")

    with gr.Row():
        pdf_input = gr.File(label="📤 Upload PDF file", type="filepath")
        pdf_output = gr.Textbox(label="📊 Processing Result")

    process_pdf_button = gr.Button("📥 Parse PDF and Store in Database")
    process_pdf_button.click(store_pdf_embeddings, inputs=pdf_input, outputs=pdf_output)

    gr.Markdown("### 🔹 Semantic Search + LLM Answer Generation")

    with gr.Row():
        query_input = gr.Textbox(label="🔍 Enter your question", placeholder="What is Gemma3?")
        query_output = gr.Textbox(label="🤖 AI Answer", interactive=True)

    search_button = gr.Button("🔎 Search and Generate Answer")
    search_button.click(generate_answer, inputs=query_input, outputs=query_output)

    gr.Markdown("💡 **Tip**: After uploading a PDF, you can ask a question such as _'What is the main content of this document?'_")

# Launch Gradio app on a specific port
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
