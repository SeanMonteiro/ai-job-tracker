from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str = Field(min_length=8)

class UserResponse(BaseModel):
    username: str
    email: str
    message: str

    class Config:
        from_attributes = True

class ResumeUpdateRequest(BaseModel):
    resume_text: str = Field(..., min_length=50)

class ResumeResponse(BaseModel):
    resume_text: Optional[str] = None
    resume_length: int

