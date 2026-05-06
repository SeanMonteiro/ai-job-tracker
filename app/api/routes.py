from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.job import JobCreate, JobResponse
# from app.core.database.database import get_db
from app.core.dependencies import get_job_service
from app.services.job_service import JobService

router = APIRouter()

@router.post("/jobs", response_model = JobResponse)
def create_job(
        job:JobCreate, 
        job_service:JobService = Depends(get_job_service)
    ):
    return job_service.create_job(job)

@router.get("/jobs", response_model = list[JobResponse])
def get_jobs(
        job_service:JobService = Depends(get_job_service)
    ):
    return job_service.get_all_jobs()

@router.get("/jobs/{job_id}", response_model = JobResponse)
def get_job(
        job_id: int, 
        job_service:JobService = Depends(get_job_service)
    ):
    return job_service.get_job(job_id)