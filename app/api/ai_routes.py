from fastapi import APIRouter, Body, Depends
from app.dependencies.auth import get_current_user
from app.services.job_pipeline_service import JobPipelineService
from app.dependencies.injector import get_job_pipeline_service
from app.core.response import success_response

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/jobs/raw")
def create_job(
    description: str = Body(..., media_type="text/plain"), 
    job_pipeline_service: JobPipelineService = Depends(get_job_pipeline_service),
    current_user = Depends(get_current_user)
):
    result = job_pipeline_service.create_raw_job_with_analysis(description, current_user.id)
    return success_response(data=result)

@router.post("jobs/{job_id}/analyze")
def analyze_existing_job(
    job_id: int,
    job_pipeline_service: JobPipelineService = Depends(get_job_pipeline_service),
    current_user = Depends(get_current_user)
):
    result = job_pipeline_service.analyze_existing_job(job_id, current_user.id)
    return success_response(data=result)