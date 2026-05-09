from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)

    jobs = relationship("Job", backref="owner")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
