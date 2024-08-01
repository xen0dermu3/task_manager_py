"""File that contains task status enum."""

from enum import Enum


class TaskStatus(Enum):
    """Task status enum."""

    TODO = 0
    IN_PROGRESS = 1
    COMPLETED = 2
