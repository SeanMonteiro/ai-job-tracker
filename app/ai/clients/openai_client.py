import os
from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def chat(self, messages):
        response = self.client.chat.completions.create(
            model = "gpt-40-mini",
            messages = messages,
            temperature = 0.2
        )

        return response.choices[0].message.content