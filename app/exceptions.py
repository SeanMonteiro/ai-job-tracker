class JobNotFoundException(Exception):
    def __init__(self, message: str = "Job not found"):
        super().__init__(message)
        self.message = message

class JobValidationException(Exception):
    def __init__(self, message: str = "Title must be at least 3 characters long"):
        super().__init__(message)
        self.message = message