from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from app.core.security.security import oauth2_scheme
from app.core.security.jwt import decode_access_token
from app.dependencies.injector import get_user_service
from app.exceptions import AppException
from app.services.user_service import UserService
from app.core.logger.logger import logger, setup_logger
logger = setup_logger()

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme),
        user_service: UserService = Depends(get_user_service)
):
    token = credentials.credentials
    payload = decode_access_token(token)

    if payload is None:
        logger.warning("AUTH FAILED: invalid or expired token")
        raise AppException("Invalid or expired token", 401)
    
    user_id = payload.get("sub")

    if user_id is None:
        logger.warning("AUTH FAILED: missing sub in token payload")
        raise AppException("Invalid token payload", 401)
    
    try:
        user_id = int(user_id)
    except ValueError:
        logger.warning("AUTH FAILED: Token sub is not integer")
        raise AppException("Invalid token payload(bad sub format)", 401)
    
    user = user_service.get_user_by_id(user_id)

    if user is None:
        logger.warning(f"AUTH FAILED: user not found | user_id={user_id}")
        raise AppException("User not found", 404)
    
    return user