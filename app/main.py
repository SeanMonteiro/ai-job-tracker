from fastapi import FastAPI
from app.models import JobCreate, JobResponse
from app.logger import setup_logger, logging
from app.handlers import (
    job_not_found_handler,
    job_validation_handler,
    global_exception_handler
)
from app.exceptions import JobNotFoundException
from app.exceptions import JobValidationException

app = FastAPI()

setup_logger()
logger = logging.getLogger("ai-job-tracker")

app.add_exception_handler(JobNotFoundException, job_not_found_handler)
app.add_exception_handler(JobValidationException, job_validation_handler)
app.add_exception_handler(Exception, global_exception_handler)

jobs = []
job_counter = 1

@app.get("/")
def read_root():
    logger.info("Home page loaded")
    return {
        "message" : "AI Job Tracker API is running"
    }

@app.post("/jobs")
def create_job(job: JobCreate):

    global job_counter

    # Business Validation
    if len(job.title.strip()) < 3:
        raise JobValidationException()
    
    job_data = {
        "id": job_counter,
        "title": job.title,
        "company": job.company,
        "description": job.description
    }

    jobs.append(job_data)
    job_counter +=1

    logger.info(f"Job created: { job_data['id']}")
    
    return job_data

@app.get("/jobs")
def get_jobs():
    return jobs

@app.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: int):
    for job in jobs:
        if job["id"] == job_id:
            return job

    raise JobNotFoundException(f"Job {job_id} not found")

@app.get("/test/server-error")
def crash():
    return 1 / 0

