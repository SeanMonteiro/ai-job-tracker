from fastapi import APIRouter, Depends
from app.schemas.job import JobCreate, JobResponse
from app.dependencies.injector import get_job_service
from app.dependencies.auth import get_current_user
from app.services.job_service import JobService
from app.core.response import success_response

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/")
def create_job(
        job:JobCreate, 
        job_service:JobService = Depends(get_job_service),
        current_user = Depends(get_current_user)
    ):
    result = job_service.create_job(job, current_user.id)
    return success_response(data=result)

@router.get("/")
def get_jobs(
        job_service:JobService = Depends(get_job_service),
        current_user = Depends(get_current_user)
    ):
    result =  job_service.get_all_jobs(current_user.id)
    return success_response(data=result)

@router.get("/{job_id}")
def get_job(
        job_id: int, 
        job_service:JobService = Depends(get_job_service),
        current_user =  Depends(get_current_user)
    ):
    result = job_service.get_job(job_id, current_user.id)
    return success_response(data=result)