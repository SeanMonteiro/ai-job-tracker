from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.core.database.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    resume_text = Column(Text, nullable=True)

    jobs = relationship("Job", backref="owner")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
