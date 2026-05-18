from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security.hashpassword import hash_password, verify_password
from app.core.security.jwt import create_access_token
from app.exceptions import AppException
from app.core.logger.logger import logger, setup_logger
logger = setup_logger()

class UserService:
    def __init__(self, repo):
        self.repo = repo

    # REGISTER USER
    
    def register_user(self, user_data: UserCreate):
        # Check for duplicate emil
        if self.repo.get_by_email(user_data.email):
            logger.warning(f"USER SERVICE: duplicate email registration attempt | email={user_data.email}")
            raise AppException("Email already exists", 400)
        
        # Check if username already in use
        if self.repo.get_by_username(user_data.username):
            logger.warning(f"USER SERVICE: duplicate username registration attempt | username={user_data.username}")
            raise AppException("Username already exists", 400)
        
        hash_pw = hash_password(user_data.password)

        user = User(
            username = user_data.username,
            email = user_data.email,
            hashed_password = hash_pw
        )
        logger.info(f"USER SERVICE: register success | user_id={user.id} | email={user.email}")
        return self.repo.create_user(user)
    
    # LOGIN USER

    def login_user(self, email:str, password:str):
        logger.info(f"USER SERVICE: login attempt | email={email}")

        user = self.repo.get_by_email(email)
        if not user:
            logger.warning(f"USER SERVICE: login failed (user not found) | email={email}")
            raise AppException("Invalid credentials", 401)
        
        if not verify_password(password, user.hashed_password):
            logger.warning(f"USER SERVICE: login failed (invalid password) | email={email}")
            raise AppException("Invalid credentials", 401)
        
        token = create_access_token (
            data = {
                "sub": str(user.id),
                "email": user.email
            }
        )
        
        return {
            "access_token" : token,
            "token_type" : "bearer"
        }
    
    # GET USER BY USER_ID
    def get_user_by_id(self, user_id: int):
        return self.repo.get_by_id(user_id)
    
    # UPDATE RESUME FOR USER
    def update_resume(self, user_id: int, resume_text: str):
        user = self.repo.get_by_id(user_id)

        if not user:
            logger.warning(f"USER SERVICE: resume update failed user not found | user_id={user_id}")
            raise AppException("User not found", 404)
        
        user.resume_text = resume_text
        return self.repo.update_user(user)
    
    # GET RESUME FOR USER
    def get_resume(self, user_id: int):
        user = self.repo.get_by_id(user_id)

        if not user:
            logger.warning(f"USER SERVICE: get resume failed user not found | user_id={user_id}")
            raise AppException("User not found", 404)
        
        return user.resume_text