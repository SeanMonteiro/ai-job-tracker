from sqlalchemy import Column, Integer, ForeignKey, JSON, String
from sqlalchemy.orm import relationship
from app.core.database.database import Base

class ResumeMatchAnalysis(Base):
    __tablename__ = "resume_match_analysis"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False)

    version = Column(Integer, default=1)
    model_version = Column(String, nullable=False)
    prompt_version = Column(String, nullable=False)

    match_result = Column(JSON, nullable=False)

    job = relationship ("Job", back_populates="resume_matches")