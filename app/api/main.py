from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.health import router as health_router

app = FastAPI(
    title="Customer Support AI",
    version="1.0.0",
    description="RAG Customer Support Chatbot using Gemini"
)

app.include_router(chat_router)
app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "API Working"}