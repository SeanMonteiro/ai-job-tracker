from pydantic import BaseModel
from typing import List, Literal

class JobAnalysisResponse(BaseModel):
    title: str
    company: str
    skills: List[str]
    experience_level: Literal["Junior", "Mid", "Senior"]
    summary: str