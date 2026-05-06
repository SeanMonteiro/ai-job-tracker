from fastapi import FastAPI
from app.core.database.database import Base, engine
from app.api.routes import router
from app.core.logger.logger import setup_logger
import logging
from app.core.logger.middleware import RequestIDMiddleware
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

# Middleware
app.add_middleware(RequestIDMiddleware)

# Map Exception Handlers
app.add_exception_handler(JobNotFoundException, job_not_found_handler)
app.add_exception_handler(JobValidationException, job_validation_handler)
app.add_exception_handler(Exception, global_exception_handler)

# register routes
app.include_router(router)

@app.on_event("startup")
def start_up():
    logger.info("Application StartUp")
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    logger.info("Home Page Up")
    return {
        "message": "AI Job Tracker API is running"
    }