from fastapi import FastAPI
from app.models import Job

app = FastAPI()

jobs = []

@app.get("/")
def read_root():
    return {
        "message" : "AI Job Tracker API is running"
    }

@app.post("/jobs")
def create_job(job: Job):
    jobs.append(job)
    return {
        "message" : "Job created", 
        "job" : job 
    }

@app.get("/jobs")
def get_jobs():
    return jobs

