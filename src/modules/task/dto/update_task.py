"""File with update task dto."""

from datetime import datetime
from typing import Optional
from pydantic import Field
from sqlmodel import SQLModel

from src.common.enums.task_priority import TaskPriority
from src.common.enums.task_status import TaskStatus


class UpdateTask(SQLModel):
    """Update task dto."""

    title: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    status: Optional[TaskStatus] = Field(default=None)
    priority: Optional[TaskPriority] = Field(default=None)
    due_date: Optional[datetime] = Field(default=None)
