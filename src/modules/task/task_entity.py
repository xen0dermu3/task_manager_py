"""File with task entity."""

from dataclasses import dataclass
import uuid
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

from src.common.enums.task_priority import TaskPriority
from src.common.enums.task_status import TaskStatus


class TaskBase(SQLModel):
    """Base pydantic class for task."""

    title: str = Field(min_length=5)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: TaskStatus = Field(default=TaskStatus.TODO)
    priority: TaskPriority = Field()
    due_date: Optional[datetime] = Field(default=None)


@dataclass
class Task(TaskBase, table=True):
    """Class with task entity."""

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default_factory=datetime.now,
        sa_column_kwargs={"onupdate": datetime.now},
    )
