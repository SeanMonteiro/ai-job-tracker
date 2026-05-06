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