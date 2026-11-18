from fastapi import FastAPI , Request
from fastapi.responses import JSONResponse

# This code defines a global exception handler for your FastAPI application. Its purpose is to catch unexpected exceptions and return a consistent JSON error response instead of exposing FastAPI's default internal error response.

def register_exception_handlers(app:FastAPI):
    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request , exc : Exception):
        return JSONResponse(status_code = 500, content = {'detail': str(exc)})
