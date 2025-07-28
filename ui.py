import chainlit as cl

# This function is called when the chatbot starts
@cl.on_chat_start
async def on_chat_start():
    # فقط رسالة ترحيبية بدون صورة
    await cl.Message(
        content="🌌 Welcome! I’m AstroBot, your friendly astronomy assistant. Ask me anything about space and the universe!"
    ).send()

    
    # نخزن الردود في جلسة المستخدم
    static_responses = {
        "hi": "Hello! 👋",
        "hello": "Hi there! ✨",
        "who are you": "I’m AstroBot, your friendly astronomy assistant! 🌠",
        "bye": "Goodbye! See you among the stars. 🚀",
    }

    cl.user_session.set("responses", static_responses)

# This function is called whenever the user sends a message
@cl.on_message
async def on_message(message: cl.Message):
    responses = cl.user_session.get("responses")

    if responses is None:
        await cl.Message(content="⚠️ Responses not initialized. Please restart the chat.").send()
        return

    user_input = message.content.strip().lower()
    reply = responses.get(user_input, "🤖 I’m just a demo bot. I didn’t understand that.")

    await cl.Message(content=reply).send()

# This function is called when the user stops the conversation
@cl.on_stop
def on_stop():
    print("👋 See you space cowboy")
