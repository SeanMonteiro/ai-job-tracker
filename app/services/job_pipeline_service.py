from app.services.job_service import JobService
from app.ai.services.job_analysis_service import JobAnalysisService

class JobPipelineService:

    def __init__(
            self, 
            job_service: JobService,
            job_analysis_service: JobAnalysisService 
        ):
        self.job_service = job_service
        self.job_analysis_service = job_analysis_service

    def create_structure_job_with_analysis(self, job_data, user_id: int):
        job = self.job_service.create_job(job_data, user_id)
        
        analysis_result = self.job_analysis_service.analyze_only(
            description= job_data.description,
            user_id= user_id
        )

        return {
            "job": job,
            "analysis": analysis_result
        }


        