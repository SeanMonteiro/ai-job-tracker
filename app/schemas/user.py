from pydantic import BaseModel, EmailStr, Field

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

