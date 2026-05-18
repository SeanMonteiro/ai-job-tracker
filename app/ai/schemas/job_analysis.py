from pydantic import BaseModel, Field
from typing import List, Literal

class JobAnalysisResponse(BaseModel):
    title: str
    company: str
    skills: List[str]
    experience_level: Literal["Junior", "Mid", "Senior"]
    summary: str


class ResumeMatchResponse(BaseModel):
    match_score: int =  Field(..., ge=0, le=100)
    matching_skills: List[str] = Field(default_factory=list)
    missing_skills: List[str] = Field(default_factory=list)
    resume_strengths: List[str] = Field(default_factory=list)
    improvement_suggestions: List[str] = Field(default_factory=list)
    focus_summary: str