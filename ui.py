import chainlit as cl
import requests

# حدد عنوان الـ API الخاص بك
API_URL = "https://grc2025-grc.hf.space/ask"  # تأكد من وجود "/ask"

@cl.on_message
async def on_message(message: cl.Message):
    question = message.content.strip()

    if not question:
        await cl.Message(content="⚠️ Please enter a valid question.").send()
        return

    try:
        # إرسال السؤال إلى الـ API
        response = requests.post(API_URL, json={"question": question})
        result = response.json()

        answer = result.get("answer", "❌ No answer received.")
    except Exception as e:
        answer = f"🚨 Error contacting the API: {e}"

    await cl.Message(content=answer).send()
