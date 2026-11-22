import logging
from starlette.middleware.base import BaseHTTPMiddleware


class Logging_Middleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logging.info(f'Request: {request.method} {request.url}')
        response = await call_next(request)
        logging.info(f'Response : {response.status_code}')
        return response
