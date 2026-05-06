# DB Access Layer
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.job import Job
from app.schemas.job import JobCreate
from app.core.logger.db_decorator import db_operation

class JobRepository:
    def __init__(self, db:Session):
        self.db = db

    @db_operation("CREATE_JOB","Job")
    def create_job(self, job):
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)
        return job

    @db_operation("GET_JOB","Job")
    def get_job(self, job_id):
        return self.db.query(Job).filter(Job.id == job_id).first()
        
    @db_operation("GET_ALL_JOBS", "Job")    
    def get_all_jobs(self):
        return self.db.query(Job).all()