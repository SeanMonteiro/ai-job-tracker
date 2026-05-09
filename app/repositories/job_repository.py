# DB Access Layer
from sqlalchemy.orm import Session
from app.models.job import Job
from app.core.logger.db_decorator import db_operation

class JobRepository:
    def __init__(self, db:Session):
        self.db = db

    @db_operation("CREATE_JOB","Job")
    def create_job(self, job: Job):
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)
        return job

    @db_operation("GET_JOB","Job")
    def get_job(self, job_id: int):
        return self.db.query(Job).filter(Job.id == job_id).first()
        
    @db_operation("GET_ALL_JOBS", "Job")    
    def get_all_jobs(self, user_id:int):
        return self.db.query(Job).filter(Job.user_id == user_id).all()
    
    @db_operation("UPDATE_JOB","JOB")
    def update_job(self, job):
        self.db.commit()
        self.db.refresh(job)
        return job
    
    @db_operation("DELETE_JOB","JOB")
    def delete_job(self, job):
        self.db.delete(job)
        self.db.commit()