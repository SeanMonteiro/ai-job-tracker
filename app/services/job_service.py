# Business Logic
from app.models.job import Job
from app.exceptions import JobNotFoundException, JobValidationException

class JobService: 
    def __init__(self, repo):
        self.repo = repo

    def create_job(self, job_data):
        if not job_data.title or len(job_data.title.strip()) < 3:
            raise JobValidationException()
        
        job = Job(
            title = job_data.title,
            company = job_data.company,
            description = job_data.description
        )
        
        return self.repo.create_job(job)
    
    def get_job(self, job_id):
        job = self.repo.get_job(job_id)
        
        if job is None:
            raise JobNotFoundException()    
        
        return job
    
    def get_all_jobs(self):
        return self.repo.get_all_jobs()