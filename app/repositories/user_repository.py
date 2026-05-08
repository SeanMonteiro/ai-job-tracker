from sqlalchemy.orm import Session
from app.models.user import User
from app.core.logger.db_decorator import db_operation

class UserRepository:
    def __init__(self, db:Session):
        self.db = db
    
    @db_operation("GET_BY_EMAIL", "USER")
    def get_by_email(self, email:str):
        return self.db.query(User).filter(User.email == email).first()
    
    @db_operation("GET_BY_USERNAME","USER")
    def get_by_username(self, username:str):
        return self.db.query(User).filter(User.username == username).first()
    
    @db_operation("REGISTER_USER","USER")
    def create_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    @db_operation("GET_USER_BY_ID","USER")
    def get_by_id(self, user_id:int):
        return self.db.query(User).filter(User.id == user_id).first()