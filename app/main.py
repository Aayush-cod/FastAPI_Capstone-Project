from fastapi import FastAPI
from app.middleware.logging_middleware import Logging_Middleware
from app.api import routes_auth , routes_predict
from app.core.exceptions import register_exception_handlers
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(titel = 'Car Price Prediction API')

# link middleware
app.add_middleware(Logging_Middleware)

# link routes
app.include_router(routes_auth.router, tags=['Auth'])
app.include_router(routes_predict.router, tags = ['Prediction'])

# Register exception handler
register_exception_handlers(app)

# monitoring with Prometheus
Instrumentator().instrument(app).expose(app)

