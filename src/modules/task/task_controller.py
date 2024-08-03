"""Controller file for task module."""

from typing import Sequence
import uuid
from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.core.database import get_session
from src.modules.task.dto.create_task import CreateTask
from src.modules.task.dto.update_task import UpdateTask
from src.modules.task.task_entity import Task
from src.modules.task.task_service import TaskService
from src.core.log import logger

task_router = APIRouter(prefix="/tasks")


def get_task_service(session: Session = Depends(get_session)) -> TaskService:
    """Get task service."""

    return TaskService(session)


@task_router.post("")
async def create_task(
    *, task_service: TaskService = Depends(get_task_service), dto: CreateTask
) -> Task:  # flake8: noqa: E501
    """Create task."""

    logger.info("Got request body: %s", dto)

    return task_service.create_task(dto)


@task_router.get("")
async def get_all_tasks(
    *, task_service: TaskService = Depends(get_task_service)
) -> Sequence[Task]:  # flake8: noqa: E501
    """Get all tasks."""

    return task_service.get_all_tasks()


@task_router.get("/{task_id}")
async def get_task_by_id(
    *,
    task_service: TaskService = Depends(get_task_service),
    task_id: uuid.UUID  # flake8: noqa: E501
) -> Task | None:
    """Get task by id."""

    return task_service.get_task_by_id(task_id)


@task_router.patch("/{task_id}")
async def update_task(
    *,
    task_service: TaskService = Depends(get_task_service),
    task_id: uuid.UUID,
    dto: UpdateTask
) -> Task | None:  # flake8: noqa: E501
    """Update task."""

    return task_service.update_task(task_id, dto)


@task_router.delete("/{task_id}")
async def delete_task(
    *,
    task_service: TaskService = Depends(get_task_service),
    task_id: uuid.UUID  # flake8: noqa: E501
) -> Task | None:
    """Delete task."""

    return task_service.delete_task(task_id)
