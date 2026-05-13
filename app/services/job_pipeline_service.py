from app.schemas.job import JobCreate, JobResponse
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
        try:
            logger.info(f"PIPELINE SERVICE: create job | title={job_data.title} | user_id={user_id}")
            job = self.job_service.create_job(job_data, user_id)

            job_response = JobResponse(
                id = job.id,
                title = job.title,
                company = job.company,
                description = job.description
            )
        
            next_version = self.analysis_repo.get_next_version(job.id)
            analysis_result = self.job_analysis_service.analyze(job_data.description)

            record = JobAnalysis(
                job_id = job.id,
                user_id=user_id,
                version = next_version,
                model_version = analysis_result["model_version"],
                prompt_version = analysis_result["prompt_version"],
                analysis=analysis_result["analysis"],
            )
            
            saved_analysis = self.analysis_repo.save(record)
            
            return {
                "job": job_response,
                "analysis": saved_analysis
            }
        except Exception as e:
            logger.error(f"PIPELINE FAILD | structured_flow | user_id={user_id} | error={str(e)}")
            exc_info=True

            return {
                "job": None,
                "analysis": None,
                "error": str(e)
            }
    
    def create_raw_job_with_analysis(self, description: str, user_id: int):

        logger.info("PIPELINE START: raw flow")
        try:
            parsed = parse_raw_job_text(description)
            logger.info(f"PIPELINE SERVICE: create job | title={parsed.get('title')} | user_id={user_id}")
            
            # Store job in service_create_job
            job_data = JobCreate (
                title= parsed["title"],
                company= parsed["company"],
                description= parsed["description"]
            )
            # logger.info(f"PARSED RAW JOB : {str(job_data)}")
            job = self.job_service.create_job(job_data, user_id)
            job_response = JobResponse(
                id = job.id,
                title = job.title,
                company = job.company,
                description = job.description
            )

            next_version = self.analysis_repo.get_next_version(job.id)
            analysis_result = self.job_analysis_service.analyze(parsed["description"])

            record = JobAnalysis(
                job_id = job.id,
                user_id=user_id,
                version = next_version,
                model_version = analysis_result["model_version"],
                prompt_version = analysis_result["prompt_version"],
                analysis = analysis_result["analysis"]
            )

            saved_analysis = self.analysis_repo.save(record)
            
            return {
                "job": job_response,
                "analysis": saved_analysis
            }
        except Exception as e:
            logger.error(f"PIPELINE FAILED | raw_flow | user_id={user_id} | error={str(e)}")
            exc_info=True

            return {
                "job": None,
                "analysis": None,
                "error": str(e)
            }
        
    def analyze_existing_job (self, job_id: int, user_id: int):
        logger.info(f"PIPELINE START: retry analysis | job_id={job_id}")
        try:
            job = self.job_service.get_job(job_id, user_id)
            job_response = JobResponse(
                id = job.id,
                title = job.title,
                company = job.company,
                description = job.description
            )
            
            analysis_result = self.job_analysis_service.analyze(job.description)

            next_version = self.analysis_repo.get_next_version(job.id)

            record = JobAnalysis (
                job_id = job.id,
                user_id = user_id,
                version = next_version,
                model_version = analysis_result["model_version"],
                prompt_version = analysis_result["prompt_version"],
                analysis = analysis_result["analysis"]
            )

            saved_analysis = self.analysis_repo.save(record)
            
            return {
                "job": job_response,
                "analysis": saved_analysis 
            }

        except Exception as e:
            logger.error(f"PIPELINE FAILED | retry_analysis | job_id={job_id}")