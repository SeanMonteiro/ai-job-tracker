from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel
from app.schemas.user import UserCreate, UserResponse, ResumeUpdateRequest, ResumeResponse
from app.services.user_service import UserService
from app.dependencies.injector import get_user_service
from app.core.response import success_response
from app.dependencies.auth import get_current_user
from app.core.logger.logger import logger, setup_logger
logger = setup_logger()

router = APIRouter(prefix="/auth", tags=["AUTH"])

class LoginRequest(BaseModel):
    email: str
    password: str

# REGISTER USER 
 
@router.post("/register", status_code=201)
def register_user(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    logger.info(f"AUTH ROUTE: registration attempt | email={user.email}")
    result = user_service.register_user(user)
    return UserResponse(
        username = result.username,
        email = result.email,
        message = "User created successfully"
    )

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
    return success_response (
        data = {
            "id" : current_user.id,
            "username" : current_user.username,
            "email": current_user.email
        }
    )

@router.put("/resume")
def update_my_resume(
    payload: str = Body(..., media_type="text/plain"),
    user_service: UserService = Depends(get_user_service),
    current_user = Depends(get_current_user)
):
    result = user_service.update_resume(
        user_id= current_user.id,
        resume_text= payload
    )

    resume_result = ResumeResponse(
        resume_length = len(result.resume_text or "")
    )

    return success_response(
        data = resume_result, 
        message = "Resume updated succesfully"
        )

@router.get("/resume")
def get_my_resume(
    current_user = Depends(get_current_user)
):
    resume_response = ResumeResponse (
        resume_text = current_user.resume_text,
        resume_length = len(current_user.resume_text or "")
    )
    
    return success_response(data = resume_response)