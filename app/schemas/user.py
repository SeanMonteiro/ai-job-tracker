from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    username: str
    email: str
    password: str = Field(min_length=8)

class UserResponse(BaseModel):
    id: int
    username: str
    email:EmailStr

    class Config:
        from_attributes = True