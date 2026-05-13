from app.schemas.job import JobCreate
from app.models.job_analysis import JobAnalysis
from app.utils.raw_job_parser import parse_raw_job_text 
import logging 

logger = logging.getLogger("ai-job-tracker")

class JobPipelineService:

    def __init__(self, job_service, job_analysis_service, analysis_repo):
        self.job_service = job_service
        self.job_analysis_service = job_analysis_service
        self.analysis_repo = analysis_repo

    def create_structure_job_with_analysis(self, job_data, user_id: int):
        logger.info("PIPELINE START: structured flow")
        
        job = self.job_service.create_job(job_data, user_id)
        analysis = self.job_analysis_service.analyze(job_data.description)

        record = JobAnalysis(
            job_id = job.id,
            user_id=user_id,
            job_description=job_data.description,
            analysis=analysis
        )
        
        saved_analysis = self.analysis_repo.save(record)
        
        return {
            "job": job,
            "analysis": saved_analysis
        }
    
    def create_raw_job_with_analysis(self, description: str, user_id: int):

        logger.info("PIPELINE START: raw flow")

        parsed = parse_raw_job_text(description)
        
        # Store job in service_create_job
        job_data = JobCreate (
            title= parsed["title"],
            company= parsed["company"],
            description= parsed["description"]
        )
        # logger.info(f"PARSED RAW JOB : {str(job_data)}")

        job = self.job_service.create_job(job_data, user_id)
        
        analysis = self.job_analysis_service.analyze(parsed["description"])

        record = JobAnalysis(
            job_id = job.id,
            user_id=user_id,
            job_description= parsed["description"],
            analysis = analysis
        )

        saved_analysis = self.analysis_repo.save(record)

        # self.job_service.enrich_job( job.id, analysis.get("title"), analysis.get("company"))
        
        return {
            "job": job,
            "analysis": saved_analysis
        }