# DB Access Layer
from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.job import JobCreate
from app.schemas.job import JobResponse
import logging

def create_job(db:Session, job: JobCreate):
    db_job = Job (
        title = job.title,
        company = job.company,
        description = job.description
    )

    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job

def get_job(db:Session, job_id:int ):
    return db.query(Job).filter(Job.id == job_id).first()

def get_all_jobs(db:Session):
    return db.query(Job).all()

