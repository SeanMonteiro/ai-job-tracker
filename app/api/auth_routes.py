from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.core.dependencies import get_user_service
from app.core.response import success_response

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register_user(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    result = user_service.register_user(user)
    return success_response(data=result)