from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions import AppException
import logging

logger = logging.getLogger("ai-job-tracker")

async def app_exception_handler(request: Request, exc: AppException):

    return JSONResponse(
        status_code = exc.status_code,
        content = {
            "success": False,
            "data": None,
            "message": str(exc)
        },
    )

async def global_exception_handler(request: Request, exc: Exception):

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "data": None,
            "message": "Internal Server Error"
        },
    )
