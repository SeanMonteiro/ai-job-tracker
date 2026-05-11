from sqlalchemy import Column, Integer, Text, ForeignKey, JSON
from app.core.database.database import Base

class JobAnalysis(Base):
    __tablename__ = "job_analysis"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    job_description = Column(Text)
    analysis = Column(JSON)