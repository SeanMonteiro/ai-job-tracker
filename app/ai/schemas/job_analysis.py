from pydantic import BaseModel
from typing import List

class JobAnalysisRespone(BaseModel):
    skills: List[str]
    experience_level: str
    summary: str

# class JobAnalysisRequest(BaseModel):
#     job_description: str