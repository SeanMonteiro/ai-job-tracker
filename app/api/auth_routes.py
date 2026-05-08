from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.core.dependencies import get_user_service
from app.core.response import success_response

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/register")
def register_user(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    result = user_service.register_user(user)
    return success_response(data=result)

@router.post("/login")
def login(
    payload: LoginRequest,
    user_service: UserService = Depends(get_user_service)
):
    return user_service.login_user(
        payload.email,
        payload.password
    )
    