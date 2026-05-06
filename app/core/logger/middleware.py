import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from contextvars import ContextVar

request_id_ctx_var = ContextVar("request_id", default="N/A")

class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_id = str(uuid.uuid4())

        # store in context (GLOBAL for this request)
        request_id_ctx_var.set(request_id)

        response = await call_next(request)
        response.headers['X-Request-ID'] = request_id

        return response