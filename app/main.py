import os
import gradio as gr
from langchain_ollama import OllamaLLM
from langchain.agents import Tool
from langchain_community.utilities.serpapi import SerpAPIWrapper
# from langchain.tools import SerpAPIWrapper, Tool
from langchain.agents import initialize_agent, Tool
from gradio.themes.base import Base
from gradio.themes.utils import colors, sizes, fonts
# from langchain.utilities import SerpAPIWrapper
from langchain.agents import Tool
from langchain_core.exceptions import OutputParserException

# Theme Definition
class Modelworks(Base):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = colors.violet,
        secondary_hue: colors.Color | str = colors.indigo,
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=gr.themes.Color(
                c50="#FFFFFF", c100="#FFFFFF", c200="#AB96BD",
                c300="#AB96BD", c400="#B88CE8", c500="#B88CE8",
                c600="#655BA6", c700="#211D26", c800="#211D26",
                c900="#211D26", c950="#332F40"
            ),
        )
        super().set(
            body_background_fill="white",
            body_background_fill_dark="#1B102E",
            block_border_width="3px",
            block_shadow="*shadow_drop_lg",
            button_primary_shadow="*shadow_drop_lg",
            button_large_padding="32px",
        )

# Instantiate theme
main_theme = Modelworks()

# LLM & Search Tool
llm = OllamaLLM(model="gemma3:1b")

# Configure SerpAPIWrapper for web search (you need your key)
search = SerpAPIWrapper(serpapi_api_key="53afbd074061caca8efc6036cacbb255962b2e8c4c39c5ebc156276cf0ba9241")
web_search_tool = Tool(
    name="Web Search",
    func=search.run,
    description="Use this to query current web results for a user’s query."
)

# Initialize a LangChain agent that can call web search + the LLM
agent = initialize_agent(
    tools=[web_search_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=False,  # set True to see tool calls in console
    handle_parsing_errors=True
)

# Chat Function
def chat_with_model(user_message, chat_history):
    # """
    # Uses a LangChain agent to decide whether to call the Web Search tool or directly invoke the LLM.
    # Appends the chosen response to the chat history.
    # """
    # # Let the agent handle tool selection and LLM invocation
    # response = agent.run(user_message)
    # chat_history = chat_history + [(user_message, response)]
    # return chat_history, ""
    try:
        result = agent.run(user_message)
    except OutputParserException:
        # fallback: just ask the model directly
        result = llm.invoke(user_message)
    chat_history.append((user_message, result))
    return chat_history, ""

# Gradio App

with gr.Blocks(theme=main_theme) as demo:
    gr.Markdown("# Modelworks Chatbot with Web Search")
    chatbot = gr.Chatbot(label="Conversation")
    with gr.Row():
        msg = gr.Textbox(placeholder="Type your message here...", label="Your message")
        send = gr.Button("Send")
    send.click(
        fn=chat_with_model,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
