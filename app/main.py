from fastapi import FastAPI
from contextlib import asynccontextmanager
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

setup_logger()
logger = logging.getLogger("ai-job-tracker")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application Startup")
    # Base.metadata.create_all(bind=engine)
    yield
    logger.info("Application Shutdown")


app = FastAPI(lifespan=lifespan)

# Middleware
app.add_middleware(RequestIDMiddleware)

# Map Exception Handlers
app.add_exception_handler(JobNotFoundException, job_not_found_handler)
app.add_exception_handler(JobValidationException, job_validation_handler)
app.add_exception_handler(Exception, global_exception_handler)

# Routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Job Tracker API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}