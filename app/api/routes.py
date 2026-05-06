from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.job import JobCreate, JobResponse
from app.core.database import get_db
from app.services import job_service

router = APIRouter()

@router.post("/jobs", response_model = JobResponse)
def create_job(job:JobCreate, db: Session = Depends(get_db)):
    return job_service.create_job(db, job)

@router.get("/jobs", response_model = list[JobResponse])
def get_jobs(db:Session = Depends(get_db)):
    return job_service.get_all_jobs(db)

@router.get("/jobs/{job_id}", response_model = JobResponse)
def get_job(job_id: int, db:Session = Depends(get_db)):
    return job_service.get_job(db, job_id)