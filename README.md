# 🤖 Customer Support AI Assistant

An intelligent AI-powered Customer Support Chatbot built using Retrieval-Augmented Generation (RAG).

The chatbot retrieves the most relevant customer support documents from a vector database and generates accurate answers using Google's Gemini Large Language Model.

---

# 🚀 Features

- AI Customer Support Assistant
- Retrieval-Augmented Generation (RAG)
- Gemini 3.6 Flash Integration
- ChromaDB Vector Database
- BAAI BGE Embedding Model
- FastAPI REST API
- Gradio Interactive Interface
- Conversation Memory
- Semantic Search
- Confidence Score
- Retrieved Sources
- Metadata Filtering

---

# 🏗️ System Architecture

```
User
   │
   ▼
Gradio UI
   │
   ▼
FastAPI
   │
   ▼
Chat Service
   │
   ├─────────────► Conversation Memory
   │
   ├─────────────► Retriever
   │                    │
   │                    ▼
   │              Embedding Model
   │                    │
   │                    ▼
   │                ChromaDB
   │
   ▼
Prompt Builder
   │
   ▼
Gemini 3.6 Flash
   │
   ▼
Final Answer
```

---

# 📂 Project Structure

```
customer-support-rag/

│

├── app/

│   ├── api/

│   ├── core/

│   ├── rag/

│   ├── services/

│   ├── models/

│   └── utils/

│

├── chroma_db/

├── data/

├── frontend/

├── notebooks/

├── tests/

├── logs/

│

├── README.md

├── requirements.txt

└── Dockerfile
```

---

# 🧠 Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Backend |
| FastAPI | REST API |
| Gradio | Chat UI |
| Gemini 3.6 Flash | LLM |
| ChromaDB | Vector Database |
| BAAI BGE | Embeddings |
| Sentence Transformers | Embedding Generation |
| Pydantic | Validation |

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository_url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
python -m uvicorn app.api.main:app --reload --port 8001
```

Run Gradio

```bash
python frontend/gradio_app.py
```

---

# 🌐 API

### POST

```
/chat/
```

Example Request

```json
{
    "question":"How can I cancel my order?"
}
```

Example Response

```json
{
    "answer":"...",
    "confidence":77.16,
    "sources":[
        {
            "category":"Order",
            "intent":"Cancel Order",
            "question":"...",
            "similarity":77.69
        }
    ]
}
```

---

# 📸 Screenshots

Add screenshots of:

- Swagger UI
- Gradio Interface
- Chat Example
- Project Structure

---

# 🎯 Future Improvements

- Authentication
- Multi-language Support
- Voice Assistant
- Dashboard
- PDF Export
- Feedback System
- Streaming Responses

