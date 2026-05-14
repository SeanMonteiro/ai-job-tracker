# API Contract
from pydantic import BaseModel, Field
from typing import Optional

class JobCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=80)
    company: str = Field(default="Unknown", max_length=100)
    description: str = Field(..., min_length=10)


class JobResponse(JobCreate):
    id: int

    class Config:
        from_attributes = True

class JobUpdate(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    description: Optional[str] = None