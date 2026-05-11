from app.models.job_analysis import JobAnalysis
from sqlalchemy.orm import Session
from app.core.logger.db_decorator import db_operation

class JobAnalysisRepository:
    def __init__(self, db:Session):
        self.db = db

    @db_operation("SAVE_ANALYSIS", "JOB_ANALYSIS")
    def save(self, analysis: JobAnalysis):
        self.db.add(analysis)
        self.db.commit()
        self.db.refresh(analysis)
        return analysis
    

    @db_operation("GET_ANALYSIS", "JOB_ANALYSIS")
    def get_by_id(self, analysis_id: int):
        return self.db.query(JobAnalysis).filter(JobAnalysis.id == analysis_id).first()