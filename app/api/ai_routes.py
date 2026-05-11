from fastapi import APIRouter, Body, Depends
from app.dependencies.auth import get_current_user
from app.ai.services.job_analysis_service import JobAnalysisService
from app.dependencies.injector import get_job_analysis_service
from app.core.response import success_response

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/analyze-job")
def analyze_job(
    job_description: str = Body(..., media_type="text/plain"),
    current_user = Depends(get_current_user),
    job_analysis_service: JobAnalysisService = Depends(get_job_analysis_service)
):
    result = job_analysis_service.analyze_and_store(
        job_description, current_user.id
    )

    return success_response(data=result, message="Job Analyzed Successfully")