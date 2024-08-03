"""File with starting point of the application."""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.common.exceptions.not_found_exception import NotFoundException
from src.modules.task.task_controller import task_router
from src.core.database import create_database_and_tables
from src.core.log import logger


@asynccontextmanager
async def lifespan(application: FastAPI):
    """Function that handles start and shutdown of the application."""

    logger.info("Creating database and tables...")
    create_database_and_tables()

    logger.info("Starting application...")

    yield

    logger.info("Shutting down application...")


app = FastAPI(lifespan=lifespan, title="Task Manager API")

app.include_router(task_router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:  # flank8: noqa E501
    """Handle body validation errors."""

    logger.info("Request body: %s", exc.body)
    logger.error("Request validation error: %s", exc.errors())

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.exception_handler(NotFoundException)
async def item_not_found_exception_handler(
    request: Request, exc: NotFoundException
):  # flake8: noqa E501
    """Handle not found exception."""

    return JSONResponse(
        status_code=404,
        content={"message": f"Item with id {exc.item_id} not found"},
    )
