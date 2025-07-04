# Schema for Multiple-Choice questions
# It describes the Request and Response format for MCQs

from typing import List
from pydantic import BaseModel, Field
from enum import Enum

class Difficulty(str, Enum):
	easy = "easy"
	medium = "medium"
	hard = "hard"

class MCQRequest(BaseModel):
	topic: str
	difficulty: Difficulty = Difficulty.medium
	num: int = Field(default=10, ge=1, le=25)

class MultipleChoiceQuestion(BaseModel):
	question: str
	answer: str
	explanation: str
	options: List[str]

class MCQResponse(BaseModel):
	questions: List[MultipleChoiceQuestion]

