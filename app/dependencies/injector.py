from app.core.database.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session

# Import Repositories
from app.repositories.job_repository import JobRepository
from app.repositories.user_repository import UserRepository

# Import Services
from app.services.job_service import JobService
from app.services.user_service import UserService

def get_job_service(db:Session = Depends(get_db)):
    repo = JobRepository(db)
    return JobService(repo)

def get_user_service(db:Session = Depends(get_db)):
    repo = UserRepository(db)
    return UserService(repo)