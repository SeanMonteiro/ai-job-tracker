from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from app.core.security.security import oauth2_scheme
from app.core.security.jwt import decode_access_token
from app.dependencies.injector import get_user_service
from app.exceptions import AppException
from app.services.user_service import UserService

def get_current_user(
        # token:str = Depends(oauth2_scheme),
        credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme),
        user_service: UserService = Depends(get_user_service)
):
    token = credentials.credentials
    payload = decode_access_token(token)

    if payload is None:
        raise AppException("Invalid or expired token", 401)
    
    user_id = payload.get("sub")

    if user_id is None:
        raise AppException("Invalio token payload", 401)
    
    try:
        user_id = int(user_id)
    except ValueError:
        raise AppException("Invalid token payliad(bad sub format)", 401)
    
    user = user_service.repo.get_by_id(int(user_id))

    if user is None:
        raise AppException("User not found", 404)
    
    return user