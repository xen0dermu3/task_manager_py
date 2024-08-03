"""File for handling task service."""

from typing import Sequence
import uuid
from sqlmodel import Session

from src.modules.task.dto.create_task import CreateTask
from src.modules.task.dto.update_task import UpdateTask
from src.modules.task.task_repository import TaskRepository
from src.modules.task.task_entity import Task


class TaskService:
    """Class for handling task service."""

    def __init__(self, session: Session):
        """Initialize task service."""

        self.repository = TaskRepository(session)

    def create_task(self, dto: CreateTask) -> Task:
        """Create task."""

        return self.repository.create_task(dto)

    def get_all_tasks(self) -> Sequence[Task]:
        """Get all tasks."""

        return self.repository.get_all_tasks()

    def get_task_by_id(self, task_id: uuid.UUID) -> Task | None:
        """Get task by id."""

        return self.repository.get_task_by_id(task_id)

    def update_task(self, task_id: uuid.UUID, dto: UpdateTask) -> Task | None:
        """Update task."""

        return self.repository.update_task(task_id, dto)

    def delete_task(self, task_id: uuid.UUID) -> Task | None:
        """Delete task."""

        return self.repository.delete_task(task_id)
