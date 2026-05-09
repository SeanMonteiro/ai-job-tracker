# Business Logic
from app.models.job import Job
from app.exceptions import JobNotFoundException, JobValidationException

class JobService: 
    def __init__(self, repo):
        self.repo = repo

    # CREATE JOB

    def create_job(self, job_data, user_id: int):
        if not job_data.title or len(job_data.title.strip()) < 3:
            raise JobValidationException()
        
        job = Job(
            title = job_data.title,
            company = job_data.company,
            description = job_data.description,
            user_id = user_id
        )
        
        return self.repo.create_job(job)
    
    # GET JOB BY ID THAT BELONG TO USER
    
    def get_job(self, job_id:int, user_id: int):
        job = self.repo.get_job(job_id)
        
        if job is None or job.user_id!= user_id:
            raise JobNotFoundException()  
        
        return job
    
    # GET JOB THAT BELONG TO USER

    def get_all_jobs(self, user_id:int):
        return self.repo.get_all_jobs(user_id)
    
    # UPDATE JOB FOR A USER

    def update_job(self, job_id:int, user_id:int, payload):
        job = self.repo.get_job(job_id)

        if job is None or job.user_id != user_id:
            raise JobNotFoundException()
        
        update_data = payload.model_dump(exclude_unset=True)

        for key,value in update_data.items():
            setattr(job, key, value)

        return self.repo.update_job(job)

    # DELETE JOB FOR A USER
    
    def delete_job(self, job_id:int, user_id: int ):
        job = self.repo.get_job(job_id)

        if job is None or job.user_id != user_id:
            raise JobNotFoundException()
        
        self.repo.delete_job(job)

        return {
            "message": "Job Delete successfully"
        }
