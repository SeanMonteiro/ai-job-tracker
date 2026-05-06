# Business Logic
from sqlalchemy.orm import Session
from app.schemas.job import JobCreate
from app.repositories import job_repository
from app.exceptions import JobNotFoundException
from app.exceptions import JobValidationException
import logging

def create_job(db:Session, job:JobCreate):
    if len(job.title.strip()) < 3:
        raise JobValidationException()
    
    return job_repository.create_job(db, job)

def get_job(db:Session, job_id: int):
    job = job_repository.get_job(db, job_id)

    if not job:
        raise JobNotFoundException(f"Job {job_id} not found")    
    
    return job

def get_all_jobs(db:Session):
    return job_repository.get_all_jobs(db)
