"""Main module"""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes.person import router as person_router

PREFIX = "/api/v1"


app = FastAPI(title="FastAPI-SQLAlchemy Demo")


@app.get("/")
def main():
    """Redirects main route to docs"""
    return RedirectResponse("/docs")


app.include_router(person_router, prefix=PREFIX)
