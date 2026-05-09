import json
from app.ai.clients.openai_client import OpenAIClient
from app.ai.prompts.job_analysis_prompt import JOB_ANALYSIS_PROMPT
from app.ai.schemas.job_analysis import JobAnalysisRespone

class JobAIService:
    def __init__(self):
        self.client = OpenAIClient()

    def analyze_job_description(self, description:str):
        messages = [
            { "role": "system", "content": JOB_ANALYSIS_PROMPT },
            { "role": "user", "content": description }
        ]

        response = self.client.chat(messages)

        try:
            data = json.loads(response)
            return JobAnalysisRespone(**data)
        except Exception:
            return {
                "skills" : [],
                "experience_level": "Unknown",
                "summary": "Failed to parse AI response"
            }