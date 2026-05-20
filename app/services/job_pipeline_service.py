from app.schemas.job import JobCreate, JobResponse
from app.models.job_analysis import JobAnalysis
from app.models.resume_match_analysis import ResumeMatchAnalysis
from app.utils.utilities import parse_raw_job_text, validate_description
from app.core.logger.logger import logger, setup_logger
from app.exceptions import AppException

logger = setup_logger()

class JobPipelineService:

    def __init__(self, job_service, job_analysis_service, analysis_repo, resume_match_repo):
        self.job_service = job_service
        self.job_analysis_service = job_analysis_service
        self.analysis_repo = analysis_repo
        self.resume_match_repo = resume_match_repo

    def create_structure_job_with_analysis(self, job_data, user_id: int):
        logger.info("PIPELINE START: structured flow")
        validate_description(job_data.description)
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
            logger.error(f"PIPELINE FAILD | structured_flow | user_id={user_id} | error={str(e)}", exc_info=True)
            return {
                "job": job_response if 'job_response' in locals() else None,
                "analysis": None,
                "message": "AI analysis failed but job was created"
            }
    
    def create_raw_job_with_analysis(self, description: str, user_id: int):
        logger.info("PIPELINE START: raw flow")
        validate_description(description)
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
                description = job.description,
                status = job.status
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
            logger.error(f"PIPELINE FAILED | raw_flow | user_id={user_id} | error={str(e)}", exc_info=True)
            return {
                "job": job_response if 'job_response' in locals() else None,
                "analysis": None,
                "message": "AI analysis failed but job was created"
            }
        
    def analyze_existing_job (self, job_id: int, user_id: int):
        logger.info(f"PIPELINE START: retry analysis | job_id={job_id}")
        try:
            job = self.job_service.get_job(job_id, user_id)
            job_response = JobResponse(
                id = job.id,
                title = job.title,
                company = job.company,
                description = job.description,
                status = job.status
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
            logger.error(f"PIPELINE FAILED | retry_analysis | job_id={job_id}", exc_info=True)
            return {
                "job": job_response if 'job_response' in locals() else None,
                "analysis": None,
                "message": "AI analysis retry failed "
            }

    # RESUME_MATCHING_ON_AN_EXISTING_JOB_BY_USER

    def match_resume_to_existing_job (self, job_id: int, user_id: int, resume_text: str):
        logger.info(
            f"PIPELINE START: RESUME MATCH ANALYSIS | job_id={job_id} | user_id={user_id}"
        )

        try:
            job = self.job_service.get_job(job_id, user_id)

            if not resume_text or len(resume_text.strip()) < 50:
                logger.warning(
                    f"PIPELINE FAILED: resume missing or too short | "
                    f"job_id={job_id} | user_id={user_id}"
                )
                raise AppException("Please update your resume before running resume match", 400)
            
            match_result = self.job_analysis_service.match_resume_to_job(
                job_description = job.description,
                resume_text = resume_text
            )

            next_version = self.resume_match_repo.get_next_version(job.id)

            record = ResumeMatchAnalysis(
                job_id = job.id,
                user_id = user_id,
                version = next_version,
                model_version = match_result["model_version"],
                prompt_version = match_result["prompt_version"],
                match_result= match_result["match_result"]
            )

            saved_match = self.resume_match_repo.save(record)

            logger.info(
                f"PIPELINE SUCCESS: resume match saved | "
                f"job_id={job_id} | user_id={user_id} | version={saved_match.version}"
            )

            return {
                "resume_match": {
                "id": saved_match.id,
                "job_id": saved_match.job_id,
                "version": saved_match.version,
                "model_version": saved_match.model_version,
                "prompt_version": saved_match.prompt_version,
                **saved_match.match_result
                }
            }

        except AppException:
            raise

        except Exception as e:
            logger.error(
                f"PIPELINE FAILED: resume match | job_id={job_id} | "
                f"user_id={user_id} | error={str(e)}", exc_info=True 
            )
            raise AppException("Resume Match failed", 500)