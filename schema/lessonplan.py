# Schema for Lesson Plan
# It describes the structure of the Response of Lesson plan deviser

from pydantic import BaseModel
from typing import List, Literal, Optional

class KeyConcept(BaseModel):
    type: Literal['definition', 'example', 'illustration', 'multimedia']
    content: str


class DiscussionQuestion(BaseModel):
    question: str


class HandsOnActivity(BaseModel):
    title: str
    description: str


class ReflectiveQuestion(BaseModel):
    question: str


class AssessmentIdea(BaseModel):
    type: Literal['quiz', 'written task', 'project']
    description: str


class SubTopic(BaseModel):
    title: str
    key_concepts: List[KeyConcept]
    discussion_questions: List[DiscussionQuestion]
    hands_on_activities: List[HandsOnActivity]
    reflective_questions: List[ReflectiveQuestion]
    assessment_ideas: List[AssessmentIdea]


class MainTopic(BaseModel):
    title: str
    subtopics: List[SubTopic]


class LessonPlanResponse(BaseModel):
    title: str
    subject: str
    learning_objectives: List[str]
    lesson_introduction: str
    main_topics: List[MainTopic]
    learning_adaptations: Optional[str] = None
    real_world_applications: str
    ethical_considerations: Optional[str] = None
