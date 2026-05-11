import json
from app.ai.clients.openai_client import OpenAIClient
from app.ai.prompts.job_analysis_prompt import JOB_ANALYSIS_PROMPT
from app.ai.schemas.job_analysis import JobAnalysisRespone
from app.models.job_analysis import JobAnalysis
from app.ai.utils.json_parser import extract_json_from_text

class JobAnalysisService:
    def __init__(self, repo):
        self.client = OpenAIClient()
        self.repo = repo

    def analyze_and_store(self, description: str, user_id: int):
        messages = [
            { "role": "system", "content": JOB_ANALYSIS_PROMPT },
            { "role": "user", "content": description }
        ]

        response = self.client.chat(messages)
        # print(response)

        # TRY SAFE PARSING
        data = extract_json_from_text(response)
        # data = json.loads(response)
        
        structured = JobAnalysisRespone(**data)

        # Store in DB
        record = JobAnalysis(
            user_id = user_id,
            job_description = description,
            analysis = structured.model_dump()
        )

        saved = self.repo.save(record)
        
        return  {
            "analysis_id" : saved.id,
            "analysis" : structured.model_dump()
        }