import os
from fastapi import APIRouter

router = APIRouter(prefix="/debug", tags=["DEBUG"])

@router.post("/ai/failure/enable")
def enable_ai_failure():
    # For Debug only
    os.environ["SIMULATE_AI_FAILURE"] = "true"
    return {
        "success": True,
        "message": "AI failure simulation enabled"
    }

@router.post("/ai/failure/disable")
def disable_ai_failure():
    os.environ["SIMULATE_AI_FAILURE"] = "false"
    return {
        "success": True,
        "message": "AI failure simulation disabled"
    }