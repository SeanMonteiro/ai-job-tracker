import logging, os
from logging.handlers import RotatingFileHandler

LOG_FILE = "logs/app.log"
os.makedirs("logs", exist_ok = True)

def setup_logger():
    logger = logging.getLogger("ai-job-tracker")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger
    
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File Handler
    file_handler = RotatingFileHandler (
        LOG_FILE,
        maxBytes = 5_000_000,
        backupCount= 3
        )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

def get_logger(name:str):
    return logging.getLogger(name)

