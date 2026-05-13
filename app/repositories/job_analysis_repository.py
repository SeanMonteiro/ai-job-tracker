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
    
    @db_operation("GET_NEXT_VERSION", "AI_ANALYSIS")
    def get_next_version(self, job_id: int):
        latest = (
            self.db.query(JobAnalysis)
            .filter(JobAnalysis.job_id == job_id)
            .order_by(JobAnalysis.version.desc())
            .first()
        )

        if not latest:
            return 1
        
        return latest.version + 1 