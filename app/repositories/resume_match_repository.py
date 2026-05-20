from sqlalchemy.orm import Session
from app.models.resume_match_analysis import ResumeMatchAnalysis
from app.core.logger.db_decorator import db_operation

class ResumeMatchRepository:
    def __init__(self, db:Session):
        self.db = db

    @db_operation("SAVE_RESUME_MATCH", "RESUME_MATCH")
    def save(self, resume_match: ResumeMatchAnalysis):
        self.db.add(resume_match)
        self.db.commit()
        self.db.refresh(resume_match)
        return resume_match
    
    @db_operation("GET_LATEST_RESUME_MATCH", "RESUME_MATCH")
    def get_latest_by_job_id(self, job_id: int):
        return (
            self.db.quer(ResumeMatchAnalysis)
            .filter(ResumeMatchAnalysis.job_id == job_id)
            .order_by(ResumeMatchAnalysis.version.desc())
            .first()
        )
    
    @db_operation("GET_NEXT_RESUME_MATCH_VERSION", "RESUME_MATCH")
    def get_next_version(self, job_id: int):
        latest = (
            self.db.query(ResumeMatchAnalysis)
            .filter(ResumeMatchAnalysis.job_id == job_id)
            .order_by(ResumeMatchAnalysis.version.desc())
            .first()
        )

        if not latest:
            return 1
        
        return latest.version + 1