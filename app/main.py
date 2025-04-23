import gradio as gr
from langchain_community.llms import Ollama
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes


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

llm = Ollama(model="gemma3:1b")

# We add an extra parameter for history since it's appropriate for the interface used (this would be different for the default interface)
def chat_with_model(prompt, history): 
    response = llm.invoke(prompt)
    return response

# Creating a more complex Gradio UI using the blocks function
with gr.Blocks(theme=main_theme) as demo:
    # This is for the header (this has a HTML format which you can customise with internal CSS)
    gr.Markdown("<div style='display: flex; margin: auto; text-align: center;'> <img style='display: block;' src='https://avatars.githubusercontent.com/u/159676205' alt='Southern Cross AI Logo' height='50' width='50'> <h2 style='display: block;'>⠀⠀⠀Modelworks Chatbot </h2> </div>"),
    # This is for the chatbot
    gr.ChatInterface(
        fn=chat_with_model,
        type="messages",
        description="Chat with Gemma3 (1B model) running on Ollama using LangChain and Gradio (set up by the Modelworks Team).",
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
