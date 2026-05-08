from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database.database import Base, engine
from app.core.logger.logger import setup_logger
import logging
from app.core.logger.middleware import RequestIDMiddleware
from app.handlers import (
    app_exception_handler,
    global_exception_handler
    )
from app.exceptions import AppException

# Import routes
from app.api.auth_routes import router as auth_router
from app.api.job_routes import router as job_router

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
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

# Routes
app.include_router(job_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "AI Job Tracker API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}