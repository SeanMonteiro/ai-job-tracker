from fastapi import APIRouter
from app.core.database.database import engine
from sqlalchemy import text

router = APIRouter(prefix="/health", tags=["HEALTH"])

@router.get("/")
def health():
    return {
        "status": "ok",
        "service": "ai-job-tracker"
    }

@router.get("/db")
def db_health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {
            "status": "ok",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "error",
            "database": "disconnected",
            "error": str(e)
        }