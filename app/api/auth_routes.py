from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.schemas.user import UserCreate
from app.services.user_service import UserService
from app.dependencies.injector import get_user_service
from app.core.response import success_response
from app.dependencies.auth import get_current_user
from app.core.logger.logger import logger, setup_logger
logger = setup_logger()

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginRequest(BaseModel):
    email: str
    password: str

# REGISTER USER 
 
@router.post("/register")
def register_user(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    logger.info(f"AUTH ROUTE: registration attempt | email={user.email}")
    result = user_service.register_user(user)
    return success_response(data=result)

# LOGIN USER

@router.post("/login")
def login(
    payload: LoginRequest,
    user_service: UserService = Depends(get_user_service)
):
    logger.info(f"AUTH ROUTE: login attempt | email={payload.email}")
    result = user_service.login_user(payload.email, payload.password)
    logger.info(f"AUTH ROUTE: login success | email={payload.email}")
    return success_response(data=result)

# Test JWT token
@router.get("/me")
def get_me(current_user = Depends(get_current_user)):
    return {
        "success": True,
        "data": {
            "id" : current_user.id,
            "username" : current_user.username,
            "email": current_user.email
        },
        "message" : None
    }