import os
from openai import OpenAI

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = os.getenv("OPENAI_MODEL")

    def chat(self, messages):
        response = self.client.chat.completions.create(
            model = self.model,
            messages = messages,
            temperature = 0.2
        )

        return response.choices[0].message.content