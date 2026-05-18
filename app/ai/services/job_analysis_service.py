from app.ai.clients.openai_client import OpenAIClient
from app.ai.prompts.job_analysis_prompt import JOB_ANALYSIS_PROMPT, PROMPT_VERSION
from app.ai.prompts.resume_match_prompt import RESUME_MATCH_PROMPT, RESUME_MATCH_PROMPT_VERSION
from app.ai.schemas.job_analysis import JobAnalysisResponse, ResumeMatchResponse
from app.ai.utils.json_parser import extract_json_from_text
from app.exceptions import AppException
from app.core.logger.logger import logger, setup_logger
import os
logger = setup_logger()

class JobAnalysisService:

    def __init__(self):
        self.client = OpenAIClient()

    # ANALYZE JOBS

    def analyze (self, description: str):
        logger.info("START: AI analysis")
        messages = [
            { "role": "system", "content": JOB_ANALYSIS_PROMPT},
            { "role": "user", "content": description }
        ]
        
        try:
            # # Simulate AI failure
            if os.getenv("SIMULATE_AI_FAILURE") == "true":
                raise AppException("Simulated AI failure", 500)

            response = self.client.chat(messages)
            logger.info(f"AI RESPONSE RECEIVED")

            if not response:
                logger.warning("NO AI RESPONSE RECEIVED")
                raise AppException("Empty AI response", 500)

            # TRY SAFE PARSING
            data = extract_json_from_text(response)
            structured = JobAnalysisResponse(**data)
            # logger.info(f"AI PARSED OUTPUT RAW : {structured.model_dump()}")
            
            return {
                "analysis": structured.model_dump(),
                "model_version": self.client.model,
                "prompt_version": PROMPT_VERSION
            }
        except Exception as e:
            logger.error(f"AI ANALYSIS FAILED: {str(e)}")
            raise AppException("AI job analysis failed", 500)
        
    # RESUME MATCH ANALYSIS
    def match_resume_to_job (self, job_description: str, resume_text: str):
        logger.info(
            f"START: RESUME MATCH ANALYSIS | "
            f"job_description_chars={len(job_description or '')} | "
            f"resume_chars={len(resume_text or '')}"
        )

        if not job_description or len(job_description.strip()) < 10:
            raise AppException("Job description is required for resume matching", 400)
        
        if not resume_text or len(resume_text.strip()) < 50:
            raise AppException("Resume text must be atleast 50 characters", 400)
        
        user_content = f"""JOB DESCRIPTION: {job_description} RESUME: {resume_text}"""

        messages = [
            {"role": "system", "content": RESUME_MATCH_PROMPT},
            {"role": "user", "content": user_content}
        ]

        try:
            if os.getenv("SIMULATE_AI_FAILURE") == "true":
                raise AppException("Simulated AI failure", 500)
            
            response = self.client.chat(messages)
            logger.info("RESUME MATCH AI RESPONSE RECEIVED")

            if not response:
                logger.warning("NO RESUME MATCH AI RESPONSE RECEIVED")
                raise AppException("Empty AI response", 500)
            
            data = extract_json_from_text(response)
            logger.info(f"RESUME MATCH PARSED DATA: {data}")
            structured = ResumeMatchResponse(**data)

            return {
                "match_result": structured.model_dump(),
                "model_version": self.client.model,
                "prompt_version": RESUME_MATCH_PROMPT_VERSION
            }
        
        except AppException:
            raise

        except Exception as e:
            logger.error(f"RESUME MATCH ANALYSIS FAILED: {str(e)}", exc_info=True)
            raise AppException("AI resume match analysis failed", 500)
