from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security.hashpassword import hash_password, verify_password
from app.core.security.jwt import create_access_token
from app.exceptions import AppException

class UserService:
    def __init__(self, repo):
        self.repo = repo

    # REGISTER USER
    
    def register_user(self, user_data: UserCreate):
        
        # Check for duplicate emil
        if self.repo.get_by_email(user_data.email):
            raise AppException("Email already exists", 400)
        
        # Check if username already in use
        if self.repo.get_by_username(user_data.username):
            raise AppException("Username already exists", 400)
        
        hash_pw = hash_password(user_data.password)

        user = User(
            username = user_data.username,
            email = user_data.email,
            hashed_password = hash_pw
        )
        return self.repo.create_user(user)
    
    # LOGIN USER

    def login_user(self, email:str, password:str):
        user = self.repo.get_by_email(email)
        if not user:
            raise AppException("Invalid credentials", 401)
        
        if not verify_password(password, user.hashed_password):
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