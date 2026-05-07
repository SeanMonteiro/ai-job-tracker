from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions import JobNotFoundException
from app.exceptions import JobValidationException
import logging

logger = logging.getLogger("ai-job-tracker")

async def job_not_found_handler(request: Request, exc: JobNotFoundException):
    # logger.warning(f"Job not found: {exc.message}")
    logger.warning(str(exc))
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": str(exc)
        },
    )

async def job_validation_handler(request: Request, exc: JobValidationException):
    logger.warning(str(exc))

    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": str(exc)
        },
    )


async def global_exception_handler(request: Request, exc: Exception):
    logger.error(str(exc))
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error"
        },
    )