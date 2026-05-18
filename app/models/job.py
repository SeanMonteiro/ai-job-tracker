# ORM 
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), nullable=False, default="Saved", server_default="Saved")

    user_id = Column(Integer, ForeignKey("users.id"))

    analysis = relationship(
        "JobAnalysis",
        back_populates = "job", 
        cascade="all, delete-orphan")
    
    resume_matches = relationship(
        "ResumeMatchAnalysis",
        back_populates = "job",
        cascade = "all, delete-orphan"
    )

    def __repr__(self):
        return f"<Job(id={self.id}, title={self.title}, status={self.status})>"
