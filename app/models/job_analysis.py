from sqlalchemy import Column, Integer, Text, ForeignKey, JSON, String
from sqlalchemy.orm import relationship
from app.core.database.database import Base

class JobAnalysis(Base):
    __tablename__ = "job_analysis"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    job_id = Column(Integer, ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False)
    version = Column(Integer, default=1)
    model_version = Column(String, nullable=False)
    prompt_version = Column(String, nullable=False)
    analysis = Column(JSON)

    job = relationship("Job", back_populates="analysis")