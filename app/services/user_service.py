from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password
from app.exceptions import AppException

class UserService:
    def __init__(self, repo):
        self.repo = repo

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