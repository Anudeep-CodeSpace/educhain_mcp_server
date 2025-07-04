# Schema of flash cards
# It describes the sturcture of flashcards and their Request and Response

from pydantic import BaseModel, Field
from typing import List, Optional

class FCRequest(BaseModel):
    topic: str
    num: int = Field(default=10, ge=1, le=100)

class FlashCard(BaseModel):
    front: str
    back: str
    explanation: Optional[str]

class FCResponse(BaseModel):
    title: str
    flashcards: List[FlashCard]