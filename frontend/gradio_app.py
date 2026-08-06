import gradio as gr
import requests

API_URL = "http://127.0.0.1:8001/chat/"


def chat(message, history):
    try:

        response = requests.post(
            API_URL,
            json={"question": message},
            timeout=120,
        )

        if response.status_code != 200:
            return f"❌ Server Error ({response.status_code})"

        data = response.json()

        answer = data["answer"]
        confidence = data["confidence"]
        sources = data["sources"]

        source_text = ""

        for i, source in enumerate(sources, start=1):

            source_text += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 Source {i}

📂 Category: {source["category"]}

🎯 Intent: {source["intent"]}

❓ Customer Question:
{source["question"]}

📈 Similarity: {source["similarity"]}%

"""

        final_answer = f"""
🤖 Answer

{answer}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Confidence

{confidence}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 Retrieved Sources

{source_text}
"""

        return final_answer

    except Exception as e:

        return f"❌ Connection Error\n\n{str(e)}"


demo = gr.ChatInterface(
    fn=chat,

    title="🤖 Customer Support AI Assistant",

    description="""
RAG Chatbot powered by Gemini + ChromaDB + FastAPI
""",

    chatbot=gr.Chatbot(
        height=600,
    ),

    textbox=gr.Textbox(
        placeholder="Type your customer support question here...",
        lines=2,
    ),

    examples=[
        "How can I cancel my order?",
        "Can I get a refund?",
        "I forgot my password.",
        "How do I track my shipment?",
        "How can I change my email address?"
    ],
)


if __name__ == "__main__":
    demo.launch()