from fastapi import APIRouter, Depends
from app.schemas.job import JobCreate, JobResponse
from app.core.dependencies import get_job_service
from app.services.job_service import JobService

router = APIRouter()

@router.post("/jobs")
def create_job(
        job:JobCreate, 
        job_service:JobService = Depends(get_job_service)
    ):
    result = job_service.create_job(job)
    return {
        "success": True,
        "data": result
    }

@router.get("/jobs")
def get_jobs(
        job_service:JobService = Depends(get_job_service)
    ):
    result =  job_service.get_all_jobs()
    return {
        "success": True,
        "data": result
    }

@router.get("/jobs/{job_id}")
def get_job(
        job_id: int, 
        job_service:JobService = Depends(get_job_service)
    ):
    result = job_service.get_job(job_id)
    return {
        "success": True,
        "data": result
    }