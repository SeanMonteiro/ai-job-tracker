# DB Access Layer
from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.job import JobCreate
from app.schemas.job import JobResponse
import logging
from app.core.logger.logging_decorator import log_db
# logger =logging.getLogger("ai-job-tracker")

@log_db("CREATE_JOB","Job")
def create_job(db:Session, job: JobCreate):
    db_job = Job (
        title = job.title,
        company = job.company,
        description = job.description
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    # logger.info(f"Created Job {db_job}")
    return db_job

@log_db("GET_JOB","Job")
def get_job(db:Session, job_id:int ):
    # logger.info(f"Fetching job {job_id}")
    return db.query(Job).filter(Job.id == job_id).first()

@log_db("GET_ALL_JOB","Jobs")
def get_all_jobs(db:Session):
    # logger.info(f"Fetching All jobs")
    return db.query(Job).all()