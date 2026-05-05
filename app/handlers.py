from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions import JobNotFoundException
from app.exceptions import JobValidationException
import logging

logger = logging.getLogger(__name__)

async def job_not_found_handler(request: Request, exc: JobNotFoundException):
    logger.warning(f"Job not found: {exc.message}")
    return JSONResponse(
        status_code=404,
        content={"message": exc.message},
    )

async def job_validation_handler(request, exc: JobValidationException):
    logger.warning(f"Job validation failed: {exc.message}")

    return JSONResponse(
        status_code=400,
        content={"message": exc.message},
    )


async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )