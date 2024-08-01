"""File with task entity."""

import uuid
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

from src.common.enums.task_priority import TaskPriority
from src.common.enums.task_status import TaskStatus


class Task(SQLModel, table=True):
    """Class with task entity."""

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field()
    description: Optional[str] = Field(default=None)
    status: TaskStatus = Field(default=TaskStatus.TODO)
    priority: TaskPriority = Field()
    due_date: Optional[datetime] = Field(default=None)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default_factory=datetime.now,
        sa_column_kwargs={"onupdate": datetime.now},
    )
