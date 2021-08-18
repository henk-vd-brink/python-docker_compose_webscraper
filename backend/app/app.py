from fastapi import FastAPI
from app.container import Application
import app.endpoints as endpoints
from app import models

from sqlalchemy import create_engine

def create_app() -> FastAPI:
    container = Application()
    container.wire(modules=[endpoints])

    engine = create_engine("postgresql://postgres:postgres@database:5432", echo=True)
    models.Base.metadata.create_all(bind=engine)
    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)
    return app


app = create_app()
