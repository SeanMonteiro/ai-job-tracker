from sql_alchemy.orm import Session
from app.models.user import User
from app.core.logger.db_decorator import db_operation

class UserRepository:
    def __init__(self, db:Session):
        self.db = db
    
    @db_operation("GET_BY_EMAIL", "USER")
    def get_by_email(self, email:str):
        return self.db_query(User).filter(User.email == email).first()
    
    @db_operation()
    def get_by_username(self, username:str):
        return self.db_query(User).filter(User.username == username).first()
    
    @db_operation()
    def create_user(self, user: User):
        self.db.add(User)
        self.db.commit()
        self.db.refresh(user)
        return user