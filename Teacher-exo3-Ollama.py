# Import necessary libraries for the chatbot
from langchain_ollama import OllamaLLM  # مكتبة Ollama الجديدة
import chainlit as cl

# This function is called when the chatbot starts
@cl.on_chat_start
async def on_chat_start():
    # فقط رسالة ترحيبية بدون صورة
    await cl.Message(
        content="🌌 Welcome! I’m AstroBot, your friendly astronomy assistant. Ask me anything about space and the universe!"
    ).send()

    
    # Create an Ollama model instance for text generation
    model = OllamaLLM(model="Mm77shallm/meshal")


    # Store the model in the user session for later use
    cl.user_session.set("model", model)

# This function is called whenever the user sends a message
@cl.on_message
async def on_message(message: cl.Message):
    # Retrieve the model stored in the user session
    model = cl.user_session.get("model")

    # Check if the model is initialized
    if model is None:
        await cl.Message(content="❌ The model is not initialized. Please restart the chat.").send()
        return

    # Generate a response from the model
    try:
        response = model.invoke(message.content)
        await cl.Message(content=response).send()
    except Exception as e:
        await cl.Message(content=f"⚠️ Error: {str(e)}").send()

# This function is called when the user stops the conversation
@cl.on_stop
def on_stop():
    print("👋 See you space cowboy")

# To launch the app, open a terminal in your project directory and type:
# chainlit run chatbot.py -w --port 8000