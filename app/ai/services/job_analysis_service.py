from app.ai.clients.openai_client import OpenAIClient
from app.ai.prompts.job_analysis_prompt import JOB_ANALYSIS_PROMPT, PROMPT_VERSION
from app.ai.schemas.job_analysis import JobAnalysisResponse
from app.ai.utils.json_parser import extract_json_from_text
from app.exceptions import AppException
from app.core.logger.logger import logger, setup_logger
logger = setup_logger()

class JobAnalysisService:

    def __init__(self):
        self.client = OpenAIClient()

    def analyze (self, description: str):
        logger.info("START: AI analysis")
        messages = [
            { "role": "system", "content": JOB_ANALYSIS_PROMPT},
            { "role": "user", "content": description }
        ]
        
        try:
            # # Simulate AI failure
            # raise AppException("Simulated AI failure", 500)

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