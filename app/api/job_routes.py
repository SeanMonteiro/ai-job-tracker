from fastapi import APIRouter, Depends
from app.schemas.job import JobCreate, JobUpdate
from app.dependencies.injector import get_job_service, get_job_pipeline_service
from app.dependencies.auth import get_current_user
from app.services.job_service import JobService
from app.services.job_pipeline_service import JobPipelineService
from app.core.response import success_response
from app.core.logger.logger import logger, setup_logger
logger = setup_logger()

router = APIRouter(prefix="/jobs", tags=["JOBS"])

# CREATE JOB BY USER - STRUCTURED JSON DATA

@router.post("/", status_code=201)
def create_job(
        job: JobCreate, 
        pipeline: JobPipelineService = Depends(get_job_pipeline_service),
        current_user = Depends(get_current_user)
    ):
    result = pipeline.create_structure_job_with_analysis(
        job_data = job, user_id= current_user.id
    )
    return success_response(data=result)

# GET JOBS FOR USER

@router.get("/")
def get_jobs(
        job_service:JobService = Depends(get_job_service),
        current_user = Depends(get_current_user)
    ):
    result =  job_service.get_all_jobs(current_user.id)
    return success_response(data=result)

# GET JOB FOR A USER

@router.get("/{job_id}")
def get_job(
        job_id: int, 
        job_service:JobService = Depends(get_job_service),
        current_user =  Depends(get_current_user)
    ):
    result = job_service.get_job(job_id, current_user.id)
    return success_response(data=result)

# UPDATE A JOB FOR THAT USER

@router.put("/{job_id}")
def update_job(
    job_id: int, 
    payload: JobUpdate,
    job_service: JobService = Depends(get_job_service),
    current_user = Depends(get_current_user)
):
    result = job_service.update_job(
        job_id,
        current_user.id,
        payload
    )   
    return success_response(data=result)

# DELETE A JOB FOR A USER

@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    job_service: JobService = Depends(get_job_service),
    current_user = Depends(get_current_user)
):
    result = job_service.delete_job(
        job_id, current_user.id
    )
    return success_response(data=result)