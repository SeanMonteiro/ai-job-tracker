from app.core.database.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session

# Import Repositories
from app.repositories.job_repository import JobRepository
from app.repositories.user_repository import UserRepository
from app.repositories.job_analysis_repository import JobAnalysisRepository

# Import Services
from app.services.job_service import JobService
from app.services.user_service import UserService
from app.ai.services.job_analysis_service import JobAnalysisService
from app.services.job_pipeline_service import JobPipelineService

def get_job_service(db:Session = Depends(get_db)):
    repo = JobRepository(db)
    return JobService(repo)

def get_user_service(db:Session = Depends(get_db)):
    repo = UserRepository(db)
    return UserService(repo)

def get_job_analysis_service(db:Session = Depends(get_db)):
    job_repo = JobRepository(db)
    analysis_repo = JobAnalysisRepository(db)
    return JobAnalysisService(
        job_repo = job_repo,
        analysis_repo = analysis_repo
        )

def get_job_pipeline_service(
        job_service: JobService = Depends(get_job_service),
        job_analysis_service: JobAnalysisService = Depends(get_job_analysis_service)
):
    return JobPipelineService(job_service, job_analysis_service)

