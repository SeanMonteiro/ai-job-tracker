class AppException(Exception):
    def __init__(self, message:str, status_code: int=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class JobNotFoundException(AppException):
    def __init__(self, message: str = "Job not found"):
        super().__init__(message, status_code=404)

class JobValidationException(AppException):
    def __init__(self, message: str = "Title must be at least 3 characters long"):
        super().__init__(message, status_code = 400)