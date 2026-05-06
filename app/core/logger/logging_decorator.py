import logging
from functools import wraps

logger = logging.getLogger("ai-job-tracker")

def log_db(action:str, entity:str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"{action} | entity={entity} | START")

            try:
                result = func(*args, **kwargs)

                # Try to extract ID from ORM object returned
                entity_id = getattr(result, "id", None)

                logger.info(
                    f"{action} | entity={entity} | SUCCESS | id={entity_id}"
                )

                return result
            except Exception as e:
                logger.error(
                    f"{action} | entity={entity} | FAILED | error={str(e)}"
                )
                raise
        return wrapper
    return decorator