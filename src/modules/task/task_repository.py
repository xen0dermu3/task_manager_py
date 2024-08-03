"""File that has task repository."""

from typing import Sequence
import uuid
from sqlmodel import Session, select

from src.common.exceptions.not_found_exception import NotFoundException
from src.modules.task.dto.create_task import CreateTask
from src.modules.task.dto.update_task import UpdateTask
from src.modules.task.task_entity import Task


class TaskRepository:
    """Class for handling task repository."""

    def __init__(self, session: Session):
        """Initialize task repository."""

        self.session = session

    def create_task(self, dto: CreateTask) -> Task:
        """Create task."""

        task = Task.model_validate(dto)

        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)

        return task

    def get_all_tasks(self) -> Sequence[Task]:
        """Get all tasks."""

        return self.session.exec(select(Task)).all()

    def get_task_by_id(self, task_id: uuid.UUID) -> Task | None:
        """Get task by id."""

        task = self.session.get(Task, task_id)

        if not task:
            raise NotFoundException(task_id)

        return task

    def update_task(self, task_id: uuid.UUID, dto: UpdateTask) -> Task | None:
        """Update task."""

        task = self.session.get(Task, task_id)

        if not task:
            raise NotFoundException(task_id)

        task_data = dto.model_dump(exclude_unset=True)

        for key, value in task_data.items():
            setattr(task, key, value)

        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)

        return task

    def delete_task(self, task_id: uuid.UUID) -> Task | None:
        """Delete task."""

        task = self.session.get(Task, task_id)

        if not task:
            raise NotFoundException(task_id)

        self.session.delete(task)
        self.session.commit()

        return task
