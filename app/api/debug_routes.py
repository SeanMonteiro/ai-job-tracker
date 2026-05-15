import os
from fastapi import APIRouter
from app.exceptions import AppException

router = APIRouter(prefix="/debug", tags=["DEBUG"])

def ensure_debug_enabled():
    if(os.getenv("ENABLE_DEBUG_ROUTES", "false").lower()!= "true"):
        raise AppException("Debug routes are disabled", 403)

@router.post("/ai/failure/enable")
def enable_ai_failure():
    # For Debug only
    ensure_debug_enabled()
    os.environ["SIMULATE_AI_FAILURE"] = "true"
    return {
        "success": True,
        "message": "AI failure simulation enabled"
    }

@router.post("/ai/failure/disable")
def disable_ai_failure():
    # For Debug only
    ensure_debug_enabled()
    os.environ["SIMULATE_AI_FAILURE"] = "false"
    return {
        "success": True,
        "message": "AI failure simulation disabled"
    }