import logging, os
from logging.handlers import RotatingFileHandler
from app.core.logger.middleware import request_id_ctx_var

LOG_FILE = "logs/app.log"
os.makedirs("logs", exist_ok = True)

class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id_ctx_var.get()
        return True

def setup_logger():
    logger = logging.getLogger("ai-job-tracker")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger
    
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s | %(request_id)s"
        # "%(asctime)s | %(levelname)s | %(name)s | %(message)s | request_id=%(request_id)s"
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.addFilter(RequestIdFilter())

    # File Handler
    file_handler = RotatingFileHandler (
        LOG_FILE,
        maxBytes = 5_000_000,
        backupCount= 3
        )
    file_handler.setFormatter(formatter)
    file_handler.addFilter(RequestIdFilter())

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

def get_logger(name:str):
    return logging.getLogger(name)