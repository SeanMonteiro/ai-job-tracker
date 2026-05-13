from app.schemas.job import JobCreate
from app.models.job_analysis import JobAnalysis
from app.utils.raw_job_parser import parse_raw_job_text 
from app.core.logger.logger import logger, setup_logger
logger = setup_logger()

class JobPipelineService:

    def __init__(self, job_service, job_analysis_service, analysis_repo):
        self.job_service = job_service
        self.job_analysis_service = job_analysis_service
        self.analysis_repo = analysis_repo

    def create_structure_job_with_analysis(self, job_data, user_id: int):
        logger.info("PIPELINE START: structured flow")
        logger.info(f"PIPELINE SERVICE: create job | title={job.title} | user_id={user_id}")
        job = self.job_service.create_job(job_data, user_id)

        try:
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
        except Exception as e:
            logger.error(f"AI ANALYSIS FAILED (non-blocking) | job_id={job.id} | error={str(e)}")
    
    def create_raw_job_with_analysis(self, description: str, user_id: int):

        logger.info("PIPELINE START: raw flow")
        parsed = parse_raw_job_text(description)
        logger.info(f"PIPELINE SERVICE: create job | title={parsed.title} | user_id={user_id}")
        
        # Store job in service_create_job
        job_data = JobCreate (
            title= parsed["title"],
            company= parsed["company"],
            description= parsed["description"]
        )
        # logger.info(f"PARSED RAW JOB : {str(job_data)}")

        job = self.job_service.create_job(job_data, user_id)
        try:
            analysis = self.job_analysis_service.analyze(parsed["description"])

            record = JobAnalysis(
                job_id = job.id,
                user_id=user_id,
                job_description= parsed["description"],
                analysis = analysis
            )

            saved_analysis = self.analysis_repo.save(record)
            
            return {
                "job": job,
                "analysis": saved_analysis
            }
        except Exception as e:
            logger.error(f"AI ANALYSIS FAILED (non-blocking) | job_id={job.id} | error={str(e)}")