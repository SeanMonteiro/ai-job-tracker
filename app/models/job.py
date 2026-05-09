# ORM 
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.core.database.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"<Job(id={self.id}, title={self.title})>"
