# API Contract
from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    title: str
    company: str
    description: Optional[str] = None


class JobResponse(JobCreate):
    id: int

    class Config:
        from_attributes = True

class JobUpdate(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    description: Optional[str] = None