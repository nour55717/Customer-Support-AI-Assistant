from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.chat_service import ChatService


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

chat_service = ChatService()


class ChatRequest(BaseModel):
    question: str


class SourceResponse(BaseModel):
    category: str
    intent: str
    question: str
    similarity: float


class ChatResponse(BaseModel):
    answer: str
    confidence: float
    sources: List[SourceResponse]


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:

        result = chat_service.ask(request.question)

        return ChatResponse(
            answer=result["answer"],
            confidence=result["confidence"],
            sources=result["sources"],
        )

    except Exception as e:

        import traceback

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )