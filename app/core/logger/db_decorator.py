import logging
from functools import wraps
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger("ai-job-tracker")

def db_operation(action:str, entity:str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"{action} | entity={entity} | START")
            repo_instance = args[0]

            try:
                result = func(*args, **kwargs)
                entity_id = getattr(result, "id", None)
                logger.info(
                    f"{action} | entity={entity} | SUCCESS | id={entity_id}"
                )
                return result
            
            except SQLAlchemyError as e:
                repo_instance.db.rollback()
                logger.error(
                    f"{action} | entity={entity} | DB_ERROR | error={str(e)}"
                )

            except Exception as e:
                logger.error(
                    f"{action} | entity={entity} | ERROR | error={str(e)}"
                )
        return wrapper
    return decorator