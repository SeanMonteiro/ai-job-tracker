from app.ai.clients.openai_client import OpenAIClient
from app.ai.prompts.job_analysis_prompt import JOB_ANALYSIS_PROMPT
from app.ai.schemas.job_analysis import JobAnalysisResponse
from app.models.job_analysis import JobAnalysis
from app.models.job import Job
from app.ai.utils.json_parser import extract_json_from_text
from app.exceptions import AppException
from pydantic import ValidationError

class JobAnalysisService:
    def __init__(self, job_repo, analysis_repo):
        self.client = OpenAIClient()
        self.job_repo = job_repo
        self.analysis_repo = analysis_repo

    def analyze_only(self, description: str, user_id: int):
        messages = [
            { "role": "system", "content": JOB_ANALYSIS_PROMPT },
            { "role": "user", "content": description }
        ]

        try:

            response = self.client.chat(messages)

            if not response:
                raise AppException("Empty AI response", 500)

            # TRY SAFE PARSING
            data = extract_json_from_text(response)
            structured = JobAnalysisResponse(**data)

            # Store Job Analysis DB
            record = JobAnalysis(
                user_id = user_id,
                job_description = description,
                analysis = structured.model_dump()
            )

            saved = self.analysis_repo.save(record)
            
            return  {
                "analysis_id" : saved.id,
                "analysis" : structured.model_dump()
            }
        
        except Exception as e:
            raise AppException("AI job analysis failed", 500)
        
    
    def analyze_and_store(self, description: str, user_id: int):
        messages = [
            { "role": "system", "content": JOB_ANALYSIS_PROMPT },
            { "role": "user", "content": description }
        ]

        try:

            response = self.client.chat(messages)

            if not response:
                raise AppException("Empty AI response", 500)

            # TRY SAFE PARSING
            data = extract_json_from_text(response)
            structured = JobAnalysisResponse(**data)

            # Store Unstructured Job in Jobs Table
            job = Job (
                title = structured.title,
                company = structured.company,
                description = description,
                user_id = user_id
            )

            saved_job = self.job_repo.create_job(job)

            # Store Job Analysis DB
            record = JobAnalysis(
                user_id = user_id,
                job_description = description,
                analysis = structured.model_dump()
            )

            saved = self.analysis_repo.save(record)
            
            return  {
                "job_id": saved_job.id,
                "analysis_id" : saved.id,
                "analysis" : structured.model_dump()
            }
        
        except ValidationError as e:
            raise AppException("Invalid AI response structure", 500)
        except ValueError as e:
            raise AppException("Faile to parse AI response", 500)
        except AppException:
            raise
        except Exception as e:
            raise AppException("AI job analysis failed", 500)