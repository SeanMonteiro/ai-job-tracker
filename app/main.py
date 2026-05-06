from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes import router
from app.logger import setup_logger
import logging
from app.handlers import (
    job_not_found_handler,
    job_validation_handler,
    global_exception_handler
)
from app.exceptions import JobNotFoundException
from app.exceptions import JobValidationException

app = FastAPI()
setup_logger()
logger = logging.getLogger("ai-job-tracker")

# Map Exception Handlers
app.add_exception_handler(JobNotFoundException, job_not_found_handler)
app.add_exception_handler(JobValidationException, job_validation_handler)
app.add_exception_handler(Exception, global_exception_handler)
print(engine.url)

# register routes
app.include_router(router)

@app.on_event("startup")
def start_up():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "AI Job Tracker API is running"
    }